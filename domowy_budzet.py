import random
import datetime
from openpyxl import Workbook

currencies = {"PLN": 0.7, "EUR": 0.2, "USD": 0.1}

family_members = ["Anna", "Piotr", "Kasia", "Marek"]

categories = ["Jedzenie", "Transport", "Mieszkanie", "Zdrowie", "Edukacja", "Rozrywka", "Inne"]
income_sources = ["Pensja", "Premia", "Zwrot podatku", "Inwestycje"]

vendors = ["Biedronka", "Lidl", "Orlen", "ZUS", "Urząd Skarbowy", "Netflix", "Amazon"]

wb = Workbook()
ws = wb.active
ws.title = "Budżet domowy"

ws.append(["Data", "Kwota", "Waluta", "Domownik", "Kategoria", "Kontrahent"])

start_day = datetime.date(2024, 1, 1)

for day in range((datetime.date.today() - start_day).days):
    date = start_day + datetime.timedelta(days=day)
    for _ in range(random.randint(1, 5)):
        currency = random.choices([*currencies], weights=currencies.values())
        if random.random() < 0.9:
            category = random.choice(categories)
            amount = round(random.uniform(10, 600), 2)
            vendor = random.choice(vendors)
            person = random.choice(family_members)
        else:
            category = random.choice(income_sources)
            amount = round(random.uniform(1000, 5000), 2)
            vendor = "-"
            person = random.choice(family_members)
        ws.append([date.strftime("%Y-%m-%d"), amount, currency[0], person, category, vendor])

wb.save("domowy_budzet.xlsx")
