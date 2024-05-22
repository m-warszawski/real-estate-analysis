import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from tkinter.scrolledtext import ScrolledText
import plotly.express as px
import plotly.io as pio
from data_processing import import_data
from modelling import train_linear_model, train_random_forest_model, train_property_classifier, perform_association_rule_analysis
from visualization import visualize_data_plotly
from reports import create_pdf_report

class RealEstateAnalysisApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Program do Analizy Rynku Nieruchomości")
        self.root.configure(bg='#34495e')
        self.data = None  # Initialize data attribute
        self.create_widgets()
        self.make_responsive()

    def create_widgets(self):
        """Create the UI components for the application."""
        # Define styles for buttons, labels, and entries
        button_width = 25
        button_font = ('Helvetica', 10, 'bold')
        button_bg = '#3498db'
        button_fg = 'white'
        label_font = ('Helvetica', 10, 'bold')
        label_bg = '#34495e'
        label_fg = 'white'
        entry_bg = '#ecf0f1'
        entry_fg = '#2c3e50'
        results_bg = '#ecf0f1'
        results_fg = '#2c3e50'
        load_button_bg = '#e74c3c'
        grey_button_bg = '#737E83' 
        
        # Header frame for the program name
        header_frame = tk.Frame(self.root, bg=label_bg)
        header_frame.grid(row=0, column=0, columnspan=2, padx=10, pady=10, sticky='we')
        header_label = tk.Label(header_frame, text="Program do Analizy Rynku Nieruchomości", bg=label_bg, fg=label_fg, font=('Helvetica', 16, 'bold'))
        header_label.pack()

        # Top frame for file loading elements
        top_frame = tk.Frame(self.root, bg=label_bg)
        top_frame.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky='we')

        self.file_path_label = tk.Label(top_frame, text="Ścieżka pliku:", bg=label_bg, fg=label_fg, font=label_font)
        self.file_path_label.grid(row=0, column=0, padx=10, pady=10, sticky='w')

        self.file_path_entry = tk.Entry(top_frame, bg=entry_bg, fg=entry_fg, width=75)
        self.file_path_entry.grid(row=0, column=1, padx=10, pady=10, sticky='we')

        self.browse_button = tk.Button(top_frame, text="Przeglądaj", command=self.browse_file, bg=grey_button_bg, fg=button_fg, font=button_font,  width=15)
        self.browse_button.grid(row=0, column=2, padx=10, pady=10, sticky='e')

        self.load_button = tk.Button(top_frame, text="Wczytaj dane", command=self.load_data, bg=load_button_bg, fg=button_fg, font=button_font, width=button_width)
        self.load_button.grid(row=0, column=3, padx=10, pady=10, sticky='e')

        # Left frame for menu buttons
        menu_frame = tk.Frame(self.root, bg=label_bg)
        menu_frame.grid(row=2, column=0, padx=10, pady=10, sticky='nsew')

        self.description_label = tk.Label(menu_frame, text="Funkcje analizy danych:", bg=label_bg, fg=label_fg, font=('Helvetica', 12, 'bold'))
        self.description_label.grid(row=0, column=0, padx=10, pady=10, sticky='we')

        # Define menu buttons
        buttons = [
            ("Analizuj dane", self.analyze_data),
            ("Trenuj model", self.train_model),
            ("Trenuj Random Forest", self.train_random_forest_regressor),
            ("Klasyfikuj nieruchomości", self.classify_properties),
            ("Analiza reguł asocjacyjnych", self.analyze_association_rules),
            ("Wizualizuj dane", self.visualize_data),
            ("Generuj raport PDF", self.generate_pdf_report),
            ("Podgląd/Edycja danych", self.show_edit_data_window)
        ]

        for idx, (text, command) in enumerate(buttons):
            tk.Button(menu_frame, text=text, command=command, bg=button_bg, fg=button_fg, font=button_font, width=button_width)\
                .grid(row=idx+1, column=0, padx=10, pady=5, sticky='we')

        # Right frame for results
        results_frame = tk.Frame(self.root, bg=label_bg)
        results_frame.grid(row=2, column=1, padx=10, pady=10, sticky='nsew')

        # Frame for results label and clear button
        results_header_frame = tk.Frame(results_frame, bg=label_bg)
        results_header_frame.pack(fill='x')

        self.results_label = tk.Label(results_header_frame, text="Wyniki analizy:", bg=label_bg, fg=label_fg, font=('Helvetica', 12, 'bold'))
        self.results_label.pack(side='left', padx=10, pady=10)

        self.clear_button = tk.Button(results_header_frame, text="Wyczyść wyniki", command=self.clear_results_text, bg=grey_button_bg, fg=button_fg, font=button_font)
        self.clear_button.pack(side='right', padx=10, pady=10)

        self.results_text = ScrolledText(results_frame, bg=results_bg, fg=results_fg, font=('Helvetica', 10))
        self.results_text.pack(fill='both', expand=True, padx=10, pady=10)

    def make_responsive(self):
        """Configure the grid layout to make the application window responsive."""
        self.root.columnconfigure(0, weight=0)  # Fixed width for menu
        self.root.columnconfigure(1, weight=1)  # Expandable width for results
        self.root.rowconfigure(1, weight=0)  # Fixed height for header
        self.root.rowconfigure(2, weight=1)  # Expandable height for main content

    def browse_file(self):
        """Open a file dialog to browse and select a file."""
        file_path = filedialog.askopenfilename()
        self.file_path_entry.delete(0, tk.END)
        self.file_path_entry.insert(0, file_path)

    def load_data(self):
        """Load data from the specified file path."""
        self.clear_results_text()  # Clear the results text
        file_path = self.file_path_entry.get()
        if file_path:
            try:
                self.data = import_data(file_path)
                messagebox.showinfo("Informacja", "Dane zostały wczytane pomyślnie.")
                self.results_text.insert(tk.END, "Dane zostały wczytane pomyślnie.\n")
            except Exception as e:
                messagebox.showerror("Błąd", f"Błąd podczas wczytywania danych: {e}")
        else:
            messagebox.showwarning("Ostrzeżenie", "Proszę podać ścieżkę pliku.")

    def analyze_data(self):
        """Perform basic data analysis and display results."""
        if self.data is not None:
            try:
                self.results_text.insert(tk.END, str(self.data.describe()) + "\n")
                fig = px.scatter_matrix(self.data)
                pio.show(fig)
            except Exception as e:
                messagebox.showerror("Błąd", f"Błąd podczas analizy danych: {e}")
        else:
            messagebox.showwarning("Ostrzeżenie", "Proszę wczytać dane.")

    def train_model(self):
        """Train a linear regression model on the data."""
        if self.data is not None:
            try:
                model = train_linear_model(self.data)
                self.results_text.insert(tk.END, 'Model regresji liniowej został przetrenowany.\n')
            except Exception as e:
                messagebox.showerror("Błąd", f"Błąd podczas trenowania modelu: {e}")
        else:
            messagebox.showwarning("Ostrzeżenie", "Proszę wczytać dane.")

    def train_random_forest_regressor(self):
        """Train a Random Forest regressor on the data."""
        if self.data is not None:
            try:
                rf_model = train_random_forest_model(self.data)
                self.results_text.insert(tk.END, 'Model Random Forest został przetrenowany.\n')
            except Exception as e:
                messagebox.showerror("Błąd", f"Błąd podczas trenowania modelu Random Forest: {e}")
        else:
            messagebox.showwarning("Ostrzeżenie", "Proszę wczytać dane.")

    def classify_properties(self):
        """Train a classifier to categorize properties."""
        if self.data is not None:
            try:
                classifier = train_property_classifier(self.data)
                self.results_text.insert(tk.END, 'Model klasyfikacji nieruchomości został przetrenowany.\n')
            except Exception as e:
                messagebox.showerror("Błąd", f"Błąd podczas klasyfikacji nieruchomości: {e}")
        else:
            messagebox.showwarning("Ostrzeżenie", "Proszę wczytać dane.")

    def analyze_association_rules(self):
        """Perform association rule analysis on the data."""
        if self.data is not None:
            try:
                rules = perform_association_rule_analysis(self.data)
                self.results_text.insert(tk.END, 'Reguły asocjacyjne zostały przeanalizowane.\n')
                self.results_text.insert(tk.END, rules.to_string() + "\n")
            except Exception as e:
                messagebox.showerror("Błąd", f"Błąd podczas analizy reguł asocjacyjnych: {e}")
        else:
            messagebox.showwarning("Ostrzeżenie", "Proszę wczytać dane.")

    def visualize_data(self):
        """Visualize the data using Plotly."""
        if self.data is not None:
            try:
                visualize_data_plotly(self.data)
                messagebox.showinfo("Informacja", "Wizualizacja została zapisana jako map.html.")
                self.results_text.insert(tk.END, 'Wizualizacja została zapisana jako map.html.\n')
            except Exception as e:
                messagebox.showerror("Błąd", f"Błąd podczas wizualizacji danych: {e}")
        else:
            messagebox.showwarning("Ostrzeżenie", "Proszę wczytać dane.")

    def generate_pdf_report(self):
        """Generate a PDF report from the analyzed data."""
        if self.data is not None:
            try:
                report_path = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF files", "*.pdf")])
                if report_path:
                    create_pdf_report(self.data, report_path)
                    messagebox.showinfo("Informacja", "Raport PDF został wygenerowany.")
            except Exception as e:
                messagebox.showerror("Błąd", f"Błąd podczas generowania raportu PDF: {e}")
        else:
            messagebox.showwarning("Ostrzeżenie", "Proszę wczytać dane.")

    def show_edit_data_window(self):
        """Open a new window to view and edit the data."""
        if self.data is not None:
            edit_window = tk.Toplevel(self.root)
            edit_window.title("Podgląd i Edycja Danych")
            edit_window.geometry("800x600")
            edit_frame = tk.Frame(edit_window)
            edit_frame.pack(fill='both', expand=True)

            self.tree = ttk.Treeview(edit_frame)
            self.tree.pack(side='left', fill='both', expand=True)

            vsb = ttk.Scrollbar(edit_frame, orient="vertical", command=self.tree.yview)
            vsb.pack(side='right', fill='y')
            self.tree.configure(yscrollcommand=vsb.set)

            self.load_treeview_data()

            save_button = tk.Button(edit_window, text="Zapisz zmiany", command=self.save_treeview_data, bg='#26c6da', fg='white', font=('Helvetica', 10, 'bold'))
            save_button.pack(pady=10)
        else:
            messagebox.showwarning("Ostrzeżenie", "Proszę wczytać dane.")

    def load_treeview_data(self):
        """Load data into the Treeview widget for viewing/editing."""
        self.tree["columns"] = list(self.data.columns)
        self.tree["show"] = "headings"
        for col in self.data.columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, anchor='center')

        for index, row in self.data.iterrows():
            self.tree.insert("", "end", values=list(row))

        self.tree.bind("<Double-1>", self.on_treeview_double_click)

    def on_treeview_double_click(self, event):
        """Handle double-click event on the Treeview to edit cell value."""
        item = self.tree.selection()[0]
        column = self.tree.identify_column(event.x)
        column_index = int(column.replace('#', '')) - 1
        old_value = self.tree.item(item, "values")[column_index]

        new_value = self.ask_for_value(old_value)
        if new_value is not None:
            self.tree.set(item, column, new_value)

    def ask_for_value(self, old_value):
        """Prompt the user to input a new value for a selected cell."""
        value_dialog = tk.Toplevel(self.root)
        value_dialog.title("Edytuj wartość")
        tk.Label(value_dialog, text="Nowa wartość:").pack(padx=10, pady=10)
        new_value_var = tk.StringVar(value_dialog, value=old_value)
        tk.Entry(value_dialog, textvariable=new_value_var).pack(padx=10, pady=10)

        result = []

        def on_ok():
            result.append(new_value_var.get())
            value_dialog.destroy()

        tk.Button(value_dialog, text="OK", command=on_ok).pack(pady=10)

        self.root.wait_window(value_dialog)
        return result[0] if result else None

    def save_treeview_data(self):
        """Save changes made in the Treeview to the data."""
        for i, item in enumerate(self.tree.get_children()):
            values = self.tree.item(item)["values"]
            self.data.iloc[i] = values

        messagebox.showinfo("Informacja", "Dane zostały zapisane pomyślnie.")

    def clear_results_text(self):
        """Clear the text in the results_text widget."""
        self.results_text.delete('1.0', tk.END)
