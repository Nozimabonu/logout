from django import forms
from .models import Customer, Product, User


class CustomerModelForm(forms.ModelForm):
    class Meta:
        model = Customer
        exclude = ()


class ProductListModelForm(forms.ModelForm):
    class Meta:
        model = Product
        exclude = ()


class LoginForm(forms.Form):
    phone_number = forms.CharField(max_length=13, min_length=13)
    password = forms.CharField(max_length=255)

    def clean_phone_number(self):
        phone_number = self.data.get('phone_number')
        if not User.objects.filter(phone_number=phone_number).exists():
            raise forms.ValidationError('Bunday raqam topilmadi')
        return phone_number

    def clean_password(self):
        phone_number = self.cleaned_data.get('phone_number')
        password = self.data.get('password')
        try:
            user = User.objects.get(phone_number=phone_number)
            if not user.check_password(password):
                raise forms.ValidationError('Parol xato')
        except User.DoesNotExist:
            raise forms.ValidationError(f'Bunday {phone_number} mavjud emas')
        return password

    # def clean(self):
    #     cleaned_data = super().clean()
    #     phone_number = self.cleaned_data.get('phone_number')
    #     password = self.cleaned_data.get('password')
    #     user = User.objects.filter(phone_number=phone_number,password=password).first()
    #     if not user:
    #         raise forms.ValidationError('User topilmadi')
    #
    #     return cleaned_data


class RegisterForm(forms.Form):
    first_name = forms.CharField(max_length=100, required=False)
    phone_number = forms.CharField(max_length=13)
    password = forms.CharField(max_length=255)
    confirm_password = forms.CharField(max_length=255)

    def clean_phone_number(self):
        phone_number = self.data.get('phone_number')
        if User.objects.filter(phone_number=phone_number).exists():
            raise forms.ValidationError(f'Bunday {phone_number} allaqachon mavjud')
        return phone_number

    def clean_password(self):
        password = self.data.get('password')
        confirm_password = self.data.get('confirm_password')
        if password != confirm_password:
            raise forms.ValidationError('Password did not match')

        return password

    # def clean(self):
    #     cleaned_data = super().clean()
    #     password = self.data.get('password')
    #     confirm_password = self.data.get('confirm_password')
    #     if password != confirm_password:
    #         raise forms.ValidationError('Parollar mos tushmadi')
    #
    #     return cleaned_data
