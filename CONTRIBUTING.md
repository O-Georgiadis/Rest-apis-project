# CONTRIBUTING


## How to build a docker image
````
docker build -t IMAGE_NAME .

````

## How to run the Dockerfile locally

````
docker run -dp 5000:5000 -w /app -v "$(pwd):/app" IMAGE_NAME sh -c "flask run --host 0.0.0.0"

````