from django.utils.text import slugify

def slug_generator(model_instance, major, slug_field):
    slug = slugify(major)
    return slug