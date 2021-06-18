FROM python:3.8-alpine
LABEL maintainer="HWANIL KIM"

ENV PYTHONUNBUFFERED 1
#ENV PATH="/scripts:${PATH}"

RUN ls
COPY ./requirements.txt /requirements.txt
RUN apk add --update --no-cache postgresql-client
RUN apk add --update --no-cache --virtual .tmp-build-deps \
      gcc libc-dev linux-headers postgresql-dev python3-dev jpeg-dev zlib-dev
RUN pip install --upgrade pip
#RUN pip install -U --force-reinstall pip
RUN pip install -r /requirements.txt
RUN apk del .tmp-build-deps

RUN mkdir /app
WORKDIR /app
COPY ./app /app

#RUN adduser --disabled-password --gecos '' user
#USER user


#RUN pip install --upgrade pip
#
#RUN apt-get update && apt-get install -y --no-install-recommends \
#    vim \
#    locales \
#    netcat \
#    && rm -rf /var/lib/apt/lists/*
#
#RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y locales
#RUN sed -i -e 's/# ko_KR.UTF-8 UTF-8/ko_KR.UTF-8 UTF-8/' /etc/locale.gen && \
#    dpkg-reconfigure --frontend=noninteractive locales && \
#    update-locale LANG=ko_KR.UTF-8
#
## Set TimeZone Seoul
#RUN ln -sf /usr/share/zoneinfo/Asia/Seoul /etc/localtime
#
#RUN locale-gen ko_KR.UTF-8
#ENV LANG ko_KR.UTF-8
#ENV LANGUAGE ko_KR:en
#ENV LC_ALL ko_KR.UTF-8
#
#RUN mkdir /app
#WORKDIR /app
#COPY ./requirements.txt .
#RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt
#COPY ./app /app
#COPY ./scripts /scripts
#RUN chmod +x /scripts/*
#
##EXPOSE 8000
#
#RUN mkdir -p /vol/web/media
#RUN mkdir -p /vol/web/static
#RUN chown -R user:user /vol/
#RUN chmod -R 755 /vol/web
#
#VOLUME /vol/web
#CMD ["entrypoint.sh"]
