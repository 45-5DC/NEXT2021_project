from django.db import models
from userApp.models import Profile

# Create your models here.
class RecipePost(models.Model):
    title = models.CharField(max_length=200, verbose_name="제목")
    content = models.TextField(max_length=200, null=True, verbose_name="내용")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="생성날짜", null=True)
    updated_at = models.DateTimeField(auto_now_add=True, verbose_name="수정날짜", null=True)
    category = models.CharField(max_length=200)
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='recipe_posts', null=True)
    like = models.IntegerField(null=True)
    def __str__(self):
        return f'{self.title} | {self.content}'

class RecipeComment(models.Model):
    posts = models.ForeignKey(RecipePost, on_delete=models.CASCADE, related_name='recipe_comments')
    content = models.TextField(verbose_name="댓글")
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='recipe_comments', null=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="생성날짜", null=True)
    updated_at = models.DateTimeField(auto_now_add=True, verbose_name="수정날짜", null=True)


class RecipeImages(models.Model):
    post = models.ForeignKey(RecipePost, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='singletable/image/%Y/%m', blank=True)