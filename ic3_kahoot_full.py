import argparse
import time
import random
import pygame
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import chromedriver_autoinstaller
from selenium.webdriver.common.by import By

# Fonction pour jouer la musique glitch en boucle
def play_music():
    pygame.mixer.init()
    pygame.mixer.music.load("glitch_music.mp3")
    pygame.mixer.music.play(-1)  # boucle infinie

# Fonction pour spammer les bots dans Kahoot
def spam_bots(code, num_bots, base_name, delay, auto_answer, headless):
    # Installe automatiquement le driver Chrome s'il n'est pas déjà installé
    chromedriver_autoinstaller.install()
    
    chrome_options = Options()
    
    # Si l'option headless est activée, on désactive l'interface graphique
    if headless:
        chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")

    for i in range(num_bots):
        try:
            bot_name = f"{base_name}_{i+1}"
            driver = webdriver.Chrome(options=chrome_options)
            driver.get("https://kahoot.it/")
            time.sleep(1)
            
            # Saisie du code du salon
            pin_input = driver.find_element(By.XPATH, '//*[@id="game-input"]')
            pin_input.send_keys(code)
            driver.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div/button').click()
            time.sleep(2)
            
            # Saisie du nom du bot
            nickname_input = driver.find_element(By.XPATH, '//input')
            nickname_input.send_keys(bot_name)
            driver.find_element(By.XPATH, '//button').click()
            print(f"[+] Bot {bot_name} rejoint avec succès !")
            
            # Logique pour la réponse automatique si activée (option à compléter si nécessaire)
            if auto_answer:
                # Logique de réponse automatique, à ajouter ici
                pass

            driver.quit()
        except Exception as e:
            print(f"[!] Erreur pour {bot_name} : {str(e)}")
        time.sleep(delay)

# Fonction principale
def main():
    # Configuration des arguments en ligne de commande avec argparse
    parser = argparse.ArgumentParser(description='Spammer Kahoot avec des bots.')
    parser.add_argument('code', type=str, help='Code du salon Kahoot')
    parser.add_argument('num_bots', type=int, help='Nombre de bots à utiliser')
    parser.add_argument('base_name', type=str, help='Nom de base des bots')
    parser.add_argument('delay', type=float, help='Délai entre l\'envoi des bots (en secondes)')
    parser.add_argument('--auto_answer', action='store_true', help='Répondre automatiquement aux questions')
    parser.add_argument('--headless', action='store_true', help='Mode headless pour Selenium')
    args = parser.parse_args()

    # Lancer la musique (en fond)
    pygame.mixer.init()
    pygame.mixer.music.load("glitch_music.mp3")
    pygame.mixer.music.play(-1)  # Jouer la musique en boucle

    # Lancer les bots avec les arguments fournis
    spam_bots(args.code, args.num_bots, args.base_name, args.delay, args.auto_answer, args.headless)

if __name__ == "__main__":
    main()
