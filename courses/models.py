from django.db import models


class Base(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        abstract = True


class Course(Base):
    title = models.CharField(max_length=255)
    url = models.URLField(unique=True)

    class Meta:
        verbose_name = 'Course'
        verbose_name_plural = 'Courses'

    def __str__(self):
        return self.title
    

class Evaluation(Base):
    course = models.ForeignKey(Course, related_name='evaluations', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    comment = models.TextField(blank=True, default='')
    evaluation = models.DecimalField(max_digits=2, decimal_places=1)

    class Meta:
        verbose_name = 'Evaluation'
        verbose_name_plural = 'Evaluations'
        unique_together = ['email', 'course']

    def __str__(self):
        return f'{self.name} avaliou o curso {self.course} com a nota {self.evaluation}'
