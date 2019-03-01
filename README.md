# django-validation-cw

Create a ModelForm for a new Car. Allow a user to sumbit the car's make, model, year, and mpg (miles per gallon). Make one page that has all of the Car database entries at the top and the form to enter a new car below that. Once the validated data has been entered into the database, send them to a different page that says "CONGRATS!!!" with a link below that going back to the first (home) page. Use validation to exclude all cars with:
- Miles per gallon less than 20. Say"That's less than a truck!!!"
- Miles per gallon that's greater than 500. Say "That's impossible (in 2019)
- Any year that's less than 2019. Say "That's not new!!!"
<hr>
1.5 points. The MPG validation doesn't work. You forgot to change the function name to be clean_mpg instead of clean_gallon.