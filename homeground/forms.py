from .models import Business, Community ,Comment
from django import forms

class NewBusinessForm(forms.ModelForm):
    class Meta:
        model = Business
        fields=('poster','title','business_image','community','location','details')

class NewCommunityForm(forms.ModelForm):
    class Meta:
        model = Community
        exclude = ['resident',]
        widgets = {
            'tags': forms.CheckboxSelectMultiple(),
        }

class NewCommentForm(forms.ModelForm):
  class Meta:
    model = Comment
    fields = ('postername','comment')
