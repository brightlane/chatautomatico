def trigger_index_now(new_urls):
    payload = {
        "host": "brightlane.github.io",
        "key": "your_indexnow_key_here", # Generate this in Bing Webmaster Tools
        "keyLocation": "https://brightlane.github.io/your_indexnow_key_here.txt",
        "urlList": new_urls
    }
    # Submit to the IndexNow API
    requests.post("https://api.indexnow.org/IndexNow", json=payload)
