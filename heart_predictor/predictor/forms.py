from django import forms

class HeartDiseaseForm(forms.Form):
    age = forms.IntegerField(label='Age')
    sex = forms.ChoiceField(choices=[('Female', 'Female'), ('Male', 'Male')], label='Sex')
    chest_pain_type = forms.ChoiceField(choices=[
        ('Typical angina', 'Typical angina'),
        ('Atypical angina', 'Atypical angina'),
        ('Non-anginal pain', 'Non-anginal pain'),
        ('Asymptomatic', 'Asymptomatic')
    ], label='Chest Pain Type')
    resting_blood_pressure = forms.IntegerField(label='Resting Blood Pressure')
    cholestoral = forms.IntegerField(label='Cholestoral')
    fasting_blood_sugar = forms.ChoiceField(choices=[
        ('Lower than 120 mg/ml', 'No'), 
        ('Greater than 120 mg/ml', 'Yes')
    ], label='Fasting Blood Sugar > 120 mg/dl')
    rest_ecg = forms.ChoiceField(choices=[
        ('Normal', 'Normal'),
        ('ST-T wave abnormality', 'ST-T wave abnormality'),
        ('Left ventricular hypertrophy', 'Left ventricular hypertrophy')
    ], label='Resting ECG')
    Max_heart_rate = forms.IntegerField(label='Maximum Heart Rate Achieved')
    exercise_induced_angina = forms.ChoiceField(choices=[('No', 'No'), ('Yes', 'Yes')], label='Exercise Induced Angina')
    oldpeak = forms.FloatField(label='Oldpeak')
    slope = forms.ChoiceField(choices=[
        ('Upsloping', 'Upsloping'),
        ('Flat', 'Flat'),
        ('Downsloping', 'Downsloping')
    ], label='Slope of ST segment')
    vessels_colored_by_flourosopy = forms.ChoiceField(choices=[
        ('Zero', '0'), ('One', '1'), ('Two', '2'), ('Three', '3'), ('Four', '4')
    ], label='Number of vessels colored by flourosopy')
    thalassemia = forms.ChoiceField(choices=[
        ('Normal', 'Normal'),
        ('Fixed Defect', 'Fixed Defect'),
        ('Reversable Defect', 'Reversable Defect'),
        ('No', 'No')
    ], label='Thalassemia')