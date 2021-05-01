import requests


def getData():
    r = requests.get('http://kams-covid-data.herokuapp.com/api/data')
    apiData = r.json()
    karnatakaCount = apiData["data"]["karnatakaCount"]
    bangaloreCount = apiData["data"]["bangaloreCount"]
    mangaloreCount = apiData["data"]["mangaloreCount"]
    udupiCount = apiData["data"]["udupiCount"]
    mangaloreDeath = apiData["data"]["mangaloreDeath"] if type(
        int(apiData["data"]["mangaloreDeath"])) else 0
    kasargodCount = apiData["data"]["kasargodCount"]
    indiaDailyConfirmed = apiData["data"]["indiaDailyConfirmed"]
    return {'karnatakaCount': karnatakaCount, 'bangaloreCount': bangaloreCount, 'mangaloreCount': mangaloreCount, 'kasargodCount': kasargodCount, 'mangaloreDeath': mangaloreDeath, 'udupiCount': udupiCount, 'indiaDailyConfirmed': indiaDailyConfirmed}
