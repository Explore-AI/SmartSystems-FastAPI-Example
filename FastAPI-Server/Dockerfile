FROM python:3.9
WORKDIR /app
COPY ./requirements.txt /app/requirements.txt
RUN apt-get update && apt-get install -y freetds-dev
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt
COPY . /app
CMD ["uvicorn", "main:api", "--host", "0.0.0.0", "--port", "8000"]