from typing import List, Tuple
from django.db import models

class Category(models.Model):
    CATEGORY_CHOICES: List[Tuple[str, str]] = [
        ('category1', 'Category1'),
        ('category2', 'Category2'),
        ('category3', 'Category3'),
        ('pepper', 'Pepper'),
        ('dwarf_tomatoes', 'Dwarf tomatoes'),
        ('basilica', 'Basilica'),
    ]

    def __str__(self):
        return self.name
