import os
import random

# --- GLOBAL-6 CONFIG ---
OUT_DIR = "manychat"
KW_FILE = "keywords.txt"
SITEMAP_FILE = "manychat-sitemap.xml"
AFFILIATE_LINK = "https://manychat.partnerlinks.io/nwkkk7vkps17"

# The 6 most spoken languages by total population (2026)
LANGS = {
    "en": {"tag": "Comparison", "cta": "Start Free Today", "desc": "Best automation for 2026."},
    "zh": {"tag": "对比", "cta": "立即免费开始", "desc": "2026年最佳营销自动化工具。"},
    "hi": {"tag": "तुलना", "cta": "आज ही मुफ्त शुरू करें", "desc": "2026 के लिए सर्वश्रेष्ठ स्वचालन।"},
    "es": {"tag": "Comparación", "cta": "Comienza Gratis Hoy", "desc": "La mejor automatización para 2026."},
    "fr": {"tag": "Comparaison", "cta": "Commencer Gratuitement", "desc": "Meilleure automatisation pour 2026."},
    "ar": {"tag": "مقارنة", "cta": "ابدأ مجاناً اليوم", "desc": "أفضل أتمتة لعام 2026."}
}

def get_intl_template(kw, lang_code):
    comp = kw.replace("ManyChat vs", "").strip()
    data = LANGS[lang_code]
    direction = "rtl" if lang_code == "ar" else "ltr"
    
    # Generate Hreflang cluster
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
        body{{margin:0;font-family:Arial,sans-serif;line-height:1.6;color:#111;background:#f9f9f9;text-align:{'right' if direction == 'rtl' else 'left'};}}
        header{{background:#222;color:#fff;padding:15px;text-align:center;font-weight:bold;}}
        section{{padding:40px 20px;max-width:900px;margin:20px auto;background:#fff;border-radius:8px;box-shadow:0 2px 5px rgba(0,0,0,0.1);}}
        .cta-button{{display:inline-block;background:#ff6600;color:#fff;padding:15px 30px;text-decoration:none;border-radius:5px;font-weight:bold;margin:20px 0;}}
        .comparison-table{{width:100%;border-collapse:collapse;margin:25px 0;}}
        .comparison-table th, .comparison-table td{{border:1px solid #ddd;padding:12px;}}
        footer{{background:#222;color:#fff;text-align:center;padding:30px;margin-top:40px;}}
    </style>
</head>
<body>
<header>ManyChat Global 2026</header>
<section>
    <h1>ManyChat vs {comp} ({lang_code.upper()})</h1>
    <p>{data['desc']}</p>
    <div style="text-align:center;">
        <a href="{AFFILIATE_LINK}" class="cta-button" target="_blank">{data['cta']} →</a>
    </div>
    <table class="comparison-table">
        <tr><th>Feature</th><th>ManyChat</th><th>{comp}</th></tr>
        <tr><td>AI Automation</td><td>Native 2026</td><td>Legacy</td></tr>
        <tr><td>Multilingual</td><td>✅ Supported</td><td>❌ Limited</td></tr>
    </table>
</section>
<footer>© 2026 | ManyChat Global Partner</footer>
</body>
</html>"""

def main():
    if not os.path.exists(OUT_DIR): os.makedirs(OUT_DIR)
    with open(KW_FILE, "r", encoding="utf-8") as f:
        keywords = [line.strip() for line in f if line.strip()]

    count = 0
    # Process 3 keywords x 6 languages = 18 pages per day
    for kw in keywords[:3]:
        for lang in LANGS:
            slug = f"{lang}-{kw.lower().replace(' ', '-')}.html"
            path = os.path.join(OUT_DIR, slug)
            if not os.path.exists(path):
                with open(path, "w", encoding="utf-8") as f:
                    f.write(get_intl_template(kw, lang))
                count += 1
    
    all_pages = os.listdir(OUT_DIR)
    with open(SITEMAP_FILE, "w", encoding="utf-8") as s:
        s.write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n')
        for p in all_pages:
            if p.endswith(".html"):
                s.write(f'  <url><loc>https://brightlane.github.io/manychat/{p}</loc></url>\n')
        s.write('</urlset>')
    print(f"Global-6 Update: {count} pages created.")

if __name__ == "__main__":
    main()
