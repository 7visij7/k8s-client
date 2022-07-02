import sys
import traceback
from k8s_client.lib.logger import log


def decorator(fn):
    def wrap(*args, **kwargs):
        try:
            return fn(*args, **kwargs)
        except Exception as err:
            log(traceback.format_exc())
            return {
                "error": {
                    "message": str(err),
                    "type": sys.exc_info()[0].__name__
                }
            }, 500 
    return wrap
