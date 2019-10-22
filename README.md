# opensips-dev-dc

Docker-compose file for developig for Opensips and Asterisk as a backend helper

Here also included rtpengine build with G.729 support

Get it with
 ```
 docker build \
    -t rtpengine:build \
    -f Dockerfile.rtpengine_builder \
    .

docker create \
    --name rtpengine-build \
    rtpengine:build

docker cp rtpengine-build:/usr/src/*.deb ./deb
 ```