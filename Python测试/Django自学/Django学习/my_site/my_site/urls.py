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
from django.urls import register_converter
from  . import converters
register_converter(converters.yearConverter, "yyyy")

urlpatterns = [
 #   path('admin/', admin.site.urls),
 #   path('test/',views.test_view),
  ##  #正则表达式，参数界定
  #  re_path(r'articles/2003/$',views.article),
  ## re_path(r'^articles/(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/(?P<slug>[\w-]+)/$',views.article3),
   # #Django自带正则
  #  path('book/',views.book_2003),
  #  path('book/<int:year>/',views.book2),
   # path('book/<int:year>/<int:month>/',views.book3),
   # path('book/<int:year>/<int:month>/<slug:slug>',views.book4),
#    path('book/<int:month>/<str:name>/',views.book5),
   # path('book/<yyyy:year>/<str:name>/',views.book6)

]
