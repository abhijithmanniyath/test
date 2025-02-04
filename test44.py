# Use a lightweight base image
FROM ubuntu:22.04

# Set environment variables
ENV DEBIAN_FRONTEND=noninteractive

# Install necessary dependencies
RUN apt-get update && apt-get install -y \
    curl \
    wget \
    git \
    vim \
    bash-completion \
    ca-certificates \
    iproute2 \
    jq \
    && rm -rf /var/lib/apt/lists/*

# Install kubectl
RUN curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl" && \
    chmod +x kubectl && mv kubectl /usr/local/bin/

# Install Helm
RUN curl -fsSL https://raw.githubusercontent.com/helm/helm/main/scripts/get-helm-3 | bash

# Install Kustomize
RUN curl -s "https://api.github.com/repos/kubernetes-sigs/kustomize/releases/latest" | \
    grep browser_download_url | grep linux_amd64 | cut -d '"' -f 4 | wget -qi - && \
    mv kustomize /usr/local/bin/ && chmod +x /usr/local/bin/kustomize

# Set working directory
WORKDIR /root

# Default command
CMD ["/bin/bash"]

