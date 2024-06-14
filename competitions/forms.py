from django import forms
from .models import Competition
INPUT_CLASSES = 'w-full py-4 px-6 rounded-xl border'
class NewItemForm(forms.ModelForm):
    class Meta:
        model = Competition
        fields = ('category', 'name', 'description', 'image', 'deadline')
        widgets = {
            'category': forms.Select(attrs={
                'class': INPUT_CLASSES
            }),
            'name': forms.TextInput(attrs={
                'class': 'w-full py-4 px-6 rounded-xl border'
            }),
            'description': forms.Textarea(attrs={
                'class': INPUT_CLASSES
            }),
            'deadline': forms.DateInput(attrs={
                'class': INPUT_CLASSES,
                
            }),
            'image': forms.FileInput(attrs={
                'class': INPUT_CLASSES
            })
        }

class EditItemForm(forms.ModelForm):
    class Meta:
        model = Competition
        fields = ('category', 'name', 'description', 'image', 'deadline', 'has_passed')
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'w-full py-4 px-6 rounded-xl border'
            }),
            'description': forms.Textarea(attrs={
                'class': INPUT_CLASSES
            }),
            'deadline': forms.DateInput(attrs={
                'class': INPUT_CLASSES
            }),
            'image': forms.FileInput(attrs={
                'class': INPUT_CLASSES
            }),
            'has_passed': forms.CheckboxInput(attrs={
                'class': INPUT_CLASSES
            })
        }