# Running the microservice using Command Line and Docker

This README provides instructions on how to run the microservice using both commandline and docker. It exposes an API that accepts an image and returns a list of rectangles within the image and their respective vertices inform of coordinates.

## Table of Contents

1. [Running the microservice using Command Line](#running-the-microservice-using-command-line)
   - [Create an environment](#create-an-environment)
   - [Install Dependencies](#install-dependencies)
   - [Run the microservice](#run-the-microservice)
   - [Running tests](#running-tests)

2. [Building and running the microservice using Docker](#building-and-running-the-microservice-using-docker)
   - [Build or pull a prebuilt Docker Image](#build-or-pull-a-prebuilt-docker-image)
   - [Run the Docker Container](#run-the-docker-container)
   - [Running tests](#running-tests-1)

3. [Using the API](#using-the-api)
   - [Sample Request](#sample-request)

## Running the microservice using Command Line

### Create an environment

Create and activate a virtual environment.

```bash
python3 -m venv venv
source venv/bin/activate
```

### Install Dependencies

Install the necessary Python dependencies for the microservice.

```bash
pip3 install --upgrade pip setuptools wheel
pip3 install -r requirements.txt
```

### Run the microservice

Execute the microservice using the following command:

```bash
python app.py
```

### Running tests

Execute tests using the following command:

```bash
cd tests && python3 -m pytest
```

## Building and running the microservice using Docker

### Build or pull a prebuilt Docker Image

To build the Docker image using the provided Dockerfile.

```bash
docker build -t rect-coords-api --target=production .
```

To use a prebuilt image.

```bash
docker pull noahnsimbe/rect-coords-api
docker tag noahnsimbe/rect-coords-api rect-coords-api
```

### Run the Docker Container

Run the Docker container using the built image.

```bash
docker run -p 5000:5000 rect-coords-api
```

### Running tests

Execute tests using the following commands:

```bash
docker build -t rect-coords-testing --target=testing .
docker run rect-coords-testing
```

## Using the API

Once the microservice is running, you can send requests to it to receive a response. Make sure to send a png image file in the request. An example image `simple.png` has been provided

The returned vertices(coordinates) are in the order of `top-left`, `bottom-left`, `bottom-right` and`top-right`.

## Sample Request

```bash
curl -s -X POST -F "file=@tests/simple.png" http://localhost:5000/extract-rect-coords | jq .
```

You can verify the coordinates using `https://www.mobilefish.com/services/record_mouse_coordinates/record_mouse_coordinates.php`
