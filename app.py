from fn import connections as cn
cn.test()


project = cn.Access()
print(project.app_id)
print(project.app_google_cloud_service_account)
print(project.app_google_cloud_project_id)
service_account = project.app_google_cloud_service_account

service_account_sign_in = cn.Gcloud(service_account)
print(service_account_sign_in)