FROM python:3.7-slim
RUN apt-get clean
RUN apt-get update
RUN apt-get install -y --no-install-recommends
RUN apt-get install -y git gcc musl-dev python3-dev
RUN apt-get install -y --no-install-recommends build-essential
RUN apt-get install -y --no-install-recommends libglib2.0-0
RUN apt-get install -y --no-install-recommends libsm6
RUN apt-get install -y --no-install-recommends libxext6
RUN apt-get install -y --no-install-recommends libxrender-dev
COPY requirements.txt ./requirements.txt
RUN pip install -r requirements.txt

ENV CUDA_HOME=/
RUN git clone https://github.com/NVIDIA/apex
RUN cd apex
RUN ls
# RUN pip install -v --disable-pip-version-check --no-cache-dir --global-option="--cpp_ext" --global-option="--cuda_ext" ./apex
RUN pip install -v --disable-pip-version-check --no-cache-dir ./apex



COPY . ./