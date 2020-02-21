import os
#from google.cloud import bigquery
from google.oauth2 import service_account


def test():
    print("test succeeded")

class Access(object):
    """ Instantiate environment variables """
    def __init__(self):
         self.app_id = os.environ['FACEBOOK_APP_ID']
         self.app_google_cloud_service_account = os.environ['SERVICE_ACCOUNT_JSON']
         self.app_google_cloud_project_id = os.environ['GOOGLE_CLOUD_PROJECT_ID']

class Gcloud(object):
    """ Grants access to Google Service Account """
    def __init__(self, service_account_path):
        self.credentials = service_account.Credentials.from_service_account_file(service_account_path)
        self.scoped_credentials = self.credentials.with_scopes(
            ['https://www.googleapis.com/auth/cloud-platform']
        )



