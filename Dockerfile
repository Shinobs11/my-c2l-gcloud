FROM gcr.io/tpu-pytorch/xla:nightly_3.8_tpuvm as begin


RUN apt-get update && apt-get install -y openssh-server
RUN groupadd sshgroup && useradd -ms /bin/bash -g sshgroup sshuser

ARG home=/home/sshuser
RUN mkdir $home/.ssh
COPY id_rsa.pub $home/.ssh/authorized_keys
RUN chown sshuser:sshgroup $home/.ssh/authorized_keys && \
    chmod 600 $home/.ssh/authorized_keys


EXPOSE 16007
EXPOSE 22

CMD service ssh start