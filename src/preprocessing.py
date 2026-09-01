"""
Funciones y configuraciones utilizadas para preparar
los datos del modelo NBA Shot Intelligence.
"""

TARGET = "SHOT_MADE"

NUMERIC_FEATURES = [
    "SHOT_DISTANCE",
    "LOC_X",
    "LOC_Y",
    "QUARTER",
    "MINS_LEFT",
    "SECS_LEFT",
]

CATEGORICAL_FEATURES = [
    "SHOT_TYPE",
    "ACTION_TYPE",
    "BASIC_ZONE",
    "ZONE_NAME",
    "ZONE_RANGE",
]

FEATURES = NUMERIC_FEATURES + CATEGORICAL_FEATURES

def validate_features(df):
    """
    Verifica que el DataFrame contenga todas las variables
    necesarias para realizar predicciones.
    """

    missing_features = [
        feature
        for feature in FEATURES
        if feature not in df.columns
    ]

    if missing_features:
        raise ValueError(
            f"Faltan variables requeridas: {missing_features}"
        )

    return True