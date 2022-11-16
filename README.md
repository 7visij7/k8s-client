# K8s-client
> Application allow create, delete, check and get list of namespaces in k8s cluster, except customs namespace.
> You can define custom namespeces [here](https://github.com/7visij7/k8s-client/blob/main/k8s_client/config/__init__.py#L2)

---

## Required variables and config
> Required enviroment variables: 
+ API_KEY - App access token.

[Here](https://github.com/7visij7/k8s-client/blob/main/k8s_client/config/swagger.yaml) is configuration for swagger.

---
## Docker
> Build Docker image from a [Dockerfile](https://github.com/7visij7/k8s-client/blob/main/Dockerfile)
```
docker build -t IMAGE_NAME
```
---

## Kubernetes

> Deploy to kubernetes cluster.
```Bash
kubectl create namespace devops
kubectl apply -f k8s/ -n namespace devops
```
---

## Gitlab CI pipelins

>  Change for you configuration parameters in [.gitlab-ci.yml](https://github.com/7visij7/k8s-client/blob/main/.gitlab-ci.yml).


## Gitlab CI pipelins
Application allows users to created, delete and check namespace in kubernetes, except systems namespace.

## How it works

> Examples of requests:
+ to create namespace:
  
        curl -X POST   'http://k8s-client.dev-company.k8s/api/v1/namespace/create'   -H 'X-API-KEY: SECRET_TOKEN'  -H "Content-Type: application/json"  --data '{"namespace":"somenamespace"}'
     

+ to ckeck namespace:

        curl -X POST   'http://k8s-client.dev-company.k8s/api/v1/namespace/check'   -H 'X-API-KEY: SECRET_TOKEN'  -H "Content-Type: application/json"  --data '{"namespace":"somenamespace"}'

+ to delete namespace:

        curl -X POST   'http://k8s-client.dev-company.k8s/api/v1/namespace/delete'   -H 'X-API-KEY: SECRET_TOKEN'  -H "Content-Type: application/json"  --data '{"namespace":"somenamespace"}'
