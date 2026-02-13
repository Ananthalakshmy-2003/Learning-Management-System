from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, 'core/home.html')

@login_required
def dashboard(request):
    from accounts.models import Profile
    try:
        profile = request.user.profile
    except Profile.DoesNotExist:
        profile = Profile.objects.create(user=request.user, role='student')
    
    if profile.role == 'teacher':
        return render(request, 'core/teacher_dashboard.html')
    else:
        return render(request, 'core/student_dashboard.html')