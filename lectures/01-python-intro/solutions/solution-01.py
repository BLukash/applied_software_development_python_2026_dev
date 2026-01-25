"""
Рішення вправи 1: Програма-привітання
"""
from datetime import datetime

name = input("Як тебе звати? ")
birth_year = int(input("Який рік твого народження? "))
current_year = datetime.now().year
age = current_year - birth_year

print(f"Привіт, {name}! Тобі {age} років.")
