import pandas as pd

def run_optimization():
    # Cargar los datos procesados
    data = pd.read_csv('data/augmented_supermarket_sales.csv')

    # Configuración: Buffer de seguridad (porcentaje)
    SAFETY_BUFFER = 1.2  # 20% de margen

    # Calcular el inventario óptimo
    data['Optimal Inventory'] = (data['Quantity'] * SAFETY_BUFFER).round()

    # Mostrar resultados de optimización
    print("\nOptimización de Inventarios:")
    print(data[['Product line', 'Quantity', 'Optimal Inventory']].head())

    # Guardar los resultados de optimización en un archivo CSV
    data.to_csv('outputs/optimized_inventory.csv', index=False)
    print("La optimización ha sido guardada en 'outputs/optimized_inventory.csv'.")
