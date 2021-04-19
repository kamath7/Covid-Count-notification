import requests

r = requests.get('http://kams-covid-data.herokuapp.com/api/data')
apiData = r.json()
karnatakaCount = apiData["data"]["karnatakaCount"]
bangaloreCount = apiData["data"]["bangaloreCount"]
mangaloreCount = apiData["data"]["mangaloreCount"]
udupiCount = apiData["data"]["udupiCount"]
indiaDailyConfirmed = apiData["data"]["indiaDailyConfirmed"]


print(karnatakaCount, bangaloreCount, mangaloreCount)
