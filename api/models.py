from django.db import models
from django.contrib.auth.models import User

class ClassifiedUser(models.Model):

	MALE = 'MALE'
	FEMALE = 'FEMALE'
	OTHER = 'OTHER'

	MARRIED = 'MARRIED'
	SEPERATED = 'SEPERATED'
	DIVORCED = 'DIVORCED'
	WIDOWED = 'WIDOWED'
	NEVER_MARRIED = 'NEVER_MARRIED'

	MARITAL_STATUS = (
		(MARRIED , 'MARRIED'),
		(SEPERATED,'SEPERATED'),
		(DIVORCED, 'DIVORCED'),
		(WIDOWED, 'WIDOWED'),
		(NEVER_MARRIED, 'NEVER_MARRIED'),
		)

	GENDER = (
		(MALE,'MALE'),
		(FEMALE,'FEMALE'),
		(OTHER,'OTHER'),
		)

	A = 'A'
	B = 'B'
	C = 'C'
	D = 'D'

	CATEGORY = (
		(A, 'A'),
		(B, 'B'),
		(C, 'C'),
		(D, 'D'),
		)

	
	user = models.OneToOneField(User,null=False,on_delete=models.CASCADE,blank=True)
	first_name = models.CharField(max_length=255,null=True,blank=True)
	last_name = models.CharField(max_length=255,null=True,blank=True)
	email = models.EmailField(null=True,blank=True)
	gender = models.CharField(max_length=255,choices=GENDER,default=MALE,blank=True)
	ever_married =  models.CharField(max_length=255,choices=MARITAL_STATUS,default=NEVER_MARRIED,blank=True)
	birth_day = models.DateField(null=True,blank=True)
	graduated = models.BooleanField(null=True,blank=True,default=False)
	profession = models.CharField(max_length=255,null=True,blank=True)
	work_experience = models.PositiveSmallIntegerField(default=0,null=True,blank=True)
	spending_score = models.PositiveIntegerField(null=True,blank=True)
	family_size = models.PositiveSmallIntegerField(default=0)
	anonymised_category = models.CharField(max_length=255,choices=CATEGORY,null=True,blank=True)
	segmentation = models.CharField(max_length=255,choices=CATEGORY,null=True,blank=True)

	def __str__(self):
		return f'Full name: {self.first_name} {self.last_name}| Cat: {self.segmentation}'


class Cars(models.Model):

	A = 'A'
	B = 'B'
	C = 'C'
	D = 'D'

	CATEGORY = (
		(A, 'A'),
		(B, 'B'),
		(C, 'C'),
		(D, 'D'),
		)

	brand = models.CharField(max_length=255,null=True,blank=True)
	model = models.CharField(max_length=255,null=True,blank=True)
	color = models.CharField(max_length=255,null=True,blank=True)
	image = models.ImageField(upload_to=f'upload/cars/',null=True,blank=True)
	category = models.CharField(max_length=255,choices=CATEGORY,null=True,blank=True)

	class Meta:
		verbose_name = 'Car'
		verbose_name_plural = 'Cars'

	def __str__(self):
		return f'{self.brand} {self.model}'

	