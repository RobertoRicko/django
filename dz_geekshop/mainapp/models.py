from django.db import models


class ProductCategory(models.Model):
    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
    name = models.CharField(verbose_name='имя категории', max_length=256, unique=True)
    description = models.TextField(verbose_name='описание категории', max_length=1000, blank=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
    category = models.ForeignKey(ProductCategory, verbose_name='категория', on_delete=models.CASCADE)
    name = models.CharField(verbose_name='имя продукта', max_length=64)
    short_desc = models.CharField(verbose_name='краткое описание продукта', max_length=60, blank=True)
    description = models.TextField(verbose_name="подробное описание продукта", blank=True)
    price = models.DecimalField(verbose_name='цена', max_digits=8, decimal_places=2, default=0)
    image = models.ImageField(verbose_name='изображение', upload_to='product_images')
    quantity = models.PositiveSmallIntegerField(verbose_name='склад', default=0)

    def __str__(self):
        return "{} ({})".format(self.name, self.category.name)



