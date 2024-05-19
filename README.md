# opensips-dev-dc

Docker-compose file for testing OpenSIPS load using Python module with multiple SSL calls.

```bash
openssl x509 -noout -text -in example.com.pem

docker compose build
docker compose up -d
docker compose logs -f opensips

docker compose run --entrypoint /bin/bash opensips

docker compose exec opensips /bin/bash
> sngrep -L udp:127.0.0.1:8888 port 8888
> sippts flood -i 127.0.0.1 -r 6051 -m OPTIONS -p tls -v -n 100000 -th 300
```
