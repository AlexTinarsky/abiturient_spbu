from functions import my_rating, my_real_opponents, educational_program, download_links
from time import time
t1 = time()
my_snils = "185-597-048 25"
my_links = ['list_ee25050d-89ab-41ba-8cfa-016f3afe1b33.html', 'list_94eb54ce-57aa-45e7-9be3-3acd8bf9ca38.html',
            'list_49aa4213-1d7b-47ba-9b37-6b506a3570a6.html', 'list_ff4e6d1e-9a62-4cd3-886f-d89ccd5ced2d.html',
            'list_6884b2b8-51fe-4e09-8de1-a2d8d72d488f.html']
IT_links = ['list_ac8fab02-79bd-48de-b2fa-394c825dbf5e.html', 'list_3a14201e-e67b-40e1-8507-b08a76cda607.html',
            'list_af2b6ada-e445-4cef-b23e-b70310b3a9d9.html', 'list_1a5c4321-6147-43d5-945e-6c54e3aa2d8d.html',
            'list_dfb9b25a-8adb-4212-baae-4a8f2bbc7276.html', 'list_394843a7-06d9-470f-8019-79a48a10c30b.html',
            'list_a7bf8989-a195-4d68-b967-31aeeab37b24.html', 'list_6b182894-edfc-40d7-8c7b-efb03ab4cef5.html',
            'list_26c0453c-2f65-4aae-a73a-ffec15e9db58.html', 'list_916cb065-29b3-4942-87f3-30a6b0ad4641.html',
            'list_d92a5b1f-c270-4976-8243-c094b7688264.html', 'list_ee25050d-89ab-41ba-8cfa-016f3afe1b33.html',
            'list_94eb54ce-57aa-45e7-9be3-3acd8bf9ca38.html', 'list_49aa4213-1d7b-47ba-9b37-6b506a3570a6.html',
            'list_ff4e6d1e-9a62-4cd3-886f-d89ccd5ced2d.html', 'list_6884b2b8-51fe-4e09-8de1-a2d8d72d488f.html']
ed_program = "list_6884b2b8-51fe-4e09-8de1-a2d8d72d488f.html"
print("Downloading...")
IT_links2 = [f"{i+1}.html" for i in range(len(IT_links))]
#download_links(IT_links)
print("Downloading successful!")
print(educational_program(ed_program))
print(my_real_opponents(ed_program, my_snils, IT_links2))
t2 = time()
print(f"Run time: {round((t2-t1)//60)} min, {round((t2-t1)%60, 1)} sec...")
# print(*my_rating(my_snils, my_links), sep="\n")
