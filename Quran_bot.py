import telebot
import requests
import os
import json

# Bot tokenini kiriting
BOT_TOKEN = '6809565231:AAF33NNKAxoegb55OtI82TFZQbxlhYZMtRw'
bot = telebot.TeleBot(BOT_TOKEN)

# Suralar ma'lumotlari
SURA_INFO = {
    1: {"name": "Al-Fotiha", "total_verses": 7},
    2: {"name": "Al-Baqara", "total_verses": 286},
    3: {"name": "Oli Imron", "total_verses": 200},
    4: {"name": "An-Niso", "total_verses": 176},
    5: {"name": "Al-Moida", "total_verses": 120},
    6: {"name": "Al-An'om", "total_verses": 165},
    7: {"name": "Al-A'rof", "total_verses": 206},
    8: {"name": "Al-Anfol", "total_verses": 75},
    9: {"name": "At-Tavba", "total_verses": 129},
    10: {"name": "Yunus", "total_verses": 109},
    11: {"name": "Hud", "total_verses": 123},
    12: {"name": "Yusuf", "total_verses": 111},
    13: {"name": "Ar-Ra'd", "total_verses": 43},
    14: {"name": "Ibrohim", "total_verses": 52},
    15: {"name": "Al-Hijr", "total_verses": 99},
    16: {"name": "An-Nahl", "total_verses": 128},
    17: {"name": "Al-Isro", "total_verses": 111},
    18: {"name": "Al-Kahf", "total_verses": 110},
    19: {"name": "Maryam", "total_verses": 98},
    20: {"name": "Toha", "total_verses": 135},
    21: {"name": "Al-Anbiyo", "total_verses": 112},
    22: {"name": "Al-Haj", "total_verses": 78},
    23: {"name": "Al-Mu'minun", "total_verses": 118},
    24: {"name": "An-Nur", "total_verses": 64},
    25: {"name": "Al-Furqon", "total_verses": 77},
    26: {"name": "Ash-Shu'aro", "total_verses": 227},
    27: {"name": "An-Naml", "total_verses": 93},
    28: {"name": "Al-Qasas", "total_verses": 88},
    29: {"name": "Al-Ankabut", "total_verses": 69},
    30: {"name": "Ar-Rum", "total_verses": 60},
    31: {"name": "Luqmon", "total_verses": 34},
    32: {"name": "As-Sajda", "total_verses": 30},
    33: {"name": "Al-Ahzob", "total_verses": 73},
    34: {"name": "Saba", "total_verses": 54},
    35: {"name": "Fotir", "total_verses": 45},
    36: {"name": "Yosin", "total_verses": 83},
    37: {"name": "As-Soffat", "total_verses": 182},
    38: {"name": "Sod", "total_verses": 88},
    39: {"name": "Az-Zumar", "total_verses": 75},
    40: {"name": "G'ofir", "total_verses": 85},
    41: {"name": "Fussilat", "total_verses": 54},
    42: {"name": "Ash-Shuro", "total_verses": 53},
    43: {"name": "Az-Zuxruf", "total_verses": 89},
    44: {"name": "Ad-Duxon", "total_verses": 59},
    45: {"name": "Al-Josiya", "total_verses": 37},
    46: {"name": "Al-Ahqof", "total_verses": 35},
    47: {"name": "Muhammad", "total_verses": 38},
    48: {"name": "Al-Fath", "total_verses": 29},
    49: {"name": "Al-Hujurot", "total_verses": 18},
    50: {"name": "Qof", "total_verses": 45},
    51: {"name": "Az-Zoriyat", "total_verses": 60},
    52: {"name": "At-Tur", "total_verses": 49},
    53: {"name": "An-Najm", "total_verses": 62},
    54: {"name": "Al-Qamar", "total_verses": 55},
    55: {"name": "Ar-Rahmon", "total_verses": 78},
    56: {"name": "Al-Voqia", "total_verses": 96},
    57: {"name": "Al-Hadid", "total_verses": 29},
    58: {"name": "Al-Mujodala", "total_verses": 22},
    59: {"name": "Al-Hashr", "total_verses": 24},
    60: {"name": "Al-Mumtahana", "total_verses": 13},
    61: {"name": "As-Saff", "total_verses": 14},
    62: {"name": "Al-Jumu'a", "total_verses": 11},
    63: {"name": "Al-Munofiqun", "total_verses": 11},
    64: {"name": "At-Tag'obun", "total_verses": 18},
    65: {"name": "At-Taloq", "total_verses": 12},
    66: {"name": "At-Tahrim", "total_verses": 12},
    67: {"name": "Al-Mulk", "total_verses": 30},
    68: {"name": "Al-Qalam", "total_verses": 52},
    69: {"name": "Al-Haqqa", "total_verses": 52},
    70: {"name": "Al-Ma'arij", "total_verses": 44},
    71: {"name": "Nuh", "total_verses": 28},
    72: {"name": "Al-Jinn", "total_verses": 28},
    73: {"name": "Al-Muzzammil", "total_verses": 20},
    74: {"name": "Al-Muddassir", "total_verses": 56},
    75: {"name": "Al-Qiyomat", "total_verses": 40},
    76: {"name": "Al-Insan", "total_verses": 31},
    77: {"name": "Al-Mursalot", "total_verses": 50},
    78: {"name": "An-Naba", "total_verses": 40},
    79: {"name": "An-Nazi'at", "total_verses": 46},
    80: {"name": "Abasa", "total_verses": 42},
    81: {"name": "At-Takvir", "total_verses": 29},
    82: {"name": "Al-Infitor", "total_verses": 19},
    83: {"name": "Al-Mutoffifin", "total_verses": 36},
    84: {"name": "Al-Inshiqoq", "total_verses": 25},
    85: {"name": "Al-Buruj", "total_verses": 22},
    86: {"name": "At-Toriq", "total_verses": 17},
    87: {"name": "Al-A'la", "total_verses": 19},
    88: {"name": "Al-G'oshiya", "total_verses": 26},
    89: {"name": "Al-Fajr", "total_verses": 30},
    90: {"name": "Al-Balad", "total_verses": 20},
    91: {"name": "Ash-Shams", "total_verses": 15},
    92: {"name": "Al-Layl", "total_verses": 21},
    93: {"name": "Ad-Duha", "total_verses": 11},
    94: {"name": "Ash-Sharh", "total_verses": 8},
    95: {"name": "At-Tin", "total_verses": 8},
    96: {"name": "Al-Alaq", "total_verses": 19},
    97: {"name": "Al-Qadr", "total_verses": 5},
    98: {"name": "Al-Bayyina", "total_verses": 8},
    99: {"name": "Az-Zalzala", "total_verses": 8},
    100: {"name": "Al-Adiyat", "total_verses": 11},
    101: {"name": "Al-Qori'a", "total_verses": 11},
    102: {"name": "At-Takasur", "total_verses": 8},
    103: {"name": "Al-Asr", "total_verses": 3},
    104: {"name": "Al-Humaza", "total_verses": 9},
    105: {"name": "Al-Fil", "total_verses": 5},
    106: {"name": "Quraysh", "total_verses": 4},
    107: {"name": "Al-Ma'un", "total_verses": 7},
    108: {"name": "Al-Kavsar", "total_verses": 3},
    109: {"name": "Al-Kofirun", "total_verses": 6},
    110: {"name": "An-Nasr", "total_verses": 3},
    111: {"name": "Al-Masad", "total_verses": 5},
    112: {"name": "Al-Ixlos", "total_verses": 4},
    113: {"name": "Al-Falaq", "total_verses": 5},
    114: {"name": "An-Nos", "total_verses": 6}
}


# Start buyrug'i uchun handler
@bot.message_handler(commands=['start'])
def send_welcome(message):
    user_name = message.from_user.first_name
    welcome_text = f"""Assalomu alaykum, {user_name}!

Qur'oni Karim oyatlarini ko'rish uchun quyidagi formatlardan foydalaning:

1️⃣ Bitta oyat uchun:
   Sura:Oyat (masalan: 2:255)

2️⃣ Bir nechta oyat uchun:
   Sura:Oyat1-Oyat2 (masalan: 2:255-257)

3️⃣ Guruhda foydalanish uchun:
   /quron Sura:Oyat (masalan: /quron 2:255)

ℹ️ Suralar haqida ma'lumot olish uchun:
   /info"""

    bot.reply_to(message, welcome_text)


# Info buyrug'i uchun handler
@bot.message_handler(commands=['info'])
def send_info(message):
    info_text = "Qur'oni Karim suralari:\n\n"
    for sura_num, info in SURA_INFO.items():
        info_text += f"{sura_num}. {info['name']} - {info['total_verses']} oyat\n"

    # Uzun xabarni bo'lib yuborish
    if len(info_text) > 4096:
        for x in range(0, len(info_text), 4096):
            bot.reply_to(message, info_text[x:x + 4096])
    else:
        bot.reply_to(message, info_text)


# Guruh uchun /quron buyrug'i
@bot.message_handler(commands=['quron'])
def handle_quran_command(message):
    try:
        # Buyruqdan keyin kelgan qismni olish
        command_parts = message.text.split()
        if len(command_parts) != 2:
            bot.reply_to(message, "Noto'g'ri format. Masalan: /quron 2:255")
            return

        verse_ref = command_parts[1]
        send_verses(message, verse_ref)
    except Exception as e:
        bot.reply_to(message, "Xatolik yuz berdi. To'g'ri format: /quron sura:oyat")


# Oddiy xabarlar uchun handler
@bot.message_handler(func=lambda message: ':' in message.text and not message.text.startswith('/'))
def handle_verse_request(message):
    send_verses(message, message.text)


def send_verses(message, verse_ref):
    try:
        # Sura va oyat raqamlarini ajratib olish
        sura_part, verse_part = verse_ref.split(':')
        sura = int(sura_part)

        # Bir nechta oyat uchun tekshirish
        if '-' in verse_part:
            start_verse, end_verse = map(int, verse_part.split('-'))
            verses_range = range(start_verse, end_verse + 1)
        else:
            verses_range = [int(verse_part)]

        for verse_num in verses_range:
            # Arabcha matnni olish
            arabic_url = f"https://api.alquran.cloud/v1/ayah/{sura}:{verse_num}/ar.asad"
            arabic_response = requests.get(arabic_url)
            arabic_data = arabic_response.json()

            # O'zbekcha tarjimani olish
            uzbek_url = f"https://api.alquran.cloud/v1/ayah/{sura}:{verse_num}/uz.sodik"
            uzbek_response = requests.get(uzbek_url)

            if arabic_response.status_code == 200:
                arabic_text = arabic_data['data']['text']

                try:
                    uzbek_data = uzbek_response.json()
                    uzbek_text = uzbek_data['data']['text']
                except:
                    uzbek_text = "Tarjima yuklanmadi"

                # Sura nomi va oyat raqamini qo'shish
                sura_name = SURA_INFO[sura]["name"] if sura in SURA_INFO else f"{sura}-sura"
                verse_info = f"\n\n📍 {sura_name}, {verse_num}-oyat"

                # Rasmni olish va yuborish
                image_url = f"https://everyayah.com/data/images_png/{sura}_{verse_num}.png"
                response = requests.get(image_url)

                if response.status_code == 200:
                    image_path = f"ayah_{sura}_{verse_num}.png"
                    with open(image_path, 'wb') as f:
                        f.write(response.content)

                    # Avval rasmni yuborish
                    with open(image_path, 'rb') as photo:
                        bot.send_photo(message.chat.id, photo)

                    # Keyin matnlarni yuborish
                    text_message = f"🔹 {arabic_text}\n\n🔸 {uzbek_text}{verse_info}"
                    bot.send_message(message.chat.id, text_message)

                    # Rasmni o'chirish
                    os.remove(image_path)

            else:
                bot.reply_to(message, f"Bunday oyat topilmadi: {sura}:{verse_num}")

    except ValueError:
        bot.reply_to(message, "Noto'g'ri format. Masalan: 2:255 yoki 2:255-257")
    except Exception as e:
        print(f"Xatolik: {str(e)}")
        bot.reply_to(message, "Xatolik yuz berdi. Iltimos qaytadan urinib ko'ring.")


# Botni ishga tushirish
bot.polling()
