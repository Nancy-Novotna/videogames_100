from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# VIDEOGAME
class Game(models.Model):
    id = models.CharField(primary_key=True, max_length=100)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)

    genre = models.ManyToManyField('Genre', related_name='games')

    developer = models.ForeignKey('Developer', on_delete=models.SET_NULL, null=True)
    publisher = models.ForeignKey('Publisher', on_delete=models.SET_NULL, null=True)

    release_date = models.DateField()
    price = models.DecimalField(max_digits=6, decimal_places=2)

    platinum_difficulty = models.IntegerField(
        help_text="Např. škála 1–10"
    )

    created_at = models.DateTimeField(auto_now_add=True)
    
    picture = models.ImageField(default='default.jpg', blank=True)
    
    slug = models.SlugField(default="", null=False)

    def __str__(self):
        return self.title

# GENRE
class Genre(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

# DEVELOPER
class Developer(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

# PUBLISHER
class Publisher(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    
# ACHIEVEMENT SYSTEM
class Achievement(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name='achievements')

    name = models.CharField(max_length=255)
    description = models.TextField()

    is_hidden = models.BooleanField(default=False)
    difficulty = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f"{self.name} ({self.game.title})"

# GUIDES
class Guide(models.Model):
    game = models.OneToOneField(Game, on_delete=models.CASCADE, related_name='guide')

    content = models.TextField()

    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    is_verified = models.BooleanField(default=False)

    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Guide for {self.game.title}"

# COMMENTS
class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    guide = models.ForeignKey(Guide, on_delete=models.CASCADE, related_name='comments')

    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.user.username}"

# PROFILE
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    is_verified = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username

# WISHLIST / COMPLETED GAMES
class UserGame(models.Model):
    STATUS_CHOICES = [
        ('wishlist', 'Wishlist'),
        ('completed', 'Completed'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)

    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    added_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'game')

# TRENDS
class GameView(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    viewed_at = models.DateTimeField(auto_now_add=True)

