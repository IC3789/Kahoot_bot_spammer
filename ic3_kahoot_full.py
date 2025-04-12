import argparse
import time
import random
import threading
import pygame
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import chromedriver_autoinstaller

# Fonction pour jouer la musique en boucle
def play_music():
    pygame.mixer.init()
    pygame.mixer.music.load("glitch_music.mp3")  # Charge la musique de fond
    pygame.mixer.music.play(-1)  # musique en boucle infinie

# Fonction de spam des bots sur Kahoot
def spam_bots(code, num_bots, base_name, delay, auto_answer, headless, log_func):
    # Vérifie si le chromedriver est installé automatiquement
    chromedriver_autoinstaller.install()

    chrome_options = Options()
    if headless:
        chrome_options.add_argument("--headless")  # Mode headless
    chrome_options.add_argument("--disable-infobars")
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")

    for i in range(num_bots):
        try:
            bot_name = f"{base_name}_{i+1}"
            driver = webdriver.Chrome(service=Service(), options=chrome_options)
            driver.get("https://kahoot.it/")
            time.sleep(1)

            # Entrée du code de la partie
            pin_input = driver.find_element(By.XPATH, '//*[@id="game-input"]')
            pin_input.send_keys(code)
            driver.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div/button').click()
            time.sleep(2)

            # Entrée du nom du bot
            nickname_input = driver.find_element(By.XPATH, '//input')
            nickname_input.send_keys(bot_name)
            driver.find_element(By.XPATH, '//button').click()
            log_func(f"[+] Bot {bot_name} rejoint avec succès !")

            # Si auto_answer est activé, répondre automatiquement
            if auto_answer:
                log_func(f"[+] Réponse automatique activée pour {bot_name}")
                answer_questions(driver, log_func)

            time.sleep(delay)

        except Exception as e:
            log_func(f"[!] Erreur pour {bot_name} : {str(e)}")
        
    log_func(">>> Tous les bots ont rejoint le jeu.")

# Fonction pour répondre aux questions automatiquement
def answer_questions(driver, log_func):
    while True:
        try:
            # Cherche les options de réponse pour la question en cours
            options = driver.find_elements(By.XPATH, '//div[@class="choice"]')
            
            if options:
                # Choisit la première option (réponse correcte)
                correct_answer = options[0]
                correct_answer.click()
                log_func("[+] Réponse correcte envoyée.")
                
                # Attendre que la question suivante apparaisse
                time.sleep(5)
            else:
                # Si aucune option n'est trouvée, sortir de la boucle
                break
        except Exception as e:
            log_func(f"[!] Erreur lors de la réponse : {str(e)}")
            break

# Fonction pour lancer l'attaque depuis la ligne de commande
def start_attack(args):
    code = args.code
    base_name = args.base_name
    num_bots = args.num_bots
    delay = args.delay
    auto_answer = args.auto_answer
    headless = args.headless

    # Démarre l'attaque sur un thread séparé pour ne pas bloquer l'interface
    threading.Thread(target=spam_bots, args=(code, num_bots, base_name, delay, auto_answer, headless, print)).start()
    print(">>> Attaque lancée...")

# Fonction principale
def main():
    # Création du parser pour les arguments en ligne de commande
    parser = argparse.ArgumentParser(description='Kahoot Spammer')
    parser.add_argument('code', type=str, help='Code du salon Kahoot')
    parser.add_argument('num_bots', type=int, help='Nombre de bots à envoyer')
    parser.add_argument('base_name', type=str, help='Nom de base des bots')
    parser.add_argument('delay', type=float, help='Délai entre chaque bot (en secondes)')
    parser.add_argument('--auto_answer', action='store_true', help='Active les réponses automatiques')
    parser.add_argument('--headless', action='store_true', help='Mode headless (sans interface graphique)')

    # Parsing des arguments
    args = parser.parse_args()

    # Lancer la musique (si nécessaire)
    threading.Thread(target=play_music).start()

    # Lancer l'attaque
    start_attack(args)

# Exécution du programme
if __name__ == "__main__":
    main()
