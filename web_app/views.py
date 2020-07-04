from django.shortcuts import render , redirect
from django.contrib.auth import login , authenticate
from .models import Profile
from .forms import UserLoginForm , UserRegisterForm
from django.contrib.auth.decorators import login_required

# Create your views here.

def login_page(request):
    form = UserLoginForm()
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('dashboard')
        if not request.user.is_authenticated:
            return redirect('login_page')
        else:
            return redirect('login_page')
    else:
        return render(request, 'web_app/login_page.html',{'form':form})

def reg_page(request):
    next = request.GET.get('next')
    form = UserRegisterForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        password = form.cleaned_data.get('password')
        user.set_password(password)
        user.save()
        new_user = authenticate(username=user.username, password=password)
        login(request, new_user)
        if next:
            return redirect(next)
        return redirect('/')

    context = {
        'form': form,
    }
    return render(request, "web_app/reg_page.html", context)


def logout_view(request):
    logout(request)
    return redirect('/')


@login_required()
def dashboard(request):
    return render(request, "web_app/dashboard.html")




