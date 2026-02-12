# How do we make a request
import requests
URL = "https://5000-firebase-pythonreview-1768490161677.cluster-ullaur4e5zdpctiwsbgszki4ws.cloudworkstations.dev/api/items"

response = requests.get(URL).json()
print(response)