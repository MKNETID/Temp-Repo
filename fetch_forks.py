import requests
import os

# Konfigurasi
REPO = "SteamAutoCracks/ManifestHub"
URL = f"https://api.github.com/repos/{REPO}/forks"
TOKEN = os.getenv("GH_TOKEN")

headers = {
    "Authorization": f"token {TOKEN}",
    "Accept": "application/vnd.github.v3+json"
}

params = {
    "sort": "pushed", # Mengurutkan berdasarkan aktivitas push terbaru
    "per_page": 5      # HANYA mengambil 5 hasil pertama dari API
}

def main():
    response = requests.get(URL, headers=headers, params=params)
    
    if response.status_code == 200:
        forks = response.json()
        
        # Menulis hasil ke file
        with open("latest_forks.txt", "w") as f:
            f.write("=== 5 FORKS TERBARU ===\n")
            for fork in forks:
                name = fork['full_name']
                url = fork['html_url']
                updated = fork['pushed_at']
                
                output = f"Repo: {name}\nURL: {url}\nLast Update: {updated}\n" + ("-"*20) + "\n"
                f.write(output)
                print(f"Berhasil mengambil: {name}")
    else:
        print(f"Error {response.status_code}: {response.text}")

if __name__ == "__main__":
    main()
