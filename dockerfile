FROM python:3.10-slim-buster

# Set the work directory of table get
RUN mkdir -p /var/layout_table/temp
WORKDIR /var/layout_table

# ADD ./sources.list /etc/apt/
# RUN apt-get update && apt-get install -y poppler-utils

ENV TZ "Asia/Shanghai"
ENV DEBIAN_FRONTEND noninteractive
ENV PIP_NO_CACHE_DIR off
RUN sed -i 's|http://deb.debian.org/debian|http://mirrors.aliyun.com/debian|g' /etc/apt/sources.list

# RUN pip install  --upgrade pip -i http://pypi.tuna.tsinghua.edu.cn/simple --trusted-host pypi.tuna.tsinghua.edu.cn
# RUN pip install --upgrade pip

# RUN pip install cupy-cuda11x -i http://pypi.tuna.tsinghua.edu.cn/simple --trusted-host pypi.tuna.tsinghua.edu.cn
# RUN pip install --progress-bar off --no-cache-dir --extra-index-url http://pypi.tuna.tsinghua.edu.cn/simple --extra-index-url http://pypi.nvidia.com nx-cugraph-cu11 --trusted-host pypi.nvidia.com --trusted-host pypi.tuna.tsinghua.edu.cn

#RUN pip install  nx-cugraph-cu11  -i http://pypi.nvidia.com --trusted-host pypi.nvidia.com

# RUN ./test.sh
COPY ./requirements.txt /var/layout_table/temp/requirements.txt
RUN apt-get update && \
    apt-get install -y gcc g++ make && \
    apt-get install -y libgl1-mesa-glx libglib2.0-0 && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*
RUN pip install -r /var/layout_table/temp/requirements.txt --no-deps -i http://pypi.tuna.tsinghua.edu.cn/simple --trusted-host pypi.tuna.tsinghua.edu.cn
LABEL org.opencontainers.image.authors="wang xin"
ADD ./ /var/layout_table/
CMD ["bash","/var/layout_table/test.sh"]

