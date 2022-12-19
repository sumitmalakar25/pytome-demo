from django.db import models

class Complain(models.Model):
    date = models.DateField()
    name=models.CharField(max_length=50)
    phone = models.CharField(max_length=12)
    address = models.CharField(max_length=400)
    complain = models.CharField(max_length=600)

    def register(self):

        # aak
        self.save()
    @staticmethod
    def get_complain_by_name(name):
        # get returns only one data filte give all records
        try:
            return Complain.objects.get(name=name)
        except:
            return False
    def isExists(self):
        if Complain.objects.filter(name=self.name):
            return True
        return False