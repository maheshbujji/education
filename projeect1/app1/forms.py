from django import  forms

class studentForms(forms.Form):
   Bookname=forms.CharField(max_length=200)
   BookNo=forms.IntegerField()
   file=forms.FileField()
