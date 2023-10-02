FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /code

COPY requirements.txt /code/requirements.txt

RUN pip install --upgrade pip \
                --no-cache-dir -r requirements.txt

COPY . /code/

EXPOSE 8000

# ENTRYPOINT ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]