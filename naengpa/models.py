from django.db import models

# Create your models here.
class Recipe(models.Model):
    name = models.CharField(max_length=200) # 음식 이름
    time = models.IntegerField() # 조리 시간
    need_ingredient = models.CharField(max_length=200)
    content = models.TextField(default='')
    create_date = models.DateTimeField() # 등록일시

    def __str__(self): # .objects.all() 조회시 id대신 name으로
        return self.name

class Answer(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete = models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()