"""my_site URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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

from django.urls import path,re_path,include
from app01 import views




extra_url=[

    # 正则表达式，参数界定
    re_path(r'2003/$', views.article),
    re_path(r'(?P<year>[0-9]{4})/$', views.article_2003),
    re_path(r'([0-9]{4})/([0-9]{2})/$', views.article_year_month),
    re_path(r'(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/(?P<slug>[\w-]+)/$', views.article3),
]

urlpatterns = [
    path('test/', views.test_view),
    path('login/', views.login_view),
    path('article/',include(extra_url)),#去掉重复的URL，使用extra定义url
    #Django自带正则
    path('book/',views.book_2003),
    path('book/<int:year>/',views.book2),
    path('book/<int:year>/<int:month>/',views.book3),
#    path('book/<int:year>/<int:month>/<slug:slug>',views.book4),
#    path('book/<int:month>/<str:name>/',views.book5),
    path('book/<int:year>/<str:name>/',views.book6,{'version':'v1.0'}),#在后面增加参数，有点鸡肋
    path('sql_test',views.sql_test),
]
