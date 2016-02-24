from django import forms

class DisciplineForm(forms.Form):
    DISCIPLINES =(
        ('D&C', 'Drilling and Completions'),
        ('HSE', 'Health, Safety, Security, Environment & Social Responsibility'),
        ('M&I', 'Management & Information'),
        ('P&O', 'Production & Operations'),
        ('PFC', 'Projects, Facilities & Construciton'),
        ('RDD', 'Reservoir Description & Dynamics'),
        ('UND', 'Undeclared'),
    )
    discipline = forms.CharField(max_length=4)
