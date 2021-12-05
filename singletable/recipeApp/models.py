from django.db import models
from userApp.models import Profile

# Create your models here.
class RecipePost(models.Model):
    title = models.CharField(max_length=200, verbose_name="제목")
    # content = models.TextField(max_length=200, null=True, verbose_name="내용") # 레시피이미지와 함께 세팅
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="생성날짜", null=True)
    updated_at = models.DateTimeField(auto_now=True, verbose_name="수정날짜", null=True)
    category = models.CharField(max_length=200)
    author = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='recipe_posts', null=True)
    like = models.IntegerField(null=True, default=0)
    def __str__(self):
        return self.title
        # return f'{self.title} | {self.content}'

class RecipeComment(models.Model):
    post = models.ForeignKey(RecipePost, on_delete=models.CASCADE, related_name='recipe_comments', null=True)
    content = models.TextField(verbose_name="댓글")
    author = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='recipe_comments', null=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="생성날짜", null=True)
    updated_at = models.DateTimeField(auto_now=True, verbose_name="수정날짜", null=True)

class RecipeImages(models.Model):
    post = models.ForeignKey(RecipePost, on_delete=models.CASCADE, related_name='recipe_images', null=True)
    image = models.ImageField(upload_to='singletable/image/%Y/%m', blank=True)
    content = models.TextField(max_length=200, null=True, verbose_name="내용")

# # 기존
# class RecipeImages(models.Model):
#     post = models.ForeignKey(RecipePost, on_delete=models.CASCADE, related_name='recipe_images', null=True)
#     image = models.ImageField(upload_to='singletable/image/%Y/%m', blank=True)