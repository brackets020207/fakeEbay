from django import forms

valid_categories = {"ele":"Electronics", "vhr":"Vehicle Related", "hag":"Home and Garden", "csa":"Clothing, Shoes, and Accessories", 
                    "spt":"Sports", "hab":"Health and Beauty", "tah":"Toys and Hobbies", "bsi":"Business and Industrial", 
                    "bmm":"Books, Music, and Movies", "caa":"Collectibles and Art", "bby":"Baby Essentials", "fd":"Food", "oth":"Other"}

class listing_form(forms.Form):
    title = forms.CharField(widget=forms.TextInput(attrs= {
            "name": "title"
            }))
    
    description = forms.CharField(widget = forms.Textarea(attrs= {
            "name": "description",
            "cols":120,
            "rows":8
        }))
    
    start_price = forms.DecimalField(widget=forms.NumberInput(attrs= {
            "name": "start_price"
            }), 
            decimal_places=2)
    
    img_url = forms.CharField(widget=forms.TextInput(attrs= {
            "name": "img_url"
            }),
            required=False)
    
    category = forms.MultipleChoiceField(choices=valid_categories.items())

class bidding_form(forms.Form):
    bid_price = forms.DecimalField(widget=forms.NumberInput(attrs= {
            "name": "bid_price"
            }), 
            decimal_places=2)
    
class comment_form(forms.Form):
    text = forms.CharField(widget = forms.Textarea(attrs= {
            "name": "comment_text",
            "cols":120,
            "rows":1
        }), label = '')