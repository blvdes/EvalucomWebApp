from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from . import tmdbAPI
from .forms import ReviewForm, SearchForm
from .models import Review

def home(request):
    currentPage = 1
    redirectVar = 'page/'

    nextPageNumber = currentPage + 1
    prevPageNumber = currentPage - 1

    context = {
        'list': tmdbAPI.prNowPlaying("1"),
        'currentPage': currentPage,
        'nextPageNumber': nextPageNumber,
        'prevPageNumber': prevPageNumber,
        'redirectVar': redirectVar
    }

    return render(request, "homeTable.html", context)


def page(request, pageNumber):
    currentPage = pageNumber
    redirectVar = 'page/'

    nextPageNumber = currentPage + 1
    prevPageNumber = currentPage - 1

    context = {
        'list': tmdbAPI.prNowPlaying(str(pageNumber)),
        'currentPage': currentPage,
        'nextPageNumber': nextPageNumber,
        'prevPageNumber': prevPageNumber,
        'redirectVar': redirectVar
    }

    return render(request, "homeTable.html", context)


def review(request, IDParam):
    if request.method == 'POST':
        reviewViewForm = ReviewForm(request.POST)
        if reviewViewForm.is_valid():
            submission = reviewViewForm.save(commit=False)
            submission.movieID = IDParam
            submission.save()

            return HttpResponseRedirect(request.path_info)
    else:
        reviewViewForm = ReviewForm()

    reviewData = Review.objects.filter(movieID = IDParam).order_by('-date').values()
    movieTitle, movieDesc, posterImage, date, avgScore = tmdbAPI.getTitleAndDesc(IDParam)

    context = {
        'reviewViewForm': reviewViewForm,
        'id': IDParam,
        'reviewData': reviewData,
        'movieTitle': movieTitle,
        'movieDesc': movieDesc,
        'movieImg': posterImage,
        'movieDate': date,
        'avgScore': avgScore,
        }

    return render(request, "reviewTemplate.html", context)


def search(request):
    if request.method == 'POST':
        searchForm = SearchForm(request.POST)
        if searchForm.is_valid():
            searchSubmission = searchForm.cleaned_data.get('text')
        
            # return HttpResponseRedirect(request.path_info)
    else:
        searchSubmission = ''
        searchForm = SearchForm()
    
    list = tmdbAPI.wideSearch(searchSubmission)

    context = {
        'searchForm': searchForm,
        'list': list,
    }

    return render(request, 'searchTemplate.html', context)


def reviews(request):
    reviewData = Review.objects.all().order_by('-date')
    dict = {}
    seenIDs = []
    orderedList = []

    for id in Review.objects.values_list('movieID'):
        id = id[0]

        if id not in seenIDs:
            dict[id] = tmdbAPI.getTitle(id)
        
        seenIDs.append(id)

    for review in reviewData:
        review.title = dict[review.movieID]

    context = {
        'reviewData': reviewData,
        'dict': dict,
        'orderedList': orderedList
    }

    return render(request, 'reviewTable.html', context)
