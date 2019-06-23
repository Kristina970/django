from django.shortcuts import render
from datetime import date

def post_list(request):
    today = date.today()
    return render(request, 'blog/post_list.html', {}, today)
