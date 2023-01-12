FROM myregistry.io:8088/tiangolo/uvicorn-gunicorn:python3.8-slim

COPY ./requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt -i https://mirrors.aliyun.com/pypi/simple/ --proxy 10.4.56.230:3128

COPY ./main.py /app