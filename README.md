# Tech Demo

## Introduction

### What is Docker?
Docker is a way to avoid the problem "it works in my machine" which could be costly.
The way Docker avoid this problem is to create a "virtual machine" called a container.
Container is basically a virtual machine that involved less work because it shares kernel 
unlike regular virtual machine where it has its own kernel
This means that Docker is very lightweight and fast to startup which is very useful when doing application development.

Within this demo, we hope this will be useful during your project since Docker is a useful tool for sharing code
since every container has the same library depending on the installation.

![](./git-images/containers-vs-virtual-machines.jpg "Containers vs VM")

Image Source: https://www.weave.works/blog/a-practical-guide-to-choosing-between-docker-containers-and-vms

Before starting, make sure to have Docker downloaded, which can be found in https://www.docker.com/

## Container

Creating a container from scratch is not what you should do with Docker, but it is necessary to know how container works,
so we will show how to solely create container.

In order to create a container:

1. Find a Docker Image on which you would like your container to be based on.
We can start by using Ubuntu by running this command on your CLI.

~~~ 
docker pull Ubuntu 
~~~

2. Name the container on whatever name you like, this way we can create the container
in which we can use them as a Ubuntu container
~~~
docker run -d -t —name [name of container] Ubuntu
~~~

3. In order to show the running processeses of list of containers you can run this on your CLI
~~~
docker ps
~~~

4. To execute or run the Docker container we can use the command
~~~
docker exec -it [name of container] bash
~~~

As we can see, we will have a running container in which it has everything installed including
Ubuntu as our base. We can use bash like any Ubuntu machine. However, take note that we cannot really 
change files because containers alone does not support persistent data storage in which we will talk about
briefly in Volumes.

In order to see the list of images, we can go to this site:
https://hub.docker.com

## Images

Creating Docker images is usually what people would use since this is usually what people share their code with.
Docker images is very important especially during deploying to a server as well since it gives instructions on how the Docker
Container is going to be setup. 

In order to create a Docker Container, just follow these steps:

0. Check Dockerfile within this directory to see the lists of useful syntax to create images

1. Create a Dockerfile to the directory

2. Dockerfile consists of a list of commands to make a docker image. 

3. Create .dockerignore in order to exclude unwanted files (similar to .gitignore)

4. Docker is a bit weird it runs on 0.0.0.0, so whenever there is a local server involved, it should be binded to 0.0.0.0

5. After the Dockerfile has been fully setup, we can build them by typing this in our CLI
~~~
docker build . -t [image name]
~~~

6. Then, we can just run them by typing this within our CLI
~~~ 
docker run -p [host port]:[docker port] [docker image id]
~~~

By following these steps we have ourselves a Docker image ready to deploy and shared.

If you are someone who is using a shared Docker that has already been setup via a Dockerfile, feel free to just run this on your CLI

~~~
docker build . -t [image name]
docker run -p 8000:8000 [docker image id]
~~~

## Volumes

Since Docker Container does not save the changes that are made, Docker has a way to do save them which is called **Volumes**. 
Volumes are a way for Docker to share the host's file with the Docker container in order to save them in a persistent way.
This way, Docker can keep track the changes being made in the host's file and send them to a container making them persistent.

## Docker in render

Check this: https://render.com/docs/docker


