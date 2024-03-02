"""
Напишите однострочный генератор словаря, который принимает на вход три списка одинаковой длины:
имена str, ставка int, премия str с указанием процентов вида “10.25%”.
В результате получаем словарь с именем в качестве ключа и суммой премии в качестве значения.
Сумма рассчитывается как ставка умноженная на процент премии
"""

names = ["Александр", "Николай", "Михаил", "Олеся"]
salary = [38000, 45000, 25000, 80000]
bonus = ["10.25%", "15.10%", "10.50%", "11.90%"]


salary_bonus = {names[i]: salary[i] * float(bonus[i].replace("%", "")) / 100 for i in range(len(names))}


for i in salary_bonus.items():
    print(*i)