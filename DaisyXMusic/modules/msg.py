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

import os
from DaisyXMusic.config import SOURCE_CODE,ASSISTANT_NAME,PROJECT_NAME,SUPPORT_GROUP,UPDATES_CHANNEL
class Messages():
      START_MSG = "**Haloo.. [{}](tg://user?id={})!**\n\nSaya dapat memutar musik untuk obrolan Grup dan Chanel Anda.Silahkan tekan /help untuk melihat apa saja yang dapat saya lakukan.\n\n`-note: jangan lupa Support saya dibawah ini untuk menambahkan energi saya`."
      HELP_MSG = [
        ".",
f"""
**Haloo 👋 Selamat datang kembali di {PROJECT_NAME}

⚪️ {PROJECT_NAME} can play music in your group's voice chat as well as channel voice chats

⚪️ Assistant name >> @{ASSISTANT_NAME}\n\nClick next for instructions**
""",

f"""
**Help's and Commands Roso-Music**

**Untuk Memutar Musik di Grup💬**
1) Jadikan bot sebagai admin Grup dan diChanel jika menggunakan cmd /cplay
2) Mulai obrolan suara
3) Coba /play [nama lagu] pertama kali lakukanlah oleh admin
`*Jika Roso-Music♬ bergabung selamat nikmati musik, Jika tidak tambahkan` @RosoAssistant `ke grup Anda dan coba lagi`

**Untuk Memutar Musik diChanel:**
1) Jadikan bot sebagai admin  Chanel Anda
2) Kirim perintah /userbotjoinchannel di grup tertaut
3) Sekarang kirim cmd di grup tertaut(cth: /play [lagu])

**Commands/Perintah** 

 **♬ Memutar Lagu 🎧**

- /play [nama lagu]: Putar lagu menggunakan musik youtube
- /play [yt url/link]: Memutar lagu melalui url youtube yang diberikan
- /play [reply audio]: Memutar audio/lagu yang dibalas
- /dplay: Memutar lagu melalui deezer
- /splay: Putar lagu melalui jio saavn

**♬ Pemutaran ⏯**

- /player: Buka menu Pengaturan player
- /skip: Melewati trek lagu saat ini
- /pause: Jeda trek lagu
- /resume: Melanjutkan trek lagu yang dijeda
- /end: Menghentikan pemutaran musik
- /current: Menampilkan trek lagu yang sedang diputar
- /playlist: Menampilkan daftar putar

`*Cmd Player dan semua cmd lainnya kecuali` /play, /current dan /playlist `hanya untuk admin grup.`

`(cmd=command/perintah)`
""",
        
f"""
**=>> Channel Music Play 🛠**

⚪️ For linked group admins only:

- /cplay [song name] - play song you requested
- /cdplay [song name] - play song you requested via deezer
- /csplay [song name] - play song you requested via jio saavn
- /cplaylist - Show now playing list
- /cccurrent - Show now playing
- /cplayer - open music player settings panel
- /cpause - pause song play
- /cresume - resume song play
- /cskip - play next song
- /cend - stop music play
- /userbotjoinchannel - invite assistant to your chat

channel is also can be used instead of c ( /cplay = /channelplay )

⚪️ If you donlt like to play in linked group:

1) Get your channel ID.
2) Create a group with tittle: Channel Music: your_channel_id
3) Add bot as Channel admin with full perms
4) Add @{ASSISTANT_NAME} to the channel as an admin.
5) Simply send commands in your group.
""",

f"""
**=>> More tools 🧑‍🔧**

- /admincache: Updates admin info of your group. Try if bot isn't recognize admin
- /userbotjoin: Invite @{ASSISTANT_NAME} Userbot to your chat

**=>> Commands for Sudo Users ⚔️**

 - /userbotleaveall - remove assistant from all chats
 - /gcast <reply to message> - globally brodcast replied message to all chats
 - /pmpermit [on/off] - enable/disable pmpermit message
*Sudo Users can execute any command in any groups

"""
      ]
