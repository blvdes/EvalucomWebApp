import requests, json

apiKey = "?api_key=1f0ed69ded3209664c2459c0c5956f74"
baseUrl = "https://api.themoviedb.org/3/movie/"

searchApiKey = '&api_key=1f0ed69ded3209664c2459c0c5956f74'
searchUrl = "https://api.themoviedb.org/3/search/movie?"


def prNowPlaying(page):
    parentList = []
    childDict = {}
    
    response = requests.get(baseUrl + "now_playing" + apiKey + "&page=" + page)

    if response.status_code == 200:
        fullResponseText = response.text
        resultsText = json.loads(fullResponseText).get('results')
        
        for movie in resultsText:
            childDict['id'] = movie.get('id')
            childDict['title'] = movie.get('title')
            childDict['desc'] = movie.get('overview')       

            parentList.append(childDict.copy())

    # print(parentList)
    return(parentList)


def specificSearch(id):
    response = json.loads(requests.get(baseUrl + str(id) + apiKey).text)
    return(response)


def getTitleAndDesc(id):
    search = specificSearch(id)
    title = search.get('title')
    desc = search.get('overview')
    date = search.get('release_date')
    avgScore = int(search.get('vote_average')) / 2 

    imagePath = "https://image.tmdb.org/t/p/original"
    image = search.get('poster_path')

    return(title, desc, imagePath + image, date, avgScore)


def wideSearch(query):
    query = query.replace(" ", "+")

    response = json.loads(requests.get(searchUrl + "query=" + query + searchApiKey).text)

    parentList = []
    childDict = {}

    for result in response.get('results'):
        childDict['id'] = result.get('id')
        childDict['title'] = result.get('title')
        childDict['desc'] = result.get('overview')       

        parentList.append(childDict.copy())

    return(parentList)

def getTitle(id):
    search = specificSearch(id)
    title = search.get('title')

    return(title)