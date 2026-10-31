from django.shortcuts import render, get_object_or_404, redirect

from webapp.forms import GuestForm, DeleteForm, SearchForm
from webapp.models import Guest


def index_view(request):
    form = SearchForm(data=request.GET)
    if form.is_valid():
        guests = Guest.objects.filter(status='active', author_name__icontains=form.cleaned_data.get('search')).order_by('-created_at')
    else:
        guests = Guest.objects.filter(status='active').order_by('-created_at')
    return render(request, 'index.html', {'guests': guests, 'form': form})


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


def guest_update_view(request, pk):
    guest = get_object_or_404(Guest, pk=pk)
    if request.method == 'GET':
        form = GuestForm(initial={'author_name': guest.author_name, 'author_email': guest.author_email, 'text': guest.text})
        return render(request, 'guest_update.html', {'form': form, 'guest': guest})
    elif request.method == 'POST':
        form = GuestForm(data=request.POST)
        if form.is_valid():
            guest.author_name = form.cleaned_data.get('author_name')
            guest.author_email = form.cleaned_data.get('author_email')
            guest.text = form.cleaned_data.get('text')
            guest.save()
            return redirect('index')
        else:
            return render(request, 'guest_update.html', {'form': form, 'guest': guest})

def guest_delete_view(request, pk):
    guest = get_object_or_404(Guest, pk=pk)
    form = DeleteForm()
    if request.method == 'GET':
        return render(request, 'guest_delete.html', {'form': form, 'guest': guest})
    elif request.method == 'POST':
        form = DeleteForm(data=request.POST)
        if form.is_valid():
            if guest.author_email == form.cleaned_data.get('email'):
                guest.delete()
                return redirect('index')
            else:
                form.add_error('email', 'Email не совпадает с почтой автора записи!')
        else:
            return render(request, 'guest_delete.html', {'form': form, 'guest': guest})
    return render(request, 'guest_delete.html', {'form': form, 'guest': guest})