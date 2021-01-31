import requests
import json

# URL for the web service, should be similar to:
# 'http://8530a665-66f3-49c8-a953-b82a2d312917.eastus.azurecontainer.io/score'
scoring_uri = 'http://your_uri/score'
# If the service is authenticated, set the key or token
key = 'hxkZ8lF62_key_eXjveXz14tmgL7'

# Two sets of data to score, so we get two results back
data = {"data":
        [
          {
            "Time": 1.1,
            "V1": 1.919565,
            "V2": 1.919565,
            "V3": 1.919565,
            "V4": 1.919565,
            "V5": 1.919565,
            "V6": 1.919565,
            "V7": 1.919565,
            "V8": 1.919565,
            "V9": 1.919565,
            "V10": 1.919565,
            "V11": 1.919565,
            "V12": 1.919565,
            "V13": 1.919565,
            "V14": 1.919565,
            "V15": 1.919565,
            "V16": 1.919565,
            "V17": 1.919565,
            "V18": 1.919565,
            "V19": 1.919565,
            "V20": 1.919565,
            "V21": 1.919565,
            "V22": 1.919565,
            "V23": 1.919565,
            "V24": 1.919565,
            "V25": 1.919565,
            "V26": 1.919565,
            "V27": 1.919565,
            "V28": 1.919565,
            "Amount": 1000
          },
          {
            "Time": 1.1,
            "V1": 1.919565,
            "V2": 1.919565,
            "V3": 1.919565,
            "V4": 10,
            "V5": 1.919565,
            "V6": 1.919565,
            "V7": 1.919565,
            "V8": 1.919565,
            "V9": 1.919565,
            "V10": 1.919565,
            "V11": 1.919565,
            "V12": 1.919565,
            "V13": 1.919565,
            "V14": 1.919565,
            "V15": 1.919565,
            "V16": 1.919565,
            "V17": 1.919565,
            "V18": 1.919565,
            "V19": 1.919565,
            "V20": 1.919565,
            "V21": 1.919565,
            "V22": 1.919565,
            "V23": 1.919565,
            "V24": 1.919565,
            "V25": 1.919565,
            "V26": 1.919565,
            "V27": 1.919565,
            "V28": 1.919565,
            "Amount": 1000
          },
      ]
    }
# Convert to JSON string
input_data = json.dumps(data)
with open("data.json", "w") as _f:
    _f.write(input_data)

# Set the content type
headers = {'Content-Type': 'application/json'}
# If authentication is enabled, set the authorization header
headers['Authorization'] = f'Bearer {key}'

# Make the request and display the response
resp = requests.post(scoring_uri, input_data, headers=headers)
print(resp.json())
