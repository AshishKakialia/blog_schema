from django.urls import path, include
from blog.views import *


urlpatterns = [
    path('', blog_list, name='blog_list'),
    path('blog/<int:blog_id>/', blog_detail, name='blog_detail'),
    # path('create_blog/', create_blog, name='create_blog'),
    path('share_blog/<int:blog_id>/', share_blog, name='share_blog'),
    path('like_comment/<int:comment_id>/<int:blog_id>', like_comment, name='like_comment'),path('', home, name='home'),
    path('add_comment/<int:blog_id>/', add_comment, name='add_comment'),
]