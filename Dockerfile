FROM python:3.7
COPY ./requirements.txt /app/requirements.txt
COPY ./setup.py /app/setup.py
RUN mkdir -p /app/audio_features_extraction/ && \
    touch /app/audio_features_extraction/__init__.py
WORKDIR /app
RUN apt-get update && apt-get install libsndfile1 -y
RUN apt-get update \
&& apt-get install -y \
        build-essential \
        cmake \
        git \
        wget \
        unzip \
        yasm \
        pkg-config \
        libswscale-dev \
        libtbb2 \
        libtbb-dev \
        libjpeg-dev \
        libpng-dev \
        libtiff-dev \
        libavformat-dev \
        libpq-dev
RUN pip install -r requirements.txt && \
    rm -rf /tmp/pip* /root/.cache
ADD ./ /app
RUN pip install -e . && \
    rm -rf /tmp/pip* /root/.cache