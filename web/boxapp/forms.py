from django import forms

from .models import Document2

class DocumentForm2(forms.ModelForm):
    class Meta:
        model = Document2
        fields = ('name','amount','timeTransfer','description', 'document',)

#class DocumentForm(forms.ModelForm):
#    class Meta:
#        model = Document
#        fields = ('description', 'document', )