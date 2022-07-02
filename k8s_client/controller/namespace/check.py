from k8s_client.lib.exceptions import decorator
from k8s_client.lib.k8s import check_namespace

@decorator
def post(*args, **kwargs):
    if check_namespace(kwargs['body']['namespace']):
        message = "Namespace %s exists" % (kwargs['body']['namespace'])
        return message, 200
    else:
        message = "Namespace %s does not exist" % (kwargs['body']['namespace'])
        return message, 404
