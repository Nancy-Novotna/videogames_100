from django import forms
import django_filters
from . models import Game, Genre


class GameFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(
        label='',
        lookup_expr='icontains',
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Search by title...'})
    )
    genre = django_filters.ModelChoiceFilter(
        label='',
        queryset=Genre.objects.all(),
        field_name='genre__name',
        lookup_expr='icontains',
        widget=forms.Select(
            attrs={'class': 'form-control', 'placeholder': 'Search by genre...'})
    )
    developer = django_filters.CharFilter(
        label='',
        field_name='developer__name',
        lookup_expr='icontains',
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Search by developer...'})
    )
    publisher = django_filters.CharFilter(
        label='',
        field_name='publisher__name',
        lookup_expr='icontains',
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Search by publisher...'})
    )

    class Meta:
        model = Game
        fields = ['title', 'genre', 'developer', 'publisher']
