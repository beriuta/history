from django.db import models

"""
这是自联表,是一个评论级别的例子
"""


# Create your models here.
class Comment(models.Model):
    content = models.CharField(max_length=20)
    push_time = models.DateTimeField(auto_now_add=True)
    p_comment = models.ForeignKey(to='Comment', null=True)

    def __str__(self):
        return self.content
