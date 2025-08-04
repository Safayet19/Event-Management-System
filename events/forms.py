from django import forms
from .models import Event, Participant, Category

class StyledFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            existing_classes = field.widget.attrs.get('class', '')
            classes = 'border rounded px-3 py-2 w-full focus:outline-none focus:ring-2 focus:ring-indigo-600'

            placeholder = f"Enter {field.label}"
            field.widget.attrs.update({
                'class': (existing_classes + ' ' + classes).strip(),
                'placeholder': placeholder,
                'autocomplete': 'off',
            })
            if field.required:
                field.widget.attrs['required'] = 'required'

class EventForm(StyledFormMixin, forms.ModelForm):
    class Meta:
        model = Event
        fields = ['name', 'location', 'date', 'time', 'category', 'description']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'time': forms.TimeInput(attrs={'type': 'time'}),
            'description': forms.Textarea(attrs={
                'rows': 4,
                'class': 'border rounded px-3 py-2 w-full focus:outline-none focus:ring-2 focus:ring-indigo-600 resize-y',
                'placeholder': 'Enter event description',
            }),
        }

class ParticipantForm(StyledFormMixin, forms.ModelForm):
    class Meta:
        model = Participant
        fields = ['name', 'email']
        widgets = {
            'email': forms.EmailInput(attrs={
                'placeholder': 'Enter email address',
                'autocomplete': 'email',
            }),
            'name': forms.TextInput(attrs={
                'placeholder': 'Enter full name',
                'autocomplete': 'name',
            }),
        }

class CategoryForm(StyledFormMixin, forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'description']
        widgets = {
            'description': forms.Textarea(attrs={
                'rows': 3,
                'class': 'border rounded px-3 py-2 w-full focus:outline-none focus:ring-2 focus:ring-indigo-600 resize-y',
                'placeholder': 'Enter category description',
            }),
            'name': forms.TextInput(attrs={
                'placeholder': 'Enter category name',
            }),
        }
