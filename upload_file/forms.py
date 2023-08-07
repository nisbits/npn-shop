from django import forms
from .models import uploaded_image
class imageform ( forms.ModelForm ) :
    class Meta :
        model = uploaded_image
        fields = ("image_name","image",)

class imageform_update( forms.ModelForm ) :
    class Meta :
        model = uploaded_image
        fields = ("image_name","image",)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
       # self.fields['image_name'].label="car_name"
        self.fields['image_name'].widget.attrs.update({'class': 'nm_inp',"id":"ima,'placeholder':'nananan'"})