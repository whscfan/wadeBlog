# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.urlresolvers import reverse
import logging
# Create your models here.
# 用户表
logger = logging.getLogger(__name__)
class Account(AbstractUser):
    qq = models.CharField(blank=True, max_length=255, null=True,verbose_name=u"QQ")
    sex = models.IntegerField(blank=True, null=True,default=1,verbose_name=u"性别")
    mobile = models.CharField(blank=True, null=True, max_length=11, unique=True,verbose_name=u"手机号")
    icon = models.ImageField(upload_to='userIcon/%Y/%m', default='sysIcon/user1.png',verbose_name=u"头像")
    aboutEducation = models.TextField(blank=True,null=True,verbose_name=u"关于教育")
    aboutWork = models.TextField(blank=True,null=True,verbose_name=u"关于工作")
    aboutSkill = models.TextField(blank=True,null=True,verbose_name=u"关于技能")
    aboutLive = models.TextField(blank=True,null=True,verbose_name=u"关于生活")
    aboutDream = models.TextField(blank=True,null=True,verbose_name=u"关于梦想")
    someWord = models.TextField(blank=True,null=True,verbose_name=u"想说的话")
    class Meta:
        db_table = 'account'
# 分类表
class Category(models.Model):
    name = models.CharField(max_length=255, default="默认分类", unique=True,verbose_name=u"分类")
    parent = models.ForeignKey('self',blank=True,null=True,verbose_name=u'父分类')
    class Meta:
        db_table = 'category'
    def __unicode__(self):
        return self.name
    def getChild(self):
        child=None
        try:
            child = Category.objects.filter(parent=self.pk)
        except:
            pass
        return child

# 文章表
class Article(models.Model):
    title = models.TextField(blank=True, null=True,verbose_name=u"文章标题")
    content = models.TextField(blank=True, null=True,verbose_name=u"文章内容")
    created = models.DateTimeField(auto_now_add=True,verbose_name=u"创建时间")
    lastModify = models.DateTimeField(auto_now=True,verbose_name=u"最后修改时间")
    tag = models.TextField(default=u"默认标签",verbose_name=u"标签")
    views = models.IntegerField(default=0,verbose_name=u'浏览量')
    category = models.ForeignKey('Category',default="1",verbose_name=u"分类")
    account = models.ForeignKey('Account', default=1,verbose_name=u"作者")

    class Meta:
        db_table = 'article'
        ordering = ['-created']
    def __unicode__(self):
        return self.title
    def get_tag(self):
        return self.tag.split(',')

# 留言
class Comment(models.Model):
    content = models.TextField(verbose_name=u"留言内容")
    created = models.DateTimeField(auto_now_add=True,verbose_name=u"创建时间")
    article = models.ForeignKey('Article', blank=True)
    user = models.CharField(max_length=255,blank=True, null=True, default="匿名用户",verbose_name=u"用户")
    email = models.CharField(max_length=255, blank=True,verbose_name=u"邮箱")
    pip = models.ForeignKey('self', blank=True, null=True,verbose_name=u"父ID")

    class Meta:
        db_table = 'comment'
        ordering = ['created']
    def __unicode__(self):
        return self.content
    def get_child(self):
        child=None
        try:
            child = Comment.objects.filter(pip=self.pk)
        except:
            pass
        return child
class friendLink(models.Model):
    url = models.TextField(verbose_name=u"链接")
    title = models.CharField(max_length=255)
    img = models.TextField(verbose_name=u"图片链接" ,blank=True,null=True)
    class Meta:
        db_table="friendlink"
