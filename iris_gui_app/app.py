import tkinter as tk
from tkinter import messagebox
import numpy as np
import pickle

# Load model
with open("E:\Git Programs\Python\iris_gui_app\iris_model.pkl", "rb") as f:
    model = pickle.load(f)

# Create GUI
root = tk.Tk()
root.title("Iris Species Predictor")

entries = []
labels = ["Sepal Length", "Sepal Width", "Petal Length", "Petal Width"]

for i, label in enumerate(labels):
    tk.Label(root, text=label).grid(row=i, column=0)
    entry = tk.Entry(root)
    entry.grid(row=i, column=1)
    entries.append(entry)

def predict():
    try:
        inputs = [float(e.get()) for e in entries]
        result = model.predict([inputs])[0]
        species = ["Setosa", "Versicolor", "Virginica"]
        messagebox.showinfo("Prediction", f"Predicted Species: {species[result]}")
    except:
        messagebox.showerror("Error", "Please enter valid numbers")

tk.Button(root, text="Predict", command=predict).grid(row=5, column=0, columnspan=2)
root.mainloop()
