# YOU must run "sbt assbmely" before running docker build
FROM openjdk:latest
RUN mkdir -p /app/data
COPY redd.h2.mv.db /app/
COPY target/scala-2.12/ModelarDB.jar /app/ModelarDB.jar
COPY conf/redd.conf /app/conf/redd.conf
WORKDIR /app
EXPOSE 9999
ENTRYPOINT ["java", "-jar", "ModelarDB.jar"]
CMD ["conf/redd.conf"]