import io
import requests
import csv

def online_csv(url):
  url = url
  r = requests.get(url)
  r.encoding = 'utf-8'
  csvio = io.StringIO(r.text, newline="")
  data = []
  for row in csv.DictReader(csvio):
      data.append(row)
  return data
