from django.shortcuts import render, redirect
# 汎用的なview用の基底クラス
from django.views import View
from .forms import PageForm
from datetime import datetime
from zoneinfo import ZoneInfo



class IndexView(View):
    # 日記アプリのトップページにアクセスした時に動くメソッド
    def get(self,request):
        datetime_now = datetime.now(
            ZoneInfo("Asia/Tokyo")
        ).strftime("%Y年%m月%d日 %H:%M:%S")
        # 画面のレスポンスを返す
        # 第二引数に返すがめんのHTMLファイルを指定
        return render(request, "diary/index.html", {"datetime_now": datetime_now})

class PageCreateView(View):
    def get(self, request):
        form = PageForm()
        # PageFormで定義した入力項目をHTML側に渡す
        return render(request, "diary/page_form.html", {"form": form})
    
    def post(self, request):
        form = PageForm(request.POST)
        # リクエストのバリデーションを行う
        if form.is_valid():
            form.save()
            # 「index」はdiary/urls.pyで紐付けしている
            return redirect("diary:index")
        # バリデーションに失敗したらフォームページに戻る
        return render(request, "diary/page_form.html", {"form":form})
      
# 関数に変換
index = IndexView.as_view()
page_create = PageCreateView.as_view()
