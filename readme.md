# RestfulFLASK

build image with `docker build --no-cache -t YOUR_IMAGE_NAME .` (this may require admin rights, i prefer --no-cache, this may take longer but ensures youre using the up to date version)
run container `docker run -d -p 5000:5000 YOUR_IMAGE_NAME ` expose container port 5000 and map it to host port 5000 the default flask port

see: https://cloud.docker.com/repository/docker/erickrg/flaskapp

### access endpoint example

go to localhost:5000/store

