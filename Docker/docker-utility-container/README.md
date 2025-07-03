Introduction
Now that you’ve installed Docker and learned it’s basic commands, it’s time to try out some Docker utilities to make managing your Docker environment a little bit easier. These 6 utilities, aim to help you control, monitor and/or manage your docker host.

## Ctop
    Ctop Docker Utilities
    Ctop is a command line utility that serves as a process and resource monitor similar to the top command on a Linux machine. It is similar to the docker stats command as it displays resource usage for each of the running containers on your docker host machine.

    In addition to showing an overview of the resource utilization of all of your running containers, ctop also allows you to “zoom in” and CPU, memory, and network utilization of any of your specific containers.

    6 Awesome Docker Utilities Everyone Should Try 1
    Installation of ctop is as simple as running the following commands on a Linux machine:

    sudo wget https://github.com/bcicen/ctop/releases/download/v0.7.3/ctop-0.7.3-linux-amd64 -O /usr/local/bin/ctop

    sudo chmod +x /usr/local/bin/ctop
    or the following commands on a machine running OS/X:

    sudo curl -Lo /usr/local/bin/ctop https://github.com/bcicen/ctop/releases/download/v0.7.3/ctop-0.7.3-darwin-amd64

    sudo chmod +x /usr/local/bin/ctop
    ctop is also available to run as a docker container by running the following docker run command.


    docker run --rm -ti \
    --name=ctop \
    --volume /var/run/docker.sock:/var/run/docker.sock:ro \
    quay.io/vektorlab/ctop:latest


## Portainer
    Portainer Containers Screen
    Portainer is an open-source application that provides a web based interface that you can use to manage your Docker host. It allows you to complete all of the basic function of managing your containers without having to use the command line interface. Portainer allows you to create and manage containers, images, volumes, and networks. You can even manage your Docker swarm.

    Portainer runs inside a Docker container. You can simply run the following docker run command to get it up and running, or you visit the guide on How to Install and Configure Portainer.

    docker run -d \
    -p 8000:8000 \
    -p 9000:9000 \
    --name=portainer \
    --restart=always \
    -v /var/run/docker.sock:/var/run/docker.sock \
    -v portainer_data:/data \
    portainer/portainer 


## Watchtower
    6 Awesome Docker Utilities Everyone Should Try 2
    Watchtower is a docker container that keeps an eye on the registry for new versions of your running containers. When it detects an updated container, it pulls the new image from the registry and then stops the old container, and starts a new container with the new image. It even manages to maintain all of your original variables in the process! Watchtower is a fantastic way to keep all of your docker containers/applications updated to the latest version. You can use the docker run command below to start a Watchtower container, or you can view the detailed guide on Watchtower.


    docker run -d \
    --name watchtower \
    -v /var/run/docker.sock:/var/run/docker.sock \
    containrrr/watchtower
