from django.db import models

class Blog(models.Model):
    blog_title=models.CharField(max_length=100)
    blog_content=models.TextField(max_length=500)
    created_at=models.DateTimeField(auto_now_add=True)
    upload_to=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.blog_title
    

class Comment(models.Model):
    blog=models.ForeignKey(Blog, on_delete=models.CASCADE , related_name='comments')
    comment_title=models.CharField(max_length=200)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.comment_title
