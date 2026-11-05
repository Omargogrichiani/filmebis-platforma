from django.db import models


class Director(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    birth_date = models.DateField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Actor(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    birth_date = models.DateField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Genre(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    is_popular = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=200)
    release_date = models.DateField()
    duration = models.PositiveIntegerField()

    director = models.ForeignKey(
        Director,
        on_delete=models.CASCADE,
        related_name="movies"
    )

    actors = models.ManyToManyField(
        Actor,
        related_name="movies"
    )

    genres = models.ManyToManyField(
        Genre,
        related_name="movies"
    )

    def __str__(self):
        return self.title


class Rating(models.Model):
    movie = models.OneToOneField(
        Movie,
        on_delete=models.CASCADE,
        related_name="rating"
    )
    score = models.FloatField()
    review = models.TextField()

    def __str__(self):
        return f"{self.movie.title} - {self.score}/10"


class Review(models.Model):
    movie = models.ForeignKey(
        Movie,
        on_delete=models.CASCADE,
        related_name="reviews"
    )
    reviewer_name = models.CharField(max_length=100)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.reviewer_name} - {self.movie.title}"
