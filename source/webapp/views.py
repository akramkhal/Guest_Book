from django.shortcuts import render
from webapp.models import Guest


def index_view(request):
    context = {
        'guests': Guest.objects.all().filter(status='active').order_by('-created_at')
    }
    return render(request, 'index.html', context)