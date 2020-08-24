# docker_flask
**A demo flask app in docker** 

#### Inspiration
A diversion from the (docker curriculum)[https://docker-curriculum.com/], I wanted to create a simple flask app to see how flask works.

#### To built and run the dockerized app
```
docker build --no-cache -t flask_site:test .
sudo docker run -d -p 8000:5000 flask_site:test
```
The following commands will help to check whether the app is running or exited!
```
docker ps -a 
docker logs $container_id
```
