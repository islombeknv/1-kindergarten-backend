from django.core.exceptions import ValidationError
from django.core.files.images import get_image_dimensions


def clean_picture(image):
    w, h = get_image_dimensions(image)
    if w != 700:
        raise ValidationError("Bu rasmni bo\'yi %i piksel. Rasmni bo\'yi 100px bo'lishi kerak" % w)
    if h != 400:
        raise ValidationError("The image is %i pixel high. It's supposed to be 200px" % h)


def news_picture(image):
    w, h = get_image_dimensions(image)
    if w != 400:
        raise ValidationError("Bu rasmni bo\'yi %i piksel. Rasmni bo\'yi 100px bo'lishi kerak" % w)
    if h != 250:
        raise ValidationError("The image is %i pixel high. It's supposed to be 200px" % h)


def staff_picture(image):
    w, h = get_image_dimensions(image)
    if w != 400:
        raise ValidationError("Bu rasmni bo\'yi %i piksel. Rasmni bo\'yi 100px bo'lishi kerak" % w)
    if h != 300:
        raise ValidationError("The image is %i pixel high. It's supposed to be 200px" % h)
