#!/bin/bash

docker pull postgres
sudo amazon-linux-extras enable python3.8
sudo yum install python3.8

docker run -p 5432:5432 -d \
-e POSTGRES_USER="guido" \
-e POSTGRES_PASSWORD="1234" \
-e POSTGRES_DB="mutt" \
-v ${PWD}/pg-data:/var/lib/postgresql/data \
--name pg-container \
postgres # Docker image

psql -U guido -d mutt