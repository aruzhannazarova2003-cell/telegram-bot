import os
import random
import asyncio
import logging
from datetime import datetime
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

# Настройка логирования
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Получаем токен из переменных окружения
TOKEN = os.getenv('BOT_TOKEN', '8265474132:AAEQ8FJ0eSE-405eyuVnZvICgaw9Tbl-peg')
TOKEN = "8265474132:AAEQ8FJ0eSE-405eyuVnZvICgaw9Tbl-peg"

# Новогодние призы 🎄
NEW_YEAR_PRIZES = [
    {"name": "🎄 БРОНЬ ОСНОВЫ", "photo": "https://images.unsplash.com/photo-1606830733744-0dff58e5037f?w=800&auto=format&fit=crop"},
    {"name": "🎅 БРОНЬ ОБЯЗА", "photo": "https://images.unsplash.com/photo-1544161515-9446384c56a8?w=800&auto=format&fit=crop"},
    {"name": "🍬 +1 БАЛЛ В БАЛЛЫ", "photo": "https://images.unsplash.com/photo-1575224300306-1b8da36134ec?w=800&auto=format&fit=crop"},
    {"name": "🎁 +5 ЛИСТИКОВ", "photo": "https://images.unsplash.com/photo-1574169208507-843761a6e738?w=800&auto=format&fit=crop"},
    {"name": "✨ ВЫПЬЕМ ШАМПАНСКОЕ ЗА ТВОЕ ЗДОРОВЬЕ", "photo": "https://images.unsplash.com/photo-1513889961551-628c1e5b2c7b?w=800&auto=format&fit=crop"},
    {"name": "⛄ +15 СНЕЖИНОК", "photo": "https://images.unsplash.com/photo-1487342800493-6ea7e5c5d5c1?w=800&auto=format&fit=crop"},
    {"name": "🧦 +10 СНЕЖИНОК", "photo": "https://images.unsplash.com/photo-1482517967863-00e15c9b44be?w=800&auto=format&fit=crop"},
    {"name": "🦌 +15 ЗВЕЗД", "photo": "https://images.unsplash.com/photo-1576502200916-3808e07386a5?w=800&auto=format&fit=crop"},
    {"name": "🥂 +30 ЗВЕЗД", "photo": "https://images.unsplash.com/photo-1513297887119-d46091b24bfa?w=800&auto=format&fit=crop"},
    {"name": "🌟 ИСПОЛНЕНИЕ 1 ЖЕЛАНИЯ", "photo": "https://images.unsplash.com/photo-1547592180-85f173990554?w=800&auto=format&fit=crop"},
    {"name": "🎆 КЭПСТВО ДРУЖЕСКОГО ТУРА", "photo": "https://images.unsplash.com/photo-1533174072545-7a4b6ad7a6c3?w=800&auto=format&fit=crop"},
    {"name": "🏆 СИГНА ОТ МАРУ", "photo": "https://images.unsplash.com/photo-1513889961551-628c1e5b2c7b?w=800&auto=format&fit=crop"}
]

# Статистика
class BotStats:
    def __init__(self):
        self.start_time = datetime.now()
        self.total_spins = 0
        self.users = set()
    
    def get_uptime(self):
        uptime = datetime.now() - self.start_time
        days = uptime.days
        hours, remainder = divmod(uptime.seconds, 3600)
        minutes, seconds = divmod(remainder, 60)
        
        if days > 0:
            return f"{days} д {hours} ч"
        elif hours > 0:
            return f"{hours} ч {minutes} мин"
        else:
            return f"{minutes} мин {seconds} сек"

stats = BotStats()

# Новогодний GIF
NEW_YEAR_GIF = "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExcnp2N3dmajVhNm5qMnl4bHIzNDdrbGh2bjN1YjJ4bWI5YjI5Y3djciZlcD12MV9naWZzX3NlYXJjaCZjdD1n/8wVRtdu0M1u0AvcDVM/giphy.gif"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Новогоднее приветствие"""
    keyboard = [
        [InlineKeyboardButton("🎄 КРУТИТЬ НОВОГОДНЕЕ КОЛЕСО", callback_data="spin")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await update.message.reply_text(
        "🎅 *С НАСТУПАЮЩИМ НОВЫМ ГОДОМ!* 🎄\n\n"
        "✨ *Добро пожаловать в Новогоднее Колесо Фортуны!*\n\n"
        "❄️ *Что вас ждет:*\n"
        "• Новогодние подарки 🎁\n"
        "• Волшебные сюрпризы ✨\n"
        "• Зимние чудеса ❄️\n"
        "• Праздничное настроение 🎉\n\n"
        "⏱️ *Время вращения:* 10 секунд\n"
        "🎲 *Шанс на чудо:* 100%\n\n"
        "🎊 *Готовы к новогоднему волшебству?*",
        reply_markup=reply_markup,
        parse_mode="Markdown"
    )

async def spin_wheel(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Новогоднее вращение колеса - ИСПРАВЛЕННАЯ ВЕРСИЯ"""
    query = update.callback_query
    await query.answer()
    
    # Прячем кнопку
    await query.edit_message_text(
        "❄️ *Готовим новогоднее волшебство...*",
        parse_mode="Markdown"
    )
    
    await asyncio.sleep(1)
    
    # Отправляем GIF с подписью
    loading_msg = await query.message.reply_animation(
        NEW_YEAR_GIF,
        caption="✨ *ЭТАП 1: ЗАЖИГАЕМ ГИРЛЯНДЫ*\n\n"
                "🎄 *Украшаем колесо огнями*\n"
                "🌟 *Создаем магию праздника*",
        parse_mode="Markdown"
    )
    
    await asyncio.sleep(2)
    
    # Этап 2: Обновляем ТОЛЬКО подпись (caption)
    await loading_msg.edit_caption(
        caption="❄️ *ЭТАП 2: ПАДАЮЩИЙ СНЕГ*\n\n"
                "🌨️ *Окутываем волшебной метелью*\n"
                "⛄ *Лепим снеговика удачи*",
        parse_mode="Markdown"
    )
    
    await asyncio.sleep(2)
    
    # Этап 3
    await loading_msg.edit_caption(
        caption="🎆 *ЭТАП 3: НОВОГОДНИЕ ОГНИ*\n\n"
                "🔥 *Запускаем фейерверки*\n"
                "💫 *Освещаем путь к удаче*",
        parse_mode="Markdown"
    )
    
    await asyncio.sleep(2)
    
    # Этап 4
    await loading_msg.edit_caption(
        caption="🎊 *ЭТАП 4: БЛЕСТЯЩИЕ КОНФЕТТИ*\n\n"
                "🪩 *Засыпаем блестками волшебства*\n"
                "🎉 *Готовим праздничный салют*",
        parse_mode="Markdown"
    )
    
    await asyncio.sleep(2)
    
    # Новогодний обратный отсчет
    new_year_countdown = ["🎄 3", "🌟 2", "✨ 1", "🎉 0!"]
    
    for count in new_year_countdown:
        await loading_msg.edit_caption(
            caption=f"⏳ *НОВОГОДНИЙ ОТСЧЕТ*\n\n"
                   f"🎅 *{count}*\n"
                   f"❄️ *Готовим сюрприз!*",
            parse_mode="Markdown"
        )
        await asyncio.sleep(1)
    
    # Выбираем новогодний приз
    prize = random.choice(NEW_YEAR_PRIZES)
    prize_name = prize["name"]
    prize_photo = prize["photo"]
    
    # Новогоднее сообщение
    new_year_message = random.choice([
        "С Новым Годом! 🎄",
        "Пусть сбудутся все мечты! ✨", 
        "Удачи в новом году! 🍀",
        "Чудес и волшебства! 🎅",
        "Счастья и здоровья! ❤️",
        "Исполнения желаний! 🌟"
    ])
    
    # Удаляем сообщение с загрузкой
    await loading_msg.delete()
    
    # Новогодний эффект открытия
    effect_msg = await query.message.reply_text(
        "🎁 *РАСПАКОВЫВАЕМ ПОДАРОК...*",
        parse_mode="Markdown"
    )
    
    # Анимация открытия подарка
    for emoji in ["🎄", "🎅", "✨", "🌟", "🎁", "🎉"]:
        await effect_msg.edit_text(f"{emoji} *ОТКРЫВАЕМ...* {emoji}")
        await asyncio.sleep(0.4)
    
    await effect_msg.delete()
    
    # Отправляем новогодний приз с фото
    try:
        await query.message.reply_photo(
            photo=prize_photo,
            caption=f"🎊 *С НОВЫМ ГОДОМ!* 🎊\n\n"
                   f"✨ *НОВОГОДНИЙ ВЫИГРЫШ!* ✨\n\n"
                   f"🎁 *Вам выпало:*\n"
                   f"🏆 **{prize_name}** 🏆\n\n"
                   f"⛄ *Время волшебства:* 10 секунд\n"
                   f"🌟 *Уровень праздника:* {random.randint(85, 100)}%\n"
                   f"🎄 *Новогоднее пожелание:* {new_year_message}\n\n"
                   f"🔄 *Хотите еще новогоднего волшебства?*",
            parse_mode="Markdown",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("🎄 КРУТИТЬ СНОВА", callback_data="spin")]
            ])
        )
    except Exception as e:
        print(f"Ошибка загрузки фото: {e}")
        # Если фото не загружается, отправляем текст
        await query.message.reply_text(
            f"🎊 *С НОВЫМ ГОДОМ!* 🎊\n\n"
            f"✨ *НОВОГОДНИЙ ВЫИГРЫШ!* ✨\n\n"
            f"🎁 *Вам выпало:*\n"
            f"🏆 **{prize_name}** 🏆\n\n"
            f"⛄ *Время волшебства:* 10 секунд\n"
            f"🌟 *Уровень праздника:* {random.randint(85, 100)}%\n"
            f"🎄 *Новогоднее пожелание:* {new_year_message}\n\n"
            f"🔄 *Хотите еще новогоднего волшебства?*",
            parse_mode="Markdown",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("🎄 КРУТИТЬ СНОВА", callback_data="spin")]
            ])
        )

async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Обработчик новогодних кнопок"""
    query = update.callback_query
    
    try:
        if query.data == "spin":
            await spin_wheel(update, context)
    except Exception as e:
        print(f"Новогодняя ошибка: {e}")
        await query.message.reply_text(
            "❄️ *Ой, снежинка упала не там!*\n\n"
            "🎄 *Попробуйте еще раз загадать желание!*",
            parse_mode="Markdown",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("🎄 ПОВТОРИТЬ", callback_data="spin")]
            ])
        )

def main():
    """Запуск новогоднего бота"""
    print("🎄 ЗАПУСКАЮ НОВОГОДНЕЕ КОЛЕСО ФОРТУНЫ...")
    print("✨ Новогоднее настроение: 100%")
    print("🎅 Волшебство: включено")
    print("⛄ Время загрузки: 10 секунд")
    
    app = Application.builder().token(TOKEN).build()
    
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("newyear", start))
    app.add_handler(CallbackQueryHandler(button_handler))
    
    print("\n✅ Новогодний бот запущен!")
    print("🎁 Желаем счастливого Нового Года!")
    
    app.run_polling()

if __name__ == "__main__":
    main()
