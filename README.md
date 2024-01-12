# opensips-dev-dc

Docker-compose file for developig for OpenSIPS as WebRTC proxy. OpenSIPS is stateless and running in host network proxy mode.

```bash
openssl x509 -noout -text -in example.com.pem

docker compose build
docker compose up -d

docker compose run --entrypoint /bin/bash opensips

docker compose exec opensips /bin/bash
> sngrep -L udp:127.0.0.1:8888 port 8888
```
