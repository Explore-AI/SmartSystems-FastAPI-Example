<h1 align=center><strong>FastAPI API & React Client POC</strong></h1>

The purpose of this Repo is to explore the capabilities of the FastAPI framework for building backend services and APIs. By creating a sample repository, we aim to showcase how FastAPI can be used to develop high-performance, scalable, and easy-to-maintain web services. Additionally, this project will help us evaluate the benefits and limitations of the FastAPI framework, including its performance, ease of use, documentation, community support, and compatibility with other tools and technologies. This project utilizes the following tech stack:

- 🐍 [FastAPI](https://fastapi.tiangolo.com/) - a modern, fast (high-performance), web framework for building APIs with Python.
- 🐳 [Docker](https://www.docker.com/) - a containerization platform used to package and run the application in a portable environment.
- 📊 [Microsoft SQL Server](https://learn.microsoft.com/en-us/sql/linux/quickstart-install-connect-docker?view=sql-server-ver16&pivots=cs1-bash) - a relational database management system that provides a robust and scalable data storage solution.
- 🦜 [Pydantic](https://pydantic-docs.helpmanual.io/) - a data validation and serialization library that provides runtime checking and validation of data types and structures.
- 🗃️ [SQLAlchemy](https://www.sqlalchemy.org/) - an Object Relational Mapper (ORM) that provides a high-level abstraction for working with databases in Python.
- 🚀 [uvicorn](https://www.uvicorn.org/) - a fast, ASGI (Asynchronous Server Gateway Interface) server that provides a lightning-fast web server interface for the FastAPI framework.

## Running the project

This project runs using docker desktop and will automatically install the neccesary packages in the requirements.txt file.
The project requires a database connection on startup and for that we use a docker-compose file to
spin up an instance of MSSQL server allongside our API container.

```shell
 cd /SmartSystems-FastAPI-Example # Navigate the ROOT project directory
 $ export ENVIRONMENT=dev  # Set the ENVIRONMENT variable to "dev"
 $ docker-compose build  # Build the Docker images for the services defined in docker-compose.yml
 $ docker-compose up -d  # Start the containers in the background
```


## Benefits of FastAPI

- **Fast Performance**: FastAPI is one of the fastest Python web frameworks out there. It can handle high-traffic applications with ease due to its high-speed ASGI server.

  Reference: [FastAPI Performance](https://fastapi.tiangolo.com/benchmarks/)

- **Easy to Use**: FastAPI is very easy to use, even for developers who are new to Python. Its syntax is concise and intuitive, making it easy to write and read code.

  Reference: [FastAPI Tutorial](https://fastapi.tiangolo.com/tutorial/)

- **Auto-Generated Documentation**: FastAPI can automatically generate documentation for your API based on your code, using the OpenAPI standard. This saves a lot of time and effort when it comes to documenting your API.

  Reference: [FastAPI Documentation](https://fastapi.tiangolo.com/)

- **Type Annotations**: FastAPI uses Python's type hints extensively, which helps with code readability and eliminates the need for manual data validation.

  Reference: [FastAPI Tutorial - Data Types](https://fastapi.tiangolo.com/tutorial/body-multiple-params/#more-about-data-types)

## Drawbacks of FastAPI

- **Limited Ecosystem**: FastAPI is a relatively new framework, so its ecosystem is not as mature as some of the other Python frameworks. This means that finding libraries and tools for FastAPI can sometimes be challenging.

- **Steep Learning Curve**: While FastAPI is easy to use for developers who are familiar with Python, it can be a bit challenging for those who are not. The framework has a lot of features and concepts that may take some time to get used to.

- **Dependency Issues**: Since FastAPI is a relatively new framework, there may be issues with dependencies that haven't been ironed out yet. This can lead to compatibility issues with other packages and libraries.(a lot of libraris and docker images do not fully support arm64 architecture of new Mac M1 chips)

## Gotchas

- **API Schema Generation**: While FastAPI's auto-generated documentation is a great feature, it can sometimes lead to issues when dealing with complex data models. The schema generation may not always be accurate, so it's important to double-check the generated documentation.

- **Performance vs Compatibility**: FastAPI's high performance comes at the cost of compatibility with some older web servers and operating systems. It's important to ensure that your server and operating system are compatible with FastAPI before you start building your API.

- **Security**: FastAPI does not provide built-in security features, so you'll need to implement your own authentication and authorization mechanisms. This can be a bit challenging, especially if you're new to web development.

## Conclusion

Overall, FastAPI is a powerful and easy-to-use framework for building back-end services and APIs. It offers fast performance, automatic documentation generation, and type annotations that help with code readability. However, it's still a relatively new framework with a limited ecosystem and a steep learning
