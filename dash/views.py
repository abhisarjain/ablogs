from django.contrib.admin.sites import AdminSite
from django.shortcuts import render
from .models import Contact,Profile,Blog,News,ipaddress,Comment
from django.conf import settings
from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User, auth
from django.contrib.auth import authenticate, get_user_model
from .forms import EditProfileForm,BlogForm
from django.contrib import messages
from django.contrib.auth.forms import PasswordChangeForm
import random
from django.core.mail import send_mail
import socket   
hostname = socket.gethostname()   
IPAddr = socket.gethostbyname(hostname) 


def homepage(request):
    blogs = Blog.objects.order_by('-views')
    context = {'blogs': blogs}
    return render(request,'homepage.html',context)


def about(request):
    return render(request,'about.html')


def contact(request):
     if request.method == 'POST':
        name_cu = request.POST['name_cu']
        mail_cu = request.POST['mail_cu']
        feedback = request.POST['feedback']
        contacts = Contact(name_cu=name_cu,mail_cu=mail_cu,feedback=feedback)
        contacts.save()
        messages.info(request, "Your feedback has been sent to the developer")
        return redirect('/')
     else:
        return render(request,'navbar.html')



def dashboard(request):
     if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        password2 = request.POST['password2']
        fn = request.POST['firstname']
        ln = request.POST['lastname']
        mail = request.POST['email']
        bio = request.POST['bio']
        dp = request.FILES.get('dp')
        otp = str(random.randint(1000,9999))
        print(otp)
        User = get_user_model()
        if password != password2:
            messages.info(request, "Passwords not matched")
            return render(request, 'dashboard.html')
        elif not User.objects.filter(username=username).exists():
            ins = User.objects.create_user(username=username, password=password, first_name=fn, last_name=ln,
                                           email=mail,bio=bio,dp=dp,otp=otp)
            ins.is_active = False
            ins.save()
            subject = 'Welcome to ABlogs'
            message = f'Hi {fn} {ln}, Thank You for registering in ABlogs. Your OTP for verification is {otp}. You will not be able to login into your account till you verify '
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [mail]
            send_mail(subject, message, email_from, recipient_list)
            print("db has been created")
            request.session['mail'] = mail
            return redirect('/dashboard/otpvalidation')
        else:
            messages.info(request, "username already taken")
            return render(request, 'dashboard.html')
     else:
        #  User = get_user_model()
        if request.user.is_authenticated:
            title = "My Profile"
        else:
            title = "Get Started"
        return render(request,'dashboard.html',{'title':title})

def otpvalidation(request):
    mail = request.session['mail']
    User = get_user_model()
    if request.method == 'POST':
        otpuser = User.objects.filter(email=mail).first()
        otp_input = request.POST['otp']
        otpcheck = otpuser.otp
        if otp_input!=otpcheck:
            messages.info(request,"You have entered wrong otp. Please Enter the otp again")
            return redirect('/dashboard/otpvalidation')
        else:
            messages.info(request,"Your accout has been created successfully")
            x= User.objects.filter(otp=otpcheck).last()
            x.is_active = True
            x.save()
            return redirect('/dashboard')
    else:
        return render(request,'otpvalidation.html')




def login(request):
    if request.method == 'POST':
        username = request.POST['usernamelg']
        password = request.POST['passwordlg']
        User = get_user_model()
        usercheck = User.objects.filter(username=username).last()
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request,"You have entered Wrong credentials")
            return render(request, 'dashboard.html')

    else:
        if request.user.is_authenticated:
            title = "My Profile"
        else:
            title = "Get Started"
        return render(request, 'dashboard.html',{'title':title})

def logout(request):
    auth.logout(request)
    return redirect('/')


def myprofile(request):
    return render(request,'myprofile.html')


def editprofile(request):
    User = get_user_model()
    if request.user.is_authenticated:
        if request.method == 'POST':
            users = User.objects.get(username=request.user)
            form = EditProfileForm(request.POST,request.FILES, instance=users)
            if form.is_valid():
                form.save()
                return redirect("/dashboard/myprofile")
        else:
            users = User.objects.get(username=request.user)
            form = EditProfileForm(instance=users)
        return render(request, 'editprofile.html', {'form': form})
    else:
        return redirect('/dashboard')
    

def blogs(request):
    blog = Blog.objects.all()
    context = {'blogs': blog}
    return render(request,'blogs.html',context)


def myblogs(request):
    if request.user.is_authenticated:
        blogs = Blog.objects.filter(user=request.user)
        context = {'blogs': blogs}
        return render(request, 'myblogs.html', context)
    else:
        return redirect('/login')



def readmore(request, title):
    add_comment = request.POST.get('comment')
    blogs = Blog.objects.filter(title=title)
    blogss = Blog.objects.get(title=title)
    ipadd = ipaddress.objects.filter(blog=blogs,ipadd=IPAddr)
    # if request.user.is_authenticated:
    comment = Comment.objects.filter(blog = blogss)
    print(blogs)
    print(blogss)
    # print(comment)
    # if not ipadd.exists():
    #     blogs.views = blogs.views + 1
    #     blogs.save()
        
    # else:
    #     ip = ipaddress(blog=blogs,ipadd=IPAddr)
    #     ip.save()
    # for c in comment:
    #     print(c)
        
       
    for blog in blogs:
        print(blog)
        print(blog.views)
        # for c in comment:
        #     print(c)
        blog.views = blog.views + 1
        blog.save()
    context = {'blogs': blogs,'comment':comment}
    if request.method == 'POST':
        addcomment = Comment(blog = blogss,user=request.user,comments=add_comment)
        addcomment.save()
    return render(request, 'readmore.html', context)


def aboutuser(request,id):
    User = get_user_model()
    get_info = User.objects.filter(id=id)
    get_blog_count = Blog.objects.filter(user=id).count()
    print(id)
    # print(get_info.id)
    print(get_blog_count)
    # print(request.user.id)
    context = {'get_info': get_info,'get_blog_count':get_blog_count}
    return render(request, 'aboutuser.html',context) 

def addblog(request):
    if request.method == 'POST':
        title = request.POST['title']
        captitle = title.capitalize()
        desc = request.POST['desc']
        author = request.POST['author']
        image = request.FILES.get('image')
        result = Blog(user=request.user,title=captitle,desc=desc,author=author,image=image)
        print(title)
        result.save()
        return redirect('/dashboard/myblogs')
    else:
        return render(request,'dashboard.html')


def blog_sortby_alphabetically(request):
    blogs = Blog.objects.order_by('title')
    context = {'blogs': blogs}
    return render(request, 'blogs.html', context)

def blog_sortby_mostviewed(request):
    blogs = Blog.objects.order_by('-views')
    context = {'blogs': blogs}
    return render(request, 'blogs.html', context)


def blog_sortby_date(request):
    blogs = Blog.objects.order_by('-date')
    context = {'blogs': blogs}
    return render(request, 'blogs.html', context)


def deleteblog(request, title):
    blogs = Blog.objects.filter(title=title)
    blogs.delete()
    messages.success(request, "Blog deleted successfully")
    return redirect('/dashboard/myblogs')

def editblog(request, title):
    if request.method == 'POST':
        blog = Blog.objects.get(title=title)
        form = BlogForm(request.POST, request.FILES, instance=blog)
        if form.is_valid():
            form.save()
            return redirect('/dashboard/myblogs')
    else:
        blog = Blog.objects.get(title=title)
        form = BlogForm(instance=blog)
    return render(request, 'editblog.html', {'form': form})


def changepassword(request):
    form = PasswordChangeForm(user=request.user)
    return render(request,'changepassword.html',{'form':form})


def search(request):
    query = request.GET['search']
    allposts = Blog.objects.filter(title__icontains=query)
    params = {'blogs': allposts, 'query': query}
    return render(request, 'search.html', params)


def chat(request):
    User = get_user_model()
    get_users = User.objects.all()
    return render(request,'chat.html',{'get_users':get_users})

def dictionary(request):
    if request.method == 'POST':
        import json
        import requests
        app_id  = "b7d38525"
        app_key  = "60065705dd7d6a8f202d6eea55a65e19"
        endpoint = "entries"
        language_code = "en-us"
        word_id = request.POST['word']
        url = "https://od-api.oxforddictionaries.com/api/v2/" + endpoint + "/" + language_code + "/" + word_id.lower() + "?fields=definitions&strictMatch=false"
        r = requests.get(url, headers = {"app_id": app_id, "app_key": app_key})
        # print("code {}\n".format(r.status_code))
        # print("text \n" + r.text)
        # print("json \n" + json.dumps(r.json()))
        dic = r.json()
        x = dic['results'][0]['lexicalEntries'][0]['entries'][0]['senses'][0]['definitions'][0]
        return render(request,'dictionary.html',{'x':x})
    else:
        return render(request,'dictionary.html')
    
def news(request):
    News.objects.all().delete()
    import requests
    from bs4 import BeautifulSoup
    req = requests.get("https://www.inshorts.com/en/read")
    soup = BeautifulSoup(req.content,"html.parser")

    headlines = soup.find_all(attrs={"itemprop": "headline"})

    for headline in headlines:
        result = News(news_title=headline.text)
        if not News.objects.filter(news_title=headline.text).exists():
            result.save()
        print(headline.text)

    # links = soup.find_all(attrs={"class": "source"})
    # for link in links:
    #     print(link['href'])
    

        
    news = News.objects.all()
   
    # for x in range(0, 25):
    #     News.objects.filter().delete()

    return render(request,'news.html',{'news':news})


