from django.db import models
#python manage.py makemigrations   创建

#python manage.py migrate 同步
# Create your models here.


##########创建表结构#################
class Account(models.Model):
    #账户表
    username=models.CharField(max_length=64,unique=True)
    email=models.EmailField(unique=True)
    password=models.CharField(max_length=255)
    register_data=models.DateTimeField(auto_now_add=True)
    signature=models.CharField(max_length=255,null=True)
# models.Account.objects.creat(
#     username="alex",
#     email="alex@luffycity.com",
#     password="abc123",
#     register_data="datatime.datatime.now()",
#     signature='chaos is a ladder.',
# )

#查询 
#models.Account.object.All()
#models.Account.object.filter(id=1)
    def __str__(self):
        return self.username


class Article(models.Model):
    title=models.CharField(max_length=255,unique=True)
    content=models.TextField()
    account=models.ForeignKey("Account",on_delete=models.CASCADE)#关联两张表里面的Account
    tags=models.ManyToManyField('Tag',null=True)
    pub_data=models.DateTimeField()
####    a2.tags.add(1,2)
######### a2.tags.set([3,4])两种添加方式

#数据绑定第一种方式
# s=models.Article(
#  title='小臂',
#  content='hehe',
#  pub_data='2018.5.3')
#  s.account_id=1
#  s.save()

class tag(models.Model):
    name=models.CharField(max_length=64,unique=True)
    data=models.DateTimeField(auto_now_add=True)



#数据创建方式
# models.Account.objects.creat(
#     username="alex",
#     email="alex@luffycity.com",
#     password="abc123",
#     register_data="datatime.datatime.now()",
#     signature='chaos is a ladder.',
# )
# o=models.Account(
#     username="jack",
#     email="jack@luffycity.com",
#     password="abc123",
#
# )
# o.save()
#数据绑定第一种方式
# s=models.Article(
#  title='小臂',
#  content='hehe',
#  pub_data='2018.5.3')
#  s.account_id=1
#  s.save()



数据绑定第二种方式
#     # a1=models.Account(
#  username='bisheng',
#  email='bisheng@qq.com',
#  password='111',
#  )
#  a1.save()
#  a2=models.Article(
#     title='test',
#      content='haha',
#     pub_data='2022-03-30',)
# a2.account=a1
# # a2.save()
#
#
# tags.set([1,2,3])
# tags.add(1,2,3)

