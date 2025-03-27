import tkinter as tk
import datetime

class Vehiculo:
    def __init__(self, placa, marca, color, tipo):
        self.placa = placa
        self.marca = marca
        self.color = color
        self.tipo = tipo
        self.hora_ingreso = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    def datos(self):
        return f"Placa: {self.placa}, Marca: {self.marca}, Color: {self.color}, Tipo: {self.tipo}, Hora: {self.hora_ingreso}"

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Registro de Vehículos")
        self.vehiculos = []
        self.campos = {}
        labels = ["Placa", "Marca", "Color", "Tipo (Residente/Visitante)"]
        
        for i, text in enumerate(labels):
            tk.Label(root, text=f"{text}:").grid(row=i, column=0, padx=5, pady=5)
            entry = tk.Entry(root)
            entry.grid(row=i, column=1, padx=5, pady=5)
            self.campos[text] = entry

        self.msg = tk.Label(root, text="", fg="red")
        self.msg.grid(row=len(labels), column=0, columnspan=2)
        
        tk.Button(root, text="Guardar", command=self.guardar).grid(row=len(labels)+1, column=0, pady=5)
        tk.Button(root, text="Limpiar", command=self.limpiar).grid(row=len(labels)+1, column=1, pady=5)
        tk.Button(root, text="Mostrar", command=self.mostrar).grid(row=len(labels)+2, column=0, columnspan=2, pady=5)

    def guardar(self):
        data = {key: campo.get() for key, campo in self.campos.items()}
        if any(not v for v in data.values()):
            self.msg.config(text="Todos los campos son obligatorios.")
            return
        if data["Tipo (Residente/Visitante)"] not in ["Residente", "Visitante"]:
            self.msg.config(text="El tipo debe ser 'Residente' o 'Visitante'.")
            return

        veh = Vehiculo(data["Placa"], data["Marca"], data["Color"], data["Tipo (Residente/Visitante)"])
        self.vehiculos.append(veh)
        self.limpiar()
        self.msg.config(text="Vehículo guardado.", fg="green")

    def limpiar(self):
        for campo in self.campos.values():
            campo.delete(0, tk.END)
        self.msg.config(text="")

    def mostrar(self):
        if not self.vehiculos:
            self.msg.config(text="No hay vehículos registrados.")
            return
        registros = "\n".join(v.datos() for v in self.vehiculos)
        print("Registro de vehículos:\n" + registros)
        self.msg.config(text=registros, fg="black")

if __name__ == "__main__":
    root = tk.Tk()
    App(root)
    root.mainloop()
