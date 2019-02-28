from django import forms
from .models import CarModel


class CarForm(forms.ModelForm):
    class Meta:
        model = CarModel
        fields = '__all__'

    def clean_gallon(self):
        gallonData = self.cleaned_data['mpg']

        if gallonData < 20:
            raise forms.ValidationError("That's less than a truck!!!")

        if gallonData > 500:
            raise forms.ValidationError("That's impossible (in 2019)")

        return gallonData

    def clean_year(self):
        yearData = self.cleaned_data['year']

        if yearData < 2019:
            raise forms.ValidationError("Thats Impossible")
        return yearData
