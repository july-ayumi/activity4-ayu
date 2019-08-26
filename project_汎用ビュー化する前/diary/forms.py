'''
htmlのinputを作っていくのは面倒だから
値のバリデーションまでしてくれるから
day_form.htmlで使っている
'''
from django import forms
from .models import Day

class DayCreateForm(forms.ModelForm):

    class Meta:
        model = Day
        fields = '__all__'
