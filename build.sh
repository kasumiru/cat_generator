#!/bin/bash

docker login
docker build -t kasumiru/cat_generator .
docker push kasumiru/cat_generator:latest
