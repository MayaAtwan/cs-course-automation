from django.shortcuts import render, redirect
from .models import Exercise
from .forms import ExerciseForm

def exercises_list(request):
    qs = Exercise.objects.all()
    return render(request, 'core/exercises_list.html', {'exercises': qs})

def exercises_add(request):
    if request.method == 'POST':
        form = ExerciseForm(request.POST)
        if form.is_valid():
            exercise = form.save(commit=False)
            exercise.tags = form.cleaned_data['tags']
            exercise.save()
            return redirect('exercises_list')
    else:
        form = ExerciseForm()
    return render(request, 'core/exercises_form.html', {'form': form})

