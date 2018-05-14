# -*- coding: utf-8 -*-


from django.db import models

# Create your models here.


# 课程类别，按课程类别爬取数据
class course_type(models.Model):
    name = models.CharField(max_length=20, verbose_name=u'课程类别名称')
    type_url = models.CharField(max_length=50, verbose_name=u'课程类别页面的url')
    class Meta:
        verbose_name = u'课程类别'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


# 课程
class course(models.Model):
    course_type = models.ForeignKey(course_type, verbose_name=u'所属课程类别')
    name = models.CharField(max_length=50, verbose_name=u'课程名称')
