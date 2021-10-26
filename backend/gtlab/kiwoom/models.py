from django.db import models
from django.conf import settings
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.

# 연습삼아 만들어봄
class textboard(models.Model):
    
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    title = models.CharField(max_length=200)
    contents = models.CharField(max_length=200)
    img_url = models.CharField(max_length=200)

    board_text = RichTextUploadingField(null=True)

    def publish(self):
        self.save()

    def __str__(self):
        return self.title

# 관리자 페이지에서 유저들의 정보를 저장하기 위해 모델 선언
class MemberInfo(models.Model):
    username    = models.CharField(max_length=100, verbose_name='유저ID')
    email       = models.EmailField(max_length=100, verbose_name='유저이메일')
    password    = models.CharField(max_length=100, verbose_name='유저비밀번호')
    created_at  = models.DateTimeField(auto_now_add=True, verbose_name='가입날짜')
    updated_at  = models.DateTimeField(auto_now=True, verbose_name='마지막수정일')

    def __str__(self):
        return self.username
    
    class Meta:
        db_table             = 'MemberInfo'
        verbose_name         = '게시판 맴버'
        verbose_name_plural  = '게시판맴버'

