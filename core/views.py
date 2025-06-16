from django.shortcuts import render, redirect
from .models import Exercise
from .forms import ExerciseForm

def exercises_list(request):
    tag = request.GET.get('tag')
    if tag:
        tag = tag.lower()
        exercises = Exercise.objects.filter(tags__contains=[tag])
    else:
        exercises = Exercise.objects.all()
    return render(request, 'core/exercises_list.html', {
        'exercises': exercises,
        'query': tag,
    })


def exercises_add(request):
    if request.method == 'POST':
        form = ExerciseForm(request.POST)
        if form.is_valid():
            exercise = form.save(commit=False)
            # Get selected tags
            selected_tags = form.cleaned_data.get('tags', [])
            # Get custom tags and split
            custom = form.cleaned_data.get('custom_tags', '')
            custom_tags = [tag.strip().lower() for tag in custom.split(',') if tag.strip()]
            # Combine all tags
            all_tags = selected_tags + custom_tags
            exercise.tags = all_tags
            exercise.save()
            return redirect('exercises_list')
    else:
        form = ExerciseForm()
    return render(request, 'core/exercises_form.html', {'form': form})
