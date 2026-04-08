from flask import Blueprint, request, jsonify, session
from app.models.character import Character, Stats
from app.engine.combat import Combat

game_bp = Blueprint("game", __name__, url_prefix="/api")

# Basit in-memory store (ilerleyin veritabanına taşıyın)
active_sessions = {}

@game_bp.route("/character/create", methods=["POST"])
def create_character():
    data = request.get_json()
    name = data.get("name")
    char_class = data.get("class", "warrior")

    char = Character(name=name, char_class=char_class)
    session_id = request.headers.get("X-Session-ID", "default")
    active_sessions[session_id] = char

    return jsonify({
        "message": f"Karakter oluşturuldu: {name}",
        "character": {
            "name": char.name,
            "class": char.char_class,
            "level": char.level,
            "hp": char.current_hp,
            "gold": char.gold,
        }
    })

@game_bp.route("/battle/start", methods=["POST"])
def start_battle():
    data = request.get_json()
    enemy_type = data.get("enemy", "goblin")
    session_id = request.headers.get("X-Session-ID", "default")

    char = active_sessions.get(session_id)
    if not char:
        return jsonify({"error": "Önce karakter oluştur"}), 400

    combat = Combat(char, enemy_type)
    result = combat.run()

    return jsonify(result)