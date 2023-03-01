from django.shortcuts import render


def index(request):
    context = {
        'title': 'short',
    }
    return render(request, 'landing_page/index.html', context)
