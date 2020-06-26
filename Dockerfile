FROM continuumio/miniconda:4.7.12

RUN mkdir -p /app
COPY ./app /app

RUN /opt/conda/bin/conda env create -f /app/requirements.yml
ENV PATH /opt/conda/envs/motion/bin:$PATH
RUN echo "source activate motion" >~/.bashrc

RUN mkdir -p /scripts
COPY ./scripts /scripts
RUN chmod +x /scripts/*
WORKDIR /app