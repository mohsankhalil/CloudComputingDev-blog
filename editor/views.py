from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from .form import EditorAuth, BlogCreateForm
from django.contrib.auth.decorators import login_required
from blog.models import Blog
from django.template.defaultfilters import slugify

# Create your views here.
def LoginViews(request):
    fm = EditorAuth()
    if request.method == "POST":
        fm = EditorAuth(request,data=request.POST)
        
        if fm.is_valid():
            username = fm.cleaned_data['username']
            pwd = fm.cleaned_data['password']
            user = authenticate(username=username,password=pwd)
            if user is not None:
                login(request,user)
                return redirect("dashboard")
    return render(request,'editor/auth/login.html',{'form':fm})


@login_required(login_url="editor_login")
def dashboardView(request):
    user = request.user
    if user.is_editor:
        blogs = Blog.objects.filter(created_by=user).order_by('-id')
    else:
        blogs = Blog.objects.all().order_by('-id')
    
    fname = user.first_name
    group = user.groups.all()
    return render(request,'editor/home/dashboard.html',{'blogs':blogs,'group':group,'full_name':fname})

@login_required(login_url="editor_login")
def AddBlogView(request):
    fm = BlogCreateForm()
    if request.method == "POST":
        fm = BlogCreateForm(request.POST)
        if fm.is_valid():
            title = fm.cleaned_data['title']
            subtitle = fm.cleaned_data['subtitle']
            post = fm.cleaned_data['post']
            status = fm.cleaned_data['status']
            
            postc = Blog(title=title,slug=slugify(title),subtitle=subtitle,post=post,status=False,created_by=request.user)
            postc.save()
            return redirect("dashboard")
            
    return render(request,'editor/home/add-blog.html',{'form':fm})
    
@login_required(login_url="editor_login")
def editPostView(request,id):
    pi = Blog.objects.get(pk=id)
    fm = BlogCreateForm(instance=pi)
    if request.method == "POST":
        fm = BlogCreateForm(request.POST,instance=pi)
        if fm.is_valid():
            fm.save()
            return redirect("dashboard")
    return render(request,'editor/home/edit-blog.html',{'form':fm})


def deletePostView(request,id):
    if request.method == "GET":
        Blog.objects.get(id=id).delete()
    return redirect("dashboard")
    


def logoutView(request):
    logout(request)
    return redirect("editor_login")