FROM python:3

ARG BUILD_SIGNATURE
ARG BUILD_NUMBER
ARG GIT_COMMIT
ARG BUILD_VERSION

LABEL org.opencontainers.image.authors=$BUILD_SIGNATURE \
      org.opencontainers.image.source="https://github.com/FforFrodo/Endocode" \
      org.opencontainers.image.build_number=$BUILD_NUMBER \
      org.opencontainers.image.commit=$GIT_COMMIT \
      org.opencontainers.image.title="/fforfrodo/endocode" \
      org.opencontainers.image.description="Endocode Challenge" \
      org.opencontainers.image.version=$BUILD_VERSION \
      org.opencontainers.image.helloworld="/helloworld" \
      org.opencontainers.image.versionz="/versionz"

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y git
    
RUN git clone https://github.com/FforFrodo/Endocode

COPY . .

CMD [ "python", "./run.py" ]