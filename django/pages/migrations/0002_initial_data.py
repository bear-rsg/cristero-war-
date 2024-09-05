from django.db import migrations
from pages import models


def create_pages(apps, schema_editor):
    """
    Create Page objects with HTML content
    """

    # Welcome
    content = """

<h3>Welcome</h3>
<p>
    Here's some content
</p>

""".strip()
    models.Page.objects.create(
        name='Welcome',
        content_es=content,
        content_en=content,
        published=True
    )

    # About
    content = """

<h2>About</h2>
<p>
    Here's some content
</p>

""".strip()
    models.Page.objects.create(
        name='About',
        content_es=content,
        content_en=content,
        published=True
    )

    # Resources
    content = """

<h2>Resources</h2>
<p>
    Here's some content
</p>

""".strip()
    models.Page.objects.create(
        name='Resources',
        content_es=content,
        content_en=content,
        published=True
    )

    # Get Involved
    content = """

<h2>Get Involved</h2>
<p>
    Here's some content
</p>

""".strip()
    models.Page.objects.create(
        name='Get Involved',
        content_es=content,
        content_en=content,
        published=True
    )


def create_fileuploads(apps, schema_editor):
    """
    Create new FileUpload objects with media files
    """

    # file_obj = models.FileUpload.objects.create(file=File(file_binary, name=file_name))



class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial')
    ]

    operations = [
        migrations.RunPython(create_pages),
        migrations.RunPython(create_fileuploads),
    ]
