import factory
from product.models import Category, Product


class CategoryFactory(factory.django.DjangoModelFactory):
    title = factory.Faker("word")
    slug = factory.Sequence(lambda n: f"category-{n}")
    description = factory.Faker("sentence")
    active = True

    class Meta:
        model = Category


class ProductFactory(factory.django.DjangoModelFactory):
    name = factory.Faker("word")
    price = factory.Faker("pyint", min_value=1, max_value=1000)
    category = factory.SubFactory(CategoryFactory)

    class Meta:
        model = Product
