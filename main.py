from functions import my_rating, my_real_opponents
from time import time

print("Downloading...")
t1 = time()
from lists import IT_links2
print("Downloading successful!")
my_snils = input("Введите номер СНИЛС (как в ЛК СПбГУ): ")
ratings = my_rating(my_snils, IT_links2)
ratings.sort(key=lambda rate: rate["priority"])
for ind, ed_pr in enumerate(ratings):
    print(
        f"{ind + 1}) {ed_pr['educational_program']}: Рейтинг - {ed_pr['rating']}, Бюджетных мест - {ed_pr['budget_places']}, Всего заявлений - {ed_pr['number_of_applications']}")
    print(f"Время последнего обновления: {ed_pr['datetime']}")
while True:
    inp = (input("Введите номер обр. программы (из списка выше), о которой хотите узнать подробнее, или \"Выход\" для завершения работы: ")).lower()
    if inp == "выход":
        break
    try:
        if int(inp) in range(1, len(ratings)+1):
            lt1 = time()
            mro = my_real_opponents(ratings[int(inp)-1]["link"], my_snils, IT_links2, ratings[int(inp)-1]["rating"]-1)
            print(f"Количество абитуриентов, которые выше вас по рейтингу и имеют приоритет \"1\" - {mro[0]}")
            print(f"Количество абитуриентов, которые выше вас по рейтингу и не проходят ни на одно более важное для себя направление - {mro[1]}")
            lt2 = time()
            print(f"Analysis time: {round((lt2 - lt1) // 60)} min, {round((lt2 - lt1) % 60, 1)} sec...")
    except ValueError:
        print("Некорректный ввод!")
t2 = time()
print(f"Run time: {round((t2 - t1) // 60)} min, {round((t2 - t1) % 60, 1)} sec...")
input("Press Enter to exit...")
