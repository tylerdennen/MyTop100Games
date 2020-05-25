from django.shortcuts import render


def mainpage(request):
    return render(request, 'rating/index.html')
