URL Shortener Application
This application utilizes Flask, Celery, SQLAlchemy, and Swagger to shorten URLs. Users can input a URL, and the application generates a shorter link that redirects to the original URL when accessed in a browser.

Features
Shortens URLs and stores them in an SQLite3 database.
Returns a clickable link that redirects to the original URL.
Fully prepared for containerization with Docker.

Getting Started
Prerequisites:
Ensure you have Docker installed on your machine.
All required dependencies are stored in requirements.txt file
Build the Docker Image
To containerize the application, navigate to your project directory and run the following command in your terminal:

docker build -t <your_image_name> .

To build the container use: 

docker-compose up --build

Configuration
In the config.py file, there are two commented lines.

If you uncomment these lines, the application will return the properly generated link using SQIDs.
If they remain commented, the application will return the Celery task ID instead.
This behavior is due to the Celery configuration for the development environment, which never changes the task status from PENDING.

Usage:
Run the application using Docker.
Access the application through your web browser.
Application is set to work on 127.0.0.1:5000
Input a URL to generate a shortened link.
To access SwaggerUI API description go to 127.0.0.1:5000/swagger
