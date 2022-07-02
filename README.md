# k8s-client
Application allows users to created, delete and check namespace in kubernetes, except systems namespace.

Examples of requests:
To create namespace:
curl -X POST   'http://k8s-client.dev-company.k8s/api/v1/namespace/create'   -H 'X-API-KEY: SECRET_TOKEN'  -H "Content-Type: application/json"  --data '{"namespace":"somenamespace"}'
To ckech namespace:
curl -X POST   'http://k8s-client.dev-company.k8s/api/v1/namespace/check'   -H 'X-API-KEY: SECRET_TOKEN'  -H "Content-Type: application/json"  --data '{"namespace":"somenamespace"}'
To delete namespace:
curl -X POST   'http://k8s-client.dev-company.k8s/api/v1/namespace/delete'   -H 'X-API-KEY: SECRET_TOKEN'  -H "Content-Type: application/json"  --data '{"namespace":"somenamespace"}'
