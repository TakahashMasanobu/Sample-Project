"""Config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path( 'admin/', admin.site.urls),
    path( 'app/',   include('app.urls',  namespace='app')),
]


#---------------------------
# add by takahab
#---------------------------
from django.contrib          import admin
from django.conf             import settings
from django.conf.urls.static import static
from django.urls             import path, include
from django.urls             import re_path
from django.views.static     import serve


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += [re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT,}),]

# 管理サイトの見出しを変更可能
#  タイトル；タイトルタグで使用
admin.site.site_title = 'タイトル'
#  サイト名：ログイン画面と管理画面上部の表示
admin.site.site_header = '管理サイトへのログイン'
#  メニュー：管理画面の見出し表示
admin.site.index_title = 'メニュー'

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        path('__debug__', include(debug_toolbar.urls)),
    ]
