import requests
import pandas as pd
from io import StringIO

url = "https://official-joke-api.appspot.com/random_ten"
response = requests.get(url).text
jokes = pd.read_json(StringIO(response))
jokes.to_html("./results/sixth_task.html")