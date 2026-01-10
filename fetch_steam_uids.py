import requests
import json

def get_steam_uids():
    url = "https://api.steampowered.com/ISteamApps/GetAppList/v2/"
    
    try:
        print("Mengambil data dari Steam API...")
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        
        # Ambil semua AppID dan urutkan
        apps = data.get("applist", {}).get("apps", [])
        uids = sorted([app["appid"] for app in apps])
        
        result = {
            "total": len(uids),
            "uids": uids
        }
        
        with open("steam_uids.json", "w") as f:
            json.dump(result, f, indent=2)
            
        print(f"Berhasil! Total {len(uids)} UID disimpan ke steam_uids.json")
        
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")
        exit(1)

if __name__ == "__main__":
    get_steam_uids()
