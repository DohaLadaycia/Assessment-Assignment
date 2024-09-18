from django import forms
#This is the list of countries and categories in  the web site 
class NewsFilterForm(forms.Form):
    CATEGORY_LISTES = [
        ('','All'),
        ('general', 'General'),
        ('business', 'Business'),
        ('entertainment', 'Entertainment'),
        ('health', 'Health'),
        ('science', 'Science'),
        ('sports', 'Sports'),
        ('technology', 'Technology'),
    ]
    
    COUNTRY_LISTES = [
        ('','All'),
        ('eg', 'Egypt'),
        ('us', 'United States'),
    ]

    category = forms.ChoiceField(choices=CATEGORY_LISTES, required=False)
    country = forms.ChoiceField(choices=COUNTRY_LISTES, required=False)
