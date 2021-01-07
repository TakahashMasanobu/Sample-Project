from django.shortcuts import render

# Create your views here.
from django.conf import settings
from django.shortcuts import redirect, render
from django.views import generic
from .models import Book, BuyingHistory

import stripe
stripe.api_key = settings.STRIPE_SECRET_KEY


class IndexView(generic.ListView):
    model = Book


class DetailView(generic.DetailView):
    model = Book

    def post(self, request, *args, **kwargs):
        """購入時の処理"""
        book = self.get_object()
        token = request.POST['stripeToken']  # フォームでのサブミット後に自動で作られる
        try:
            # 購入処理
            charge = stripe.Charge.create(
                amount=book.price,
                currency='jpy',
                source=token,
                description='メール:{} 書籍名:{}'.format(request.user.email, book.title),
            )
        except stripe.error.CardError as e:
            # カード決済が上手く行かなかった(限度額超えとか)ので、メッセージと一緒に再度ページ表示
            context = self.get_context_data()
            context['message'] = 'Your payment cannot be completed. The card has been declined.'
            return render(request, 'app/book_detail.html', context)
        else:
            # 上手く購入できた。Django側にも購入履歴を入れておく
            BuyingHistory.objects.create(book=book, user=request.user, stripe_id=charge.id)
            return redirect('app:index')

    def get_context_data(self, **kwargs):
        """STRIPE_PUBLIC_KEYを渡したいだけ"""
        context = super().get_context_data(**kwargs)
        context['publick_key'] = settings.STRIPE_PUBLIC_KEY
        return context
