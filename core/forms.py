from django import forms
from .models import Exercise
from .models import Assignment

PREDEFINED_TAGS = [
    ('trees', 'Trees'),
    ('dfs', 'DFS'),
    ('recursion', 'Recursion'),
    ('sorting', 'Sorting'),
]

class ExerciseForm(forms.ModelForm):
    tags = forms.MultipleChoiceField(
        choices=PREDEFINED_TAGS,
        widget=forms.CheckboxSelectMultiple,
        required=False
    )
    custom_tags = forms.CharField(
        required=False,
        label='Other tags (comma separated)',
        widget=forms.TextInput(attrs={'placeholder': 'e.g. dp, backtracking'})
    )

    class Meta:
        model = Exercise
        fields = ['title', 'content', 'difficulty', 'tags', 'custom_tags']


class AssignmentForm(forms.ModelForm):
    class Meta:
        model = Assignment
        fields = ['title', 'description', 'due_date', 'group_type', 'exercises']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
            'due_date': forms.DateInput(attrs={'type': 'date'}),
            'exercises': forms.CheckboxSelectMultiple()
        }
