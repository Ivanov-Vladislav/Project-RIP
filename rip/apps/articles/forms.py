from .models import Articles11
from django.forms import ModelForm

class Task1Form(ModelForm):
    class Meta:
        model = Articles11
        fields = ["article_title", "article_author", "article_text", "date", "avatar"]