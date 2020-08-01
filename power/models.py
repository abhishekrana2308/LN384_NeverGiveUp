from django.db import models

# Create your models here.

class Sector(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Board(models.Model):
    sector = models.ForeignKey(Sector, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    state = models.CharField(max_length=100)
    url = models.TextField(max_length=1000, default="http://www.mperc.in/consolidated-reg.htm")
    xpath = models.TextField(max_length=1000, default="/html/body/table/tbody/tr/td/div/center/table[1]/tbody/tr/td[6]/table/tbody/tr/td[2]/table/tbody/tr/td/table/tbody/tr[2]/td[69]")
    # person = models.ForeignKey(Person,on_delete=models.CASCADE)
    modified = models.CharField(max_length=100, default="Today")

    def __str__(self):
        return self.name
