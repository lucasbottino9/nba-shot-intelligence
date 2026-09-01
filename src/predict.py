"""
Funciones para generar predicciones xFG utilizando
el modelo entrenado de NBA Shot Intelligence.
"""

from pathlib import Path

import joblib
import pandas as pd

from src.preprocessing import FEATURES, validate_features


MODEL_PATH = (
    Path(__file__).resolve().parent.parent
    / "models"
    / "xfg_xgboost.joblib"
)


def load_model(model_path=MODEL_PATH):
    """
    Carga el pipeline entrenado de xFG.
    """

    return joblib.load(model_path)


def predict_xfg(df, model=None):
    """
    Calcula la probabilidad esperada de conversión (xFG)
    para cada lanzamiento.
    """

    validate_features(df)

    if model is None:
        model = load_model()

    probabilities = model.predict_proba(
        df[FEATURES]
    )[:, 1]

    results = df.copy()
    results["xFG"] = probabilities

    return results