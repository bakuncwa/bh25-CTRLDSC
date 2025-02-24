import numpy as np
from django.shortcuts import render, redirect
from .models import Farm
from catboost import CatBoostClassifier
from django.shortcuts import render
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

def load_model(file_path):
    loaded_model = CatBoostClassifier()
    loaded_model.load_model(file_path)
    print(f"Model loaded from {file_path}")
    return loaded_model

loadModel = load_model('models/soil_acidity_model_v3.bin')

def index(request):
    return render(request, 'ligtas_ani/index.html')

def add_location(request):
    prediction = None

    if request.method == 'POST':
        new_farm = Farm()
        new_farm.farm_name = request.POST.get('farm_name')
        new_farm.city = request.POST.get('city')
        new_farm.farm_location = request.POST.get('location')
        new_farm.save()

        acidity = [
            float(request.POST.get('rainfall_val', 0)),
            float(request.POST.get('H_val', 0)),
            float(request.POST.get('Zn_val', 0)),
            float(request.POST.get('Mn_val', 0)),
            float(request.POST.get('Fe_val', 0)),
            float(request.POST.get('Cu_val', 0)),
            float(request.POST.get('P_val', 0)),
            float(request.POST.get('Na_val', 0)),
            float(request.POST.get('N_val', 0)),
            # float(request.POST.get('pHIndicator_val', 0)),
        ]

        location = request.POST.get('location')

        soil_parameters = {
            'Loc1': [38.45, 0.119, 0.154, 0.137, 0.149, 0.124, 0.210, 0.008, 0.150],
            'Loc2': [96.07, 0.110, 0.183, 0.118, 0.039, 0.191, 0.120, 0.006, 0.018],
            'Loc3': [74.19, 0.005, 0.057, 0.066, 0.200, 0.028, 0.166, 0.170, 0.055],
            'Loc4': [60.86, 0.078, 0.143, 0.001, 0.141, 0.029, 0.100, 0.073, 0.178],
            'Loc5': [16.60, 0.087, 0.131, 0.114, 0.036, 0.128, 0.144, 0.183, 0.121],
        }

        values = soil_parameters.get(location)

        if values:
            input_array = np.array([values + acidity[:len(values)]]).reshape(1, -1)

            prediction = loadModel.predict(input_array)[0]  # ML model prediction

    return render(request, 'ligtas_ani/add_location.html', {'prediction': prediction})

def feature_importance_view(request):
    model = CatBoostClassifier()
    model.load_model("soil_acidity_model_v3.bin")  # Load trained model

    feature_importances = model.get_feature_importance(prettified=True)

    top_features = feature_importances.head(8)

    plt.figure(figsize=(10, 5))
    sns.barplot(x=top_features["Importance"], y=top_features["Feature"], palette="viridis")
    plt.xlabel("Importance Score")
    plt.ylabel("Feature Name")
    plt.title("Top Feature Importances (Soil Acidity)")
    plt.grid(axis="x", linestyle="--")

    plot_path = "static/ligtas_ani/img/feature_importance_plot.png"
    plt.savefig(plot_path, bbox_inches="tight")
    plt.close()

    return render(request, "ligtas_ani/add_location.html", {"plot_url": plot_path})