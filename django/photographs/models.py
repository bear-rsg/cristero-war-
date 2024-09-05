from django.db import models
from django.urls import reverse
from account.models import User
from django.utils import timezone
from ckeditor_uploader.fields import RichTextUploadingField


class PhotographGroup(models.Model):
    """
    A group of related photographs
    """

    related_name = 'photographgroups'

    name = models.CharField(max_length=255)
    notes = models.TextField(blank=True, null=True, help_text='Notes are for admins only and will not be visible on the public website')

    def __str__(self):
        return self.name


class Photograph(models.Model):
    """
    A photograph and related data
    """

    related_name = 'photographs'

    image = models.ImageField(upload_to='photographs', blank=True, null=True)
    image_name_es = models.CharField(max_length=255, blank=True, null=True, help_text="A brief name/title for the image in Spanish", verbose_name="Name (Spanish)")
    image_name_en = models.CharField(max_length=255, blank=True, null=True, help_text="A brief name/title for the image in English", verbose_name="Name (English)")
    group = models.ForeignKey('PhotographGroup', on_delete=models.PROTECT, blank=True, null=True, related_name=related_name)
    description_es = RichTextUploadingField(blank=True, null=True, verbose_name='Description (Spanish)')
    description_en = RichTextUploadingField(blank=True, null=True, verbose_name='Description (English)')
    acknowledgements = models.TextField(blank=True, null=True)
    order = models.IntegerField(blank=True, null=True, help_text='Photographs are ordered by their group, then by this order field (in ascending order), and then by date created.')
    published = models.BooleanField(default=False, help_text='Check this box to include this photograph on the public website')
    notes = models.TextField(blank=True, null=True, help_text='Notes are for admins only and will not be visible on the public website')

    # Metadata
    meta_created_by = models.ForeignKey(User, related_name=f'{related_name}_created_by', on_delete=models.PROTECT, blank=True, null=True, verbose_name="created by")
    meta_created_datetime = models.DateTimeField(default=timezone.now, verbose_name="created")
    meta_lastupdated_by = models.ForeignKey(User, related_name=f'{related_name}_lastupdated_by', on_delete=models.PROTECT, blank=True, null=True, verbose_name="last updated by")
    meta_lastupdated_datetime = models.DateTimeField(blank=True, null=True, verbose_name="last updated")

    @property
    def admin_url(self):
        return reverse('admin:photographs_photograph_change', args=[self.id])

    def __str__(self):
        return f'#{self.id}'

    def get_absolute_url(self):
        return reverse('photographs:detail', args=[self.id])

    class Meta:
        ordering = ('group', 'order', 'meta_created_datetime')


class PhotographUserContribution(models.Model):
    """
    A user's contribution in response to a photograph
    """

    related_name = 'photographusercontributions'

    photograph = models.ForeignKey(Photograph, related_name=related_name, on_delete=models.PROTECT)
    contribution = models.TextField()
    name = models.CharField(max_length=200, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    agree_to_ethics = models.BooleanField(default=False)
    notes = models.TextField(blank=True, null=True, help_text='Notes are for admins only and will not be visible on the public website')

    # Metadata
    meta_created_datetime = models.DateTimeField(default=timezone.now, verbose_name="created")
    meta_lastupdated_datetime = models.DateTimeField(blank=True, null=True, verbose_name="last updated")

    def __str__(self):
        return f'User contribution for "{self.photograph}" on {str(self.meta_created_datetime)[:19]}'
