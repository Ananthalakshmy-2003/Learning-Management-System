from django.shortcuts import render, redirect   

# Create your views here.
from django.contrib.auth.decorators import login_required
from .models import Note
@login_required
def upload_note(request):
    if request.user.profile.role != 'teacher':
        return redirect('dashboard')
    if request.method == 'POST':
        Note. objects.create(
            title=request.POST['title'],
            file=request.FILES['file'],
            uploaded_by=request.user
        )
        return redirect('dashboard')
    return render(request, 'courses/upload_note.html')
@login_required
def note_list(request):
    notes=Note.objects.all()
    return render(request, 'courses/note_list.html', {'notes': notes})