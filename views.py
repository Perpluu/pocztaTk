import tkinter as tk
from tkinter import messagebox 

# Funkcja do przycisku "Sprawdź cenę"
def sprawdz_cene():
    wybrana_przesylka = przesylka_var.get()

    obraz = None
    cena = ""

    if wybrana_przesylka == "Pocztówka":
        obraz = "pocztowka.png"
        cena = "Cena: 1 zł"
    elif wybrana_przesylka == "List":
        obraz = "list.png"
        cena = "Cena: 1.5 zł"
    elif wybrana_przesylka == "Paczka":
        obraz = "paczka.png"
        cena = "Cena: 10 zł"

    if obraz:
        obraz_label.config(image=obrazy[obraz])
        cena_label.config(text=cena)
    else:
        messagebox.showinfo("Błąd", "Proszę wybrać typ przesyłki")

# Funkcja sprawdzajaca kod pocztowy
def waliduj_kod_pocztowy():
    kod_pocztowy = kod_pocztowy_var.get().replace("-", "")

    if len(kod_pocztowy) != 5:
        messagebox.showerror("Błąd", "Nieprawidłowa liczba cyfr w kodzie pocztowym")
    elif not kod_pocztowy.isdigit():
        messagebox.showerror("Błąd", "Kod pocztowy powinien składać się z samych cyfr")
    else:
        messagebox.showinfo("Sukces", "Dane przesyłki zostały wprowadzone")

# Tworzenie okna aplikacji
root = tk.Tk()
root.title("Nadaj Przesyłkę. PESEL:00000000000")

# Wczytanie obrazow
obrazy = {
    "pocztowka.png": tk.PhotoImage(file="pocztowka.png"),
    "list.png": tk.PhotoImage(file="list.png"),
    "paczka.png": tk.PhotoImage(file="paczka.png")
}

# Pola radio
przesylka_var = tk.StringVar()
przesylka_var.set("Pocztówka")  # Domyślnie zaznaczone pole "Pocztówka"
przesylka_frame = tk.Frame(root)
przesylka_frame.pack()

przesylka_pocztowka = tk.Radiobutton(przesylka_frame, text="Pocztówka", variable=przesylka_var, value="Pocztówka")
przesylka_list = tk.Radiobutton(przesylka_frame, text="List", variable=przesylka_var, value="List")
przesylka_paczka = tk.Radiobutton(przesylka_frame, text="Paczka", variable=przesylka_var, value="Paczka")

przesylka_pocztowka.pack()
przesylka_list.pack()
przesylka_paczka.pack()

# Pola edycyjne
dane_przesylki_frame = tk.Frame(root)
dane_przesylki_frame.pack()

ulica_label = tk.Label(dane_przesylki_frame, text="Ulica z numerem")
kod_pocztowy_label = tk.Label(dane_przesylki_frame, text="Kod pocztowy")
miasto_label = tk.Label(dane_przesylki_frame, text="Miasto")

ulica_entry = tk.Entry(dane_przesylki_frame)
kod_pocztowy_var = tk.StringVar()
kod_pocztowy_entry = tk.Entry(dane_przesylki_frame, textvariable=kod_pocztowy_var)
miasto_entry = tk.Entry(dane_przesylki_frame)

ulica_label.grid(row=0, column=0)
kod_pocztowy_label.grid(row=1, column=0)
miasto_label.grid(row=2, column=0)

ulica_entry.grid(row=0, column=1)
kod_pocztowy_entry.grid(row=1, column=1)
miasto_entry.grid(row=2, column=1)

# Przycisk "Sprawdź cenę"
sprawdz_cene_button = tk.Button(root, text="Sprawdź cenę", command=sprawdz_cene)
sprawdz_cene_button.pack()

# Wyświetlanie obrazu i ceny
obraz_label = tk.Label(root, image=obrazy["pocztowka.png"])
obraz_label.pack()

cena_label = tk.Label(root, text="Cena: 1 zł", font=("Helvetica", 12, "bold"))
cena_label.pack()

# Przycisk "Zatwierdź"
zatwierdz_button = tk.Button(root, text="Zatwierdź", command=waliduj_kod_pocztowy)
zatwierdz_button.pack()

root.mainloop()
