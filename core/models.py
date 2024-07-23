from django.db import models
from stdimage.models import StdImageField
import uuid

def gen_file_path(_instance, filename):
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'
    return filename


class Base(models.Model):
    created_at = models.DateTimeField('Ceated at', auto_now_add=True)
    updated_at = models.DateTimeField('Updated at', auto_now=True)
    is_active = models.BooleanField('Active ', default=True)

    class Meta:
        abstract = True

        
class Services(Base):
    ICONE_CHOICES = (
        ('lni-cog', 'Gear'),
        ('lni-stats-up', 'Graphical'),
        ('lni-users', 'Users'),
        ('lni-layers', 'Design'),
        ('lni-mobile', 'Mobile'),
        ('lni-rocket', 'Rocket'),
    )
    
    service = models.CharField('Service', max_length=100)
    description = models.CharField('Description', max_length=255)
    icon = models.CharField('Icon', max_length=12, choices=ICONE_CHOICES)
    
    class Meta:
        verbose_name = 'Service'
        verbose_name_plural = 'Services'

    def __str__(self):
        return self.service


class Position(Base):
    title = models.CharField('Title', max_length=100)
    
    class Meta:
        verbose_name = 'Position'
        verbose_name_plural = 'Positions'
    
    def __str__(self):
        return self.title


class Team(Base):
    name = models.CharField('Name', max_length=100)
    position = models.ForeignKey('core.Position', verbose_name='Position',
                                on_delete=models.CASCADE)
    bio = models.TextField('Bio', max_length=255)
    image = StdImageField('Image', upload_to=gen_file_path, variations={
        'thumb': {'width': 450, 'height': 450, 'crop': True}})
    facebook = models.CharField('Facebook', max_length=255)
    instagram = models.CharField('Instagram', max_length=255)
    twitter = models.CharField('Twitter', max_length=255)

    class Meta:
        verbose_name = 'Team Member'
        verbose_name_plural = 'Team Members'

    def __str__(self):
        return self.name


class Features(Base):
    ICONE_CHOICES = (
        ('lni-cog', 'Gear'),
        ('lni-leaf', 'Leaf'),
        ('lni-layers', 'Design'),
        ('lni-laptop-phone', 'Laptop'),
        ('lni-rocket', 'Rocket'),
    )
    title = models.CharField('Title', max_length=100)
    description = models.CharField('Description', max_length=255)
    icon = models.CharField('Icon', max_length=16, choices=ICONE_CHOICES)

    class Meta:
        verbose_name = 'Feature'
        verbose_name_plural = 'Features'

    def __str__(self):
        return self.title
