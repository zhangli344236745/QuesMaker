# Generated by Django 4.2.7 on 2024-03-31 16:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="ApiWhiteList",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        help_text="Id",
                        primary_key=True,
                        serialize=False,
                        verbose_name="Id",
                    ),
                ),
                (
                    "description",
                    models.CharField(
                        blank=True,
                        help_text="描述",
                        max_length=255,
                        null=True,
                        verbose_name="描述",
                    ),
                ),
                (
                    "modifier",
                    models.CharField(
                        blank=True,
                        help_text="修改人",
                        max_length=255,
                        null=True,
                        verbose_name="修改人",
                    ),
                ),
                (
                    "dept_belong_id",
                    models.CharField(
                        blank=True,
                        help_text="数据归属部门",
                        max_length=255,
                        null=True,
                        verbose_name="数据归属部门",
                    ),
                ),
                (
                    "update_datetime",
                    models.DateTimeField(
                        auto_now=True, help_text="修改时间", null=True, verbose_name="修改时间"
                    ),
                ),
                (
                    "create_datetime",
                    models.DateTimeField(
                        auto_now_add=True,
                        help_text="创建时间",
                        null=True,
                        verbose_name="创建时间",
                    ),
                ),
                (
                    "is_deleted",
                    models.BooleanField(
                        db_index=True,
                        default=False,
                        help_text="是否软删除",
                        verbose_name="是否软删除",
                    ),
                ),
                (
                    "url",
                    models.CharField(
                        help_text="url地址", max_length=200, verbose_name="url"
                    ),
                ),
                (
                    "method",
                    models.IntegerField(
                        blank=True,
                        default=0,
                        help_text="接口请求方法",
                        null=True,
                        verbose_name="接口请求方法",
                    ),
                ),
                (
                    "enable_datasource",
                    models.BooleanField(
                        blank=True,
                        default=True,
                        help_text="激活数据权限",
                        verbose_name="激活数据权限",
                    ),
                ),
                (
                    "creator",
                    models.ForeignKey(
                        db_constraint=False,
                        help_text="创建人",
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_query_name="creator_query",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="创建人",
                    ),
                ),
            ],
            options={
                "verbose_name": "接口白名单",
                "verbose_name_plural": "接口白名单",
                "db_table": "api_white_list",
                "ordering": ("-create_datetime",),
            },
        ),
    ]
