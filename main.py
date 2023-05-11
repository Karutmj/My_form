import sqlite3
import tkinter as tk
import tkinter.font as TkFont



# łączenie z bazą danych SQLite
conn = sqlite3.connect('database.db')

# tworzenie tabeli 'users'
conn.execute('''CREATE TABLE IF NOT EXISTS users 
             (ID INT PRIMARY KEY     NOT NULL,
             NAME           TEXT    NOT NULL,
             EMAIL          TEXT    NOT NULL);''')
cur=conn.cursor()
result=cur.fetchall()
for row in result:
    print(row)
# tworzenie funkcji do obsługi przycisku 'Zapisz'
def save_data():
    # pobieranie wartości z pól tekstowych
    id_val = id_entry.get()
    name_val = name_entry.get()
    email_val = email_entry.get()

    # dodawanie rekordu do tabeli 'users'
    conn.execute("INSERT INTO users (ID, NAME, EMAIL) \
                  VALUES (?, ?, ?)", (id_val, name_val, email_val))

    # zatwierdzanie zmian w bazie danych
    conn.commit()

    # czyszczenie pól tekstowych po zapisie danych
    id_entry.delete(0, tk.END)
    name_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)



# tworzenie okna aplikacji
root = tk.Tk()
root.geometry('1000x550+500+200')
root.title("Formularz użytkownika")
root["background"]='#4B0082'

# tworzenie etykiet i pól tekstowych dla ID
id_label = tk.Label(root, text="User ID:")
font = TkFont.Font (family="Helvetica",size=20,weight="bold")
id_label["justify"]="center"
id_label.place(x = 200,
        y = 100,
        width=150
        )
id_label["fg"]="#20B2AA"
id_label["background"]="#4B0082"
id_label["font"]=font
id_entry = tk.Entry(root)
id_entry["font"]=("Helvetica",20)
id_entry["background"]="#EE82EE"
id_entry.place(x=360,
               y=100,
               width=350,
               height=35)

# tworzenie etykiet i pól tekstowych dla nazwy
name_label = tk.Label(root, text="Nazwa:")
font = TkFont.Font (family="Helvetica",size=20,weight="bold")
name_label["justify"]="center"
name_label.place(x = 200,
        y = 150,
        width=150)
name_label["fg"]="#20B2AA"
name_label["background"]="#4B0082"
name_label["font"]=font
name_entry = tk.Entry(root)
name_entry["font"]=("Helvetica",20)
name_entry["background"]="#EE82EE"
name_entry.place(x=360,
               y=150,
               width=350,
               height=35)


# tworzenie etykiet i pól tekstowych dla adresu e-mail
email_label = tk.Label(root, text="Adres e-mail:")
font = TkFont.Font (family="Helvetica",size=20,weight="bold")
email_label["justify"]="center"
email_label.place(x = 170,
        y = 200,)
email_label["fg"]="#20B2AA"
email_label["background"]="#4B0082"
email_label["font"]=font

email_entry = tk.Entry(root)
email_entry["font"]=("Helvetica",20)
email_entry["background"]="#EE82EE"
email_entry.place(x=360,
               y=200,
               width=350,
               height=35)



# tworzenie przycisku 'Zapisz'
save_button = tk.Button(root, text="Sign in", command=save_data)
font = TkFont.Font (family="Helvetica",size=20,weight="bold")
save_button["font"]=font
save_button["background"]="#20B2AA"
save_button["fg"]="white"

save_button.place(x=400,
                  y=250,
                  width=250,
                  height=50)

# uruchamianie głównej pętli aplikacji
root.mainloop()
# zamykanie połączenia z bazą danyc
cur.close()
conn.close()
