import sys
import csv
from google_play_scraper import reviews

# Ubah encoding default ke UTF-8 untuk Windows
sys.stdout.reconfigure(encoding='utf-8')

# Tentukan ID aplikasi
app_id = 'com.miHoYo.GenshinImpact'

# Ambil 3000 komentar dari aplikasi ini
result, _ = reviews(
    app_id,
    lang='id',  # Bahasa Indonesia
    country='id',  # Lokasi Indonesia
    count=3000  # Jumlah komentar yang diambil
)


with open("data_playstore.csv", "w", newline='', encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=['userName', 'at', 'content'])
    writer.writeheader()  # Menulis header CSV
    for review in result:
        writer.writerow({
            'userName': review.get('userName', 'N/A'),
            'at': review.get('at', 'N/A'),
            'content': review.get('content', 'N/A')
        })

print("Data komentar berhasil diambil dan disimpan di 'data_playstore.csv'.")
