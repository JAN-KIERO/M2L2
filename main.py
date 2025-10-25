import discord
import random
from wherebin import eko
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

C1 = "Zacznij od noszenia własnej butelki na wodę 💧"
C2 = "Noś wielorazową torbę na zakupy zamiast plastikowej 🛍"
C3 = "Zamień jednorazowe słomki na metalowe lub silikonowe 🍹"
C4 = "Kup jedzenie na wagę i używaj własnych pojemników 🥜"
C5 = "Używaj wielorazowych kubków na wynos zamiast papierowych ☕"
C6 = "Kiedy możesz — wybieraj produkty bez zbędnego opakowania 📦"
C7 = "Segreguj śmieci w domu — to prosty nawyk ♻"
C8 = "Oddawaj niepotrzebne ubrania zamiast wyrzucać 👕"
C9 = "Naprawiaj zepsute rzeczy zamiast od razu kupować nowe 🔧"
C10 = "Kupuj kosmetyki w większych opakowaniach lub w kostce 🧼"
C11 = "Wybieraj produkty z recyklingu (papier, plastik) 📝"
C12 = "Zrób listę przed zakupami, żeby nie marnować jedzenia 📝"
C13 = "Zamień jednorazowe ręczniki papierowe na szmatki 🧽"
C14 = "Kup lokalne produkty — krótszy transport = mniej emisji 🚜"
C15 = "Używaj własnych sztućców zamiast plastikowych 🍴"
C16 = "Kupuj odzież z drugiej ręki — vintage jest fajne 👗"
C17 = "Zbieraj deszczówkę do podlewania roślin (jeśli możesz) 🌧"
C18 = "Wypożycz narzędzia lub sprzęt zamiast kupować rzadko używane 🔩"
C19 = "Unikaj produktów jednorazowych do higieny — wybierz wielorazowe 🩸"
C20 = "Planuj posiłki, żeby nie wyrzucać jedzenia 🍽"
C21 = "Zamień folię aluminiową na pojemniki wielorazowe 🥡"
C22 = "Kupuj owoce i warzywa luzem, nie w plastikowych tackach 🍎"
C23 = "Używaj aplikacji do sprzedaży/oddawania rzeczy zamiast wyrzucać 📱"
C24 = "Zrób własne ekologiczne środki czystości z octu i sody 🧴"
C25 = "Ogranicz drukowanie — zapisuj notatki elektronicznie 🖥"
C26 = "Zaangażuj znajomych w eko-wyzwanie — razem łatwiej 👥"
C27 = "Kupuj baterie wielokrotnego ładowania zamiast jednorazowych 🔋"
C28 = "Wybieraj produkty z minimalną ilością plastiku przy pakowaniu 🧴"
C29 = "Przekazuj książki i gry znajomym zamiast kupować nowe 📚"
C30 = "Zbieraj i kompostuj resztki organiczne, jeśli masz taką możliwość 🥕"
C31 = "Wybieraj produkty z certyfikatami ekologicznymi (gdzie to możliwe) 🌱"
C32 = "Używaj pralki i zmywarki pełnymi ładunkami, oszczędzasz wodę i energię 🧺"
C33 = "Kupuj mniej — zastanów się przed każdym impulsywnym zakupem 🤔"
C34 = "Używaj szkła zamiast plastiku do przechowywania żywności 🍯"
C35 = "Zmieniaj żarówki na energooszczędne LED — dłużej działają 💡"
C36 = "Noś przy sobie mały zestaw wielorazowych sztućców i słomki 🧳"
C37 = "Wymieniaj się ubraniami z przyjaciółmi zamiast ciągle kupować 👚"
C38 = "Wybieraj ekologiczne opakowania na prezent — np. materiałowe 🎁"
C39 = "Stawiaj na jakość — lepsze rzeczy rzadziej trzeba wyrzucać 🛠"
C40 = "Szanuj i naprawiaj elektronikę — odłączaj ładowarki gdy nie używasz 🔌"
C41 = "Kupuj próbniki kosmetyków wielorazowo lub w ekonomicznych opakowaniach 💄"
C42 = "Unikaj produktów z mikroplastikiem (np. niektóre peelingi) 🧴"
C43 = "Zapisuj resztki jedzenia i twórz z nich nowe potrawy (zero waste cooking) 🥗"
C44 = "Ucz się i dziel się wiedzą — im więcej osób, tym większy efekt 🗣"
C45 = "Wybieraj napoje w szkle lub kartonie zamiast w plastikowych butelkach 🥤"
C46 = "Zamień jednorazowe torebki na silikonowe woreczki wielokrotnego użytku 🥪"
C47 = "Organizuj wymiany rzeczy na serwerze/ze znajomymi (swap party) 🔁"
C48 = "Kupuj w hurtowniach lub sklepach zero waste, jeśli masz dostęp 🏪"
C49 = "Używaj programów lojalnościowych oferujących eko-nagrody (jeśli są) 🎟"
C50 = "Świętuj swoje małe sukcesy — każde zmniejszenie odpadów się liczy 🎉"

porady = [
    C1, C2, C3, C4, C5, C6, C7, C8, C9, C10,
    C11, C12, C13, C14, C15, C16, C17, C18, C19, C20,
    C21, C22, C23, C24, C25, C26, C27, C28, C29, C30,
    C31, C32, C33, C34, C35, C36, C37, C38, C39, C40,
    C41, C42, C43, C44, C45, C46, C47, C48, C49, C50 ]


@bot.event
async def on_ready():
    print(f'Zalogowaliśmy się jako {bot.user}')

    channel_id = 1421409966090354728
    channel = bot.get_channel(channel_id)
    
@bot.command()
async def eko_start(ctx):
    """Eko porady"""
    porada = random.choice(porady)
    await ctx.send(porada)

@bot.command()
async def eko_bin(ctx, *, wordls = ""):
    """Pomoc w segregacji odpadów"""
    await ctx.send(eko(wordls))

@bot.command()
async def pomoc(ctx):
    """Pomoc w komendach"""
    for command in bot.commands:
        await ctx.send(f' ${command.name}: {command.help}')

@bot.command()
async def help_bin(ctx):
    await ctx.send("- **♻️ Jeśli wpiszesz `eko_bin <JAKIŚ ODPAD>`, CHATBOT wskaże Ci odpowiedni pojemnik 🗑️. Możesz pytać o takie odpady jak:**")
    await ctx.send("- 📰 GAZETA, CZASOPISMO, ULOTKA REKLAMOWA, KSIĄŻKA 📖, ZESZYT, KARTKA PAPIERU 📄, TORBA PAPIEROWA 🛍️, PUDEŁKO KARTONOWE 📦, TEKTURA FALISTA, ROLKA PO PAPIERZE TOALETOWYM, ROLKA PO RĘCZNIKU PAPIEROWYM, KOPERTA ✉️, PAPIER DO PAKOWANIA PREZENTÓW 🎁, BILET AUTOBUSOWY 🎟️, WYDRUK KOMPUTEROWY, PUDEŁKO PO BUTACH 👟, KARTONOWY WYKŁADZINA NA JAJKA 🥚")
    await ctx.send("- 🍾 BUTELKA PO PIWIE, BUTELKA PO WINIE 🍷, SŁOIK PO DŻEMIE, SŁOIK PO KONCENTRACIE POMIDOROWYM 🍅, BUTELKA PO SOKU, SŁOIK PO OGÓRKACH, OPAKOWANIE PO PERFUMACH, BUTELKA PO OLIWIE, PUSTY SŁOIK PO KAWIE ROZPUSZCZALNEJ ☕, BUTELKA PO WODZIE MINERALNEJ")
    await ctx.send("- 🥤 PLASTIKOWA BUTELKA PO WODZIE, PLASTIKOWA BUTELKA PO NAPOJU, KARTON PO MLEKU 🥛, KARTON PO SOKU, PUSZKA PO NAPOJU, PUSZKA PO KONSERWIE 🥫, FOLIA ALUMINIOWA, PLASTIKOWY KUBECZEK PO JOGURCIE, OPAKOWANIE PO SERKU WIEJSKIM, PLASTIKOWA NAKRĘTKA OD BUTELKI, METALOWA ZAKRĘTKA OD SŁOIKA, OPAKOWANIE PO CHIPSACH 🥔")
    await ctx.send("- 🛍️ PLASTIKOWA TORBA NA ZAKUPY, FOLIA BĄBELKOWA, OPAKOWANIE PO CHEMII GOSPODARCZEJ 🧼, BUTELKA PO SZAMPONIE, OPAKOWANIE PO MYDLE W PŁYNIE, DONICZKA PLASTIKOWA, PLASTIKOWE OPAKOWANIE PO OWOCACH 🍓, STYROPIAN OPAKOWANIOWY, OPAKOWANIE PO MAŚLE/MARGARYNIE 🧈, KAPSEL OD PIWA, PUSTA TUBKA PO PAŚCIE DO ZĘBÓW, WIADRO PLASTIKOWE 🪣, ZABAWKA 🧸")
    await ctx.send("- 🌱 OBIERKI Z ZIEMNIAKÓW, RESZTKI WARZYW 🥕, OGRYZEK JABŁKA 🍎, SKÓRKA OD BANANA 🍌, FUSY PO KAWIE, TOREBKA PO HERBACIE EKSPRESOWEJ 🍵, RESZTKI HERBATY LIŚCIASTEJ, SKORUPKI JAJEK, ZWIĘDŁE KWIATY 🥀, SKOSZONA TRAWA, LIŚCIE 🍃, DROBNE GAŁĘZIE 🪵, RESZTKI OWOCÓW, PESTKI Z ARBUZA 🍉, TROCINY, NIEZJEDZONY CHLEB 🍞")
    await ctx.send("- 🍖 RESZTKI MIĘSA, KOŚCI, ZUŻYTY RĘCZNIK PAPIEROWY, PARAGON FISKALNY, ZUŻYTA CHUSTECZKA HIGIENICZNA, WACIK KOSMETYCZNY, PATYCZEK DO USZU, ZUŻYTA PIELUCHA JEDNORAZOWA, PODPASKA/TAMPON, ROZBITY TALERZ CERAMICZNY 🍽️, POTŁUCZONA SZKLANKA, STARE LUSTRO, ŻWIREK DLA KOTA 🐈, ODCHODY ZWIERZĘCE 🐾")
    await ctx.send("- 🚬 WOREK Z ODKURZACZA, NIEDOPAŁEK PAPIEROSA, ZUŻYTA ŻARÓWKA 💡, SKÓRZANY PASEK, GĄBKA DO MYCIA NACZYŃ, ZUŻYTA SZCZOTECZKA DO ZĘBÓW, ZUŻYTY OLEJ PO SMAŻENIU, POPIÓŁ Z KOMINKA 🔥, OPAKOWANIE PO LEKACH 💊, ZDJĘCIA FOTOGRAFICZNE 📷, UBRANIA NIENADAJĄCE SIĘ DO NOSZENIA 👕")

bot.run("")
