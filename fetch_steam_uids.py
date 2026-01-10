import requests
import json

def get_steam_uids():
    # URL v2 yang lebih stabil dengan format json eksplisit
    url = "https://api.steampowered.com/ISteamApps/GetAppList/v2/?format=json"
    
    # Menambahkan Header agar tidak dianggap bot yang mencurigakan
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    
    try:
        print("Mengambil data dari Steam API...")
        response = requests.get(url, headers=headers, timeout=30)
        
        # Cek status code
        if response.status_code != 200:
            print(f"Gagal akses API. Status Code: {response.status_code}")
            # Coba fallback ke v1 jika v2 gagal
            print("Mencoba fallback ke API v1...")
            url_v1 = "https://api.steampowered.com/ISteamApps/GetAppList/v0001/"
            response = requests.get(url_v1, headers=headers, timeout=30)
        
        response.raise_for_status()
        data = response.json()
        
        # Struktur JSON Steam: applist -> apps -> list of dicts
        apps = data.get("applist", {}).get("apps", [])
        
        if not apps:
            print("Data kosong atau format JSON berubah.")
            return

        # Mengambil AppID, pastikan unik dengan set, lalu urutkan
        uids = sorted(list(set(app["appid"] for app in apps)))
        
        result = {
            "total": len(uids),
            "uids": uids
        }
        
        with open("steam_uids.json", "w") as f:
            json.dump(result, f) # Tanpa indentasi agar ukuran file lebih kecil (opsional)
            
        print(f"Berhasil! Total {len(uids)} UID disimpan ke steam_uids.json")
        
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")
        exit(1)

if __name__ == "__main__":
    get_steam_uids()
