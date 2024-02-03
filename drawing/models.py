from django.db import models

class TimestampMode(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Sensor(TimestampMode):
    sensor_name = models.CharField(verbose_name="传感器名称", max_length=50, unique=True, null=False, blank=False)

    class Meta:
        db_table = "draw_sensor"

    def __str__(self):
        return "%s" % (self.sensor_name)


class Project(TimestampMode):
    project_name = models.CharField(verbose_name="项目名称", max_length=50, unique=True, null=False, blank=False)
    sensor = models.ForeignKey(verbose_name="所属传感器",to=Sensor,on_delete=models.PROTECT)

    class Meta:
        db_table = "draw_project"

    def __str__(self):
        return "%s" % (self.project_name)


class Data(TimestampMode):
    data_name = models.CharField(verbose_name="资料名称", max_length=50, unique=True, null=False, blank=False)
    sensor = models.ForeignKey(verbose_name="所属传感器",to=Sensor,on_delete=models.PROTECT)
    project = models.ForeignKey(verbose_name="所属项目", to=Project, on_delete=models.PROTECT)

    class Meta:
        db_table = "draw_data"

    def __str__(self):
        return "%s" % (self.data_name)


class Drawing(TimestampMode):
    material_code = models.CharField(verbose_name="物料编号", max_length=50, blank=False)
    sensor = models.ForeignKey(verbose_name="所属传感器", to=Sensor, on_delete=models.PROTECT)
    project = models.ForeignKey(verbose_name="所属项目", to=Project, on_delete=models.PROTECT)
    data = models.ForeignKey(verbose_name="所属资料", to=Data, on_delete=models.PROTECT)
    drawing_name = models.CharField(verbose_name="材料名称", max_length=50, blank=False)
    drawing_spec = models.CharField(verbose_name="规格/图纸号", max_length=50, blank=False)
    drawing_page = models.CharField(verbose_name="图纸页数", max_length=50, blank=False)
    drawing_client_id = models.CharField(verbose_name="客户编号", max_length=50)
    drawing_version = models.CharField(verbose_name="版本号", max_length=50, blank=False)
    drawing_remark = models.CharField(verbose_name="备注", max_length=100)
    drawing_url = models.CharField(verbose_name="地址", max_length=100)
    is_deleted = models.IntegerField(verbose_name="逻辑删除0否1是", blank=False, default=0)

    class Meta:
        db_table = "draw_drawing"

    def __str__(self):
        return "%s" % (self.drawing_name)










