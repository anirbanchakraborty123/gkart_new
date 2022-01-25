
from .models import Category


def all_category(request):
    cate= Category.objects.all()
    return dict(category=cate)
