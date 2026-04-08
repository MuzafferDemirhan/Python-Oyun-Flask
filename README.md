#  Python Web RPG

> Tarayıcıda oynanan, Python backend'li bir rol yapma oyunu.

![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python)
![Flask](https://img.shields.io/badge/Flask-or-FastAPI-green)
![License](https://img.shields.io/badge/license-MIT-lightgrey)
![Status](https://img.shields.io/badge/status-in%20development-yellow)

---

##  Özellikler

- Karakter oluşturma (Savaşçı, Büyücü, Haydut)
- Sıra tabanlı savaş sistemi
- Seviye atlama ve XP sistemi
- Düşman çeşitliliği (Goblin, Orc, İskelet, Ejder)
- Kritik vuruş ve savuşturma mekaniği
- Altın ve envanter sistemi

##  Proje Yapısı

```
rpg-game/
├── app/
│   ├── models/       # Karakter, düşman, item modelleri
│   ├── routes/       # API endpoint'leri
│   └── engine/       # Savaş ve dünya motoru
├── templates/        # HTML arayüz
├── database/         # SQLite DB
└── tests/            # Testler
```

##  Kurulum

```bash
# Repoyu klonla
git clone https://github.com/KULLANICI_ADIN/rpg-game.git
cd rpg-game

# Virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Bağımlılıkları yükle
pip install -r requirements.txt

# Çalıştır
# Flask:
python main.py

# FastAPI:
uvicorn main:app --reload
```

Tarayıcıda aç: `http://localhost:5000`

##  API Endpoints

| Method | Endpoint | Açıklama |
|--------|----------|----------|
| `POST` | `/api/character/create` | Yeni karakter oluştur |
| `POST` | `/api/battle/start` | Savaş başlat |
| `GET`  | `/api/world/locations` | Mevcut konumları listele |

**Örnek istek:**
```bash
curl -X POST http://localhost:5000/api/character/create \
  -H "Content-Type: application/json" \
  -H "X-Session-ID: abc123" \
  -d '{"name": "Aragorn", "class": "warrior"}'
```

##  Testleri Çalıştır

```bash
pytest tests/ -v
```

##  Kullanılan Teknolojiler

| Katman | Teknoloji |
|--------|-----------|
| Backend | Flask / FastAPI |
| ORM | SQLAlchemy |
| Doğrulama | Pydantic |
| Veritabanı | SQLite (geliştirme), PostgreSQL (prod) |
| Frontend | Vanilla JS + HTML/CSS |

##  Roadmap

- [x] Temel savaş sistemi
- [x] Karakter modeli
- [ ] Envanter sistemi
- [ ] Skill ağacı
- [ ] Çok oyunculu (WebSocket)
- [ ] Harita sistemi

##  Lisans

MIT — dilediğin gibi kullanabilirsin.
