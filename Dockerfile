#FROM debian:buster
FROM alpine


#RUN apt-get update && \
#apt-get install -y git python3 python3-pip && \
#/usr/bin/env python3 -m pip install flask && \
#git clone https://github.com/kasumiru/cat_generator.git ; \
#cd cat_generator
#
#WORKDIR /cat_generator
#CMD [ "/usr/bin/python3", "/cat_generator/main.py", "5000" ]

#RUN apk add --no-cache python3 py3-pip git gcc musl-dev python3-dev linux-headers && \
#ln -s /usr/bin/python3 /usr/bin/python && \
#/usr/bin/env python3 -m pip install flask && \
#git clone https://github.com/kasumiru/cat_generator.git && \
#cd cat_generator

#RUN apk add --no-cache python3 py3-pip gcc musl-dev python3-dev git && \
#    python3 -m pip install --upgrade pip && \
#    pip install --no-cache-dir flask \
#    git clone https://github.com/kasumiru/cat_generator.git && \
#    cd cat_generator


RUN apk add --no-cache python3 py3-pip gcc musl-dev python3-dev git && \
    python3 -m pip install --upgrade pip

RUN pip install --no-cache-dir flask

RUN git clone https://github.com/kasumiru/cat_generator.git /app/cat_generator && \
    cd /app/cat_generator

RUN if [ -f /app/cat_generator/requirements.txt ]; then \
        pip install --no-cache-dir -r /app/cat_generator/requirements.txt; \
    fi

RUN echo $(date)


WORKDIR /app/cat_generator

# WORKDIR /cat_generator
CMD [ "/usr/bin/python3", "/app/cat_generator/main.py", "5000" ]

