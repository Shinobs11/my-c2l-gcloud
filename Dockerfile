FROM python:3.11-buster as apt_packages



FROM apt_packages as copy_reqs
COPY ./my-c2l/requirements.txt /tmp/requirements.txt

FROM copy_reqs as python_packages
RUN --mount=type=cache,mode=0777,target=/var/cache/pip \
/usr/local/bin/python3 -m pip install -r /tmp/requirements.txt

FROM python_packages as copy_files
WORKDIR /src
COPY ./my-c2l/* ./