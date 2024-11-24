import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error

def run_prediction():
    # Cargar datos
    data = pd.read_csv('data/augmented_supermarket_sales.csv')

    # Manejar diferentes formatos de fecha
    data['Date'] = pd.to_datetime(data['Date'], errors='coerce', dayfirst=True)

    # Verificar y eliminar fechas inválidas
    if data['Date'].isna().any():
        print("Fechas inválidas encontradas y eliminadas.")
        data = data.dropna(subset=['Date'])

    # Preprocesar datos
    data['Day'] = data['Date'].dt.day
    data['Month'] = data['Date'].dt.month
    data['Year'] = data['Date'].dt.year

    # Seleccionar características y variable objetivo
    X = data[['Day', 'Month', 'Year', 'Quantity', 'Unit price']].values
    y = data['Total'].values

    # Escalar las características
    scaler = StandardScaler()
    X = scaler.fit_transform(X)

    # Dividir en conjuntos de entrenamiento y prueba
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Construir el modelo (puede ser TensorFlow o scikit-learn)
    # Ejemplo simplificado
    from sklearn.ensemble import RandomForestRegressor
    model = RandomForestRegressor(random_state=42)
    model.fit(X_train, y_train)

    # Evaluar el modelo
    predictions = model.predict(X_test)
    mse = mean_squared_error(y_test, predictions)
    print(f"MSE del modelo: {mse}")

    # Guardar predicciones
    results = pd.DataFrame({'Actual': y_test, 'Predicted': predictions})
    results.to_csv('outputs/predictions.csv', index=False)
    print("Predicciones guardadas en 'outputs/predictions.csv'")
