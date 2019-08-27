from django.db import models
from authapp.models import ShopUser
from mainapp.models import Product


class BasketSlot(models.Model):
    class Meta:
        verbose_name = 'Слот корзины'
        verbose_name_plural = 'Слоты корзины'
    user = models.ForeignKey(ShopUser, verbose_name='пользователь', on_delete=models.CASCADE, related_name='basket')
    product = models.ForeignKey(Product, verbose_name='продукт', on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField(verbose_name='количество', default=1)
    created = models.DateTimeField(verbose_name='дата и время создания', auto_now_add=True)

    def __str__(self):
        return '{} - {}'.format(self.user.username, self.product.name)
