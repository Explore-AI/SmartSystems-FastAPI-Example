FROM python:3.9
# Install required dependencies for pymssql
RUN apt-get update && apt-get install -y \
    freetds-dev \
    freetds-bin \
    locales \
    tdsodbc \
    unixodbc-dev
# Set the locale to UTF-8
RUN echo "en_US.UTF-8 UTF-8" > /etc/locale.gen && \
    locale-gen
# Create a working directory 
WORKDIR /app
# Copy the requirement files to the working directory
COPY ./requirements.txt /app/requirements.txt
# Install the required Python packages
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt
# Copy the rest of the application into the working directory 
COPY . /app

# start the api server
CMD ["uvicorn", "main:api", "--host", "0.0.0.0", "--port", "8001", "--reload"]