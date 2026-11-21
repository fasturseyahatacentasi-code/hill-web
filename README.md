# HILL ile Zamanda Yolculuk — web sitesi

Bir Fas Tur yapımı. Türkçe (`index.html`) ve İngilizce (`en/index.html`).

## Nasıl güncellenir
1. Metin, bölüm, durak ya da video değişikliği yalnız **`icerik.json`** dosyasında yapılır.
2. Sonra üretici çalıştırılır: `py arac\uret.py` (Mac: `python3 arac/uret.py`).
3. Bakmak için: bu klasörde `py -m http.server 8010`, tarayıcıda `http://localhost:8010/`.

## Video ekleme
`icerik.json` → `"videolar"` listesine her video için bir satır:
`{"youtubeId": "ABC123xyz", "baslik_tr": "Bölüm 1 · Fes", "baslik_en": "Episode 1 · Fez"}`
Video eklenince "Çok yakında" etiketleri kendiliğinden kalkar.

## Kurallar
- Hill bir yapay zekâ karakteridir; bu not sitede kalır.
- Görsellerde ✦ / "Veo" işareti olmaz; kopyalama koruması (robots.txt, `noai` etiketi, sağ tık kapalı) Hilal Hanım söylemeden kaldırılmaz.
- Tarih ve olay bilgileri kaynakla teyit edilir; belirsiz bilgi "rivayete göre" yazılır.
- İngilizce metinler çeviri taslağıdır; Hilal Hanım onayı bekliyor.
- Kaynak: `YZ Film Projelerim\04-Hill\Senaryo\00-Yonetmen-Notu.md` (onaylı yönetmen notu, 11.11.2026).
