from k8s_client.lib.exceptions import decorator
from k8s_client.lib.k8s import create_namespace

@decorator
def post(*args, **kwargs):
    resp = create_namespace(kwargs['body']['namespace'])
    print(resp)
    message = "Namespace  %s has created" % (kwargs['body']['namespace'])
    return message
    