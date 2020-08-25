# docker_flask
**A demo flask app in docker** 

#### Inspiration
A diversion from the [docker curriculum](https://docker-curriculum.com/), I wanted to create a simple flask app to see how flask works.

Further traveling into the Flask road, I found the youtube tutorial by [Corey Schafer](https://www.youtube.com/playlist?list=PL-osiE80TeTs4UjLw5MM6OjgkjFeUxCYH) and dived deep into creating a blog website using Flask. 

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
