from django.contrib.flatpages.models import FlatPage
from django.shortcuts import render

def search(request):
    query = request.GET['q']
    results = FlatPage.objects.filter(content__icontains=query)
    return render(request, 'search/search.html', {
                    "query":query,
                    "results":results}
                )
        