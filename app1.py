import customtkinter as ctk
from tkinter import filedialog, messagebox
from optimizer import run_optimizer
import threading

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

BG    = "#0d0d0d"
WHITE = "#ffffff"
GRAY  = "#aaaaaa"
DIM   = "#555555"

selected_file = None


def show_info():
    info_win = ctk.CTkToplevel(app)
    info_win.title("About the Optimizer")
    info_win.geometry("560x380")
    info_win.resizable(False, False)
    info_win.configure(fg_color=BG)
    info_win.grab_set()

    ctk.CTkLabel(
        info_win,
        text="Portfolio Optimizer — How it works",
        font=("Arial", 18, "bold"),
        text_color=WHITE,
    ).pack(pady=(28, 12))

    body = (
        "This tool calculates the optimal asset allocation of a portfolio\n"
        "using two well-established quantitative finance models:\n\n"
        "•  Markowitz Mean-Variance Optimization\n"
        "   Finds the portfolio weights that maximise expected return\n"
        "   for a given level of risk (efficient frontier).\n\n"
        "•  Michaud Resampled Efficiency\n"
        "   Improves on Markowitz by resampling input parameters via\n"
        "   Monte Carlo simulation, producing more robust and\n"
        "   diversified allocations.\n\n"
        "Input:  an Excel file with historical asset closing prices.\n"
        "Output: optimal weights saved in an Excel report."
    )

    ctk.CTkLabel(
        info_win,
        text=body,
        font=("Arial", 13),
        text_color=GRAY,
        justify="left",
        fg_color="transparent",
    ).pack(padx=35, pady=5, anchor="w")

    ctk.CTkButton(
        info_win,
        text="Close",
        width=100,
        command=info_win.destroy,
    ).pack(pady=18)


def browse_file():
    global selected_file
    selected_file = filedialog.askopenfilename(
        title="Select Excel File",
        filetypes=[
            ("Excel files", "*.xlsx *.xlsm"),
            ("All files", "*.*"),
        ],
    )
    if selected_file:
        file_label.configure(text=selected_file)
        status_label.configure(text="File selected. Ready to optimize.")


def run_optimizer_thread():
    global selected_file
    if not selected_file:
        messagebox.showerror("Error", "Please select an Excel file first.")
        return

    run_button.configure(state="disabled", text="Optimizing…")
    browse_button.configure(state="disabled")
    status_label.configure(text="Running Markowitz & Michaud optimization. Please wait…")

    try:
        result = run_optimizer(selected_file)
        status_label.configure(text="Optimization completed.")
        messagebox.showinfo("Done", result)
    except Exception as e:
        status_label.configure(text="An error occurred during optimization.")
        messagebox.showerror("Error", str(e))
    finally:
        run_button.configure(state="normal", text="Run Optimization")
        browse_button.configure(state="normal")


def start_optimizer():
    thread = threading.Thread(target=run_optimizer_thread)
    thread.start()


# ── Main window ──────────────────────────────────────────────────────────────
app = ctk.CTk()
app.title("Portfolio Optimizer")
app.geometry("750x470")
app.resizable(False, False)
app.configure(fg_color=BG)

# Info button — top right corner
ctk.CTkButton(
    app,
    text="Info",
    width=64,
    height=28,
    font=("Arial", 12),
    command=show_info,
).place(x=672, y=13)

# Title
ctk.CTkLabel(
    app,
    text="Portfolio Optimizer",
    font=("Arial", 28, "bold"),
    text_color=WHITE,
    fg_color="transparent",
).pack(pady=(35, 8))

# Subtitle
ctk.CTkLabel(
    app,
    text="Select an Excel file and run the Markowitz + Michaud calculation.",
    font=("Arial", 15),
    text_color=GRAY,
    fg_color="transparent",
).pack(pady=(0, 28))

# Browse button
browse_button = ctk.CTkButton(
    app,
    text="Browse Excel File",
    width=220,
    height=40,
    command=browse_file,
)
browse_button.pack(pady=8)

# Selected file path
file_label = ctk.CTkLabel(
    app,
    text="No file selected",
    wraplength=650,
    font=("Arial", 13),
    text_color=GRAY,
    fg_color="transparent",
)
file_label.pack(pady=10)

# Run button
run_button = ctk.CTkButton(
    app,
    text="Run Optimization",
    width=220,
    height=45,
    command=start_optimizer,
)
run_button.pack(pady=22)

# Status label
status_label = ctk.CTkLabel(
    app,
    text="Waiting for Excel file.",
    font=("Arial", 13),
    text_color=GRAY,
    fg_color="transparent",
)
status_label.pack(pady=4)

# ── Contact section ──────────────────────────────────────────────────────────
ctk.CTkFrame(app, height=1, fg_color="#2a2a2a").pack(fill="x", padx=40, pady=(22, 8))

ctk.CTkLabel(
    app,
    text="Alessio Bisceglia  ·  alessiobisceglia04@gmail.com",
    font=("Arial", 11),
    text_color=DIM,
    fg_color="transparent",
).pack(pady=(0, 14))

app.mainloop()
