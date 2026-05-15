import requests

def chercher_reseaux(pseudo):
    print(f"\n[+] 🔎 Scan GLOBAL lance pour le pseudo : {pseudo}")
    print("-" * 60)
    
    # Ta liste unique de tous les reseaux
    sites = {
        # --- LES GEANTS ---
        "TikTok": f"https://www.tiktok.com/@{pseudo}",
        "Instagram": f"https://www.instagram.com/{pseudo}/",
        "Snapchat": f"https://www.snapchat.com/add/{pseudo}",
        "YouTube": f"https://www.youtube.com/@{pseudo}",
        "Twitter / X": f"https://x.com/{pseudo}",
        "Threads": f"https://www.threads.net/@{pseudo}",
        "Pinterest": f"https://www.pinterest.com/{pseudo}/",
        "Facebook": f"https://www.facebook.com/{pseudo}",

        # --- GAMING & COMMUNAUTES ---
        "Roblox": f"https://www.roblox.com/user.aspx?username={pseudo}",
        "Twitch": f"https://www.twitch.tv/{pseudo}",
        "Reddit": f"https://www.reddit.com/user/{pseudo}/",
        "Steam": f"https://steamcommunity.com/id/{pseudo}",

        # --- MUSIQUE ---
        "Spotify": f"https://open.spotify.com/user/{pseudo}",
        "SoundCloud": f"https://soundcloud.com/{pseudo}",

        # --- PRO ---
        "LinkedIn": f"https://www.linkedin.com/in/{pseudo}/"
    }

    # Faux navigateur pour eviter les blocages de securite
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "Accept-Language": "fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7"
    }

    compte_trouve = 0

    for nom, url in sites.items():
        try:
            # On attend maximum 4 secondes par site pour que ce soit rapide
            reponse = requests.get(url, headers=headers, timeout=4)
            
            # Code 200 = Le compte existe !
            if reponse.status_code == 200:
                print(f"[🟢 TROUVE] {nom:<12} : {url}")
                compte_trouve += 1
            else:
                print(f"[❌ LIBRE]  {nom:<12} n'existe pas")
                
        except requests.exceptions.RequestException:
            print(f"[⚠️ ERREUR] {nom:<12} : Connexion impossible (Timeout)")

    print("-" * 60)
    print(f"[+] Scan termine. {compte_trouve} comptes trouves au total !")

if __name__ == "__main__":
    pseudo_cible = input("Entre le pseudo a chercher partout : ")
    chercher_reseaux(pseudo_cible)