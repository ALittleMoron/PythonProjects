from django import forms
from .models import Article, Category


# class ArticleForm(forms.Form):
#     title = forms.CharField(max_length=150, label="Заголовок", widget=forms.TextInput(attrs={"class": 'form-control'}))
#     content = forms.CharField(label="Текст", widget=forms.Textarea(attrs={"class": 'form-control'}))
#     is_published = forms.BooleanField(label="Опубликовано?", initial=True)
#     category = forms.ModelChoiceField(label="Категория", empty_label="Выберите категорию", widget=forms.Select(attrs={'class': 'form-control'}), queryset=Category.objects.all())


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = '__all__'
        widgets = {
            'title': forms.TextInput(attrs={"class": 'form-control'}),
            'content': forms.Textarea(attrs={"class": 'form-control'}),
            'category': forms.Select(attrs={"class": 'form-control'}),
        }
