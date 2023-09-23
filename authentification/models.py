from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)

class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email


# class Book(models.Model):
#     title = models.CharField(max_length=255)
#     author = models.CharField(max_length=255)
#     summary = models.TextField()
#     publication_date = models.DateField()
#     image = models.ImageField(upload_to='books/', blank=True, null=True)

#     def __str__(self):
#         return self.title

# class Review(models.Model):
#     book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='reviews')
#     user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviews')
#     content = models.TextField()
#     rating = models.PositiveSmallIntegerField()
#     date_posted = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return f"Review for {self.book.title} by {self.user.email}"

# class ReviewRequest(models.Model):
#     book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='review_requests')
#     user = models.ForeignKey(User, on_delete=models.CASCADE,related_name='review_requests')
#     message = models.TextField()
#     date_requested = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return f"Review request for {self.book.title} by {self.user.email}"
