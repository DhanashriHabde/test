from django.db import models

class District(models.Model):
	name=models.CharField(max_length=50,null=False,blank=False)

	def __str__(self):
		return self.name

class Taluka(models.Model):
	name=models.CharField(max_length=50,null=False,blank=False)
	district=models.ForeignKey(District,on_delete=models.CASCADE,related_name='talukas')

	def __str__(self):
		return self.name


class Hospital(models.Model):
	name=models.CharField(max_length=50,null=False,blank=False)
	phone=models.CharField(max_length=12,null=False,blank=False)
	address=models.CharField(max_length=500,null=False,blank=False)
	taluka=models.ForeignKey(Taluka,on_delete=models.CASCADE,related_name='hospitals')

	def __str__(self):
		return self.name
'''	
class Services(models.Model):
	hospital=models.OneToOneField(Hospital,on_delete=models.CASCADE,primary_key=True)
	oxygen_beds_total=models.IntegerField(default=0)
	oxygen_beds_available=models.IntegerField(default=0)
	oxygen_cylinder_total=models.IntegerField(default=0)
	oxygen_cylinder_available=models.IntegerField(default=0)
	ventilator_total=models.IntegerField(default=0)
	ventilator_available=models.IntegerField(default=0)

	def __str__(self):
		return self.hospital.name
'''
class Facility(models.Model):
	title = models.CharField(max_length=60,null=False,blank=False,default="")
	def __str__(self):
		return self.title

	class Meta:
		verbose_name_plural="Facilities"

class Availability(models.Model):
	hospital=models.ForeignKey(Hospital,on_delete=models.CASCADE,related_name="availabilities")
	facility=models.ForeignKey(Facility,on_delete=models.CASCADE,related_name="availabilities")
	total=models.IntegerField(default=0)
	available=models.IntegerField(default=0)
	updated_at=models.DateTimeField(auto_now_add=True)

	class Meta:
		verbose_name_plural="Availabilities"

class Headline(models.Model):
	headline=models.CharField(max_length=200,null=True,blank=True)

	def __str__(self):
		return self.headline
