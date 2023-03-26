FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN apt update
RUN apt install -y iputils-ping
RUN apt install -y iproute2
RUN pip install --no-cache-dir -r requirements.txt


COPY . .

CMD [ "python","-u", "./server.py" ]