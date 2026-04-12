import os

# --- CONFIGURATION ---
OUT_DIR = "manychat"
KW_FILE = "keywords.txt"
SITEMAP_FILE = "manychat-sitemap.xml"

# Your 5 Confirmed Rotating Affiliate Links
AFFILIATE_LINKS = [
    "https://manychat.partnerlinks.io/bbwxetk27f88-64kfxo", # #1
    "https://manychat.partnerlinks.io/98hj6b3pr28k-4znb59", # #2
    "https://manychat.partnerlinks.io/emwcbue22i01-ogcg6e", # #3
    "https://manychat.partnerlinks.io/t8let4hhqtqg-wki14",  # #4
    "https://manychat.partnerlinks.io/nwkkk7vkps17"         # #5
]

# Top 6 Global Languages (Total Population Reach)
LANGS = {
    "en": {"tag": "Comparison", "cta": "Start Free Today", "desc": "Best automation for 2026."},
    "zh": {"tag": "对比", "cta": "立即免费开始", "desc": "2026年最佳营销自动化工具。"},
    "hi": {"tag": "तुलना", "cta": "आज ही मुफ्त शुरू करें", "desc": "2026 के लिए सर्वश्रेष्ठ स्वचालन।"},
    "es": {"tag": "Comparación", "cta": "Comienza Gratis Hoy", "desc": "La mejor automatización para 2026."},
    "fr": {"tag": "Comparaison", "cta": "Commencer Gratuitement", "desc": "Meilleure automatisation pour 2026."},
    "ar": {"tag": "مقارنة", "cta": "ابدأ مجاناً اليوم", "desc": "أفضل أتمتة لعام 2026."}
}

def get_template(kw, lang_code, link):
    comp = kw.replace("ManyChat vs", "").strip()
    data = LANGS[lang_code]
    direction = "rtl" if lang_code == "ar" else "ltr"
    
    # Hreflang Cluster for International SEO
    hreflangs = ""
    for l in LANGS:
        hreflangs += f'<link rel="alternate" hreflang="{l}" href="https://brightlane.github.io/manychat/{l}-{kw.lower().replace(" ", "-")}.html">\n    '

    return f"""<!DOCTYPE html>
<html lang="{lang_code}" dir="{direction}">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>ManyChat vs {comp} | 2026 {data['tag']}</title>
    {hreflangs}
    <style>
        body{{margin:0;font-family:sans-serif;line-height:1.6;color:#111;background:#f4f4f4;text-align:{'right' if direction == 'rtl' else 'left'};}}
        .hero{{background:#222;color:#fff;padding:60px 20px;text-align:center;}}
        .container{{max-width:800px;margin:-40px auto 40px;background:#fff;padding:40px;border-radius:12px;box-shadow:0 4px 15px rgba(0,0,0,0.1);}}
        .btn{{display:inline-block;background:#ff6600;color:#fff;padding:18px 35px;text-decoration:none;border-radius:8px;font-weight:bold;font-size:1.2rem;}}
        .footer{{text-align:center;padding:40px;font-size:0.9rem;color:#666;}}
    </style>
</head>
<body>
    <div class="hero">
        <h1>ManyChat vs {comp}</h1>
        <p>Global Automation Audit 2026</p>
    </div>
    <div class="container">
        <h2>{data['tag']} ({lang_code.upper()})</h2>
        <p>{data['desc']}</p>
        <div style="text-align:center;margin:30px 0;">
            <a href="{link}" class="btn" target="_blank">{data['cta']} →</a>
        </div>
        <p>Scale your engagement and sales with the world's #1 chatbot platform.</p>
    </div>
    <div class="footer">© 2026 ManyChat Global Partner | <a href="../legal.html">Legal Disclosure</a></div>
</body>
</html>"""

def main():
    if not os.path.exists(OUT_DIR): os.makedirs(OUT_DIR)
    
    with open(KW_FILE, "r", encoding="utf-8") as f:
        keywords = [line.strip() for line in f if line.strip()]

    count = 0
    # Process 3 Keywords daily = 18 total international pages
    for i, kw in enumerate(keywords[:3]):
        # Rotate link per keyword set
        current_link = AFFILIATE_LINKS[i % len(AFFILIATE_LINKS)]
        
        for lang in LANGS:
            slug = f"{lang}-{kw.lower().replace(' ', '-')}.html"
            path = os.path.join(OUT_DIR, slug)
            if not os.path.exists(path):
                with open(path, "w", encoding="utf-8") as f:
                    f.write(get_template(kw, lang, current_link))
                count += 1
    
    # Update Sitemap
    all_pages = [p for p in os.listdir(OUT_DIR) if p.endswith(".html")]
    with open(SITEMAP_FILE, "w", encoding="utf-8") as s:
        s.write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n')
        for p in all_pages:
            s.write(f'  <url><loc>https://brightlane.github.io/manychat/{p}</loc></url>\n')
        s.write('</urlset>')
    
    print(f"Success: {count} international pages generated with 5-link rotation.")

if __name__ == "__main__":
    main()
