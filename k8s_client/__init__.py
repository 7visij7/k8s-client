import connexion
import os
from connexion.resolver import RestyResolver

def daemon():
    options = {"swagger_ui": True}
    app = connexion.FlaskApp('K8S-client API company', server='tornado', options=options)
    here = os.path.abspath(os.path.dirname(__file__))
    app.add_api('%s/config/swagger.yaml' % here, resolver=RestyResolver('k8s_client.controller'))
    app.run(port=os.environ['PORT'], debug=True)
