from django import forms
from .models import Exercise

TAG_CHOICES = [
    ('trees', 'Trees'),
    ('dfs', 'DFS'),
    ('recursion', 'Recursion'),
    ('sorting', 'Sorting'),
]

class ExerciseForm(forms.ModelForm):
    tags = forms.MultipleChoiceField(
        choices=TAG_CHOICES,
        widget=forms.CheckboxSelectMultiple,
        required=False
    )

    class Meta:
        model = Exercise
        fields = ['title', 'content', 'difficulty', 'tags']

    def clean_tags(self):
        tags = self.cleaned_data.get('tags', [])
        return [tag.lower() for tag in tags]  # 💡 normalize to lowercase
