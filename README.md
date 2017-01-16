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
```
docker exec -it [container_name] mongo --host mongodb
```


To run tests
```
docker exec -it [container_name] python3 test.py
```

Use `docker ps` to get the container name of the api.
