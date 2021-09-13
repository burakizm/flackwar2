# (C) supun-maduraga my best friend for his project on call-music-plus

from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, Chat, CallbackQuery
from helpers.decorators import authorized_users_only
from config import BOT_NAME, BOT_USERNAME, OWNER_NAME, GROUP_SUPPORT, UPDATES_CHANNEL, ASSISTANT_NAME
from handlers.play import cb_admin_check


@Client.on_callback_query(filters.regex("cbstart"))
async def cbstart(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""<b>✨ **Welcome user, i'm {query.message.from_user.mention}** \n
💭 **[{BOT_NAME}](https://t.me/{BOT_USERNAME}) telegram sesli sohbetlerinde müzik çalabilir !**

💡 **Tüm bot komutlarını ve nasıl çalıştıklarını aşağıdaki butona tıklayarak öğrenin. » 📚 komut butonu!**

❓ **Bot hakkında tüm bilgi ve özellikler için /help**
</b>""",
        reply_markup=InlineKeyboardMarkup(
            [ 
                [
                    InlineKeyboardButton(
                        "➕ Gruba Ekle ➕", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")
                ],[
                    InlineKeyboardButton(
                        "❓ beni nasıl kullanabilirsin", callback_data="cbhowtouse")
                ],[
                    InlineKeyboardButton(
                         "📚 komutlar", callback_data="cbcmds"
                    ),
                    InlineKeyboardButton(
                        "💝 iletişim", url=f"https://t.me/{OWNER_NAME}")
                ],[
                    InlineKeyboardButton(
                        "👥 Official Group", url=f"https://t.me/{GROUP_SUPPORT}"
                    ),
                    InlineKeyboardButton(
                        "📣 Official Channel", url=f"https://t.me/{UPDATES_CHANNEL}")
                ],[
                    InlineKeyboardButton(
                        "🌐 tag ve dc botu", url="https://t.me/flackwardev")
                ],[
                    InlineKeyboardButton(
                        "🧪Grubunuza özel bot kurmak için 🧪", url="https://t.me/flackwardev"
                    )
                ]
            ]
        ),
     disable_web_page_preview=True
    )


@Client.on_callback_query(filters.regex("cbhelp"))
async def cbhelp(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""<b>💡 Merhaba, yardım menüsüne hoş geldiniz!</b>

bu menüde birkaç kullanılabilir komut menüsü açabilirsiniz, her komut menüsünde ayrıca her komutun kısa bir açıklaması vardır.

⚡ __tarafından geliştirildi {BOT_NAME} A.I__""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "📚 Basit komutlar", callback_data="cbbasic"
                    ),
                    InlineKeyboardButton(
                        "📕 geliştirilmiş komutlar", callback_data="cbadvanced"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "📘 admin komutu", callback_data="cbadmin"
                    ),
                    InlineKeyboardButton(
                        "📗 geliştirici komutları", callback_data="cbsudo"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "📙 sahip komutları", callback_data="cbowner"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "📔 eğlence", callback_data="cbfun"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "🏡 yardıma geri dön", callback_data="cbguide"
                    )
                ]
            ]
        )
    )


@Client.on_callback_query(filters.regex("cbbasic"))
async def cbbasic(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""<b>🏮işte temel komutlar</b>

🎧 [ GRUP VC CMD ]

/play (şarkı adı) - youtube'dan şarkı çal
/ytp (şarkı adı) - doğrudan youtube'dan şarkı çal
/stream (sesi yanıtla) - ses dosyasını kullanarak şarkıyı çal
/playlist - listedeki şarkıyı sıraya koyar
/song (şarkı adı) - youtube'dan şarkı indir
/search (video adı) - youtube'dan ayrıntılı video arama
/vsong (video adı) - ayrıntılı olarak youtube'dan video indir
/lyric - (şarkı adı) şarkı sözü kazıyıcı
/vk (şarkı adı) - satır içi moddan şarkı indir

🎧 [ KANAL VC CMD ]

/cplay - kanal sesli sohbetinde müzik akışı
/cplayer - şarkıyı akışta göster
/cpause - müzik akışını duraklat
/cresume - duraklatılan akışı devam ettir
/cskip - akışı sonraki şarkıya atla
/cend - müzik akışını sonlandır
/admincache - yönetici önbelleğini yenile
/ubjoinc - asistanı kanalınıza katılması için davet edin

⚡ __tararından {BOT_NAME} A.I__""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🏡 geri", callback_data="cbhelp"
                    )
                ]
            ]
        )
    )


@Client.on_callback_query(filters.regex("cbadvanced"))
async def cbadvanced(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""<b>işte gelişmiş komutlar</b>

/start (grupta) - botun canlı durumunu görün
/ yeniden yükle - botu yeniden yükle ve yönetici listesini yenile
/cache - yönetici önbelleğini yenile
/ping - botun ping durumunu kontrol edin
/uptime - botun çalışma süresi durumunu kontrol edin

⚡ __tarafından geliştirildi {BOT_NAME} A.I__""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🏡 geri", callback_data="cbhelp"
                    )
                ]
            ]
        )
    )


@Client.on_callback_query(filters.regex("cbadmin"))
async def cbadmin(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""<b>🏮 işte yönetici komutları</b>

/player - müzik çalma durumunu göster
/pause - müzik akışını duraklat
/resume - müziğin duraklatıldığını yeniden başlat
/atla - sonraki şarkıya atla
/end - müzik akışını durdur
/userbotjoin - asistanı grubunuza katılmaya davet edin
/auth - müzik botunu kullanmak için yetkili kullanıcı
/deauth - müzik botu kullanmak için yetkisiz
/control - oynatıcı ayarları panelini aç
/delcmd (açık | kapalı) - del cmd özelliğini etkinleştir / devre dışı bırak
/musicplayer (açık / kapalı) - grubunuzdaki müzik çaları devre dışı bırakın / etkinleştirin
/b ve /tb (ban / geçici ban) - gruptaki kullanıcı kalıcı veya geçici olarak yasaklandı
/ub - yasaklanmamış kullanıcı için gruptan yasaklandınız
/m ve /tm (sessiz / geçici sessiz) - gruptaki kalıcı veya geçici olarak sessize alınmış kullanıcının sesini kapat
/um - grupta sessize aldığınız kullanıcının sesini açmak için

⚡ __tarafından geliştirildi {BOT_NAME} A.I__""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🏡 geri", callback_data="cbhelp"
                    )
                ]
            ]
        )
    )


@Client.on_callback_query(filters.regex("cbsudo"))
async def cbsudo(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""<b><b>🏮 işte sudo komutları</b>

/userbotleaveall - asistana tüm gruptan ayrılmasını emreder
/gcast - asistandan bir yayın mesajı gönderir
/stats - bot istatistiğini göster
/rmd - indirilen tüm dosyaları kaldır
/clean - Tüm ham dosyaları kaldır

⚡ __tarafından geliştirildi {BOT_NAME} A.I__""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🏡 GERİ", callback_data="cbhelp"
                    )
                ]
            ]
        )
    )


@Client.on_callback_query(filters.regex("cbowner"))
async def cbowner(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""<b>🏮 geliştirici komutları</b>

/stats - bot istatistiğini göster
/yayın - bottan bir yayın mesajı gönder
/block (kullanıcı kimliği - süre - neden) - kullanıcıyı botunuzu kullanması için engelle
/unblock (kullanıcı kimliği - nedeni) - botunuzu kullandığı için engellediğiniz kullanıcının engellemesini kaldırın
/blocklist - botunuzu kullanmaktan dolayı engellenen kullanıcı listesini gösterir
📝 not: Bu botun sahip olduğu tüm komutlar, istisnasız olarak botun sahibi tarafından yürütülebilir.

⚡ __tarafından geliştirildi {BOT_NAME} A.I__""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🏡 geri", callback_data="cbhelp"
                    )
                ]
            ]
        )
    )


@Client.on_callback_query(filters.regex("cbfun"))
async def cbfun(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""<b>🏮 eğlence komutları</b>

/chika - kendini kontrol et
/wibu - kendini kontrol et
/asupan - kendini kontrol et
/truth - kendini kontrol et
/dare - kendin için kontrol et

⚡ __Powered by {BOT_NAME} A.I__""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🏡 geri", callback_data="cbhelp"
                    )
                ]
            ]
        )
    )


@Client.on_callback_query(filters.regex("cbguide"))
async def cbguide(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""❓ BU BOT NASIL KULLANILIR:

1.) önce beni grubunuza ekleyin.
2.) sonra beni yönetici olarak terfi ettir ve anonim yönetici hariç tüm izinleri ver.
3.) @{ASSISTANT_NAME} grubunu ekleyin veya onu davet etmek için /userbotjoin yazın.
4.) Müzik çalmaya başlamadan önce sesli sohbeti açın.

⚡ __Tarafından geliştirildi {BOT_NAME} A.I__""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "📚 komut listesi", callback_data="cbhelp"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "🗑 kapat", callback_data="close"
                    )
                ]
            ]
        )
    )


@Client.on_callback_query(filters.regex("close"))
async def close(_, query: CallbackQuery):
    await query.message.delete()


@Client.on_callback_query(filters.regex("cbback"))
@cb_admin_check
async def cbback(_, query: CallbackQuery):
    await query.edit_message_text(
        "**💡 here is the control menu of bot :**",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "⏸ durdur", callback_data="cbpause"
                    ),
                    InlineKeyboardButton(
                        "▶️ devam", callback_data="cbresume"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "⏩ atla", callback_data="cbskip"
                    ),
                    InlineKeyboardButton(
                        "⏹ bitir", callback_data="cbend"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "⛔ anti spam", callback_data="cbdelcmds"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "🛄 grup ayarları", callback_data="cbgtools"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "🗑 kapat", callback_data="close"
                    )
                ]
            ]
        )
    )


@Client.on_callback_query(filters.regex("cbgtools"))
@cb_admin_check
@authorized_users_only
async def cbgtools(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""<b>özellik bilgisi budur:</b>

💡 Özellik: Bu özellik, grubunuzdaki kullanıcıları yasaklayabilen, sessize alabilen, yasağı kaldırabilen, sesini açabilen işlevleri içerir.

ayrıca grubunuzdaki üyeler için yasaklama ve sessize alma cezaları için bir süre belirleyebilirsiniz, böylece belirtilen süre ile cezadan kurtulabilirler.

❔ kullanım:

1️⃣ Kullanıcıyı grubunuzdan yasaklayın ve geçici olarak yasaklayın:
   » /b kullanıcı adı/mesaj yasağını kalıcı olarak yanıtla yazın
   » /tb kullanıcı adı/mesajı yanıtla/süre yazın kullanıcıyı geçici olarak banlayın
   » /ub kullanıcı adı/yanıtla kullanıcı yasağını kaldır

2️⃣ Grubunuzdaki kullanıcıyı sessize alın ve geçici olarak sessize alın:
   » /m kullanıcı adı/mesajı yanıtla yaz, kalıcı olarak sessize al
   » /tm kullanıcı adı/mesajı yanıtla/süre yazın, kullanıcıyı geçici olarak sessize alın
   » kullanıcının sesini açmak için /um kullanıcı adı/mesajı yanıtla yazın

📝 not: cmd /b, /tb ve /ub, kullanıcıyı grubunuzdan yasaklama/yasağı kaldırma işlevidir, oysa /m, /tm ve /um, grubunuzdaki kullanıcıyı sessize almak/açmak için kullanılan komutlardır.

⚡ __Powered by {BOT_NAME} A.I__""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🏡 Geri dön", callback_data="cbback"
                    )
                ]
            ]
        )
    )


@Client.on_callback_query(filters.regex("cbdelcmds"))
@cb_admin_check
@authorized_users_only
async def cbdelcmds(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""<b>bu bir özellik bilgilendirmesidir :</b>
        
**💡 özellik:** Gruptaki tüm spamları engellee !

❔ kullanım:**

 1️⃣ to turn on feature:
     » type `/delcmd on`
    
 2️⃣ to turn off feature:
     » type `/delcmd off`
      
⚡ __Powered by {BOT_NAME} A.I__""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🏡 geri dön", callback_data="cbback"
                    )
                ]
            ]
        )
    )


@Client.on_callback_query(filters.regex("cbcmds"))
async def cbhelps(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""<b>💡 Merhabaa yardım menüsüne hoş geldiniz !</b>

**bu menüde birkaç kullanılabilir komut menüsü açabilirsiniz, her komut menüsünde ayrıca her komutun kısa bir açıklaması vardır. **

⚡ __Powered by {BOT_NAME} A.I__""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "📚 basit komutlar", callback_data="cbbasic"
                    ),
                    InlineKeyboardButton(
                        "📕 geliştirilmiş komutlar", callback_data="cbadvanced"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "📘 Admin komutları", callback_data="cbadmin"
                    ),
                    InlineKeyboardButton(
                        "📗 Sudo kullanıcıları", callback_data="cbsudo"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "📙 geliştiriciler için", callback_data="cbowner"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "📔 eğlence :)", callback_data="cbfun"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "🏡 GERİ DÖN", callback_data="cbstart"
                    )
                ]
            ]
        )
    )


@Client.on_callback_query(filters.regex("cbhowtouse"))
async def cbguides(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""❓ BU BOTU NASIL KULLANALIR:

1.) önce beni grubunuza ekleyin.
2.) sonra beni yönetici olarak terfi ettir ve anonim yönetici hariç tüm izinleri ver.
3.) @{ASSISTANT_NAME} grubunu ekleyin veya onu davet etmek için /userbotjoin yazın.
4.) Müzik çalmaya başlamadan önce sesli sohbeti açın.

⚡ __Powered by {BOT_NAME} A.I__""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🏡 GERİ DÖN", callback_data="cbstart"
                    )
                ]
            ]
        )
    )