FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8

COPY ./requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt -i https://mirrors.aliyun.com/pypi/simple/ 

COPY ./main.py /app
