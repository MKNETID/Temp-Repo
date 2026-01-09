import requests
import os

def main():
    repo = "SteamAutoCracks/ManifestHub"
    url = f"https://api.github.com/repos/{repo}/forks?sort=pushed&per_page=5"
    
    # Ambil data
    print("Mengambil data dari GitHub API...")
    response = requests.get(url)
    
    if response.status_code == 200:
        forks = response.json()
        print(f"Ditemukan {len(forks)} repo.")
        
        # Tulis file
        with open("latest_forks.txt", "w", encoding="utf-8") as f:
            for fork in forks:
                data = f"Repo: {fork['full_name']}\nURL: {fork['html_url']}\nUpdate: {fork['pushed_at']}\n---\n"
                f.write(data)
        
        print("Berhasil menulis ke latest_forks.txt")
    else:
        print(f"Gagal! Status code: {response.status_code}")

if __name__ == "__main__":
    main()
