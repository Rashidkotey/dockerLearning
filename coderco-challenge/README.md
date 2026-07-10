README FOR MAIN CODERCO CHALLENGE

The challenge was to: Create a multi-container application that consists of a simple Python Flask web application and a Redis database. The Flask application should use Redis to store and retrieve data.

The count.py file contains the config for the flask application. The initial config was just to print ‘Welcome to the CoderCo Container Challenge
‘ On the main route (/) and then count the number of times the page is been visited, which is seen as ‘This page has been visited {count} times.
‘ , when you visit the count route (/count).
The {count} is defined in the code as the number of times a user visits the page. So on the page you will see something like this: ‘This page has been visited 17 times.’  Meaning the page has been visited 17 times.

I wrote the Dockerfile and the docker compose file but built the image all at once using the docker compose file instead of building the image using the Dockerfile before running  it again using the docker compose.

In this application I used redid as the database. I used the redid container on the port 6379 and the latest version of it.

I used volumes to make the data persistent. This will allow user to continue from where they left even when the container goes down. The logic behind it is that, docker containers are ephemeral - this means that data inside a container is deleted when the container stops or is removed. The explanation of the ephemeral is what happens when you don’t use volumes, the user has to always start again whenever the container goes down and back up. Volumes detach data from the container lifecycle, all data will still be available after container goes down or even the host reboots.

I decided to implement load balancing  and reverse proxy using nginx.
In the case where there is a lot of users accessing the web, one web service or container may not be able to handle the load so I have to scale the container during those periods.
In the count.py file I imported ‘os’, then instead of hard coding the ports for the database (redid) I created an environment variable for the redis host and port.
In the docker-compose file I defined the environment variable and exposed only port-5002 instead of binding the port to the host (5002:5002).
The reason for this is that since a lot of users are going to be visiting the site from different systems, if we bind the host to the port of the web service only one user will be able to visit the site (i.e the host). So I have to expose 5002 so that users can connect to that port from any system and then I use the nginx to reverse proxy it to the container.

The file ‘dockercomposefile-onDockerChallenge-nginxchange’ contains the config for the docker compose having the nginx change and the file ‘nginxconfigfile-forDockerChallenge’ contains the nginx configs.