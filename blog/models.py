from django.db import models
from accounts.models import ExtendUser

class Blog(models.Model):
    title = models.CharField(max_length=100, default='title of blog')
    content = models.TextField()
    author = models.ForeignKey(ExtendUser, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta():
        verbose_name = "Blog" 
    
    def __str__(self):
        return self.title

class Comment(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(ExtendUser, on_delete=models.CASCADE, related_name='comments')
    email = models.EmailField(blank=True, null=True)
    name = models.CharField(max_length=100, null=True)
    text = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(ExtendUser, related_name='comment_likes')

    def __str__(self):
        return self.blog.title