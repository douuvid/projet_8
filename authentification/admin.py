from django.contrib import admin
from .models import Book, ReviewRequest, Review

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'author']

@admin.register(ReviewRequest)
class ReviewRequestAdmin(admin.ModelAdmin):
    list_display = ['user', 'book', 'date_requested']

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['user', 'book', 'content', 'date_posted']
