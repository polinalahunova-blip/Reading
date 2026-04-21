days = ["Понеділок", "Вівторок", "Середа", "Четвер", "П'ятниця", "Субота", "Неділя"]
pages = []

print("📖 Щоденник читання")
print("-" * 30)

for day in days:
    while True:
        try:
            p = int(input(f"{day}: скільки сторінок прочитано? "))
            if p < 0:
                print("Кількість сторінок не може бути від'ємною. Спробуйте ще раз.")
            else:
                pages.append(p)
                break
        except ValueError:
            print("Введіть ціле число. Спробуйте ще раз.")

total = sum(pages)
average = total / len(pages)

print("-" * 30)
print(f"Загалом прочитано: {total} сторінок")
print(f"Середнє за день: {average:.1f} сторінок")

if average < 5:
    print("Потрібно читати більше")
elif average <= 15:
    print("Хороший результат")
else:
    print("Відмінна робота!")