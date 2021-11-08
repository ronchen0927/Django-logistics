from django.db import models


class Store(models.Model):
    name = models.CharField('店家', max_length=30, blank=True, default='')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'tb_store'


class Driver(models.Model):
    name = models.CharField('司機', max_length=30, blank=True, default='')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'tb_driver'


class Order(models.Model):
    is_completed = models.BooleanField(default=False)
    store = models.ForeignKey(Store, on_delete=models.CASCADE, null=True)
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE, null=True)
    food = models.CharField('食物', max_length=30, blank=True, default='')
    drink = models.CharField('飲料', max_length=30, blank=True, default='')
    created_dt = models.DateTimeField(auto_now_add=True)
    is_store_completed = models.BooleanField(default=False)
    is_driver_completed = models.BooleanField(default=False)

    def __str__(self):
        return f"食物:{self.food} 飲料:{self.drink}"

    class Meta:
        db_table = 'tb_order'


def _get_all_order():
    return Order.objects.all()
