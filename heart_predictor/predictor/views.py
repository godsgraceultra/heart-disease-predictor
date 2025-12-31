from django.shortcuts import render
from .forms import HeartDiseaseForm
import pandas as pd
import pickle
import os
from django.conf import settings

# Paths
ML_DIR = os.path.join(settings.BASE_DIR, 'predictor', 'ml')
rf_model = pickle.load(open(os.path.join(ML_DIR, 'rf_heart_disease_model.pkl'), 'rb'))
xgb_model = pickle.load(open(os.path.join(ML_DIR, 'xgb_heart_disease_model.pkl'), 'rb'))
scaler = pickle.load(open(os.path.join(ML_DIR, 'scaler.pkl'), 'rb'))

# Exact order from Notebook
NUMERIC_COLS = ['age', 'resting_blood_pressure', 'cholestoral', 'Max_heart_rate', 'oldpeak']
MULTI_CLASS_COLS = ['chest_pain_type', 'rest_ecg', 'slope', 'vessels_colored_by_flourosopy', 'thalassemia']

def home(request):
    form = HeartDiseaseForm()
    context = {'form': form}

    if request.method == 'POST':
        form = HeartDiseaseForm(request.POST)
        if form.is_valid():
            df = pd.DataFrame([form.cleaned_data])

            # 1. Binary Encoding (Mirroring .cat.codes)
            df['sex'] = df['sex'].map({'Female': 0, 'Male': 1})
            df['fasting_blood_sugar'] = df['fasting_blood_sugar'].map({'Greater than 120 mg/ml': 0, 'Lower than 120 mg/ml': 1})
            df['exercise_induced_angina'] = df['exercise_induced_angina'].map({'No': 0, 'Yes': 1})

            # 2. Scale Numerics
            df[NUMERIC_COLS] = scaler.transform(df[NUMERIC_COLS])

            # 3. One-Hot Encode (drop_first=True)
            df = pd.get_dummies(df, columns=MULTI_CLASS_COLS, drop_first=True)

            # 4. Align with Training Features
            # Note: 0 = High Risk in your model, 1 = Low Risk
            features = rf_model.feature_names_in_
            df_final = df.reindex(columns=features, fill_value=0)

            # 5. Predict
            rf_raw = int(rf_model.predict(df_final)[0])
            xgb_raw = int(xgb_model.predict(df_final)[0])

            # 6. Get Probabilities
            rf_probs = rf_model.predict_proba(df_final)[0]
            xgb_probs = xgb_model.predict_proba(df_final)[0]

            # Calculate confidence based on the prediction made
            # if prediction is 0, confidence is probs[0]. If 1, confidence is probs[1].
            rf_conf = rf_probs[rf_raw]
            xgb_conf = xgb_probs[xgb_raw]

            context.update({
                'rf_prediction': rf_raw,
                'rf_confidence': round(rf_conf * 100, 2),
                'xgb_prediction': xgb_raw,
                'xgb_confidence': round(xgb_conf * 100, 2),
            })

    return render(request, 'index.html', context)