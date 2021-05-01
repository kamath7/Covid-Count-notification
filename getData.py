import requests
from requests import api


def getData():
    r = requests.get('http://kams-covid-data.herokuapp.com/api/data')
    apiData = r.json()
    karnatakaCount = apiData["data"]["karnatakaCount"]
    bangaloreCount = apiData["data"]["bangaloreCount"]
    mangaloreCount = apiData["data"]["mangaloreCount"]
    udupiCount = apiData["data"]["udupiCount"]
    kodaguCount = apiData["data"]["kodaguCount"]
    kasargodCount = apiData["data"]["kasargodCount"]

    mangaloreDeath = apiData["data"]["mangaloreDeath"] if type(
        int(apiData["data"]["mangaloreDeath"])) else 0

    mangaloreVaccinations = apiData["data"]["mangaloreVaccinations"]
    karnatakaVaccinations = apiData["data"]["karnatakaVaccinations"]
    keralaVaccinations = apiData["data"]["keralaVaccinations"]

    indiaDailyConfirmed = apiData["data"]["indiaDailyConfirmed"]
    return {'karnatakaCount': karnatakaCount, 'bangaloreCount': bangaloreCount, 'mangaloreCount': mangaloreCount, 'kodaguCount': kodaguCount,  'udupiCount': udupiCount, 'kasargodCount': kasargodCount, 'mangaloreVaccinations': mangaloreVaccinations, 'karnatakaVaccinations': karnatakaVaccinations, 'keralaVaccinations': keralaVaccinations, 'mangaloreDeath': mangaloreDeath, 'indiaDailyConfirmed': indiaDailyConfirmed}
