# Pets-API

Build docker container
```
docker-compose build
```

Run mongodb
```
docker-compose up -d db
```

Run api
```
docker-compose run  --service-ports web
```

Connect to mongo instance
```docker exec -it `petsapi_web_run_30` mongo - h mongodb```
where `petsapi_web_run_30` is container name use `docker ps`.
