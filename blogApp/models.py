from django.db import models
from datetime import datetime
#  author and content in creation


class Content(models.Model):
  blog_num=models.AutoField
  title=models.CharField(max_length=50, default="")
  content=models.CharField(max_length=1500, default="")
  category=models.CharField(max_length=25, default="General")
  author=models.CharField(max_length=25,default="Admin")
  image=models.ImageField(upload_to="blog/images", default="")
  pub_date = models.DateField(default=datetime.now)
  slug = models.CharField(max_length=130,default="")

  def __str__(self):
        return self.title