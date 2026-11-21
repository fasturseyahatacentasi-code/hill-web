"""HILL ile Zamanda Yolculuk — site üreticisi.
icerik.json'dan Türkçe (index.html) ve İngilizce (en/index.html) sayfaları, robots.txt ve .nojekyll üretir.
Çalıştırma:  py arac\\uret.py   (Mac: python3 arac/uret.py)
"""
import html, json, os

KOK = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
V = json.load(open(os.path.join(KOK, 'icerik.json'), encoding='utf-8'))


def e(x):
    return html.escape(str(x or ''), quote=True)


def resim(ad, k, alt='', w=540, h=960, cls=''):
    return (f'<picture><source type="image/webp" srcset="{k}assets/img/{ad}.webp">'
            f'<img{f" class={chr(34)}{cls}{chr(34)}" if cls else ""} src="{k}assets/img/{ad}.jpg" alt="{e(alt)}" width="{w}" height="{h}" loading="lazy"></picture>')


SAAT = ('<svg viewBox="0 0 200 200" aria-hidden="true"><circle cx="100" cy="100" r="96"/><circle cx="100" cy="100" r="80" class="ince"/><g>'
        + ''.join(f'<line x1="100" y1="6" x2="100" y2="{16 if i % 5 == 0 else 11}" transform="rotate({i * 6} 100 100)"/>' for i in range(60))
        + '</g><g>' + ''.join(f'<text x="100" y="32" transform="rotate({i * 30} 100 100)">{r}</text>'
                              for i, r in enumerate(['XII', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX', 'X', 'XI'])) + '</g></svg>')


def sayfa(d, k, diger_adres):
    T = V[d]
    vids = V.get('videolar') or []
    yakinda = '' if vids else f'<span class="rozet">{e(T["yakinda"])}</span>'
    seri = T['bolumler'] + [{'cag': T['bugunCag'], 'sehir': T['bugunSehir'], 'simdi': True}]
    rota = ''.join(f'<li class="{"simdi" if b.get("simdi") else ""}"><b>{e(b["cag"])}</b><span>{e(b["sehir"])}</span></li>' for b in seri)
    bolumler = ''.join(
        f'<article class="bolum"><div class="bolum-g">{resim(b["gorsel"], k, T["ad"] + " · " + b["sehir"])}<span class="bolum-no">{e(T["bolumEtiket"])} {b["no"]}</span></div>'
        f'<div class="bolum-ic"><h3>{e(b["sehir"])} · {e(b["cag"])}</h3><p>{e(b["metin"])}</p><p class="imza">“{e(b["imza"])}”</p>'
        f'<div class="bolum-alt">{yakinda}<a href="{e(V["fasturTurlar"])}" target="_blank" rel="noopener">{e(b["sehir"])} {e(T["bugunLink"])} →</a></div></div></article>'
        for b in T['bolumler'])
    if vids:
        videolar = '<div class="videolar">' + ''.join(
            f'<figure class="video"><div class="oran"><iframe src="https://www.youtube-nocookie.com/embed/{e(v["youtubeId"])}?rel=0" title="{e(v.get("baslik_" + d) or v.get("baslik_tr", ""))}" loading="lazy" '
            f'allow="accelerometer; encrypted-media; gyroscope; picture-in-picture" allowfullscreen referrerpolicy="strict-origin-when-cross-origin"></iframe></div>'
            f'<figcaption>{e(v.get("baslik_" + d) or v.get("baslik_tr", ""))}</figcaption></figure>' for v in vids) + '</div>'
    else:
        videolar = f'<p class="bos">{e(T["videoBos"])}</p>'
    duraklar = ''.join(f'<figure class="durak">{resim(x["gorsel"], k, T["ad"] + " · " + x["ad"])}<figcaption><b>{e(x["ad"])}</b><span>{e(T["hazirlaniyor"])}</span></figcaption></figure>' for x in T['duraklar'])
    M = T['menu']
    return f'''<!doctype html>
<html lang="{T["lang"]}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{e(T["baslik"])}</title>
<meta name="description" content="{e(T["aciklama"])}">
<meta name="robots" content="noai, noimageai, noimageindex"><!-- 🔒 görsel koruması (Hilal Hanım); yalnız onun açık talimatıyla kaldırılır -->
<link rel="alternate" hreflang="tr" href="{"./" if d == "tr" else "../"}"><link rel="alternate" hreflang="en" href="{"en/" if d == "tr" else "./"}">
<link rel="icon" href="{k}assets/img/fastur-simge.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,500;0,9..144,600;1,9..144,500&family=Nunito+Sans:wght@400;600;700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{k}assets/css/hill.css">
</head>
<body>
<div class="yildizlar" aria-hidden="true"></div>
<header class="ust"><div class="kap">
<a class="marka" href="./">HILL<small>{e(T["altBaslik"])}</small></a>
<nav aria-label="Menü"><a href="#seri">{e(M["seri"])}</a><a href="#rota">{e(M["rota"])}</a><a href="#bolumler">{e(M["bolumler"])}</a><a href="#izle">{e(M["videolar"])}</a><a href="#duraklar">{e(M["duraklar"])}</a></nav>
<a class="dil" href="{diger_adres}" hreflang="{"en" if d == "tr" else "tr"}">{e(T["dil"])}</a>
</div></header>
<main>
<section class="giris" id="seri"><div class="kap">
<div class="portal"><div class="saat">{SAAT}</div>
<div class="afis">{resim("hill-kapak", k, T["ad"], 720, 1280)}<span class="afis-ust">{e(T["ust"])}</span>
<div class="afis-alt"><h1>{e(T["ad"])}</h1><p class="afis-slogan">{e(T["altBaslik"])}</p>{yakinda}</div></div></div>
<div class="tanitim"><p class="motto">{e(T["motto"])}</p><p>{e(T["tanitim"])}</p></div>
</div></section>
<section class="blok" id="rota"><div class="kap"><h2>{e(T["rotaBaslik"])}</h2><ol class="zaman">{rota}</ol></div></section>
<section class="blok" id="bolumler"><div class="kap"><h2>{e(T["bolumlerBaslik"])}</h2><div class="bolumler">{bolumler}</div>
<div class="bugun"><div class="bugun-g">{resim("hill-cag-bugun", k, T["ad"])}</div><div><span class="etiket">{e(T["bugun"]["etiket"])}</span><h2>{e(T["bugun"]["baslik"])}</h2><p>{e(T["bugun"]["metin"])}</p>
<a class="dugme" href="{e(V["fasturTurlar"])}" target="_blank" rel="noopener">{e(T["bugun"]["link"])}</a></div></div></div></section>
<section class="blok" id="izle"><div class="kap"><h2>{e(T["videoBaslik"])}</h2>{videolar}</div></section>
<section class="blok" id="duraklar"><div class="kap"><h2>{e(T["duraklarBaslik"])}</h2><div class="duraklar">{duraklar}</div></div></section>
</main>
<footer class="alt"><div class="kap">
<a class="yapim" href="{e(V["fasturAdres"])}" target="_blank" rel="noopener"><img src="{k}assets/img/fastur-simge.svg" alt="" width="40" height="40"><span>{e(T["yapim"])}<small>{e(T["fasturLink"])} →</small></span></a>
<p>{e(T["yzNot"])}</p><p class="telif">© Fas Tur · {e(T["telif"])}</p>
</div></footer>
<script src="{k}assets/js/hill.js"></script>
</body>
</html>
'''


ROBOTS = """# 🔒 Görsel koruması (Hilal Hanım): yapay zekâ ve görsel arama botları engelli
User-agent: GPTBot
Disallow: /
User-agent: ClaudeBot
Disallow: /
User-agent: Google-Extended
Disallow: /
User-agent: CCBot
Disallow: /
User-agent: PerplexityBot
Disallow: /
User-agent: Bytespider
Disallow: /
User-agent: Googlebot-Image
Disallow: /
User-agent: *
Content-Signal: ai-train=no, ai-input=no
Disallow: /assets/img/
"""


def yaz(yol, metin):
    p = os.path.join(KOK, yol)
    os.makedirs(os.path.dirname(p), exist_ok=True)
    open(p, 'w', encoding='utf-8', newline='\n').write(metin)


yaz('index.html', sayfa('tr', '', 'en/'))
yaz('en/index.html', sayfa('en', '../', '../'))
yaz('robots.txt', ROBOTS)
yaz('.nojekyll', '')
print('Tamam: index.html (TR), en/index.html (EN), robots.txt')
