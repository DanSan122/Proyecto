import pandas as pd

def generate_alerts():
    # Cargar los datos procesados
    data = pd.read_csv('data/augmented_supermarket_sales.csv')

    # Configuración: Nivel de inventario bajo
    LOW_INVENTORY_THRESHOLD = 5

    # Filtrar productos con inventario bajo
    low_inventory = data[data['Quantity'] < LOW_INVENTORY_THRESHOLD]

    # Mostrar alertas
    if low_inventory.empty:
        print("No se encontraron productos con inventario bajo.")
    else:
        print("\nAlertas de Inventario Bajo:")
        print(low_inventory[['Product line', 'Quantity']])

        # Guardar las alertas en un archivo CSV
        low_inventory.to_csv('outputs/alerts.csv', index=False)
        print("Las alertas han sido guardadas en 'outputs/alerts.csv'.")
