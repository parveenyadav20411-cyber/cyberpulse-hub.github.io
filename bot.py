import logging
import urllib.parse
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    CallbackQueryHandler,
    MessageHandler,
    ContextTypes,
    filters
)

BOT_TOKEN = "8720521721:AAECw3a-sWSqLGbOH3ODjuWFGGTdIZ3lPu8"
DRIVE_LINK = "https://drive.google.com/drive/u/0/mobile/folders/1unpmYt_y8O8anjPu_n3BlOENXCu3ayw-"
UPI_ID = "8178152316@fam"
SUPPORT_USERNAME = "Akira_verse"

used_utrs = set()

# 3D Ghost Hyper-Realistic Banner & Glitch VFX
GHOST_3D_POSTER = "https://images.unsplash.com/photo-1509198397868-475647b2a1e5?auto=format&fit=crop&w=1000&q=80"
GHOST_VFX_GIF = "https://media.giphy.com/media/Y4v7Yg5Isuh0eXkO7b/giphy.gif"

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)

def get_main_menu():
    upi_intent = f"upi://pay?pa={UPI_ID}&pn=AkiraStore&am=29&cu=INR&tn=150kReelsBundle"
    keyboard = [
        [
            InlineKeyboardButton("⚡ Pay ₹29 (Direct UPI)", url=upi_intent),
            InlineKeyboardButton("📷 Scan 3D QR", callback_data="show_qr")
        ],
        [
            InlineKeyboardButton("📂 Vault Categories", callback_data="categories"),
            InlineKeyboardButton("⚙️ How It Works", callback_data="how_it_works")
        ],
        [
            InlineKeyboardButton("💀 Akira Verse Support", callback_data="support")
        ]
    ]
    return InlineKeyboardMarkup(keyboard)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    name = user.first_name if user else "Warrior"

    # Send 3D Glitch VFX first
    try:
        await context.bot.send_animation(
            chat_id=update.effective_chat.id,
            animation=GHOST_VFX_GIF,
            caption="⚡ *AKIRA VERSE VAULT SYSTEM ACTIVATED* ⚡",
            parse_mode="Markdown"
        )
    except Exception as e:
        logging.error(f"Media error: {e}")

    welcome_text = (
        f"🔥 *WELCOME {name.upper()} | 150,000+ ULTRA HD REELS*\n\n"
        "⚡ *Quality:* 1080p 60FPS | Watermark-Free | Ready-to-Post\n"
        "💎 *Limited Drop:* ~~₹499~~ **₹29 Only** (Lifetime Drive Access)\n\n"
        "Niche buttons se Categories check karo ya direct access lo!"
    )

    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=welcome_text,
        parse_mode="Markdown",
        reply_markup=get_main_menu()
    )
  
