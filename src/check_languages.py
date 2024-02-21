import locale

translations = {
    "en_US": [
    """=== RULES ===
--- Main menu ---
    In the main menu You'll see two buttons:
    1. Choose - choose a level.
    2. Shop - show the shop.
--- Shop ---
    1. In the shop You'll see your points and maximum amount of attempts.
    2. If You have enough points to buy attempts You will see buttons to buy one attempt (the price will change every time You buy an attempt, the price is in points).
--- Points ---
    1. You earn points when You pass a level. If the level is 11 You will earn 11 points, if the level is 15 You will earn 15 points, etc.
    2. By default You have  10 points.
--- Attempts ---
    1. You can buy attempts in the shop.
    2. By default You have 3 attempts.
--- Levels ---
    1. You can select a level in the main menu.
    2. There isn't a maximum level (there is infinity of levels).

DON'T CHANGE, RENAME OR DELETE FILES IN THIS GAME'S FOLDER. OTHERWISE THE GAME WON'T WORK.
""",
        "I've read all rules and I agree with them",
        "Shop",
        "Your points",
        "Your attempts",
        "Main screen",
        "Go back",
        "You don't have enough points to buy attempts",
        "Select",
        "Enter a level: ",
        "Level",
        "Buy +1 attempt (cost: {} {})",
        "points",
        "point",
        "points",
        "Check",
        "Enter a correct number: ",
        "Enter a correct level: ",
        "You have {} more {}. Enter a number (from 1 to {}): ",
        "attempts",
        "attempt",
        "attempts",
        "You have {} more {}. ",
        "Try bigger",
        "Try less", "Yes",
        "Next number",
        """You've lost. Your winning streak: {} {}.
Your longest winning streak: {} {}""",
        "wins",
        "win",
        "wins",
        "Restart"],

    "uk_UA": [
       """=== ПРАВИЛА ===
--- Головне меню ---
    На головному меню є дві кнопки:
    1. Обрати - обрати рівень.
    2. Магазин - показати магазин.
--- Магазин ---
    1. У магазині Ви побачите свої бали та максимальну кількість спроб.
    2. Якщо у Вас достатньо балів для покупки спроб, Ви побачите кнопки для покупки однієї спроби (ціна змінюватиметься щоразу, коли Ви купуєте спробу, ціна станоВить у балах).
--- Бали ---
    1. Ви заробляєте бали, коли проходите рівень. Якщо рівень 11, Ви отримаєте 11 балів, якщо рівень 15, Ви отримаєте 15 балів і т. д.
    2. За замовчуванням у Вас 10 балів.
--- Спроби ---
    1. Ви можете купити спроби в магазині.
    2. За замовчуванням у Вас є 3 спроби.
--- Рівні ---
    1. Ви можете обрати рівень у головному меню.
    2. Максимального рівня немає (існує нескінченність рівнів).

НЕ ЗМІНЮЙТЕ, НЕ ПЕРЕЙМЕНОВУЙТЕ ТА НЕ ВИДАЛЯЙТЕ ФАЙЛИ В ПАПЦІ З ЦІЄЮ ГРОЮ, ІНАКШЕ ГРА НЕ БУДЕ ПРАЦЮВАТИ.
""",
        "Я прочитав правила і погоджуюся з ними",
        "Магазин",
        "Кількість балів",
        "Кількість спроб",
        "Головне меню",
        "Назад",
        "Ви не маєте достатньо балів, щоб купити спроби",
        "Обрати",
        "Введіть рівень: ",
        "Рівень",
        "Купити +1 спробу (ціна: {} {})",
        "балів",
        "бал",
        "бала",
        "Перевірити",
        "Введіть коректне число: ",
        "Введіть коректний рівень: ",
        "У Вас залишилося {} {}. Введіть число (від 1 до {}): ",
        "спроб",
        "спроба",
        "спроби",
        "У Вас залишилося {} {}. ",
        "Спробуйте більше",
        "Спробуйте менше",
        "Так",
        "Наступне число",
        """Ви не вгадали. Ваша серія перемог: {} {}.
Ваша найдовша серія перемог: {} {}""",
        "перемог",
        "перемога",
        "перемоги",
        "Зіграти ще раз"
    ]
}

all_locales = locale.locale_alias
available = [l for l in translations if l.lower() in all_locales]
ukrainian_locales = [l for l in all_locales if l.lower().startswith("uk")]
russian_locales = [l for l in all_locales if (l.lower().startswith("ru_") or l.lower() == "russian" or l == "ru") and l not in ukrainian_locales]
all_locales = "\n   ".join(all_locales)
print(f"""Available locales: {', '.join(available)} ({len(translations) / len(available) * 100}%)
All available locales: 
    {all_locales}
Ukrainian locales:
    {ukrainian_locales}
Russian locales:
    {russian_locales}
""")
