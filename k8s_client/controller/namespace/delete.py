from k8s_client.lib.exceptions import decorator
from k8s_client.lib.k8s import delete_namespace
from k8s_client import config


@decorator
def post(*args, **kwargs):
    if kwargs['body']['namespace'] in config.forbidden_namespace:
        return "Access denied", 403
    resp = delete_namespace(kwargs['body']['namespace'])
    print(resp)
    message = "Namespace %s has deleted" % (kwargs['body']['namespace'])
    return message