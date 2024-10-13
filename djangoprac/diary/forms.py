from django.forms import ModelForm
from .models import Page

# 日記のページ用のフォーム
class PageForm(ModelForm):
    class Meta:
        model = Page
        # フィールドにユーザが入力する項目を指定
        fields = ["title", "body", "page_date", "picture"]