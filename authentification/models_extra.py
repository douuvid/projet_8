from .models import User


from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    summary = models.TextField()
    publication_date = models.DateField()
    image = models.ImageField(upload_to='books/', blank=True, null=True)

    def __str__(self):
        return self.title

class Review(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviews')
    content = models.TextField()
    rating = models.PositiveSmallIntegerField()
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review for {self.book.title} by {self.user.email}"

class ReviewRequest(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='review_requests')
    user = models.ForeignKey(User, on_delete=models.CASCADE,related_name='review_requests')
    message = models.TextField()
    date_requested = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review request for {self.book.title} by {self.user.email}"
