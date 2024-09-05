from django.contrib import admin
from django.utils import timezone
from . import models


def publish(modeladmin, request, queryset):
    """
    Sets all selected objects in queryset to published
    """
    for object in queryset:
        object.admin_published = True
        # Set first published datetime, if applicable
        try:
            if object.meta_firstpublished_datetime is None:
                object.meta_firstpublished_datetime = timezone.now()
        except Exception:
            pass
        object.save()


publish.short_description = "Publish selected photographs (will appear on main site)"


def unpublish(modeladmin, request, queryset):
    """
    Sets all selected objects in queryset to not published
    """
    for object in queryset:
        object.admin_published = False
        object.save()


unpublish.short_description = "Unpublish selected photographs (will not appear on main site)"


class PhotographUserContributionStackedInline(admin.StackedInline):
    """
    A subform/inline form for EntityHistory, to be used in the EntityAdminView
    """
    model = models.PhotographUserContribution
    extra = 0
    fk_name = 'photograph'
    readonly_fields = ('meta_created_datetime', 'meta_lastupdated_datetime')


@admin.register(models.PhotographGroup)
class PhotographGroupAdminView(admin.ModelAdmin):
    """
    Customise the admin interface for PhotographGroup model
    """

    list_display = ('id', 'name', 'notes')


@admin.register(models.Photograph)
class PhotographAdminView(admin.ModelAdmin):
    """
    Customise the admin interface for Photograph model
    """

    list_display = ('id',
                    'image',
                    'image_name_es',
                    'group',
                    'order',
                    'published',
                    'meta_created_by',
                    'meta_created_datetime',
                    'meta_lastupdated_by',
                    'meta_lastupdated_datetime')
    list_select_related = ('meta_created_by',
                           'meta_lastupdated_by',)
    list_filter = ('published',)
    search_fields = ('image',
                     'image_name_es',
                     'image_name_en',
                     'description_es',
                     'description_en',
                     'notes')
    readonly_fields = ('meta_created_by',
                       'meta_created_datetime',
                       'meta_lastupdated_by',
                       'meta_lastupdated_datetime')
    actions = (publish, unpublish)
    inlines = (PhotographUserContributionStackedInline,)
    list_per_page = 50

    def save_model(self, request, obj, form, change):
        # Meta: created (if not yet set) or last updated by (if created already set)
        if obj.meta_created_by is None:
            obj.meta_created_by = request.user
            # meta_created_datetime default value set in model so not needed here
        else:
            obj.meta_lastupdated_by = request.user
            obj.meta_lastupdated_datetime = timezone.now()

        obj.save()


@admin.register(models.PhotographUserContribution)
class PhotographUserContributionAdminView(admin.ModelAdmin):
    """
    Customise the admin interface for PhotographUserContribution model
    """

    list_display = ('id',
                    'photograph',
                    'contribution',
                    'name',
                    'email',
                    'agree_to_ethics')
    list_select_related = ('photograph',)
    list_filter = ('photograph',)
    autocomplete_fields = ('photograph',)
    search_fields = ('contribution',
                     'name',
                     'email',
                     'notes')
    readonly_fields = ('meta_created_datetime',
                       'meta_lastupdated_datetime')
    list_per_page = 100
