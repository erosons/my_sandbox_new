FROM quay.io/astronomer/astro-runtime:12.1.1
WORKDIR /home
COPY java.sh .
COPY . .
RUN ls -ltr
USER root
RUN chmod +x java.sh && ./java.sh