import os

workshop.title = "Foundations of OpenShift"

workshop.courses = [
  "training-workshop"
]

user = os.environ.get("JUPYTERHUB_USER", "developer")
user = os.environ.get("OPENSHIFT_USER", user)

password = os.environ.get("OPENSHIFT_PASSWORD", "openshift")

workshop.context = {
  "OPENSHIFT_USER": user,
  "OPENSHIFT_PASSWORD": password,
}
