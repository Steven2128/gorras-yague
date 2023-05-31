# Django
from django.core.validators import MinValueValidator
from django.db import models


class Category(models.Model):
    """Model Category"""
    description = models.CharField(max_length=100, unique=True, verbose_name='Descripción')

    def __str__(self):
        return self.description

    class Meta:
        verbose_name_plural = 'Categorias'


class Brand(models.Model):
    """Model Brand"""
    description = models.CharField(max_length=100, verbose_name='Descripción')

    def __str__(self):
        return self.description

    class Meta:
        verbose_name_plural = 'Marcas'


class Product(models.Model):
    """Model Product"""
    description = models.CharField(max_length=200, verbose_name='Descripción')
    price = models.FloatField(default=0, verbose_name='Precio')
    size = models.FloatField(max_length=10, verbose_name='Talla')
    color = models.CharField(max_length=45, verbose_name='Color')
    stock = models.IntegerField(default=0, verbose_name='Existencia', validators=[MinValueValidator(1)])
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, verbose_name='Marca')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Categoría')
    image = models.ImageField(upload_to='products_pics', verbose_name='Imagén del producto', blank=True, null=True)

    def __str__(self):
        return self.description

    def save(self):
        self.description = self.description.upper()
        super(Product, self).save()

    class Meta:
        verbose_name_plural = 'Productos'


class PQR(models.Model):
    """Model PQR"""
    REQUEST_TYPE_CHOICES = [
        ('', 'Seleccione el tipo de solicitud'),
        ('P', 'Pregunta'),
        ('Q', 'Queja'),
        ('R', 'Reclamo')
    ]
    request_type = models.CharField(max_length=1, choices=REQUEST_TYPE_CHOICES, blank=False, null=False, verbose_name='Tipo de solicitud')
    description = models.TextField(blank=False, null=False, verbose_name='Detalle de la solicitud')

    def __str__(self):
        return self.get_request_type_display()

    class Meta:
        verbose_name = 'Pregunta, Queja y Reclamo'
        verbose_name_plural = 'Preguntas, Quejas y Reclamos'


class OrderHeader(models.Model):
    """Model Order Header"""
    fecha = models.DateField(auto_now_add=True)
    sub_total = models.FloatField(default=0)
    discount = models.FloatField(default=0)
    total = models.FloatField(default=0)

    def __str__(self):
        return '{}, {}'.format(self.id, self.fecha)

    def save(self):
        self.total = self.sub_total - self.descuento
        super(OrderHeader, self).save()

    class Meta:
        verbose_name_plural = 'Encabezado Pedido'
        verbose_name = 'Encabezado Pedido'


class OrderDet(models.Model):
    """model Order Detail"""
    order = models.ForeignKey(OrderHeader, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    amount = models.BigIntegerField(default=0)
    price = models.FloatField(default=0)
    sub_total = models.FloatField(default=0)
    discount = models.FloatField(default=0)
    total = models.FloatField(default=0)

    def __str__(self):
        return '{}, {}'.format(self.product, self.order)

    def save(self):
        self.sub_total = float(float(int(self.amount)) * float(self.price))
        self.total = self.sub_total - float(self.discount)
        super(OrderDet, self).save()

    class Meta:
        verbose_name_plural = 'Detalles Pedido'
        verbose_name = 'Detalle Pedido'