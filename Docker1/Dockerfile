# Use amazon linux to build packages
FROM amazonlinux
RUN yum install -y python3 python3-libs python3-devel python3-pip log unzip
RUN yum update -y python python3
COPY . /work/
WORKDIR /work

WORKDIR /work
RUN pip3 install --no-cache-dir -r requirements.txt

USER root
ENTRYPOINT ["/work/entrypoint.sh"]