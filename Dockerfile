# This code uses python as the base image
FROM python:3.12-slim

# sets the working directory inside the container
WORKDIR /app

# This code copies the requirements file first
COPY requirements.txt .

# installs all the dependencies needed
RUN pip install -r requirements.txt

# copies the rest of the code
COPY . .

# tells the docker which port the app must runs on
EXPOSE 5000

# This is the command to run the app
CMD ["python", "app.py"]