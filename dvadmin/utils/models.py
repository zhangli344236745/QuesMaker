import uuid
from django.apps import apps
from django.db import models
from django.db.models import QuerySet
from django.contrib.auth.models import User

class SoftDeleteQuerySet(QuerySet):
    def delete(self,soft_delete=True):
        if soft_delete:
            return self.update(is_deleted=True)
        else:
            return super(SoftDeleteQuerySet,self).delete()

class SoftDeleteManager(models.Manager):
    def __init__(self,*args,**kwargs):
        self.__add_is_del_filter = False
        super(SoftDeleteManager,self).__init__(*args, **kwargs)

    def fitler(self,*args,**kwargs):
        if not kwargs.get("is_deleted") is None:
            self.__add_is_del_filter = True
        return super(SoftDeleteManager,self).filter(*args, **kwargs)

    def get_queryset(self):
        if self.__add_is_del_filter:
            return SoftDeleteQuerySet(self.model, using=self._db).exclude(is_deleted=False)
        return SoftDeleteQuerySet(self.model).exclude(is_deleted=True)

    def get_by_natural_key(self,name):
        return SoftDeleteQuerySet(self.model).get(username=name)

class CoreModel(models.Model):
    """
    核心标准抽象模型模型,可直接继承使用
    增加审计字段, 覆盖字段时, 字段名称请勿修改, 必须统一审计字段名称
    """
    id = models.BigAutoField(primary_key=True, help_text="Id", verbose_name="Id")
    description = models.CharField(max_length=255, verbose_name="描述", null=True, blank=True, help_text="描述")
    creator = models.ForeignKey(to=User, related_query_name='creator_query', null=True,
                                verbose_name='创建人', help_text="创建人", on_delete=models.SET_NULL, db_constraint=False)
    modifier = models.CharField(max_length=255, null=True, blank=True, help_text="修改人", verbose_name="修改人")
    dept_belong_id = models.CharField(max_length=255, help_text="数据归属部门", null=True, blank=True, verbose_name="数据归属部门")
    update_datetime = models.DateTimeField(auto_now=True, null=True, blank=True, help_text="修改时间", verbose_name="修改时间")
    create_datetime = models.DateTimeField(auto_now_add=True, null=True, blank=True, help_text="创建时间",
                                           verbose_name="创建时间")
    is_deleted = models.BooleanField(verbose_name="是否软删除",help_text='是否软删除', default=False, db_index=True)
    objects = SoftDeleteManager()


    class Meta:
        abstract = True
        verbose_name = '核心模型'
        verbose_name_plural = verbose_name

    def delete(self, using=None, soft_delete=True, *args, **kwargs):
        """
        Soft delete object (set its ``is_deleted`` field to True).
        Actually delete object if setting ``soft`` to False.
        """
        if soft_delete:
            self.is_deleted = True
            self.save(using=using)
        else:
            return super(CoreModel, self).delete(using=using, *args, **kwargs)