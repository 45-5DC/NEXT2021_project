from django.db import models
from user.models import User

# Create your models here.
class Purchase(models.Model):
    title = models.CharField(max_length=200, verbose_name="제목")
    content = models.TextField(max_length=200, null=True, verbose_name="내용")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="생성날짜", null=True)
    updated_at = models.DateTimeField(auto_now_add=True, verbose_name="수정날짜", null=True)
    category = models.CharField(max_length=200)
    image = models.ImageField(blank=True, upload_to='purchase/image/%Y/%m')
    link = models.TextField(null=True, verbose_name="구매링크")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts', null=True)
    def __str__(self):
        return f'{self.title} | {self.content}'

class PurchaseComment(models.Model):
    posts = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField(verbose_name="댓글")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments', null=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="생성날짜", null=True)
    updated_at = models.DateTimeField(auto_now_add=True, verbose_name="수정날짜", null=True)