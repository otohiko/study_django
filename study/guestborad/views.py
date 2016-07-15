#coding:utf-8
# ページネーター
from django.core.paginator import (
    Paginator,  # ページネーター本体のクラス
    EmptyPage,  # ページ番号が範囲外だった場合に発生する例外クラス
    PageNotAnInteger  # ページ番号が数字でなかった場合に発生する例外クラス
)
from django.shortcuts import (
    render,
    redirect,
)
from .models import Posting
from .forms import PostingForm

def _get_page(list_, page_no, count=5):
    paginator = Paginator(list_,count)
    try:
        page = paginator.page(page_no)
    except (EmptyPage, PageNotAnInteger):
        page =paginator.page(1)
    return page

def index(request):
    """表示と投稿を処理する"""
    form = PostingForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
        #save()メソッドを用いるだけで、DBに登録できる
            form.save()
            #メッセージフレームワークを使い、ユーザーに投稿の成功を伝える
            messages.success(request, '投稿を受け付けました。')
            return redirect('guestborad:index')
        else:
            messages.errors(request, '入力内容に誤りがあります。')
    page = _get_page(
        Posting.objects.order_by('-id'),  #投稿が新しい順に並び替えて取得する
        request.GET.get('page') #GETクエリからページ番号を取得する。
    )
    context = {
        'form' : form,
        'page' : page,
    }
    return render(request,'guestborad/index.html', context)