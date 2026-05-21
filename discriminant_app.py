from tkinter import Tk
from tkinter import ttk


def _format_number(value: float) -> str:
    if value.is_integer():
        return str(int(value))
    return f"{value:.6g}"


def discriminant(x2_entry: ttk.Entry, x_entry: ttk.Entry, x0_entry: ttk.Entry, result_label: ttk.Label) -> None:
    try:
        a = float(x2_entry.get().replace(",", "."))
        b = float(x_entry.get().replace(",", "."))
        c = float(x0_entry.get().replace(",", "."))
    except ValueError:
        result_label.config(text="Введите числа во все поля.")
        return

    if a == 0:
        result_label.config(text="Коэффициент a не должен быть равен 0.")
        return

    d = b**2 - 4 * a * c

    if d > 0:
        sqrt_d = d**0.5
        x1 = (-b + sqrt_d) / (2 * a)
        x2 = (-b - sqrt_d) / (2 * a)
        result = (
            f"D = {_format_number(d)}\n"
            f"x1 = {_format_number(x1)}\n"
            f"x2 = {_format_number(x2)}"
        )
    elif d == 0:
        root = -b / (2 * a)
        result = f"D = 0\nx = {_format_number(root)}"
    else:
        result = f"D = {_format_number(d)}\nДействительных корней нет."

    result_label.config(text=result)


def discriminant_window(notebook: ttk.Notebook) -> None:
    discriminant_frame = ttk.Frame(notebook, padding=10)
    notebook.add(discriminant_frame, text="Диск")

    ttk.Label(discriminant_frame, text="Введите коэффициент a:").grid(column=0, row=0, sticky="w")
    equation_x2 = ttk.Entry(discriminant_frame)
    equation_x2.grid(column=1, row=0, padx=5, pady=5)

    ttk.Label(discriminant_frame, text="Введите коэффициент b:").grid(column=0, row=1, sticky="w")
    equation_x = ttk.Entry(discriminant_frame)
    equation_x.grid(column=1, row=1, padx=5, pady=5)

    ttk.Label(discriminant_frame, text="Введите коэффициент c:").grid(column=0, row=2, sticky="w")
    equation_x0 = ttk.Entry(discriminant_frame)
    equation_x0.grid(column=1, row=2, padx=5, pady=5)

    result_label = ttk.Label(discriminant_frame, text="")
    result_label.grid(column=0, row=4, columnspan=2, pady=10, sticky="w")

    disc_button = ttk.Button(
        discriminant_frame,
        text="Вычислить",
        command=lambda: discriminant(equation_x2, equation_x, equation_x0, result_label),
    )
    disc_button.grid(column=0, row=3, columnspan=2, pady=5)


def main() -> None:
    root = Tk()
    root.title("Калькулятор")

    notebook = ttk.Notebook(root)
    discriminant_window(notebook)

    pifagor_frame = ttk.Frame(notebook, padding=10)
    notebook.add(pifagor_frame, text="ПИФАГОР")
    ttk.Label(pifagor_frame, text="Раздел в разработке.").pack()

    notebook.pack(expand=True, fill="both", padx=10, pady=10)
    root.mainloop()


if __name__ == "__main__":
    main()
