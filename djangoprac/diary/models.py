from django.db import models
from pathlib import Path
import uuid

class Page(models.Model):
    # verbose_name : そのデータを説明する名前
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, verbose_name="ID")
    title = models.CharField(max_length=100, verbose_name="タイトル")
    body = models.TextField(max_length=2000, verbose_name="本文")
    page_date = models.DateField(verbose_name="日付")
    # アップロードされたファイルを"diary/picture/"に保存する
    picture = models.ImageField(
        upload_to="diary/picture/", blank=True, null=True, verbose_name="写真")
    # auto_now_add : そのデータが初めて作成されたその時の日時を保存
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="作成日時")
    # auto_now : このデータが保存・更新される旅にその時の日常を保存
    updated_at = models.DateTimeField(auto_now=True, verbose_name="更新日時")

    def __str__(self):
        # どのデータか判断するときにわかりやすいクラス変数ßを返却
        return self.title
    
    # *args,**kargs:可変長引数
    def delete(self, *args, **kargs):
        picture = self.picture
        super().delete(*args, **kargs)
        if picture:
            Path(picture.path).unlink(missing_ok=True)
