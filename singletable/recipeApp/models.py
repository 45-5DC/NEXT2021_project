from django.db import models
from userApp.models import Profile

# Create your models here.
class RecipePost(models.Model):
    title = models.CharField(max_length=200, verbose_name="제목")
    content = models.TextField(max_length=200, null=True, verbose_name="내용")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="생성날짜", null=True)
    updated_at = models.DateTimeField(auto_now=True, verbose_name="수정날짜", null=True)
    category = models.CharField(max_length=200)
    author = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='recipe_posts', null=True)
    like = models.IntegerField(null=True)
    def __str__(self):
        return f'{self.title} | {self.content}'

class RecipeComment(models.Model):
    post = models.ForeignKey(RecipePost, on_delete=models.CASCADE, related_name='recipe_comments')
    content = models.TextField(verbose_name="댓글")
    author = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='recipe_comments', null=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="생성날짜", null=True)
    updated_at = models.DateTimeField(auto_now=True, verbose_name="수정날짜", null=True)


class RecipeImages(models.Model):
    post = models.ForeignKey(RecipePost, on_delete=models.CASCADE, related_name='recipe_images')
    image = models.ImageField(upload_to='singletable/image/%Y/%m', blank=True)

# # 이미지-컨텐츠 연결 위한 새 이미지 모델
# # (사용 시) 위의 이름 같은 모델과 교체 + RecipePost에서 content 빼기
# class RecipeImages(models.Model):
#     post = models.ForeignKey(RecipePost, on_delete=models.CASCADE, related_name='recipe_images')
#     image = models.ImageField(upload_to='singletable/image/%Y/%m', blank=True)
#     content = models.TextField(max_length=200, null=True, verbose_name="내용")
