
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [    

    path('', views.homepage,name='homepage'),
    path('about/', views.about,name='about'),
    path('contact/', views.contact,name='contact'),
    path('dashboard/', views.dashboard,name='dashboard'),
    path("search/", views.search,name = "search"),
    path('dashboard/otpvalidation/', views.otpvalidation,name='otpvalidation'),
    path('login/', views.login,name='login'),
    path("logout/", views.logout,name = "logout"),
    path('blogs/',views.blogs,name='blogs'),
    path('blogs/alphabetically/',views.blog_sortby_alphabetically,name='alphabetically'),
    path('blogs/mostviewed/',views.blog_sortby_mostviewed,name='mostviewed'),
    path('blogs/newest/',views.blog_sortby_date,name='newest'),
    path("blogs/<str:title>/", views.readmore,name = "readmore"),
    path("aboutuser/<int:id>/", views.aboutuser,name = "aboutuser"),
    path('dashboard/myprofile/',views.myprofile,name='myprofile'),
    path('dashboard/chat/',views.chat,name='chat'),
    path('dashboard/myblogs/',views.myblogs,name='myblogs'),
    path('dashboard/dictionary/',views.dictionary,name='dictionary'),
    path('dashboard/news/',views.news,name='news'),
    path('dashboard/myblogs/addblog/',views.addblog,name='addblog'),
    path("dashboard/<str:title>/deleteblog/", views.deleteblog,name = "deleteblog"),
    path("dashboard/<str:title>/editblog/", views.editblog,name = "editblog"),
    path('dashboard/myprofile/editprofile/',views.editprofile,name='editprofile'),
    path('dashboard/myprofile/changepassword/',views.changepassword,name='changepassword'),

    # FORGOT PASSWORD URLs
    path('reset_password/',auth_views.PasswordResetView.as_view(template_name='reset_password.html'),name='reset_password'),
    path('reset_password_sent/',auth_views.PasswordResetDoneView.as_view(template_name='reset_password_sent.html'),name='password_reset_done'),
    path('reset/<uidb64>/<token>',auth_views.PasswordResetConfirmView.as_view(template_name='reset_password_confirm.html'),name='password_reset_confirm'),
    path('reset_password_complete/',auth_views.PasswordResetCompleteView.as_view(template_name='reset_password_complete.html'),name='password_reset_complete'),
]

