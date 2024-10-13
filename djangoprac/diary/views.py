from django.shortcuts import render, redirect, get_object_or_404
# 汎用的なview用の基底クラス
from django.views import View
from .forms import PageForm
from .models import Page
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
        # 写真等のアップロードにはrequest.FILESの指定が必要
        form = PageForm(request.POST, request.FILES)
        # リクエストのバリデーションを行う
        if form.is_valid():
            form.save()
            # 「index」はdiary/urls.pyで紐付けしている
            return redirect("diary:index")
        # バリデーションに失敗したらフォームページに戻る
        return render(request, "diary/page_form.html", {"form":form})
      
class PageListView(View):
    def get(self, request):
        # DBから日記ページのデータをすべて取得
        # page_list = Page.objects.all()

        # DBから日記ページのデータを日付をキーに並び替えて取得
        # 昇順の場合はそのまま、降順の場合はフィールド名の前に"-"をつける
        page_list = Page.objects.order_by("-page_date")
        return render(request, "diary/page_list.html", {"page_list": page_list})

class PageDetailView(View):
    def get(self, request, id):
        # DBからIDが一致うるPageのデータを取得する
        # 合致するIDがDBになければ404へ
        page = get_object_or_404(Page, id=id)
        return render(request, "diary/page_detail.html", {"page": page})

class PageUpdateView(View):
    def get(self, request, id):
        page = get_object_or_404(Page, id=id)
        # inctance=page:元々登録されたいたデータをFormに送る
        form = PageForm(instance=page)
        return render(request, "diary/page_update.html", {"form": form})
    
    def post(self, request, id):
        page = get_object_or_404(Page, id=id)
        form = PageForm(request.POST, request.FILES, instance=page)
        if form.is_valid():
            form.save()
            return redirect("diary:page_detail", id=id)
        return render(request, "diary/page_form.html", {"form": form})

class PageDeleteView(View):
    def get(self, request, id):
        page = get_object_or_404(Page, id=id)
        return render(request, "diary/page_confirm_delete.html", {"page": page})
    
    def post(self, request, id):
        page = get_object_or_404(Page, id=id)
        page.delete()
        return redirect('diary:page_list')


# 関数に変換
index = IndexView.as_view()
page_create = PageCreateView.as_view()
page_list = PageListView.as_view()
page_detail = PageDetailView.as_view()
page_update = PageUpdateView.as_view()
page_delete = PageDeleteView.as_view()
