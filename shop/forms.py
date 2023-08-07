from email.policy import default
from django import forms
from .models import CatList,CatWiseItems,contactus
from django.contrib.auth.models import User
from shop_accounts.models import profile
class cat_list_form( forms.ModelForm ) :
    class Meta :
        model = CatList
        fields = ("category_name",)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
       # self.fields['image_name'].label="car_name"
        self.fields['category_name'].widget.attrs.update()


class  cat_wise_items_form( forms.ModelForm ):
    class Meta :
        cat = forms.ModelChoiceField(queryset=CatList.objects.all(),initial=1)
        model = CatWiseItems
        fields = ("cat","item_name","short_discription","long_discription","price","image","specs")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
       # self.fields['image_name'].label="car_name" "class":"fm-input"
        self.fields['short_discription'].widget.attrs.update({"cols":10,"rows":6,"class":"fm-input"})
        self.fields['long_discription'].widget.attrs.update({"cols":10,"rows":10,"class":"fm-input"})
        self.fields['specs'].widget.attrs.update({"cols":10,"rows":6,"class":"fm-input"})
        self.fields['cat'].widget.attrs.update({"class":"fm-input"})
        self.fields['item_name'].widget.attrs.update({"class":"fm-input"})
        self.fields['image'].widget.attrs.update({"class":"fm-input"})


class pass_change_form( forms.Form ) :

    password=forms.CharField( label="New Password",
        max_length=70,
        widget=forms.PasswordInput(),
        required=True,)

    confm_pass=forms.CharField( label="Confirm Password",
        max_length=70,
        widget=forms.PasswordInput(),
        required=True,)
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
       # self.fields['image_name'].label="car_name"
        # self.fields['category_name'].widget.attrs.update()




class user_change_form( forms.ModelForm ) :

    class Meta :
        model = User
        fields = ("first_name","last_name")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
       # self.fields['image_name'].label="car_name"
        # self.fields['category_name'].widget.attrs.update()

class profile_change_form( forms.ModelForm ) :

    class Meta :
        model = profile
        fields = ("pro_pic",)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['pro_pic'].label="Profile Image"
        # self.fields['category_name'].widget.attrs.update()

class pass_forget_form( forms.Form ) :

    email=forms.CharField( label="Enter your registered Email",
        max_length=70,
        widget=forms.TextInput(),
        required=True,)


class contactus_form(forms.ModelForm) :

    class Meta :
        model = contactus
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].label="Name*"