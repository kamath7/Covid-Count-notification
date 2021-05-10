import requests


def getData():
    r = requests.get('http://kams-covid-data.herokuapp.com/api/data')
    apiData = r.json()
    karnatakaCount = apiData["data"]["karnatakaCount"]
    bangaloreCount = apiData["data"]["bangaloreCount"]
    mangaloreCount = apiData["data"]["mangaloreCount"]
    udupiCount = apiData["data"]["udupiCount"]
    shimogaCount = apiData["data"]["shimogaCount"]
    mysoreCount = apiData["data"]["mysoreCount"]
    kodaguCount = apiData["data"]["kodaguCount"]

    kasargodCount = apiData["data"]["kasargodCount"]
    wayanadCount = apiData["data"]["wayanadCount"]

    mangaloreDeath = apiData["data"]["mangaloreDeath"] if type(
        int(apiData["data"]["mangaloreDeath"])) else 0
    shimogaDeath = apiData["data"]["shimogaDeath"] if type(
        int(apiData["data"]["shimogaDeath"])) else 0
    mysoreDeath = apiData["data"]["mysoreDeath"] if type(
        int(apiData["data"]["mysoreDeath"])) else 0
    kodaguDeath = apiData["data"]["kodaguDeath"] if type(
        int(apiData["data"]["kodaguDeath"])) else 0

    mangaloreVaccinations = apiData["data"]["mangaloreVaccinations"]
    karnatakaVaccinations = apiData["data"]["karnatakaVaccinations"]
    keralaVaccinations = apiData["data"]["keralaVaccinations"]

    indiaDailyConfirmed = apiData["data"]["indiaDailyConfirmed"]
    return {'wayanadCount': wayanadCount, 'shimogaCount': shimogaCount, 'mysoreCount': mysoreCount, 'shimogaDeath': shimogaDeath, 'mysoreDeath': mysoreDeath, 'kodaguDeath': kodaguDeath, 'karnatakaCount': karnatakaCount, 'bangaloreCount': bangaloreCount, 'mangaloreCount': mangaloreCount, 'kodaguCount': kodaguCount,  'udupiCount': udupiCount, 'kasargodCount': kasargodCount, 'mangaloreVaccinations': mangaloreVaccinations, 'karnatakaVaccinations': karnatakaVaccinations, 'keralaVaccinations': keralaVaccinations, 'mangaloreDeath': mangaloreDeath, 'indiaDailyConfirmed': indiaDailyConfirmed}
