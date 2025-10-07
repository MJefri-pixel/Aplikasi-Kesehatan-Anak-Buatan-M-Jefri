import tkinter as tk
from tkinter import messagebox
import pandas as pd

# List untuk menyimpan data
data_pasien = []

# Fungsi untuk menghitung IMT dan status gizi
def hitung_imt(berat, tinggi):
    tinggi_m = tinggi / 100
    imt = berat / (tinggi_m ** 2)
    imt = round(imt, 2)
    
    if imt < 17:
        status = "Sangat kurus"
    elif 17 <= imt < 18.5:
        status = "Kurus"
    elif 18.5 <= imt < 25:
        status = "Normal"
    elif 25 <= imt < 27:
        status = "Gemuk"
    else:
        status = "Obesitas"
    
    return imt, status

# Fungsi ketika tombol "Simpan" ditekan
def simpan_data():
    try:
        nama = entry_nama.get()
        usia = int(entry_usia.get())
        berat = float(entry_berat.get())
        tinggi = float(entry_tinggi.get())
        
        imt, status = hitung_imt(berat, tinggi)
        
        data = {
            "Nama": nama,
            "Usia": usia,
            "Berat (kg)": berat,
            "Tinggi (cm)": tinggi,
            "IMT": imt,
            "Status Gizi": status
        }
        
        data_pasien.append(data)
        
        # Simpan ke Excel
        df = pd.DataFrame(data_pasien)
        df.to_excel("data_pasien_anak.xlsx", index=False)
        
        messagebox.showinfo("Sukses", f"Data berhasil disimpan!\nStatus Gizi: {status} (IMT: {imt})")
        
        # Kosongkan input
        entry_nama.delete(0, tk.END)
        entry_usia.delete(0, tk.END)
        entry_berat.delete(0, tk.END)
        entry_tinggi.delete(0, tk.END)
        
    except ValueError:
        messagebox.showerror("Error", "Mohon masukkan data dengan benar!")

# ================== GUI ==================
root = tk.Tk()
root.title("Aplikasi Kesehatan Anak Buatan M Jefri")

# Ukuran window
root.geometry("400x300")

# Label dan entry input
tk.Label(root, text="Nama Anak:").grid(row=0, column=0, padx=10, pady=5, sticky='e')
entry_nama = tk.Entry(root)
entry_nama.grid(row=0, column=1)

tk.Label(root, text="Usia (tahun):").grid(row=1, column=0, padx=10, pady=5, sticky='e')
entry_usia = tk.Entry(root)
entry_usia.grid(row=1, column=1)

tk.Label(root, text="Berat Badan (kg):").grid(row=2, column=0, padx=10, pady=5, sticky='e')
entry_berat = tk.Entry(root)
entry_berat.grid(row=2, column=1)

tk.Label(root, text="Tinggi Badan (cm):").grid(row=3, column=0, padx=10, pady=5, sticky='e')
entry_tinggi = tk.Entry(root)
entry_tinggi.grid(row=3, column=1)

# Tombol simpan
btn_simpan = tk.Button(root, text="Simpan Data", command=simpan_data, bg="green", fg="white")
btn_simpan.grid(row=5, column=0, columnspan=2, pady=20)

# Jalankan aplikasi
root.mainloop()
