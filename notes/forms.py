
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Note
from django import forms
from .models import Note
from .models import Folder
class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']



class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['title', 'content', 'folder', 'is_public', 'editable']
        widgets = {
            'is_public': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'editable': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        note = kwargs.get('instance', None)
        super().__init__(*args, **kwargs)

        # 如果不是作者，就不顯示權限欄位，並設初始值為原值
        if note and user and note.owner != user:
            self.fields['is_public'].widget = forms.HiddenInput()
            self.fields['editable'].widget = forms.HiddenInput()
            self.fields['is_public'].initial = note.is_public
            self.fields['editable'].initial = note.editable




class FolderForm(forms.ModelForm):
    class Meta:
        model = Folder
        fields = ['name']
