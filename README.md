# opensips-dev-dc

Docker-compose file for developig for OpenSIPS as WebRTC proxy. OpenSIPS is stateless and running in host network proxy mode.

```bash
openssl x509 -noout -text -in example.com.pem
docker compose run --entrypoint /bin/bash opensips
```