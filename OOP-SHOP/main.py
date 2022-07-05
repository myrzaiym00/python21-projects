from shop.models import Product, Category
from abstract.serializers import BaseSerializer

cat = Category("phones")

obj1 = Product("iphone", 234, "...", 3, cat)
obj2 = Product("lenovo", 34, "...", 5, cat)
obj3 = Product("samsung", 87, "...", 10, cat)

res = BaseSerializer().serialize_queryset([obj1, obj2, obj3])
from pprint import pprint
pprint(res)