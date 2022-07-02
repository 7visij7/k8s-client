from k8s_client.lib.exceptions import decorator
from k8s_client.lib.k8s import get_all_namespace

@decorator
def search(*args, **kwargs):
    return get_all_namespace()