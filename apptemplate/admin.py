from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Recipe, Review, Profile


@admin.register(Recipe)
class RecipeAdmin(SummernoteModelAdmin):
    prepopulated_fields = {
        'slug': ('title',)
    }
    list_filter = ('status', 'created_on')
    list_display = ('title', 'slug', 'status', 'created_on')
    search_fields = ('title', 'content')
    summernote_fields = ('content')


@admin.register(Review)
class ReviewAdmin(SummernoteModelAdmin):
    list_filter = ('approved', 'created_on')
    list_display = ('name', 'body', 'recipe', 'created_on', 'approved')
    search_fields = ('name', 'email', 'body')
    summernote_fields = ('body')
    actions = ['approve_reviews']

    def approve_reviews(self, request, queryset):
        queryset.update(approved=True)


@admin.register(Profile)
class ProfileAdmin(SummernoteModelAdmin):
    list_filter = ('name', 'username', 'fav_food', 'experience')
    list_display = ('name', 'username', 'experience', 'fav_food')
    search_fields = ('name', 'username', 'fav_food', 'experience', 'about')
    summernote_fields = ('about')
