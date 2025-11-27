from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Teacher

# Demo credentials
VALID_USERNAME = 'David'
VALID_PASSWORD = '123'

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if username == VALID_USERNAME and password == VALID_PASSWORD:
            request.session['is_logged_in'] = True
            request.session['user_name'] = username

            messages.success(request, f"Welcome back, {username}! Login successful. ✅")

            # Redirect USING URL NAME (not template filename)
            return redirect('dashboard')

        else:
            messages.error(request, "🔴 Invalid username or password. Please try again.")
            return render(request, 'login.html', {'last_username': username})

    return render(request, 'login.html')


def dashboard(request):
    if not request.session.get('is_logged_in'):
        messages.warning(request, "You must log in to view the dashboard.")
        return redirect('login')

    return render(request, 'dashboard.html', {
        'username': request.session.get('user_name')
    })


def logout(request):
    request.session.flush()
    messages.info(request, "You have been logged out.")
    return redirect('login')


def show_teacher(request):
    teachers = Teacher.objects.all()
    return render(request, 'teacher.html', {'teachers': teachers})
