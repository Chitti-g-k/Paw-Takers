from django.shortcuts import render, redirect
from .forms import UserProfileForm
from .models import UserProfile

def add_user(request):
    from .views import success # import here to avoid circular imports
    if request.method == 'POST':
        form = UserProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('caretaker:success')
    else:
        form = UserProfileForm()
    return render(request, 'add_user.html', {'form': form})

def success(request):
    users = UserProfile.objects.all()
    return render(request, 'success.html', {'users': users})
