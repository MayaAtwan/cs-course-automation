from django.shortcuts import render, redirect
from .models import Exercise
from .forms import ExerciseForm
from django.shortcuts import get_object_or_404
from .forms import AssignmentForm
from .models import Assignment  # make sure Assignment is imported

def assignments_list(request):
    assignments = Assignment.objects.all().order_by('-created_at')
    return render(request, 'assignments/assignments_list.html', {'assignments': assignments})

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


def exercises_delete(request, pk):
    exercise = get_object_or_404(Exercise, pk=pk)
    if request.method == 'POST':
        exercise.delete()
        return redirect('exercises_list')
    return render(request, 'core/exercises_confirm_delete.html', {'exercise': exercise})


def exercises_edit(request, pk):
    exercise = Exercise.objects.get(pk=pk)
    if request.method == 'POST':
        form = ExerciseForm(request.POST, instance=exercise)
        if form.is_valid():
            exercise = form.save(commit=False)
            exercise.tags = form.cleaned_data['tags']
            exercise.save()
            return redirect('exercises_list')
    else:
        form = ExerciseForm(instance=exercise)
    return render(request, 'core/exercises_form.html', {'form': form, 'edit': True})


def create_assignment(request):
    if request.method == 'POST':
        form = AssignmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('assignments_list')  # Create this URL/view next
    else:
        form = AssignmentForm()
    return render(request, 'assignments/assignment_form.html', {'form': form})
