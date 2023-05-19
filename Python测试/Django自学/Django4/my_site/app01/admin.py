from django.contrib import admin
from app01 import models
# Register your models here.


#定制
class AccountAdmin(admin.ModelAdmin):
    list_display=('username','email','signature')#列表显示
    search_fields=('username','email')
    list_filter=('username',)
class ArticleAdmin(admin.ModelAdmin):
    list_display=('title','pub_data','account','get_comment','get_tag')#列表显示
    search_fields=('username','pub_data')
    list_filter=('account','pub_data')
    #fields = ('title','content',('pub_data','read_count'))
    data_hierarchy='pub_data'
 #   fields = ('account','title')####过滤显示，不建议使用


class TagAdmin(admin.ModelAdmin):
    list_display = ['name', 'colored_name']
admin.site.register(models.Account,AccountAdmin)#绑定需要定制的东西
admin.site.register(models.Article,ArticleAdmin)
admin.site.register(models.tag,TagAdmin)

# #后台注册
# admin.site.register(models.Account)
# admin.site.register(models.Article)
# admin.site.register(models.tag)

