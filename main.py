import discord
import random
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

@bot.command()
async def hello(ctx):
    """Przywitanie Bota"""
    await ctx.send('Jestem **Ekobot** pomogę ci zmniejszyć ilośc wytwarzanych odpadów!')

@bot.command()
async def eko_start(ctx):
    """Eko porady"""
    eko = random.choice(porady)
    await ctx.send(eko)

@bot.command()
async def pomoc(ctx):
    """Pomoc w komendach"""
    for command in bot.commands:
        await ctx.send(f' ${command.name}: {command.help}')
        
bot.run("")
