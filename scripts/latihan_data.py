import pandas as pd
import numpy as np

# Simulasi data transaksi harian selama 30 hari
data = {
    'tanggal': pd.date_range(start='2026-01-01', periods=30),
    'nominal_zakat': [100, 150, 120, 200, 250, 180, 300, 320, 280, 400, 
                      450, 380, 500, 550, 520, 600, 650, 620, 700, 750,
                      720, 800, 850, 820, 900, 950, 920, 1000, 1050, 1020]
}
df = pd.DataFrame(data)
df.to_csv('transaksi_zakat.csv', index=False)
print("Dataset latihan berhasil dibuat!")