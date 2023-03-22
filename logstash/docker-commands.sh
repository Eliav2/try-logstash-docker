# local quick run: run logstash with config mounted from host
docker run --rm -it --name try-logstash -v ~/config/:/usr/share/logstash/config/ docker.elastic.co/logstash/logstash:8.6.2


# build docker image
docker build -t try-logstash:latest .

# run custom docker image
docker run --rm -it try-logstash:latest


# run docker compose
docker compose up 