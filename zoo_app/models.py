from random import randint
from django.db.models import *
from django.urls import reverse
from django.utils import timezone

# Create your models here.

AVIARY_CLASS = [
    ('Wa', 'Water'),  # Бассеин-вольер
    ('Gr', 'Ground'),  # Обычный вольер
    ('Fl', 'Flying'),  # Закрытый вольер для летающих
]

ANIMALIA_DANGER = [
    ('Hu', 'Hunter'),  # Хищник
    ('He', 'Herbivores'),  # Травоядные
    ('Om', 'Omnivores'),  # Всеядные
]


class Aviary(Model):  # Класс вольера
    name = CharField(max_length=30)
    description = TextField()
    type = CharField(
        max_length=2,
        choices=AVIARY_CLASS,
        default='Gr',
    )
    img = ImageField(
        upload_to="AVIARY",
        blank=True
    )
    slug = SlugField(
        allow_unicode=True
    )

    def createSlug(self):
        slug = self.name + str(randint(100, 999))
        self.slug = slug
        self.save()

    def __str__(self):
        return self.name

    def get_delete_url(self):
        return reverse("deleteaviary", kwargs={
            'slug': self.slug
        })


class Animalia(Model):  # Класс животных - типо ежи, медведи, студенты
    name = CharField(max_length=30)
    description = TextField()
    area = ForeignKey(
        Aviary,
        on_delete=CASCADE
    )
    type = CharField(
        max_length=2,
        choices=ANIMALIA_DANGER,
        default='Om'
    )
    img = ImageField(
        upload_to="ANIMALIA",
        blank=True
    )
    slug = SlugField(
        allow_unicode=True
    )

    def createSlug(self):
        slug = self.name + str(randint(100, 999))
        self.slug = slug
        self.save()

    def __str__(self):
        return self.name

    def get_delete_url(self):
        return reverse("deleteanimalia", kwargs={
            'slug': self.slug
        })


class Animal(Model):  # класс конкреного животного например студент-богослов
    AnimaliaType = ForeignKey(
        Animalia,
        on_delete=CASCADE
    )
    name = CharField(max_length=30)
    description = TextField()
    img = ImageField(
        upload_to="ANIMAL",
        blank=True
    )
    slug = SlugField(
        allow_unicode=True
    )

    def createSlug(self):
        slug = self.name + str(randint(100, 999))
        self.slug = slug
        self.save()

    def __str__(self):
        return self.name

    def get_delete_url(self):
        return reverse("deleteanimal", kwargs={
            'slug': self.slug
        })
