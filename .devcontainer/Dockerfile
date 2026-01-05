FROM ubuntu:24.04
ENV DEBIAN_FRONTEND=noninteractive
ARG HOME="/home/user"
ARG VERSION="8.5.1rc1"
ARG TARGETARCH
ARG BAZEL_RELEASE_URL="https://github.com/bazelbuild/bazel/releases/download/8.5.1rc1/"
RUN apt-get update && apt-get -y install \
    build-essential \
    git \
    python3 \
    wget && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*
RUN useradd -rm -d ${HOME} -s /bin/bash -g root -G sudo -u 1001 user
RUN chown -R user ${HOME}
RUN case "${TARGETARCH}" in "amd64") ARCH=x86_64;; "arm64") ARCH=arm64;; esac && \
    FILE=bazel-${VERSION}-linux-${ARCH} && \
    wget -O /usr/bin/bazel ${BAZEL_RELEASE_URL}/${FILE} && chmod a+x /usr/bin/bazel
USER user
