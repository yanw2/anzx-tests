# Technical Tests 1

## Java Keystore vs. Truststore

Keystore is used to store private key and identity certificates that a specific program should present to both parties (server or client) for verification.

Truststore is used to store certificates from Certified Authorities (CA) that verify the certificate presented by the server in SSL connection.

## Solution

This dictory containers a multi-stage Dockerfile to build a Java container with a custom ceritifcate included in the default Java truststore file.

The first stage generates the updated truststore file and in a more practical example would be used for application build, the output being a JAR / WAR file ready for deployment.

The second stage copies the newly generated truststore file into the system default location and is levergaing the JRE image. This reduces the overall size of the resulting image and reduces the attack surface. However the image is still ~280MB and could most likely be reduced further if tuned correctly for the required application stack. An example would be potentially starting with Alpine Linux if there is no issues using differnet C libraries.
