from django.contrib import admin
from .models import Person
from .models import Morbidity
from .models import LabVitals
from .models import Food
from .models import FoodEntry
from .models import Serving
from .models import JournalEntry
from .models import ExerciseEntry

# Register your models here.
admin.site.register(Person)
admin.site.register(Morbidity)
admin.site.register(LabVitals)
admin.site.register(Food)
admin.site.register(FoodEntry)
admin.site.register(Serving)
admin.site.register(JournalEntry)
admin.site.register(ExerciseEntry)