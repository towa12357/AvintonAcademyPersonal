# [Apache Superset 概要と環境構築](https://avinton.com/academy/apache-superset-overview-and-environment-setup/)
## Prerequisite
- [Install Docker Engine on Ubuntu](https://docs.docker.com/engine/install/ubuntu/)

## Procedure
- Install ApacheSuperset
```
git clone -b 1.5.0 https://github.com/apache/superset.git
cd superset
docker-compose -f docker-compose-non-dev.yml up -d
```

## Review

