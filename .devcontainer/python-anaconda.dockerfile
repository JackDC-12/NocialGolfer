FROM continuumio/anaconda3

RUN python3 -m pip install --user --upgrade clingo

ENTRYPOINT [ "bin/bash" ]