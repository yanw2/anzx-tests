# build stage
FROM openjdk:9-jdk-slim AS build-jdk
COPY cacerts/ca_certs.pem /usr/local/share/ca-certificates/certificates
RUN apt-get update && \
    apt-get install --no-install-recommends -y -qq ca-certificates-java && \
    update-ca-certificates

# final stage
FROM openjdk:9-jdk-slim
COPY --from=build-jdk /etc/ssl/certs/java/cacerts /etc/ssl/certs/java/
RUN groupadd --gid 1000 java && \
    useradd --uid 1000 --gid java --shell /bin/bash --create-home java && \
    chmod -R a+w /home/java
WORKDIR /home/java
