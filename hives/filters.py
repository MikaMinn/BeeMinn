import django_filters
from django_filters import DateFilter, CharFilter, NumberFilter, ChoiceFilter, ModelChoiceFilter, filters
from .models import Hives, Zones
from django.forms import ModelForm, TextInput, Textarea, DateInput, Select, NumberInput, SelectDateWidget, PasswordInput, EmailInput


class HivesFilter(django_filters.FilterSet):
    
    name = CharFilter(widget=TextInput(attrs={'class': 'form-control mb-2','placeholder': 'Ruche 000 '}), lookup_expr='icontains')
    year = NumberFilter(widget=NumberInput(attrs={'class': 'form-control mb-2','placeholder': '2018'}))
    origin = CharFilter(widget=TextInput(attrs={'class': 'form-control mb-2','placeholder': 'Essaimage'}))
    zone = ModelChoiceFilter(queryset=Zones.objects.all(),widget=Select(attrs={'class': 'form-control mb-2'}))
    hive_type = ModelChoiceFilter(queryset=Hives.objects.values_list('hive_type',flat=True).distinct(),widget=Select(attrs={'class': 'form-control'}))

    class Meta:
        model = Hives
        fields = '__all__'
        exclude = ["user","description","created_at","frame_number"]
