from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .forms import SkinChangeForm
from .models import SkinChange
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as django_login
from django.contrib import messages


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            django_login(request, user)
            messages.success(request, 'You have been successfully logged in.')
            return redirect('image_list')  # Przekierowanie po udanym zalogowaniu
        else:
            messages.error(request, 'Invalid username or password. Please try again.')

    return render(request, 'registration/login.html')


def delete_image(request, image_id):
    image = get_object_or_404(SkinChange, id=image_id)
    if image.user == request.user:
        image.delete()

    return redirect('image_list')
@login_required
def image_list(request):
    images = SkinChange.objects.filter(user=request.user)
    return render(request, 'skin_changes/image_list.html', {'images': images})

@login_required
def upload_image(request):
    if request.method == 'POST':
        form = SkinChangeForm(request.POST, request.FILES)
        if form.is_valid():
            skin_change = form.save(commit=False)
            skin_change.user = request.user
            skin_change.save()
            return redirect('image_list')
    else:
        form = SkinChangeForm()
    return render(request, 'skin_changes/upload_image.html', {'form': form})

@login_required
def edit_image(request, image_id):
    skin_change = SkinChange.objects.get(id=image_id)
    if request.method == 'POST':
        form = SkinChangeForm(request.POST, request.FILES, instance=skin_change)
        if form.is_valid():
            form.save()
            return redirect('image_list')
    else:
        form = SkinChangeForm(instance=skin_change)

    return render(request, 'skin_changes/edit_image.html', {'form': form, 'object': skin_change})




