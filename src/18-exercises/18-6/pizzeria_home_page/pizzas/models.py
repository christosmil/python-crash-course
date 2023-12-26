from django.db import models


class Pizza(models.Model):
    """A pizza that the pizzeria serves."""
    name = models.CharField(max_length=100)

    def __str__(self):
        """Return a string representation of the model."""
        return self.name


class Topping(models.Model):
    """A topping for a pizza."""
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        """Return a string representation of the model."""
        return self.name