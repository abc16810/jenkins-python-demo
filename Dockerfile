FROM tiangolo/uvicorn-gunicorn:python3.8-slim

COPY ./requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt -i https://mirrors.aliyun.com/pypi/simple/

COPY ./main.py /app