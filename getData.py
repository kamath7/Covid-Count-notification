import requests


def getData():
    r = requests.get('http://kams-covid-data.herokuapp.com/api/data')
    apiData = r.json()
    karnatakaCount = apiData["data"]["karnatakaCount"]
    bangaloreCount = apiData["data"]["bangaloreCount"]
    mangaloreCount = apiData["data"]["mangaloreCount"]
    kasargodCount = apiData["data"]["kasargodCount"]
    udupiCount = apiData["data"]["udupiCount"]
    indiaDailyConfirmed = apiData["data"]["indiaDailyConfirmed"]
    return {'karnatakaCount': karnatakaCount, 'bangaloreCount': bangaloreCount, 'mangaloreCount': mangaloreCount,'kasargodCount':kasargodCount ,'udupiCount': udupiCount, 'indiaDailyConfirmed': indiaDailyConfirmed}
