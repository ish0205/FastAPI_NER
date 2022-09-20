FROM python:3.8.14-slim
RUN apt-get update
WORKDIR /app
COPY . /app
RUN pip3 install torch>=1.6.0 --no-cache-dir
RUN python3 -m pip install en_chia_ner_pipeline_trf-0.0.0.tar.gz
RUN pip3 install -r requirements.txt
# RUN python3 -m spacy download en_core_web_sm
# RUN python3 -m pip install en_chia_ner_pipeline_trf-0.0.0.tar.gz
EXPOSE 8000
ENTRYPOINT ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000","--reload"]
# CMD ["uvicorn","main:app","--reload"]
