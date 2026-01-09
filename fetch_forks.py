import requests
import os
from datetime import datetime

# Konfigurasi
REPO = "SteamAutoCracks/ManifestHub"
URL = f"https://api.github.com/repos/{REPO}/forks"
# GitHub Actions secara otomatis menyediakan GITHUB_TOKEN
TOKEN = os.getenv("GH_TOKEN")

headers = {
    "Accept": "application/vnd.github.v3+json"
}

# Tambahkan token ke header jika tersedia
if TOKEN:
    headers["Authorization"] = f"token {TOKEN}"

params = {
    "sort": "pushed",
    "per_page": 5
}

def main():
    print(f"Memulai pengambilan data untuk {REPO}...")
    try:
        response = requests.get(URL, headers=headers, params=params)
        print(f"Status Code: {response.status_code}")
        
        # Jika kena rate limit atau error lain
        if response.status_code != 200:
            print(f"Error Detail: {response.text}")
            return

        forks = response.json()
        print(f"Jumlah fork ditemukan: {len(forks)}")

        # Membuka file dengan encoding utf-8 agar aman
        with open("latest_forks.txt", "w", encoding="utf-8") as f:
            f.write(f"Terakhir Diperbarui: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} (WIB/UTC)\n")
            f.write("="*30 + "\n")
            
            if not forks:
                f.write("Tidak ada fork yang ditemukan atau diupdate baru-baru ini.\n")
            else:
                for fork in forks:
                    line = f"Repo: {fork['full_name']}\nURL: {fork['html_url']}\nPush: {fork['pushed_at']}\n"
                    f.write(line + "-"*20 + "\n")
                    print(f"Menulis: {fork['full_name']}")
                
        print("Proses penulisan file selesai.")
        
    except Exception as e:
        print(f"Terjadi error saat eksekusi: {e}")

if __name__ == "__main__":
    main()
