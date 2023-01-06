#coding:utf-8
import sys

import uvicorn
from fastapi import FastAPI

version = f"{sys.version_info.major}.{sys.version_info.minor}"

app = FastAPI()


@app.get("/")
async def read_root():
    message = f"Hello world! From FastAPI running on Uvicorn with Gunicorn. Using Python {version}"
    return {"message": message}


if __name__ == "__main__":
    uvicorn.run(app="main:app", host="127.0.0.1", port=8080, reload=True, log_level='debug')