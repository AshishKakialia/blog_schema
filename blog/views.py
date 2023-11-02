import os
from django.shortcuts import render
from django.shortcuts import render, redirect
from .models import Blog, Comment
from .forms import BlogForm, CommentForm
from django.core.paginator import Paginator
from django.http import JsonResponse
from django.core.mail import send_mail
from django.core.exceptions import ValidationError
from django.contrib import messages


def home(request):
    if 'username' in request.session:
        user = request.user
        blog = Blog.objects.all()
        return render(request, 'main/home.html', {'blog':blog, 'user':user}) 
    return redirect('/accounts/login')

def blog_list(request):
    if 'username' in request.session:
        user = request.user
        blogs = Blog.objects.all()
        paginator = Paginator(blogs, 5)  # Show 5 blogs per page
        page = request.GET.get('page')
        blogs = paginator.get_page(page)
        return render(request, 'blog/blog_list.html', {'blogs': blogs, 'user':user})
    return redirect('/accounts/login')

def blog_detail(request, blog_id):
    if 'username' in request.session:
        user = request.user
        blog = Blog.objects.get(id=blog_id)
        comments = blog.comments.filter(blog=blog)

        if request.method == 'POST':
            comment_form = CommentForm(request.POST)
            if comment_form.is_valid():
                new_comment = comment_form.save(commit=False)
                new_comment.blog = blog
                new_comment.user = request.user
                new_comment.save()
                return redirect('blog:blog_detail', blog_id=blog.id)
        else:
            comment_form = CommentForm()
        return render(request, 'blog/blog_detail.html', {'blog': blog, 'comments': comments, 'comment_form': comment_form, 'user':user})
    return redirect('/accounts/login')

def like_comment(request, comment_id, blog_id):
    if 'username' in request.session:
        # if request.method == 'POST':
        comment = Comment.objects.get(id=comment_id)
        user = request.user
        if user in comment.likes.all():
            comment.likes.remove(user)
        else:
            comment.likes.add(user)
        return redirect('blog_detail',blog_id=blog_id)
    return redirect('/accounts/login')

def share_blog(request, blog_id):
    if 'username' in request.session:
        if request.method == 'POST':
            blog = Blog.objects.get(id=blog_id)
            recipient_email = request.POST.get('recipient_email')
            auth_user=os.environ.get('EMAIL_HOST_USER'),
            auth_password=os.environ.get('EMAIL_HOST_PASSWORD')
            print(auth_user,auth_password)
            if recipient_email:
                try:
                    send_mail(
                        'Check out this blog!',
                        f"Hey, I thought you might like this blog: {blog.title}. Check it out at {request.build_absolute_uri()}.",
                        os.environ.get('EMAIL_HOST_USER'),
                        [recipient_email],
                        fail_silently=False,
                        auth_user=os.environ.get('EMAIL_HOST_USER'),
                        auth_password=os.environ.get('EMAIL_HOST_PASSWORD')
                    )
                    messages.success(request, "Blog shared")
                    # return JsonResponse({'success': True})
                except ValidationError as msg:
                    messages.warning(request, msg)
                    print('validation error = ', msg)
                    # return JsonResponse({'success': False})
            else:
                return JsonResponse({'success': False})
    return redirect('/accounts/login')

def add_comment(request, blog_id):
    if request.method == 'POST':
        blog = Blog.objects.get(id=blog_id)
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.blog = blog
            new_comment.user = request.user  # Assuming you're using user authentication
            new_comment.save()
            return redirect('blog_detail', blog_id=blog.id)
        