# utils/lang_helper.py

from flask import request
from utils.translations import translations

def get_translation(key, lang=None):
    """Dil ve anahtar ile mesaj döndür."""
    lang = lang or request.headers.get("lang", "en")  # Varsayılan dil İngilizce
    return translations.get(lang, translations["en"]).get(key, key)