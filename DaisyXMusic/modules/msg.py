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

🍺**Roso-Music dapat memutar musik di obrolan suara grup Anda serta obrolan suara Channel**

🤖**Nama asisten ⊵** @RosoAssistant\n\n`klik tombol dibawah untuk melihat instruksi selanjutnya`
""",

f"""
**Help's and Commands Roso-Music**

**Untuk Memutar Musik di Grup💬**:
1) Jadikan bot sebagai admin Grup dan diChanel jika menggunakan cmd /cplay
2) Mulai obrolan suara
3) Coba /play [nama lagu] pertama kali lakukanlah oleh admin
`*Jika Roso-Music♬ bergabung selamat nikmati musik, Jika tidak tambahkan` @RosoAssistant `ke grup Anda dan coba lagi`

**Untuk Memutar Musik diChanel🔊**:
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
**⊵ Untuk memutar Musik di Chanel 🔊**

👤**Cmd khusus untuk admin grup tertaut:**

- /cplay [nama lagu] : putar lagu yang Anda minta
- /cdplay [nama lagu] : putar lagu yang Anda minta melalui deezer
- /csplay [nama lagu] : putar lagu yang Anda minta melalui jio saavn
- /cplaylist : Tampilkan daftar yang sedang diputar
- /cccurrent : Tampilkan sekarang diputar
- /cplayer : buka panel pengaturan pemutar musik
- /cpause : jeda pemutaran lagu
- /cresume : melanjutkan pemutaran lagu
- /cskip : putar lagu berikutnya
- /cend : hentikan pemutaran musik
- /userbotjoinchannel : undang asisten ke obrolan Anda

`channel juga bisa digunakan sebagai pengganti` /cplay = /channelplay

🔉**Jika Anda tidak suka memutar musik di grup tertaut:**

1) Dapatkan ID Chanel Anda.
2) Buat grup dengan judul: Channel Music:(id_chanel_anda)
3) Tambahkan bot sebagai admin Chanel dengan izin penuh
4) Tambahkan @RosoAssistant ke chanel sebagai admin.
5) Cukup kirim perintah di grup Anda.
""",

f"""
**⊵  Pengaturan tambahan📍**

- /admincache: Memperbarui info admin grup Anda. Coba jika bot tidak mengenali admin
- /userbotjoin: Undang @RosoAssistant Userbot ke dalam obrolan Anda

"""
      ]
