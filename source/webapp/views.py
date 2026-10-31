from django.shortcuts import render, get_object_or_404, redirect

from webapp.forms import GuestForm
from webapp.models import Guest


def index_view(request):
    context = {
        'guests': Guest.objects.all().filter(status='active').order_by('-created_at')
    }
    return render(request, 'index.html', context)

def guest_add_view(request):
    form = GuestForm()
    if request.method == 'GET':
        return render(request, 'guest_add.html', {'form': form})
    elif request.method == 'POST':
        form = GuestForm(data=request.POST)
        if form.is_valid():
            author_name = form.cleaned_data.get('author_name')
            author_email = form.cleaned_data.get('author_email')
            text = form.cleaned_data.get('text')
            Guest.objects.create(author_name=author_name, author_email=author_email, text=text)
            return redirect('index')
        else:
            return render(request, 'guest_add.html', {'form': form})
