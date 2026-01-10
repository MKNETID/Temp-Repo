import requests
import json
import time

def get_steam_uids():
    # Menggunakan URL alternatif yang sering digunakan untuk fetching data massal
    # Tanpa tanda kurung atau versi v0001 yang sudah usang
    url = "https://api.steampowered.com/ISteamApps/GetAppList/v2"
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'Accept': 'application/json'
    }
    
    # Mencoba hingga 3 kali jika gagal koneksi
    for attempt in range(3):
        try:
            print(f"Mencoba mengambil data (Percobaan {attempt + 1})...")
            response = requests.get(url, headers=headers, timeout=60)
            
            if response.status_code == 200:
                data = response.json()
                apps = data.get("applist", {}).get("apps", [])
                
                if apps:
                    # Ambil AppID dan urutkan
                    uids = sorted(list(set(app["appid"] for app in apps)))
                    
                    result = {
                        "total": len(uids),
                        "uids": uids
                    }
                    
                    with open("steam_uids.json", "w") as f:
                        json.dump(result, f)
                    
                    print(f"Berhasil! Ditemukan {len(uids)} UID.")
                    return
                else:
                    print("Data kosong, mencoba lagi...")
            else:
                print(f"Server merespons dengan status: {response.status_code}")
                
        except Exception as e:
            print(f"Error: {e}")
        
        # Tunggu sebentar sebelum mencoba lagi (avoid rate limit)
        time.sleep(5)

    print("Gagal mengambil data setelah beberapa percobaan.")
    exit(1)

if __name__ == "__main__":
    get_steam_uids()
