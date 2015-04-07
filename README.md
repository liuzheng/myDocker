
# Install Guide

    apt-get install apt-transport-https
    apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys 36A1D7869245C8950F966E92D8576A8BA88D21E9
    bash -c "echo deb https://get.docker.io/ubuntu docker main > /etc/apt/sources.list.d/docker.list"
    apt-get update
    apt-get install lxc-docker -y --force-yes

    cat <<EOF>> /etc/default/docker
    DOCKER_OPTS="-H unix:///var/run/docker.sock -H 0.0.0.0:4243 --insecure-registry 10.58.113.37:5000"
    EOF

    sudo docker run -d -e SETTINGS_FLAVOR=dev -e STORAGE_PATH=/tmp/registry -v /opt/data/registry:/tmp/registry  -p 5000:5000 registry
