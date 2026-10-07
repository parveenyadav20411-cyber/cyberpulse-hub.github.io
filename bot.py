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

# ================= CONFIGURATION =================
BOT_TOKEN = "8720521721:AAECw3a-sWSqLGbOH3ODjuWFGGTdIZ3lPu8"
DRIVE_LINK = "https://drive.google.com/drive/u/0/mobile/folders/1unpmYt_y8O8anjPu_n3BlOENXCu3ayw-"
UPI_ID = "8178152316@fam"
SUPPORT_USERNAME = "Akira_verse"

# Fraud Prevention Track
used_utrs = set()

# Media Elements: 3D Scary Ghost Glitch & Phonk Audio Track
GHOST_SCARE_GIF = "https://media.giphy.com/media/Y4v7Yg5Isuh0eXkO7b/giphy.gif"
PHONK_TRACK_URL = "https://cdn.pixabay.com/download/audio/2023/06/13/audio_49c3b87a8b.mp3?filename=brazilian-phonk-153372.mp3"

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
            InlineKeyboardButton("🎧 Play Phonk Vibe", callback_data="play_phonk"),
            InlineKeyboardButton("📂 Vault Categories", callback_data="categories")
        ],
        [
            InlineKeyboardButton("⚙️ How It Works", callback_data="how_it_works"),
            InlineKeyboardButton("💀 Akira Support", callback_data="support")
        ]
    ]
    return InlineKeyboardMarkup(keyboard)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    name = user.first_name if user else "Warrior"
    chat_id = update.effective_chat.id

    # 1. Send 3D Ghost Scare Jump Animation
    try:
        await context.bot.send_animation(
            chat_id=chat_id,
            animation=GHOST_SCARE_GIF,
            caption="⚠️ *CRITICAL WARNING: AKIRA VERSE SYSTEM ACTIVATED* ⚠️",
            parse_mode="Markdown"
        )
    except Exception as e:
        logging.error(f"GIF error: {e}")

    # 2. Drop Phonk Track in Chat
    try:
        await context.bot.send_audio(
            chat_id=chat_id,
            audio=PHONK_TRACK_URL,
            title="Akira Drift Phonk (Montagem)",
            performer="Akira Verse Audio",
            caption="🎧 *NOW PLAYING: AKIRA BASS DROP* 💀"
        )
    except Exception as e:
        logging.error(f"Audio error: {e}")

    # 3. Main Welcome Interface
    welcome_text = (
        f"👁️ *WELCOME TO THE SHADOWS, {name.upper()}...*\n\n"
        "🔥 *150,000+ ULTRA HD REELS BUNDLE* (No Watermark)\n"
        "⚡ *Format:* 1080p 60FPS | AI, Sigma, Phonk, Supercars & Luxury\n\n"
        "💎 *Limited Drop Deal:* ~~₹499~~ **₹29 Only** (Lifetime Drive Access)\n\n"
        "Niche diye buttons se Instant QR Scan karein ya UPI se pay karein!"
    )

    await context.bot.send_message(
        chat_id=chat_id,
        text=welcome_text,
        parse_mode="Markdown",
        reply_markup=get_main_menu()
    )

async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == "show_qr":
        upi_string = f"upi://pay?pa={UPI_ID}&pn=AkiraStore&am=29&cu=INR&tn=150kReelsBundle"
        encoded_upi = urllib.parse.quote(upi_string)
        qr_url = f"https://api.qrserver.com/v1/create-qr-code/?size=350x350&data={encoded_upi}"

        qr_caption = (
            "📷 *INSTANT SCAN & PAY ₹29*\n\n"
            f"• UPI ID: `{UPI_ID}`\n"
            "• Amount: *₹29*\n\n"
            "Payment complete hone ke baad transaction ka *12-digit UTR / Ref No.* yahan send karo."
        )
        back_markup = InlineKeyboardMarkup([[InlineKeyboardButton("⬅️ Back to Menu", callback_data="home")]])
        await query.message.reply_photo(photo=qr_url, caption=qr_caption, parse_mode="Markdown", reply_markup=back_markup)

    elif query.data == "play_phonk":
        try:
            await query.message.reply_audio(
                audio=PHONK_TRACK_URL,
                title="Akira Verse Phonk",
                performer="Akira Beats",
                caption="🔊 *Turn up the volume!*"
            )
        except Exception as e:
            await query.message.reply_text("Audio buffering error...")

    elif query.data == "categories":
        cat_text = (
            "📁 *150K+ VAULT CATEGORIES:*\n\n"
            "• 🧠 *AI Cyber & Futuristic Tech*\n"
            "• 🏎️ *Supercars, Mansions & Luxury*\n"
            "• 💀 *Hard Phonk & Gym Motivation*\n"
            "• 📈 *Crypto, Money & Millionaire Mindset*\n"
            "• 🎌 *Anime 4K Edits & Aesthetics*\n\n"
            "⚡ Sabhi videos bina kisi watermark ke ready hain."
        )
        back_markup = InlineKeyboardMarkup([[InlineKeyboardButton("⬅️ Back to Menu", callback_data="home")]])
        await query.message.edit_text(cat_text, parse_mode="Markdown", reply_markup=back_markup)

    elif query.data == "how_it_works":
        steps_text = (
            "⚙️ *HOW TO GET ACCESS:*\n\n"
            "1. 'Pay ₹29' dabao ya QR scan karke ₹29 bhejo.\n"
            "2. Payment receipt ka *12-digit UTR* copy karo.\n"
            "3. UTR chat me send karte hi bot Drive unlock kar dega."
        )
        back_markup = InlineKeyboardMarkup([[InlineKeyboardButton("⬅️ Back to Menu", callback_data="home")]])
        await query.message.edit_text(steps_text, parse_mode="Markdown", reply_markup=back_markup)

    elif query.data == "support":
        supp_text = (
            "💀 *AKIRA VERSE SUPPORT*\n\n"
            f"👤 Admin: @{SUPPORT_USERNAME}\n"
            "⚡ Active Status: Instant Reply"
        )
        back_markup = InlineKeyboardMarkup([[InlineKeyboardButton("⬅️ Back to Menu", callback_data="home")]])
        await query.message.edit_text(supp_text, parse_mode="Markdown", reply_markup=back_markup)

    elif query.data == "home":
        await query.message.edit_text(
            "🔥 *150,000+ ULTRA HD REELS BUNDLE*\n"
            "💰 *Deal:* ₹29 Only (Lifetime Access)\n\n"
            "Niche diye buttons se options select karein:",
            parse_mode="Markdown",
            reply_markup=get_main_menu()
        )

async def handle_utr(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.strip()

    if len(text) == 12 and text.isdigit():
        if text in used_utrs:
            await update.message.reply_markdown(
                "❌ *ACCESS DENIED!*\n"
                "Yeh UTR number already claim ho chuka hai. Fake entry block kar di gayi hai."
            )
            return

        used_utrs.add(text)

        success_msg = (
            "⚡ *PAYMENT VERIFIED | VAULT UNLOCKED!* ⚡\n\n"
            f"Txn Ref: `{text}`\n"
            "Aapka 150,000+ Reels Bundle ready hai:\n\n"
            f"🔗 *Google Drive Link:* [CLICK HERE TO ACCESS]({DRIVE_LINK})\n\n"
            f"Support: @{SUPPORT_USERNAME}"
        )
        await update.message.reply_markdown(success_msg, disable_web_page_preview=True)

    else:
        await update.message.reply_markdown(
            "⚠️ *INVALID UTR FORMAT!*\n\n"
            "Kripya sirf valid *12-digit UPI UTR number* bhejein jo payment receipt par hota hai."
        )

if __name__ == "__main__":
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("buy", start))
    app.add_handler(CallbackQueryHandler(button_handler))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_utr))

    print("Akira Verse Bot is live with 3D VFX & Phonk Audio...")
    app.run_polling()
        
