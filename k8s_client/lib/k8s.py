from kubernetes import client
import os


def get_bearer():
    with open('/var/run/secrets/kubernetes.io/serviceaccount/token') as fd:
        BEARER_TOKEN = fd.read()
    return BEARER_TOKEN


def k8s_instance():
    configuration = client.Configuration()
    configuration.api_key["authorization"] = get_bearer()
    configuration.ssl_ca_cert = os.environ['CA_CRT']
    configuration.api_key_prefix['authorization'] = 'Bearer' 
    configuration.host = os.environ['K8S_HOST']
    v1 = client.CoreV1Api(client.ApiClient(configuration))
    return v1


def get_pods_kuber(v1):
    pods_list = v1.list_pod_for_all_namespaces(watch=False)
    return pods_list


def check_namespace(namespace):
    list = get_all_namespace()
    if namespace in list:
        return True
    return False


def get_all_namespace():
    list = []
    v1= k8s_instance()
    response = v1.list_namespace()
    for i in response.items:
        list.append(i.metadata.name)
        print(i.metadata.name)
    return list


def create_namespace(namespace):
    v1= k8s_instance()
    body = client.V1Namespace()
    body.metadata = client.V1ObjectMeta(name=namespace)
    resp = v1.create_namespace(body)
    return resp
    

def delete_namespace(namespace):
    v1= k8s_instance()
    resp = v1.delete_namespace(name=namespace, body=client.V1DeleteOptions())
    return resp
    