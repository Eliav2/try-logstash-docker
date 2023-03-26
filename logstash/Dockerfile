FROM docker.elastic.co/logstash/logstash:8.6.2
# install mongoDB plugin

USER root
RUN apt update
RUN apt install -y iputils-ping
RUN apt install -y iproute2

USER logstash
RUN logstash-plugin install logstash-output-mongodb logstash-filter-json_encode

# RUN rm -f /usr/share/logstash/pipeline/logstash.conf
COPY pipeline/ /usr/share/logstash/pipeline/
COPY config/ /usr/share/logstash/config/
