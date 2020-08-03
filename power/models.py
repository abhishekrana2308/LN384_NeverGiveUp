from django.db import models

# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    aadhar = models.CharField(max_length=12, default="000012340000")
    mob = models.CharField(max_length=100, default="0000")
    is_user = models.BooleanField(default=True)

    def __str__(self):
        return self.name
    

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
    person = models.ForeignKey(Person,on_delete=models.CASCADE)
    modified = models.CharField(max_length=100, default="Today")

    def __str__(self):
        return self.name

class Notification(models.Model):
    uid = models.IntegerField()
    bid = models.IntegerField()
    
class Table(models.Model):
    uid = models.IntegerField(default=2)
    name = models.CharField(max_length=100)
    url = models.TextField(max_length=1000, default = 'https://www.upsldc.org/real-time-data')
    xpath = models.TextField(max_length=1000, default = '/html/body/div[2]/div[2]/div/div/div/div/div/div/div/div[1]/div/div/div/div[2]/div/div/div[2]/table')

    def __str__(self):
        return self.name


class Alert(models.Model):
    uid = models.IntegerField(default=2)
    name = models.CharField(max_length=100)
    starttime = models.CharField(max_length=100)
    endtime = models.CharField(max_length=100)
    key = models.CharField(max_length=100)
    avgvalue = models.CharField(max_length=100)
    minmattr = models.CharField(max_length=100)
    minmvalue = models.CharField(max_length=100)
    maxmattr = models.CharField(max_length=100)
    maxmvalue = models.CharField(max_length=100)
    attr = models.IntegerField(default=0)

    def __str__(self):
        return self.name


