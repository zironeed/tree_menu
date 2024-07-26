from django.db import models

class Menu(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name='menu name')

    class Meta:
        verbose_name = 'Menu'
        verbose_name_plural = 'Menus'

    def __str__(self):
        return self.name


class MenuItem(models.Model):
    menu = models.ForeignKey(Menu, related_name='items', on_delete=models.CASCADE, verbose_name='menu')
    parent = models.ForeignKey('self', null=True, blank=True, related_name='children',
                               on_delete=models.CASCADE, verbose_name='parent item')

    title = models.CharField(max_length=100, verbose_name='item title')

    class Meta:
        verbose_name = 'Item'
        verbose_name_plural = 'Items'

    def __str__(self):
        return self.title
