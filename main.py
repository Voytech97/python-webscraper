# Wersja z samodzielnym uzupełnianiem inputa
from bs4 import BeautifulSoup
import requests
import tkinter as tk
from urllib.parse import urlparse

def get_text_from_html(html_content, line_numbers):
    soup = BeautifulSoup(html_content, 'html.parser')
    lines = soup.get_text().split('\n')
    selected_lines = '\n'.join([lines[num - 1] for num in line_numbers])
    whole_text = soup.get_text()  # Pobranie całej zawartości strony bez znaczników HTML
    return selected_lines, whole_text

def collect_data():
    # Pobieranie adresu URL z pola tekstowego
    selected_url = url_entry.get()
    
    # Dodanie przedrostka "https://" jeśli nie jest już dodany
    if not selected_url.startswith("http://") and not selected_url.startswith("https://"):
        selected_url = "https://" + selected_url
    
    # Pobieranie zawartości strony
    response = requests.get(selected_url)
    
    # Sprawdzanie, czy pobranie danych było udane
    if response.status_code == 200:
        # Pobieranie wybranych linii tekstu z zawartości strony oraz całej zawartości strony bez znaczników HTML
        selected_lines, whole_text = get_text_from_html(response.content, [44])
        
        # Tworzenie nazwy pliku na podstawie wybranego URL
        parsed_url = urlparse(selected_url)
        filename = "tekst_" + parsed_url.netloc + ".txt"
        
        # Zapisywanie pobranych linii tekstu oraz całej zawartości strony do pliku tekstowego
        with open(filename, 'w', encoding="utf-8") as file:
            file.write(whole_text + "\n")  # Zapisanie całej zawartości strony
            file.write(selected_lines + "\n")  # Zapisanie wybranych linii tekstu

            
        status_label.config(text=f"Pomyślnie zapisano wybrane linie i całą zawartość strony do pliku '{filename}'")
        print(f"Pomyślnie zapisano wybrane linie i całą zawartość strony do pliku '{filename}'")
    else:
        status_label.config(text="Wystąpił błąd podczas pobierania danych ze strony")
        print("Wystąpił błąd podczas pobierania danych ze strony")

# Tworzenie głównego okna
root = tk.Tk()
root.title("Pobieranie danych")

# Ramka dla adresu URL
url_frame = tk.Frame(root)
url_frame.pack(pady=10)

# Etykieta i pole tekstowe dla adresu URL
tk.Label(url_frame, text="Wpisz Adres: ").grid(row=0, column=0)
url_entry = tk.Entry(url_frame)
url_entry.grid(row=0, column=1)

# Przycisk do zbierania danych
collect_button = tk.Button(root, text="Zbierz dane", command=collect_data)
collect_button.pack(pady=5)

# Etykieta na status
status_label = tk.Label(root, text="")
status_label.pack(pady=5)

root.mainloop()

# Wersja z predefiniowaną listą adresów

# from bs4 import BeautifulSoup
# import requests
# import tkinter as tk
# from urllib.parse import urlparse

# def get_text_from_html(html_content, line_numbers):
#     soup = BeautifulSoup(html_content, 'html.parser')
#     lines = soup.get_text().split('\n')
#     selected_lines = '\n'.join([lines[num - 1] for num in line_numbers])
#     whole_text = soup.get_text()  # Pobranie całej zawartości strony bez znaczników HTML
#     return selected_lines, whole_text

# def collect_data():
#     # Pobieranie adresu URL z listy rozwijanej
#     selected_url = url_choice.get()
    
#     # Sprawdzenie czy "https://" jest już dodane do adresu URL, jeśli nie, dodaj
#     if not selected_url.startswith("http://"):
#         selected_url = "http://" + selected_url
    
#     # Pobieranie zawartości strony
#     response = requests.get(selected_url)
    
#     # Sprawdzanie, czy pobranie danych było udane
#     if response.status_code == 200:
#         # Pobieranie wybranych linii tekstu z zawartości strony oraz całej zawartości strony bez znaczników HTML
#         selected_lines, whole_text = get_text_from_html(response.content, [44])
        
#         # Tworzenie nazwy pliku na podstawie wybranego URL
#         parsed_url = urlparse(selected_url)
#         filename = "tekst_" + parsed_url.netloc.replace('.', '_') + ".txt"
        
#         # Zapisywanie pobranych linii tekstu oraz całej zawartości strony do pliku tekstowego
#         with open(filename, 'w', encoding="utf-8") as file:
#             file.write(whole_text + "\n")  # Zapisanie całej zawartości strony
#             file.write(selected_lines + "\n")  # Zapisanie wybranych linii tekstu

            
#         status_label.config(text=f"Pomyślnie zapisano wybrane linie i całą zawartość strony do pliku '{filename}'")
#         print("Pomyślnie zapisano wybrane linie i całą zawartość strony do pliku '{filename}'")
#     else:
#         status_label.config(text="Wystąpił błąd podczas pobierania danych ze strony")
#         print("Wystąpił błąd podczas pobierania danych ze strony")

# # Tworzenie głównego okna
# root = tk.Tk()
# root.title("Pobieranie danych")

# # Lista dostępnych adresów URL
# available_urls = ["pypi.org/project/beautifulsoup4/", "github.com", "cda.pl"]

# # Ramka dla adresu URL
# url_frame = tk.Frame(root)
# url_frame.pack(pady=10)

# # Etykieta i lista rozwijana dla adresu URL
# tk.Label(url_frame, text="Wybierz Adres: ").grid(row=0, column=0)
# url_choice = tk.StringVar()
# url_choice.set(available_urls[0])  # Domyślnie wybierany pierwszy URL
# url_dropdown = tk.OptionMenu(url_frame, url_choice, *available_urls)
# url_dropdown.grid(row=0, column=1)

# # Przycisk do zbierania danych
# collect_button = tk.Button(root, text="Zbierz dane", command=collect_data)
# collect_button.pack(pady=5)

# # Etykieta na status
# status_label = tk.Label(root, text="")
# status_label.pack(pady=5)

# root.mainloop()




# import requests
# import tkinter as tk
# from urllib.parse import urlparse
# from bs4 import BeautifulSoup

# def get_text_from_html(html_content, line_numbers):
#     soup = BeautifulSoup(html_content, 'html.parser')
#     lines = soup.get_text().split('\n')
#     selected_lines = '\n'.join([lines[num - 1] for num in line_numbers])
#     return selected_lines

# def collect_data():
#     # Pobieranie adresów URL z pól tekstowych
#     url = url_entry.get()
#     secondurl = second_url_entry.get()
#     imie = "wojtek"
#     # Pobieranie zawartości stron
#     response = requests.get(url)
#     responsetwo = requests.get(secondurl)
    
#     # Sprawdzanie, czy pobranie danych było udane
#     if response.status_code == 200 and responsetwo.status_code == 200:
#         # Pobieranie wybranych linii tekstu z zawartości stron
#         selected_lines_first_url = get_text_from_html(response.content, [7, 49, 50, 75])
#         selected_lines_second_url = get_text_from_html(responsetwo.content, [2, 23])
        
#         # Tworzenie nazwy pliku na podstawie pierwszego wprowadzonego URL
#         parsed_url = urlparse(url)
#         filename = "tekst_" + parsed_url.netloc.replace('.', '_') + ".txt"
        
#         # Zapisywanie pobranych linii tekstu do pliku tekstowego
#         with open(filename, 'w', encoding="utf-8") as file:
#             file.write(selected_lines_first_url + "\n")
#             file.write(selected_lines_second_url + "\n")
            
#         status_label.config(text=f"Pomyślnie zapisano wybrane linie do pliku '{filename}'")
#     else:
#         status_label.config(text="Wystąpił błąd podczas pobierania danych ze strony")

# # Tworzenie głównego okna
# root = tk.Tk()
# root.title("Pobieranie danych")

# # Ramka dla adresów URL
# url_frame = tk.Frame(root)
# url_frame.pack(pady=10)

# # Etykiety i pola tekstowe dla adresów URL
# tk.Label(url_frame, text="URL: ").grid(row=0, column=0)
# url_entry = tk.Entry(url_frame, width=50)
# url_entry.grid(row=0, column=1)

# tk.Label(url_frame, text="Second URL: ").grid(row=1, column=0)
# second_url_entry = tk.Entry(url_frame, width=50)
# second_url_entry.grid(row=1, column=1)

# # Przycisk do zbierania danych
# collect_button = tk.Button(root, text="Zbierz dane", command=collect_data)
# collect_button.pack(pady=5)

# # Etykieta na status
# status_label = tk.Label(root, text="")
# status_label.pack(pady=5)

# root.mainloop()
