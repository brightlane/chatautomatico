# --- GLOBAL-6 CONFIG ---
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
    
    # Handle Right-to-Left (RTL) for Arabic
    direction = "rtl" if lang_code == "ar" else "ltr"
    
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
        section{{padding:40px 20px;max-width:900px;margin:20px auto;background:#fff;border-radius:8px;}}
        .cta-button{{display:inline-block;background:#ff6600;color:#fff;padding:15px 30px;text-decoration:none;border-radius:5px;font-weight:bold;}}
        .comparison-table{{width:100%;border-collapse:collapse;margin:25px 0;}}
        .comparison-table th, .comparison-table td{{border:1px solid #ddd;padding:12px;}}
    </style>
</head>
<body>
<header>ManyChat Global 2026</header>
<section>
    <h1>ManyChat vs {comp} ({lang_code.upper()})</h1>
    <p>{data['desc']}</p>
    <div style="text-align:center;">
        <a href="https://manychat.partnerlinks.io/nwkkk7vkps17" class="cta-button">{data['cta']}</a>
    </div>
</section>
</body>
</html>"""

def main():
    # Loop through 3 keywords daily to produce 18 international pages
    for kw in keywords[:3]:
        for lang in LANGS:
            # ... generation logic ...
