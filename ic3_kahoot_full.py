
import tkinter as tk
from tkinter import scrolledtext, messagebox
import threading
import time
import random
import pygame
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

# Lancement de la musique glitch en boucle
def play_music():
    pygame.mixer.init()
    pygame.mixer.music.load("glitch_music.mp3")
    pygame.mixer.music.play(-1)  # boucle infinie

# Fonction de spam de bots (simulation)
def spam_bots(code, num_bots, base_name, delay, auto_answer, headless, log_func):
    chrome_options = Options()
    if headless:
        chrome_options.add_argument("--headless=new")
    chrome_options.add_argument("--disable-infobars")
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")

    for i in range(num_bots):
        try:
            bot_name = f"{base_name}_{i+1}"
            driver = webdriver.Chrome(executable_path="/usr/bin/chromedriver", options=chrome_options)
            driver.get("https://kahoot.it/")
            time.sleep(1)
            pin_input = driver.find_element(By.XPATH, '//*[@id="game-input"]')
            pin_input.send_keys(code)
            driver.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div/button').click()
            time.sleep(2)
            nickname_input = driver.find_element(By.XPATH, '//input')
            nickname_input.send_keys(bot_name)
            driver.find_element(By.XPATH, '//button').click()
            log_func(f"[+] Bot {bot_name} rejoint avec succès !")
        except Exception as e:
            log_func(f"[!] Erreur pour {bot_name} : {str(e)}")
        time.sleep(delay)

# Lancement de l'attaque depuis le bouton
def start_attack():
    code = entry_code.get()
    base_name = entry_name.get()
    try:
        num_bots = int(entry_bots.get())
        delay = float(entry_delay.get())
        auto_answer = var_auto.get()
        headless = var_stealth.get()
        threading.Thread(target=spam_bots, args=(code, num_bots, base_name, delay, auto_answer, headless, log_bot)).start()
        log_bot(">>> Attaque lancée...")
    except ValueError:
        messagebox.showerror("Erreur", "Merci de vérifier les paramètres.")

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
entry_bots.insert(0, "5")
entry_bots.pack()

tk.Label(root, text="Nom des bots :", bg="black", fg="red").pack()
entry_name = tk.Entry(root, bg="black", fg="white")
entry_name.insert(0, "IC3")
entry_name.pack()

tk.Label(root, text="Délai (sec) entre bots :", bg="black", fg="red").pack()
entry_delay = tk.Entry(root, bg="black", fg="white")
entry_delay.insert(0, "0.5")
entry_delay.pack()

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
threading.Thread(target=play_music).start()
root.mainloop()
