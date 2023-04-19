from django import forms
from .models import Product


class ProductAdminForm(forms.ModelForm):
    class Meta:
        model = Product
        exclude = ()  # Trong trường hợp này là mình ko muốn biểu thị trường nào
        # exclude=['a', 'b'] # Hiển thị hết các trường ngoại trừ trường a, b
        # fields = '__all__' # Hiển thị hết các trường luôn


# class ProductAddToCartForm(forms.Form):
#     quantity = forms.IntegerField(widget=forms.TextInput(attrs={'size': '2', 'value': '1', 'class': 'quantity p-1 w-25', 'maxlength': '5'}),
#                                   error_messages={'invalid': 'Please enter a valid quantity.'}, min_value=1)
#     product_slug = forms.CharField(widget=forms.HiddenInput())

#     # override the default __init__ so we can set the request
#     def __init__(self, request=None, *args, **kwargs):
#         self.request = request
#         super(ProductAddToCartForm, self).__init__(*args, **kwargs)

#     # custom validation to check for cookies
#     def clean(self):
#         if self.request:
#             if not self.request.session.test_cookie_worked():
#                 raise forms.ValidationError("Cookies must be enabled.")
#         return self.cleaned_data
