from urllib.request import urlopen, urlretrieve
from bs4 import BeautifulSoup
from re import findall
from progress.bar import IncrementalBar

def my_rating(snils, links):
    ratings = []
    for link in links:
        html = link
        soup = BeautifulSoup(html, 'html.parser')
        if len(findall(f"<td>(\d*)</td>\r\n\s\s<td>{snils}</td>", html)) == 1:
            rating = int(findall(f"<td>(\d*)</td>\r\n\s\s<td>{snils}</td>", html)[0])
            priority = int(findall(f"<td>{snils}</td>\r\n\s\s<td>.*?</td>\r\n\s\s<td>(\d*)</td>", html)[0])
            educational_program = " ".join(
                (findall(r"Образовательная программа: (.*)", soup.body.p.text)[0]).split()[1:])
            budget_places = int(findall(r"КЦП по конкурсу: (.*) ", soup.body.p.text)[0])
            number_of_applications = int(findall(r"Количество поданных заявлений: (.*) ", soup.body.p.text)[0])
            ratings.append({"rating": rating, "priority": priority, "educational_program": educational_program,
                            "budget_places": budget_places, "number_of_applications": number_of_applications, "link": html})
    return ratings


def all_links():
    resp1 = urlopen('https://cabinet.spbu.ru/Lists/1k_EntryLists/index_comp_groups.html').read().decode("utf8")
    soup1 = BeautifulSoup(resp1, 'html.parser')
    links = []
    for link in soup1.find_all('a'):
        if link.text == "Госбюджетная":
            links.append(link.get('href'))
    return links


def my_real_opponents(link, my_snils, links, max_for_bar):
    IT_links2 = links
    html = link
    soup = BeautifulSoup(html, 'html.parser')
    F = True
    count1 = 0  # number of priorities "1"
    opponents = 0
    bar = IncrementalBar('Opponents', max=max_for_bar)
    for child in soup.table.tbody.recursiveChildGenerator():
        if F:
            if child.name == "tr":
                a = []  # [my_rating, snils, type_of_competition, priority]
                for child2 in child.recursiveChildGenerator():
                    if child2.name == "td":
                        if len(a) < 4:
                            a.append(child2.text)
                        else:
                            if a[1] == my_snils:
                                F = False
                            else:
                                if (int(a[3]) == 1):
                                    count1 += 1
                                    opponents += 1
                                else:
                                    prior = int(a[3])
                                    snils = a[1]
                                    opponent = True
                                    for ed_prog in my_rating(snils, IT_links2):
                                        if (ed_prog["rating"] <= ed_prog["budget_places"]) and (
                                                ed_prog["priority"] < prior):
                                            opponent = False
                                            break
                                    if opponent:
                                        opponents += 1
                                bar.next()
                            break
        else:
            bar.finish()
            break
    if not F:
        return (count1, opponents)

def educational_program(link):
    resp = urlopen('https://cabinet.spbu.ru/Lists/1k_EntryLists/' + link)
    html = resp.read().decode('utf8')
    soup = BeautifulSoup(html, 'html.parser')
    return " ".join((findall(r"Образовательная программа: (.*)", soup.body.p.text)[0]).split()[1:])

def download_links(links):
    ans = []
    for link in links:
        resp = urlopen('https://cabinet.spbu.ru/Lists/1k_EntryLists/' + link)
        html = resp.read().decode('utf8')
        ans.append(html)
    return ans