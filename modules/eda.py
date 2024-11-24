import pandas as pd
import matplotlib.pyplot as plt

def run_exploration():
    # Cargar datos
    data = pd.read_csv('data/augmented_supermarket_sales.csv')

    # Visualizar ventas por categoría
    sales_by_category = data.groupby('Product line')['Total'].sum()
    sales_by_category.plot(kind='bar', title='Ventas por Categoría', color='skyblue')
    plt.xlabel('Categoría')
    plt.ylabel('Ventas Totales')
    plt.savefig('outputs/visualizations/sales_by_category.png')
    plt.close()

    # Estadísticas descriptivas
    data.describe().to_csv('outputs/visualizations/data_statistics.csv')
    print("Exploración de datos completada.")
