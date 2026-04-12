import requests

def ping_engines():
    sitemap_url = "https://brightlane.github.io/manychat-sitemap.xml"
    
    # Bing Ping (Immediate)
    bing_url = f"https://www.bing.com/ping?sitemap={sitemap_url}"
    r_bing = requests.get(bing_url)
    
    # Google Ping (Standard)
    google_url = f"https://www.google.com/ping?sitemap={sitemap_url}"
    r_google = requests.get(google_url)
    
    print(f"Bing: {r_bing.status_code} | Google: {r_google.status_code}")

if __name__ == "__main__":
    ping_engines()
