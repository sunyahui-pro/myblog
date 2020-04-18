from django.db import models


class Comment(models.Model):
    content = models.TextField(verbose_name='评论内容',max_length=140)
    datetime = models.DateTimeField(verbose_name='评论时间',auto_now_add=True)
    comment_user = models.CharField(verbose_name='评论人',max_length=20)