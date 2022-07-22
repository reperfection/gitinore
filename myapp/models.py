from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField('data published')
    body = models.TextField()
    image = models.ImageField(upload_to = 'images/', blank = True)
    hashtags = models.ManyToManyField('HashTag', blank = True)
    def __str__(self):
        return self.title
    
class Comment(models.Model):
    def __str__(self):
        return self.text
        
    blog_id = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='comments')
    text = models.CharField(max_length=50)

class HashTag(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name
    