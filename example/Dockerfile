FROM python:3.6

RUN adduser --disabled-password --gecos '' developer
RUN mkdir -p /home/developer
RUN mkdir -p /root/.pycharm_helpers
RUN chown developer /home/developer
RUN chmod -R 0777 /home/developer

ADD ./requirements.txt /opt/requirements.txt

RUN pip install --upgrade pip
RUN pip install -r /opt/requirements.txt

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
       git-core \
       build-essential \
       libssl-dev libfreetype6-dev libfreetype6 libfontconfig1-dev libfontconfig \
       ffmpeg
