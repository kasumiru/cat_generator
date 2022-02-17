FROM debian:buster


RUN apt-get update && \
apt-get install -y git python3 python3-pip && \
/usr/bin/env python3 -m pip install flask && \
git clone https://github.com/kasumiru/cat_generator.git ; \
cd cat_generator

WORKDIR /cat_generator
CMD [ "/usr/bin/python3", "/cat_generator/main.py", "5000" ]
