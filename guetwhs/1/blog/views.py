#-*- coding:utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse,Http404
from django.contrib import auth
from django.views.generic import View,ListView,CreateView,UpdateView,DetailView,DeleteView
from django.core.exceptions import PermissionDenied
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from haozi.settings import PER_PAGE_COUNT
from django.db.models import Q
import json,logging
import urlparse
from models import *
from itertools import chain
# logger = logging.getLogger(__name__)
# Create your views here.
def logRequestIp(request):
    ip=""
    if request.META.has_key('HTTP_X_FORWARDED_FOR'):
        ip =  request.META['HTTP_X_FORWARDED_FOR']
    else:
        ip = request.META['REMOTE_ADDR']
    # logger.info("有IP请求："+ip)
class userCenter(View):
    def get(self, request, *args, **kwargs):
        raise Http404
    def post(self,request, *args, **kwargs):
        option=None
        try:
            option = self.kwargs.get('option')
        except:
            # logger.error(u'请求参数错误！')
            raise PermissionDenied
        if option == 'login':
            return self.login(request,args,kwargs)
        if option == 'logout':
            return self.logout(request,args,kwargs)
        raise PermissionDenied
    def login(self,request,*args,**kwargs):
        logRequestIp(request)
        refer_string = request.META['HTTP_REFERER']
        url = urlparse.urlparse(refer_string)
        params=urlparse.parse_qs(url.query,True)
        refer = params.get('next','/')
        if request.user.is_authenticated():
            msg = {"error":[],'refer':refer}
            return HttpResponse(json.dumps(msg),content_type="application/json")
        username = request.POST.get('username',"")
        password = request.POST.get('password',"")
        user = auth.authenticate(username=username,password=password)
        error=[]
        if user is not None:
            auth.login(request,user)
        else:
            error.append("用户名或者密码错误")
            logger.error(error)
        msg = {"error":error,'refer':refer}
        return HttpResponse(json.dumps(msg),content_type="application/json")
    def logout(self,request,*args,**kwargs):
        if not request.user.is_authenticated():
            # logger.error(u'[UserControl]用户未登陆')
            raise PermissionDenied
        else:
            auth.logout(request)
            return HttpResponse('OK')
class categoryList(ListView):
    model = Category
    template_name = 'blog/category.html'
    context_object_name = 'category'
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(categoryList, self).dispatch(*args, **kwargs)
class categoryUpdate(UpdateView):
    model = Category
    context_object_name = 'category'
    fields = ['name','parent']
    template_name = 'blog/post_form.html'
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(categoryUpdate, self).dispatch(*args, **kwargs)
    def get_success_url(self):
        return reverse('category')
class categoryCreate(CreateView):
    model = Category
    context_object_name = 'category'
    fields = ['name','parent']
    template_name = 'blog/post_form.html'
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(categoryCreate, self).dispatch(*args, **kwargs)
    def get_success_url(self):
        return reverse('category')
class categoryDelete(DeleteView):
    model = Category
    context_object_name = 'category'
    template_name = "blog/post_form.html"
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(categoryDelete, self).dispatch(*args, **kwargs)
    def get_success_url(self):
        return reverse('category')
class articleList(ListView):
    model = Article
    context_object_name = "article_list"
    allow_empty = True
    paginate_by = PER_PAGE_COUNT

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(articleList, self).get_context_data(**kwargs)
        tag_list=[]
        for item in self.object_list.all():
            tag_list.extend(item.get_tag())
        tag_list=list(set(tag_list))
        tag_list = makeTagCloud(tag_list)
        category = Category.objects.filter(parent=None)
        link_list = friendLink.objects.all()
        context['link_list'] = link_list
        context['category'] = category
        context['tag_list']=tag_list
        return context
class articleDetail(DetailView):
    model = Article
    template_name = "blog/blog_detail.html"
    context_object_name = 'article'
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(articleDetail, self).get_context_data(**kwargs)
        category = Category.objects.filter(parent=None)
        comment = Comment.objects.filter(Q(article=self.kwargs.get('pk'))&Q(pip=None))
        tag_list=[]
        for item in Article.objects.all():
            tag_list.extend(item.get_tag())
        tag_list=list(set(tag_list))
        tag_list = makeTagCloud(tag_list)
        link_list = friendLink.objects.all()
        context['link_list'] = link_list
        context['tag_list']=tag_list
        context['category'] = category
        context['comment'] = comment
        return context
class article_by_category(ListView):
    model = Article
    template_name = "blog/list_by_category.html"
    context_object_name = "article_list"
    allow_empty = True
    paginate_by = PER_PAGE_COUNT
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(article_by_category, self).get_context_data(**kwargs)
        category = Category.objects.filter(parent=None)
        tag_list=[]
        for item in Article.objects.all():
            tag_list.extend(item.get_tag())
        tag_list=list(set(tag_list))
        tag_list = makeTagCloud(tag_list)
        link_list = friendLink.objects.all()
        context['link_list'] = link_list
        context['tag_list']=tag_list
        context['category'] = category
        return context
    def get_queryset(self):
        category = Category.objects.filter(id=self.kwargs['pk'])
        article=Article.objects.filter(category=category)
        return article
class article_by_tag(ListView):
    model = Article
    template_name = "blog/list_by_category.html"
    context_object_name = "article_list"
    allow_empty = True
    paginate_by = PER_PAGE_COUNT
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(article_by_tag, self).get_context_data(**kwargs)
        category = Category.objects.filter(parent=None)
        tag_list=[]
        for item in Article.objects.all():
            tag_list.extend(item.get_tag())
        tag_list=list(set(tag_list))
        tag_list = makeTagCloud(tag_list)
        link_list = friendLink.objects.all()
        context['link_list'] = link_list
        context['tag_list']=tag_list
        context['category'] = category
        return context
    def get_queryset(self):
        article = Article.objects.filter(Q(tag__contains=self.kwargs['pk']))
        return article
class articleUpdate(UpdateView):
    model = Article
    template_name = "blog/create.html"
    context_object_name = "article"
    fields = ['title','content','tag','category']
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(articleUpdate, self).dispatch(*args, **kwargs)
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(articleUpdate, self).get_context_data(**kwargs)
        category = Category.objects.filter(parent=None)
        context['category'] = category
        return context
    def get_success_url(self):
        return reverse('detail', kwargs={
            'pk': self.object.pk,
        })
class articleCreate(CreateView):
    model = Article
    template_name = "blog/create.html"
    context_object_name = "article"
    fields = ['title','content','tag','category']
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(articleCreate, self).dispatch(*args, **kwargs)
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(articleCreate, self).get_context_data(**kwargs)
        category = Category.objects.exclude(parent=None)
        context['category'] = category
        return context
    def get_success_url(self):
        return reverse('detail', kwargs={
            'pk': self.object.pk,
        })
class articleDelete(DeleteView):
    model = Article
    success_url = "/"
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(articleDelete, self).dispatch(*args, **kwargs)
class search(View):
    def get(self, request, *args, **kwargs):
        keyword  = request.GET.get('keyword')
        articles = self.query_data(keyword)
        return render(request,"blog/search.html",{"article_list":articles,"keyword":keyword})
    def post(self, request, *args, **kwargs):
        keyword  =  request.POST.get('keyword')
        articles = self.query_data(keyword)
        return render(request,"blog/search.html",{"article_list":articles,"keyword":keyword})
    def query_data(self,keyword):
        article_1 = Article.objects.filter(Q(title__contains=keyword)|
                                           Q(content__contains=keyword)|
                                           Q(tag__contains=keyword))
        category = Category.objects.filter(Q(name__contains=keyword))
        article_2 = Article.objects.filter(category=category)
        articles = article_1 | article_2
        return articles
class commentCreate(CreateView):
    model = Comment
    fields = ['user','email','content','article','pip']
    template_name = "blog/post_form.html"
    def get_success_url(self):
        return reverse('detail', kwargs=self.kwargs)
class linkCreate(CreateView):
    model = friendLink
    context_object_name = "link"
    fields = ["url","title","img"]
    template_name = "blog/post_form.html"
    def get_success_url(self):
        return reverse("index")
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(linkCreate, self).dispatch(*args, **kwargs)
class linkUpdate(UpdateView):
    model = friendLink
    context_object_name = 'link'
    fields = ["url","title","img"]
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(linkUpdate, self).dispatch(*args, **kwargs)
    def get_success_url(self):
        return reverse("index")
class linkDelete(DeleteView):
    model = friendLink
    template_name = "blog/post_form.html"
    success_url = "/"
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(linkDelete, self).dispatch(*args, **kwargs)
class about(View):
    def get(self, request, *args, **kwargs):
        user = Account.objects.get(id=1)
        someWord = user.someWord
        aboutObject = {
            "关于教育":user.aboutEducation,
            "关于工作":user.aboutWork,
            "关于生活":user.aboutLive,
            "关于梦想":user.aboutDream,
            "关于技能":user.aboutSkill
        }
        return render(request,"blog/about.html",{"about":aboutObject,"word":someWord})
    def post(self, request, *args, **kwargs):
        raise Http404
class updateAbout(UpdateView):
    model = Account
    fields = ['aboutEducation','aboutWork','aboutLive','aboutDream','aboutSkill','someWord']
    template_name = 'blog/modifyAbout.html'
    context_object_name = 'about'
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(updateAbout, self).dispatch(*args, **kwargs)
    def get_success_url(self):
        return reverse('about')
def makeTagCloud(tagList):
    wordList = []
    num =16
    for tag in tagList:
        if tag == tagList[-1]:
            word = """{text:"%s",weight: %0.1f,link:"/tag/list/%s/"}""" %(tag,num,tag)
        else:
            word = """{text:"%s",weight: %0.1f,link:"/tag/list/%s/"},""" %(tag,num,tag)
        wordList.append(word)
        if num >2 :
            num = num - 0.5
    return wordList