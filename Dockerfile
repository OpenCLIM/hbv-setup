FROM python:slim

WORKDIR /src

COPY run.py .

CMD ["python", "run.py"]