# Daisyxmusic (Telegram bot project )
# Copyright (C) 2021  Inukaasith

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

import logging
from handlers.msg import Messages as tr
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from config import ASSISTANT_NAME,PROJECT_NAME,SUPPORT_GROUP,UPDATES_CHANNEL,BOT_USERNAME
logging.basicConfig(level=logging.INFO)

@Client.on_message(
    filters.command("start")
    & filters.private
    & ~ filters.edited
)
async def start_(client: Client, message: Message):
    await message.reply_text(
        f"""<b>Hello Friend, {message.from_user.first_name} π
Saya Alexa, Saya akan membantumu memutar music di Voice Chat Telegram Groups & Channel, dengan fitur-fitur yang menarik.
\nβKetik /help untuk melihat panduan pemakaiannya
βKetik /start untuk memuat ulang.
\nβββββββββββββββββββββββββββββββββββ
\nπΊππππ πππππ πππππ ππππ, ππππ πππππ πππππ πππππ πππππ πππππππ ππππ. π·πππππππ πππππππ πππππππ/ππππππππππ πππππ πππππ ππππ
\nβββββββββββββββββββββββββββββββββββ
\nβ Manage by :  [OWNER](https://t.me/justthetech)  
β Support dengan doa aja guys! Thanks!
β NB : Maaf jika ada kekurangan didalam bot ini
</b>""",

# Edit Yang Seharusnya Lu Edit Aja:D
# Tapi Jangan di Hapus Special Thanks To nya Yaaa :'D

        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(

                        "βοΈ α΄α΄α΄Κα΄Κα΄α΄Ι΄ α΄α΄ Ι’Κα΄Κ βοΈ", url=f"https://t.me/alexagroup_bot?startgroup=true")
                ],
                [
                    InlineKeyboardButton(

                        "β α΄α΄α΄α΄α΄α΄", url=f"https://t.me/robotprojectx"), 

                    InlineKeyboardButton(

                        "α΄α΄‘Ι΄α΄Κ β", url=f"https://t.me/justthetech")
                ],
                [
                    InlineKeyboardButton(
                        "βοΈ α΄α΄κ°α΄α΄Κ α΄α΄ΚΙͺΙ΄α΄α΄Κ βοΈ", url="https://telegra.ph/ROBOT-04-23-2"
                    )
                ]
            ]
        ),
        reply_to_message_id=message.message_id
        )

@Client.on_message(filters.private & filters.incoming & filters.command(['help']))
def _help(client, message):
    client.send_message(chat_id = message.chat.id,
        text = tr.HELP_MSG[1],
        parse_mode="markdown",
        disable_web_page_preview=True,
        disable_notification=True,
        reply_markup = InlineKeyboardMarkup(map(1)),
        reply_to_message_id = message.message_id
    )

help_callback_filter = filters.create(lambda _, __, query: query.data.startswith('help+'))

@Client.on_callback_query(help_callback_filter)
def help_answer(client, callback_query):
    chat_id = callback_query.from_user.id
    disable_web_page_preview=True
    message_id = callback_query.message.message_id
    msg = int(callback_query.data.split('+')[1])
    client.edit_message_text(chat_id=chat_id,    message_id=message_id,
        text=tr.HELP_MSG[msg],    reply_markup=InlineKeyboardMarkup(map(msg))
    )


def map(pos):
    if(pos==1):
        button = [
            [InlineKeyboardButton('β α΄α΄‘Ι΄α΄Κ', url=f"https://t.me/justthetech"), 
             InlineKeyboardButton('α΄α΄α΄α΄α΄α΄ β', url=f"https://t.me/robotprojectx")
            ], 
            [InlineKeyboardButton(text = 'ππππ βΆ', callback_data = "help+2")]
                 ] 
    elif(pos==len(tr.HELP_MSG)-1):
        url = f"https://t.me/{SUPPORT_GROUP}"
        button = [
                    [InlineKeyboardButton('β α΄α΄‘Ι΄α΄Κ', url=f"https://t.me/justthetech"), 
                     InlineKeyboardButton('α΄α΄α΄α΄α΄α΄ β', url=f"https://t.me/robotprojectx")
                    ], 
                    [InlineKeyboardButton(text = 'β π½πΌπΎπ', callback_data = f"help+{pos-1}")] 
                 ]
    else:
        button = [
            [
                InlineKeyboardButton(text = 'β π½πΌπΎπ', callback_data = f"help+{pos-1}"),
                InlineKeyboardButton(text = 'ππππ βΆ', callback_data = f"help+{pos+1}")
            ],
        ]
    return button


@Client.on_message(
    filters.command("start")
    & filters.group
    & ~ filters.edited
)
async def start(client: Client, message: Message):
    await message.reply_text(
        "**π΄ {PROJECT_NAME} is online**",
        reply_markup=InlineKeyboardMarkup(
            [   
                [

                        InlineKeyboardButton(

                        "β α΄α΄α΄α΄α΄α΄ β", url=f"https://t.me/robotprojectx"

                    )

                ]
            ]
        )
    )


@Client.on_message(
    filters.command("help")
    & filters.group
    & ~ filters.edited
)
async def help(client: Client, message: Message):
    await message.reply_text(
        """**Klik Tombol dibawah untuk Melihat Cara Menggunakan Bot**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [

                    InlineKeyboardButton(

                        "βοΈ α΄α΄κ°α΄α΄Κ α΄α΄ΚΙͺΙ΄α΄α΄Κ βοΈ", url=f"https://t.me/robotxmusic_bot?start"

                    )

                ]
            ]
        ),
    )  


@Client.on_message(
    filters.command("reload")
    & filters.group
    & ~ filters.edited
)
async def reload(client: Client, message: Message):
    await message.reply_text("""β Bot **berhasil dimulai ulang!**\n\nβ’ **Daftar admin** telah **diperbarui**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(

                        "β α΄α΄α΄α΄α΄α΄ β", url=f"https://t.me/robotprojectx"

                    )
                ]
            ]
        )
   )

