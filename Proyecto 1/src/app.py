import tkinter as tk
from tkinter import filedialog, messagebox
from lexer import lex
from html_generator import generate_html

class GUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Traductor de HTML")

        self.window_width = 800
        self.window_height = 700
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x = (screen_width - self.window_width) // 2
        y = (screen_height - self.window_height) // 2
        self.geometry(f"{self.window_width}x{self.window_height}+{x}+{y}")

        self.input_frame = tk.Frame(self)
        self.input_frame.pack(side="left", fill="both", expand=True, padx=10, pady=10)

        self.output_frame = tk.Frame(self)
        self.output_frame.pack(side="right", fill="both", expand=True, padx=10, pady=10)

        self.text_input_label = tk.Label(self.input_frame, text="Archivo de entrada:")
        self.text_input_label.pack(side="top", padx=10, pady=5)

        self.text_input = tk.Text(self.input_frame, wrap="word")
        self.text_input.pack(fill="both", expand=True, padx=10, pady=5)

        self.btn_open = tk.Button(self.input_frame, text="Abrir archivo", command=self.open_file)
        self.btn_open.pack(side="top", fill="x", padx=10, pady=5)

        self.text_output_label = tk.Label(self.output_frame, text="Código HTML generado:")
        self.text_output_label.pack(side="top", padx=10, pady=5)

        self.text_output = tk.Text(self.output_frame, wrap="word")
        self.text_output.pack(fill="both", expand=True, padx=10, pady=5)

        self.btn_translate = tk.Button(self.input_frame, text="Traducir", command=self.translate_file)
        self.btn_translate.pack(side="bottom", fill="x", padx=10, pady=5)

        self.input_frame.pack_propagate(False)
        self.output_frame.pack_propagate(False)
        self.text_input.pack_propagate(False)
        self.text_output.pack_propagate(False)

    def open_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Archivos de Texto", "*.txt"), ("Archivos JSON", "*.json"), ("Archivos HTML", "*.html")])
        if file_path:
            with open(file_path, "r") as file:
                content = file.read()
                self.text_input.delete(1.0, "end")
                self.text_input.insert("end", content)

    def translate_file(self):
        input_content = self.text_input.get(1.0, "end").strip()
        if not input_content:
            return

        # Llamar al analizador léxico y generador de HTML
        tokens = lex(input_content)
        html_content = generate_html(tokens)

        # Mostrar el código HTML generado en el área de salida
        self.text_output.delete(1.0, "end")
        self.text_output.insert("end", html_content)

        # Mostrar un mensaje de éxito
        messagebox.showinfo("Éxito", "Traducción a HTML completada con éxito.")

if __name__ == "__main__":
    app = GUI()
    app.mainloop()

