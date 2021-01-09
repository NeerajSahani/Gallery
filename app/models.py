import io
import os
import uuid
from PIL import Image
from django.db import models
from django.core.files import File
from django.utils.text import slugify


class Tags(models.Model):
    class Meta:
        verbose_name_plural = 'Tags'

    tag = models.CharField(max_length=50, unique=True)
    created = models.DateTimeField(auto_now_add=True)

    @property
    def popularity(self):
        return self.images_set.count()

    def __str__(self) -> str:
        return self.tag


class Images(models.Model):
    class Meta:
        verbose_name_plural = 'Images'

    title = models.CharField(max_length=50, default='image')
    slug = models.SlugField(editable=False, unique=True)
    image = models.ImageField(upload_to='gallery')
    tag = models.ManyToManyField(Tags, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs) -> None:
        if not self.id:
            self.slug = slugify(f"{self.title}-{uuid.uuid4().hex}")
        return super().save(*args, **kwargs)

    def rotate_image(self, angle):
        # Renaming is not required but browser wasn't changing images after rotation, even never_cache decorator is used
        old_img_path = self.image.path
        original_image = io.BytesIO(self.image.read())
        rotated_image = io.BytesIO()
        image = Image.open(original_image)
        image = image.rotate(angle, expand=True)
        image.save(rotated_image, 'JPEG')
        rotated_image.seek(0)
        path = f'{self.slug}-{uuid.uuid4().hex}.jpg'
        self.image = File(rotated_image, path)
        self.save()
        original_image.close()
        rotated_image.close()
        os.remove(old_img_path)
