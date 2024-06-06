import tkinter as tk
from tkinter import messagebox, ttk

class ElectroMagnetApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Diagnóstico de Eletroímãs")
        self.failure_data = {
            "Não desimanta": {
                "causas": ["Molha", "Sobrecarga"],
                "mitigacoes": ["Secar o eletroímã", "Substituir a bobina"]
            },
            "Baixa imantação": {
                "causas": ["Fiação danificada", "Núcleo desgastado"],
                "mitigacoes": ["Substituir o cabo de alimentação", "Substituir o núcleo"]
            },
            "Superaquecimento": {
                "causas": ["Sobrecorrente", "Ventilação inadequada"],
                "mitigacoes": ["Verificar e ajustar a corrente", "Melhorar a ventilação"]
            },
            "Vibração excessiva": {
                "causas": ["Desbalanceamento", "Desgaste mecânico"],
                "mitigacoes": ["Balancear o eletroímã", "Verificar e reparar desgastes"]
            }
            # Adicione mais efeitos de falha aqui
        }
        self.measurements = []
        self.create_widgets()

    def create_widgets(self):
        self.create_failure_effect_section()
        self.create_measurement_entry_section()
        self.create_diagnosis_section()
        self.create_clear_button()

    def create_failure_effect_section(self):
        frame = tk.Frame(self.root)
        frame.pack(pady=10)

        self.failure_effect_label = tk.Label(frame, text="Selecione o Efeito de Falha:")
        self.failure_effect_label.pack(side=tk.LEFT)

        self.failure_effect_var = tk.StringVar(value=list(self.failure_data.keys())[0])
        self.failure_effect_menu = tk.OptionMenu(frame, self.failure_effect_var, *self.failure_data.keys())
        self.failure_effect_menu.pack(side=tk.LEFT)

    def create_measurement_entry_section(self):
        frame = tk.Frame(self.root)
        frame.pack(pady=10)

        self.measurements_label = tk.Label(frame, text="Insira as Medições do Campo Magnético:")
        self.measurements_label.pack()

        entry_frame = tk.Frame(frame)
        entry_frame.pack()

        self.measurements_entry = tk.Entry(entry_frame)
        self.measurements_entry.pack(side=tk.LEFT)

        self.add_measurement_button = tk.Button(entry_frame, text="Adicionar Medição", command=self.add_measurement)
        self.add_measurement_button.pack(side=tk.LEFT, padx=5)

        self.measurements_list = tk.Listbox(frame, height=6)
        self.measurements_list.pack()

        self.calculate_average_button = tk.Button(frame, text="Calcular Média", command=self.calculate_average)
        self.calculate_average_button.pack(pady=5)

        self.average_label = tk.Label(frame, text="Média das Medições:")
        self.average_label.pack()

    def create_diagnosis_section(self):
        frame = tk.Frame(self.root)
        frame.pack(pady=10)

        self.diagnosis_button = tk.Button(frame, text="Diagnosticar", command=self.diagnose)
        self.diagnosis_button.pack()

        self.diagnosis_label = tk.Label(frame, text="Diagnóstico:")
        self.diagnosis_label.pack()

        self.mitigation_text = tk.Text(frame, height=10, width=50)
        self.mitigation_text.pack()

        self.scrollbar = tk.Scrollbar(frame, command=self.mitigation_text.yview)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.mitigation_text.config(yscrollcommand=self.scrollbar.set)

    def create_clear_button(self):
        frame = tk.Frame(self.root)
        frame.pack(pady=10)

        self.clear_button = tk.Button(frame, text="Limpar", command=self.clear_all)
        self.clear_button.pack()

    def add_measurement(self):
        measurement = self.measurements_entry.get()
        if measurement:
            try:
                measurement = float(measurement)
                self.measurements.append(measurement)
                self.measurements_list.insert(tk.END, measurement)
                self.measurements_entry.delete(0, tk.END)
            except ValueError:
                messagebox.showerror("Erro", "Por favor, insira um número válido.")
        else:
            messagebox.showerror("Erro", "Por favor, insira uma medição.")

    def calculate_average(self):
        if self.measurements:
            average = sum(self.measurements) / len(self.measurements)
            self.average_label.config(text=f"Média das Medições: {average:.2f}")
        else:
            messagebox.showerror("Erro", "Nenhuma medição inserida.")

    def diagnose(self):
        effect = self.failure_effect_var.get()
        if not self.measurements:
            messagebox.showerror("Erro", "Nenhuma medição inserida.")
            return

        average = sum(self.measurements) / len(self.measurements)
        diagnosis = f"O eletroímã está {'bom' if average > 10 else 'ruim'}.\n"

        causes = self.failure_data[effect]["causas"]
        mitigations = self.failure_data[effect]["mitigacoes"]

        causes_str = "Causas Prováveis:\n" + "\n".join(causes) + "\n"
        mitigations_str = "Ações de Mitigação:\n" + "\n".join(mitigations) + "\n"

        self.mitigation_text.delete(1.0, tk.END)
        self.mitigation_text.insert(tk.END, diagnosis + causes_str + mitigations_str)

    def clear_all(self):
        self.failure_effect_var.set(list(self.failure_data.keys())[0])
        self.measurements_entry.delete(0, tk.END)
        self.measurements_list.delete(0, tk.END)
        self.average_label.config(text="Média das Medições:")
        self.mitigation_text.delete(1.0, tk.END)
        self.measurements.clear()

if __name__ == "__main__":
    root = tk.Tk()
    app = ElectroMagnetApp(root)
    root.mainloop()
