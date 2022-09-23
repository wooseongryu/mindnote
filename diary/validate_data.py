import random
from .models import Page


def validate_pages():
    pages = Page.objects.all()
    for page in pages:
        if page.score < 0 or page.score > 10:
            value = random.randint(1, 10)
            page.score = value
            page.save()
