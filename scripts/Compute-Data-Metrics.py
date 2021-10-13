import json
import os
import sys
import tempfile

import pandas
import pyarrow
import pyorc
import tables
from sklearn import metrics
import fastdtw

# Types
class Metadata(object):
    def __init__(self, path):
        self.mtidToModelName = {}
        self.columnNameToGid = {}
        with open(path) as f:
            self.samplingInterval = int(next(f))
            next(f)

            for line in f:
                split = line.strip().split(" ")
                if len(line) == 1:
                    break
                self.mtidToModelName[int(split[0])] = split[1]

            for line in f:
                split = line.strip().split(" ")
                self.columnNameToGid[split[1]] = int(split[0])

    def getModelTypeName(self, mtid):
        return self.mtidToModelName[mtid]

    def getGid(self, column):
        return self.columnNameToGid[column]


# Writer Functions
# The compression level for each writer is set to the highest value possible as
# the defaults differs and the lowest disable compression for some writers.
compressionPerFormat = {}

# https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_feather.html
# https://arrow.apache.org/docs/python/generated/pyarrow.feather.write_feather.html#pyarrow.feather.write_feather
compressionPerFormat['feather'] = [('zstd', 2147483647), 'lz4', 'uncompressed']
def writeFeather(path, df, compression):
    # Index must start from zero when using Feather and it cannot be excluded,
    # the compression level is left as the default to reduce the permeations.
    if type(compression) is tuple:
        df.reset_index().to_feather(path=path, compression=compression[0],
                compression_level=compression[1]) # Seems to be zstd only
    else:
        df.reset_index().to_feather(path=path, compression=compression)

# https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_hdf.html
# https://www.pytables.org/usersguide/datatypes.html
compressionPerFormat['hdf'] = ['zlib', 'lzo', 'bzip2', 'blosc',
        'blosc:blosclz', 'blosc:lz4', 'blosc:lz4hc', 'blosc:snappy',
        'blosc:zlib', 'blosc:zstd']
def writeHDF(path, df, compression):
    # Complevel is set to the highest value as it is zero (off) by default.
    df.to_hdf(path_or_buf=path.name, key='key',
            complib=compression, complevel=9, data_columns=[])

# https://pyorc.readthedocs.io/en/latest/api.html#writer
# https://stackoverflow.com/questions/58728634/convert-pandas-dataframe-from-to-orc-file
# https://github.com/noirello/pyorc/issues/2#issuecomment-577881934
compressionPerFormat['orc'] = [pyorc.CompressionKind.NONE, 
        pyorc.CompressionKind.ZLIB, pyorc.CompressionKind.ZSTD]
def writeORC(path, df, compression):
    # pyorc are used directly as pandas does not implement to_orc
    schema = []
    types = {'int32': 'int', 'datetime64[ns]': 'timestamp', 
            'object': 'binary', 'float32': 'float'}
    for column, type in zip(df.columns, df.dtypes):
        schema.append(column + ':' + types[type.name])
    schema = 'struct<' + ','.join(schema) + '>'
    schema = schema.replace('-', '_') # Prevents Error: Unrecognized character

    writer = pyorc.Writer(path, schema, compression=compression,
            compression_strategy=pyorc.CompressionStrategy.COMPRESSION)
    rows = df.itertuples(index=False, name=None)
    writer.writerows(rows)
    writer.close()

# https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_parquet.html
# https://arrow.apache.org/docs/python/generated/pyarrow.parquet.write_table.html
compressionPerFormat['parquet'] = \
        [None, 'snappy', 'gzip', ('brotli', 2147483647), 'lz4', ('zstd', 2147483647)]
def writeParquet(path, df, compression):
    if type(compression) is tuple:
        df.to_parquet(path=path, engine='pyarrow', compression=compression[0],
                compression_level=compression[1], index=False)
    else:
        df.to_parquet(path=path, engine='pyarrow', compression=compression,
                index=False)

def measureFormats(df, lightweight):
    results = {}
    if lightweight:
        return results

    global compressionPerFormat
    for writer in [writeParquet]: # sans writeHDF, writeFeather, writeORC,
        formatResults = {}
        formatName = writer.__name__[5:].lower()
        for compression in compressionPerFormat[formatName]:
            tempFile = tempfile.NamedTemporaryFile(delete=False)
            writer(tempFile, df, compression)
            tempFile.flush()
            tempFile.close()
            size = os.path.getsize(tempFile.name)
            formatResults[str(compression)] = size
            os.remove(tempFile.name)
        results[formatName] = formatResults
    return results

# Error Functions
def computeRelativeErrorUniformNorm(raw, decompressed):
    maxError = -1
    for (r, d) in zip(raw, decompressed):
        if r == d:
            error = 0.0
        else:
            error = abs((r - d) / r) * 100.0
        maxError = max(maxError, error)
    return maxError

def computeRelativeAverageError(raw, decompressed):
    diffSum = 0.0
    rawSum = 0.0
    for (r, d) in zip(raw, decompressed):
        diffSum += abs(r - d)
        rawSum += abs(r)
    return (diffSum / rawSum) * 100.0

def computeMetrics(raw, decompressed):
    return {
            'Relative_Error_Uniform_Norm': 
            computeRelativeErrorUniformNorm(raw, decompressed),
            'Relative_Average_Error': 
            computeRelativeAverageError(raw, decompressed),
            'Mean_Absolute_Value': 
            float(metrics.mean_absolute_error(raw, decompressed)),
            'Mean_Absolute_Percentage_Error': 
            float(metrics.mean_absolute_percentage_error(raw, decompressed)),
            'Mean_Squared_Error': 
            float(metrics.mean_squared_error(raw, decompressed)),
            'Fast_Dynamic_Time_Warping': fastdtw.fastdtw(raw, decompressed)[0]
            }


# Model Type
def sumModelTypesUsed(df, metadata):
    # The sampling interval is converted from millis to ns as values is in ns
    si = metadata.samplingInterval * 1000000
    mtu = {}
    for row in df.itertuples():
        modelType = metadata.getModelTypeName(row.mtid)
        dataPoints = ((row.end_time - row.start_time).value / si) + 1
        mtu[modelType] = mtu.get(modelType, 0) + int(dataPoints)
    return mtu

def int64ToTimestamp(df, column):
    df[column] = pandas.to_datetime(df[column], unit='ms')

def processFile(anOutputFile, lightweight):
    # Determine what the input files are called without the shared suffix
    if os.path.isfile(anOutputFile):
        pathWithoutSuffix = anOutputFile[:anOutputFile.rfind("output") + 7]
    elif anOutputFile.endswith("_output_"):
        pathWithoutSuffix = anOutputFile
    else:
        pathWithoutSuffix = anOutputFile + "_output_"

    # Read Parquet file with segments and converts the int64s to timestamps
    metadata = Metadata(pathWithoutSuffix + "segments_metadata.txt")
    segmentsDF = pandas.read_parquet(pathWithoutSuffix + "segments.parquet")
    int64ToTimestamp(segmentsDF, 'start_time')
    int64ToTimestamp(segmentsDF, 'end_time')

    # Read Parquet file with data points and converts the int64 to timestamps
    dataPointsDF = \
            pandas.read_parquet(pathWithoutSuffix + "data_points.parquet")
    int64ToTimestamp(dataPointsDF, 'datetime')

    # Initialize result and measure the size of the segment and data point files
    result = {}
    result['size_unit'] = 'bytes'
    result['model_type_unit'] = 'data_points'
    result['length'] = len(dataPointsDF)
    result['file'] = {
            'segments': measureFormats(segmentsDF, lightweight),
            'data_points': measureFormats(dataPointsDF, lightweight) }

    # Measure the size and the error of the segment and data point columns
    for column in dataPointsDF.columns[1:]:  # Superset of segmentsDF
        columnResults = {}
        dpcdf = dataPointsDF[[dataPointsDF.columns[0], column]]
        columnResults['data_points'] = measureFormats(dpcdf, lightweight)

        if not column.endswith('-R'):  # Raw values are not stored as segments
            scdf = segmentsDF[segmentsDF.gid == metadata.getGid(column)]
            columnResults['segments'] = measureFormats(scdf, lightweight)

            columnResults['model_types'] = sumModelTypesUsed(scdf, metadata)

            raw = dataPointsDF[column[:column.rfind('-')]  + '-R']
            decompressed = dataPointsDF[column]
            columnResults['metrics'] = computeMetrics(raw, decompressed)
        result[column] = columnResults 
    return result


# Main Function
if __name__ == '__main__':
    argv_length = len(sys.argv)
    if argv_length == 2:
        anOutputFile = sys.argv[1]
        lightweight = False
    elif argv_length == 3 and sys.argv[1] == '-l':
        anOutputFile = sys.argv[2]
        lightweight = True
    else:
        print("usage: " + str(sys.argv[0]) +" [-l] anOutputFile")
        sys.exit(0)

    result = processFile(anOutputFile, lightweight)
    print(json.dumps(result, sort_keys=True, indent=4))
