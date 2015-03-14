$ sudo docker run -d -e SETTINGS_FLAVOR=dev -e STORAGE_PATH=/tmp/registry -v /opt/data/registry:/tmp/registry  -p 5000:5000 registry
