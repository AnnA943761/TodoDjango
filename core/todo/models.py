from django.db import models

class Todo(models.Model):
	title = models.CharField('Task', max_length=40)
	complete = models.BooleanField('Done', default=False)
	
	def __str__(self):
		return self.title
	
