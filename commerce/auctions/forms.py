from django import forms

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
    
    category = forms.CharField(widget=forms.TextInput(attrs= {
            "name": "category"
            }), 
            required=False)
    