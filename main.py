import tkinter as tk
from tkinter import messagebox
from modules import eda, prediction, optimization, alerts

def run_eda():
    eda.run_exploration()
    messagebox.showinfo("Exploración de Datos", "Análisis exploratorio completado. Gráficos guardados en 'outputs/visualizations'.")

def run_prediction():
    prediction.run_prediction()
    messagebox.showinfo("Predicción de Demanda", "Predicción completada. Resultados guardados en 'outputs/predictions.csv'.")

def run_optimization():
    optimization.run_optimization()
    messagebox.showinfo("Optimización de Inventarios", "Optimización completada. Resultados guardados en 'outputs/optimized_inventory.csv'.")

def run_alerts():
    alerts.generate_alerts()
    messagebox.showinfo("Generación de Alertas", "Alertas generadas. Resultados guardados en 'outputs/alerts.csv'.")

# Configuración de la ventana principal
root = tk.Tk()
root.title("Sistema de Gestión de Inventarios")
root.geometry("500x400")

# Título
label_title = tk.Label(root, text="Sistema de Gestión de Inventarios", font=("Arial", 16), pady=10)
label_title.pack()

# Botones para cada funcionalidad
btn_eda = tk.Button(root, text="Exploración de Datos", font=("Arial", 12), command=run_eda)
btn_eda.pack(pady=10)

btn_prediction = tk.Button(root, text="Predicción de Demanda", font=("Arial", 12), command=run_prediction)
btn_prediction.pack(pady=10)

btn_optimization = tk.Button(root, text="Optimización de Inventarios", font=("Arial", 12), command=run_optimization)
btn_optimization.pack(pady=10)

btn_alerts = tk.Button(root, text="Generar Alertas", font=("Arial", 12), command=run_alerts)
btn_alerts.pack(pady=10)

# Botón de salida
btn_exit = tk.Button(root, text="Salir", font=("Arial", 12), command=root.quit)
btn_exit.pack(pady=10)

# Ejecutar la aplicación
root.mainloop()
