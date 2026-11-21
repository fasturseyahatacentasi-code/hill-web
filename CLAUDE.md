# HILL ile Zamanda Yolculuk — Web Ekibi

Bu klasörde sen **Hill sitesinin koordinatörüsün.** Site: "HILL ile Zamanda Yolculuk" — bir Fas Tur yapımı, Türkçe + İngilizce.
Hitap: "Hilal Hanım". Sade, yapısal konuş; teknik terimi açıklamadan kullanma. Bilgisayar Windows.

- Depo: github.com/fasturseyahatacentasi-code/hill-web (herkese açık) · Test adresi: https://fasturseyahatacentasi-code.github.io/hill-web/
- Ana site (ayrı depo, ayrı çalışma alanı): `C:\Users\serda\FAS TUR\fastur-web` → fasturtravel.com. Oraya bu klasörden yazma.

## Dosya haritası
| Ne | Nerede |
|---|---|
| **Tüm metinler (TR + EN), bölümler, duraklar, videolar, Fas Tur bağlantıları** | `icerik.json` (**tek içerik dosyası**) |
| Üretici | `arac/uret.py` → `index.html` (TR), `en/index.html` (EN), `robots.txt`, `.nojekyll` |
| Stil / betik | `assets/css/hill.css` · `assets/js/hill.js` |
| Görseller | `assets/img/` (540×960 ve 720×1280 webp + jpg yedek) |

**`index.html` ve `en/index.html` elle düzenlenmez**; `icerik.json` değişir, sonra `py arac\uret.py`.
Önizleme: bu klasörde `py -m http.server 8010` → `http://localhost:8010/`.

## Çalışma düzeni
1. İş öncesi GitHub Desktop'ta "Fetch origin / Pull origin".
2. Değişikliği yap → üreticiyi çalıştır → tarayıcıda bilgisayar ve telefon genişliğinde bak (ekran görüntüsüyle kontrol et).
3. Hilal Hanım'a göster; **onay verince** commit + push (commit mesajı "Claude: ..."). `--force` asla.

## Video ekleme ("Hill videolarını çek")
YouTube'daki Hill videolarını `icerik.json > "videolar"` listesine ekle: `{"youtubeId": "...", "baslik_tr": "...", "baslik_en": "..."}`.
Kanal adresi `icerik.json > "youtube"` (boşsa Hilal Hanım'a sor). Video olunca "Çok yakında" etiketleri kendiliğinden kalkar.

## Kesin kurallar
1. **Hill kurgu bir yapay zekâ karakteridir** (Hilal Hanım, 19.11.2026). "Hill bir yapay zekâ karakteridir…" notu sitede kalır.
2. **Görsellerde ✦ / "Veo" işareti olmaz.** Köşe işareti varsa temizle ya da kırp; yazı/logo çizdirme.
3. **Tarih ve olay bilgisi uydurulmaz.** Kaynak: `C:\Users\serda\OneDrive\Desktop\YZ Film Projelerim\04-Hill\Senaryo\00-Yonetmen-Notu.md` (onaylı) ve `Kaynaklar/`. Belirsiz bilgi "rivayete göre" yazılır.
4. **İngilizce metinler çeviri taslağıdır**; Hilal Hanım onaylayana kadar öyle kalır.
5. 🔒 **Görsel koruması — Hilal Hanım açıkça söylemeden kaldırılmaz, gevşetilmez:** `robots.txt` (yapay zekâ + görsel botları engelli), her sayfada `<meta name="robots" content="noai, noimageai, noimageindex">`, `hill.css` + `hill.js` "GÖRSEL KORUMA" (sağ tık/sürükleme kapalı), alt bilgide telif notu.
6. Vaat dili yok ("garanti", "en ucuz", sahte aciliyet). Fiyat/tarih bu sitede yazılmaz; turlar için Fas Tur'a bağlantı verilir.
7. Depo herkese açık: şifre, anahtar, müşteri bilgisi girmez.
8. Alan adı, DNS, hesap/ücret işlemleri yalnız Hilal Hanım'ındır; sen adım adım tarif edersin.

## Bekleyen işler (21.11.2026)
- İngilizce metinlerin onayı · bölüm tarihlerinin kaynakla teyidi · Mısır/Roma/Londra durakları senaryoda yok, Hilal Hanım'a sorulacak · kendi alan adı (isteğe bağlı).
- Aşçı Oğuz ileride kendi sitesine geçecek (şapkalı yeni görünüm bekleniyor).
