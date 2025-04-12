import tkinter as tk
from tkinter import scrolledtext, messagebox
import threading
import time
import pygame
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import chromedriver_autoinstaller  # Gestion automatique de Chromedriver

# Lancement de la musique glitch en boucle
def play_music():
    pygame.mixer.init()
    pygame.mixer.music.load("glitch_music.mp3")
    pygame.mixer.music.play(-1)  # boucle infinie

# Fonction de spam de bots (simulation)
def spam_bots(code, num_bots, base_name, auto_answer, headless, log_func):
    chrome_options = Options()
    if headless:
        chrome_options.add_argument("--headless=new")
    chrome_options.add_argument("--disable-infobars")
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")

    # Télécharge et installe automatiquement la bonne version de chromedriver
    chromedriver_autoinstaller.install()

    # Fonction pour démarrer chaque bot dans un thread
    def start_bot(bot_name):
        try:
            service = Service()  # Pas besoin de spécifier de chemin, chromedriver_autoinstaller gère cela
            driver = webdriver.Chrome(service=service, options=chrome_options)

            # Accéder à Kahoot
            driver.get("https://kahoot.it/")
            time.sleep(0.5)  # Plus court délai pour accélérer

            # Saisie du code PIN
            pin_input = driver.find_element(By.ID, "game-input")
            pin_input.send_keys(code)
            driver.find_element(By.XPATH, '//button[@type="submit"]').click()
            time.sleep(1)  # Délais réduits

            # Saisie du pseudo
            nickname_input = driver.find_element(By.XPATH, '//input[@type="text"]')
            nickname_input.send_keys(bot_name)
            driver.find_element(By.XPATH, '//button[@type="submit"]').click()

            log_func(f"[+] Bot {bot_name} a rejoint avec succès.")
        except Exception as e:
            log_func(f"[!] Erreur pour {bot_name} : {str(e)}")
        finally:
            try:
                driver.quit()
            except:
                pass

    # Démarrage des bots dans des threads parallèles
    threads = []
    for i in range(num_bots):
        bot_name = f"{base_name}_{i+1}"
        thread = threading.Thread(target=start_bot, args=(bot_name,))
        thread.start()
        threads.append(thread)

    # Attente de la fin de tous les threads
    for thread in threads:
        thread.join()

# Lancement de l'attaque depuis le bouton
def start_attack():
    code = entry_code.get()
    base_name = entry_name.get()
    try:
        num_bots = int(entry_bots.get())
        auto_answer = var_auto.get()
        headless = var_stealth.get()

        # Lancer l'attaque dans un thread séparé
        threading.Thread(
            target=spam_bots,
            args=(code, num_bots, base_name, auto_answer, headless, log_bot),
            daemon=True
        ).start()

        log_bot(">>> Attaque lancée...")
    except ValueError:
        messagebox.showerror("Erreur", "Merci de vérifier les paramètres.")

# Fonction de logging dans la zone de texte
def log_bot(msg):
    log_area.insert(tk.END, msg + '\n')
    log_area.yview(tk.END)

# GUI
root = tk.Tk()
root.title("IC3 | KAHOOT SPAMMER // GL!TCH CORE")
root.configure(bg='black')
root.geometry("750x600")

tk.Label(root, text="Code du salon :", bg="black", fg="red").pack()
entry_code = tk.Entry(root, bg="black", fg="white")
entry_code.pack()

tk.Label(root, text="Nombre de bots :", bg="black", fg="red").pack()
entry_bots = tk.Entry(root, bg="black", fg="white")
entry_bots.insert(0, "10")
entry_bots.pack()

tk.Label(root, text="Nom des bots :", bg="black", fg="red").pack()
entry_name = tk.Entry(root, bg="black", fg="white")
entry_name.insert(0, "IC3")
entry_name.pack()

var_auto = tk.BooleanVar()
check_auto = tk.Checkbutton(root, text="Réponse auto activée", variable=var_auto, bg="black", fg="red")
check_auto.pack()

var_stealth = tk.BooleanVar()
check_stealth = tk.Checkbutton(root, text="Mode furtif (headless)", variable=var_stealth, bg="black", fg="red")
check_stealth.pack()

btn_start = tk.Button(root, text="Lancer l'attaque", command=start_attack, bg="red", fg="black")
btn_start.pack(pady=10)

log_area = scrolledtext.ScrolledText(root, bg="black", fg="lime", height=15)
log_area.pack(fill=tk.BOTH, expand=True)

# Démarrer musique
threading.Thread(target=play_music, daemon=True).start()
root.mainloop()
