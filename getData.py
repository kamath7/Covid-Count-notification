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
    keralaCount = apiData["data"]["keralaCount"]
    mangaloreDeath = apiData["data"]["mangaloreDeath"] if type(
        int(apiData["data"]["mangaloreDeath"])) else 0
    bangaloreUrbanDeath = apiData["data"]["bangaloreUrbanDeath"] if type(
        int(apiData["data"]["bangaloreUrbanDeath"])) else 0
    shimogaDeath = apiData["data"]["shimogaDeath"] if type(
        int(apiData["data"]["shimogaDeath"])) else 0
    mysoreDeath = apiData["data"]["mysoreDeath"] if type(
        int(apiData["data"]["mysoreDeath"])) else 0
    kodaguDeath = 0 #apiData["data"]["kodaguDeath"] if type( #     int(apiData["data"]["kodaguDeath"])) else 0

    # mangaloreVaccinations =  0 #apiData["data"]["mangaloreVaccinations"]
    # karnatakaVaccinations =  0 #apiData["data"]["karnatakaVaccinations"]
    # keralaVaccinations = 0 #apiData["data"]["keralaVaccinations"]

    indiaDailyConfirmed = apiData["data"]["indiaDailyConfirmed"]
    return {'wayanadCount': wayanadCount, 'shimogaCount': shimogaCount, 'mysoreCount': mysoreCount, 'shimogaDeath': shimogaDeath, 'mysoreDeath': mysoreDeath, 'karnatakaCount': karnatakaCount, 'bangaloreCount': bangaloreCount, 'mangaloreCount': mangaloreCount, 'kodaguCount': kodaguCount,  'udupiCount': udupiCount, 'kasargodCount': kasargodCount, 'mangaloreDeath': mangaloreDeath, 'kodaguDeath': kodaguDeath,'indiaDailyConfirmed': indiaDailyConfirmed, 'bangaloreUrbanDeath': bangaloreUrbanDeath, 'keralaCount': keralaCount}
