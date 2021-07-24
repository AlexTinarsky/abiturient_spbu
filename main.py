from functions import my_rating, my_real_opponents, educational_program
from time import time

print("Downloading...")
from lists import IT_links, IT_links2

print("Downloading successful!")
t1 = time()
my_snils = input("Введите номер СНИЛС: ")
ratings = my_rating(my_snils, IT_links2)
ratings.sort(key=lambda rate: rate["priority"])
my_links = []
for ind, ed_pr in enumerate(ratings):
    my_links.append(ed_pr["link"])
    print(
        f"{ind + 1}) {ed_pr['educational_program']}: Рейтинг - {ed_pr['rating']}, Бюджетных мест - {ed_pr['budget_places']}, Всего заявлений - {ed_pr['number_of_applications']}")

    print(my_real_opponents(ed_pr["link"], my_snils, IT_links2, ed_pr["rating"]-1))
t2 = time()
print(f"Run time: {round((t2 - t1) // 60)} min, {round((t2 - t1) % 60, 1)} sec...")
