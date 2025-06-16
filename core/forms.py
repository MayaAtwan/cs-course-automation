from django import forms
from .models import Exercise

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
