
# ⚠️ IC3 | KAHOOT SPAMMER - V3 ⚠️

**Projet fun et créatif, à utiliser de manière responsable.**

---

## ✨ Ce que le logiciel peut faire

- Interface graphique glitch rouge/noir
- Envoi automatique de bots dans un salon Kahoot
- Réponses aux questions gérées automatiquement
- Musique glitch stylée en fond
- Affichage des logs en temps réel
- Panneau de contrôle complet :
  - Choix du nombre de bots
  - Nom personnalisé pour les bots
  - Délais configurables
  - Mode discret (headless)
  - Activation/désactivation des réponses auto

---

## 🎥 À quoi ça ressemble ?

> Une interface stylée, animée et fluide, inspirée des thèmes Red Tiger / Hacker.

![glitch](https://media.giphy.com/media/3o7btPCcdNniyf0ArS/giphy.gif)

---

## ⚙️ Comment le lancer (Kali Linux)

1. Installe Python et les dépendances :

```bash
sudo apt install python3 python3-pip -y
pip install selenium pygame
```

2. Donne les droits d’exécution :

```bash
chmod +x start.sh
```

3. Lance le spammer :

```bash
bash start.sh
```

Par défaut, le chemin de `chromedriver` est :
```bash
/usr/bin/chromedriver
```

---

## 🛠️ Les options dispo dans le panel

| Option                  | Ce que ça fait                              |
|------------------------|---------------------------------------------|
| Code du salon          | Le code du Kahoot que tu veux spammer       |
| Nombre de bots         | Le nombre total de bots à envoyer           |
| Nom des bots           | Le nom de base des bots (ex : IC3_)         |
| Délai                  | Temps entre chaque envoi de bot             |
| Réponse automatique    | Active ou non la fonction auto-réponse      |
| Mode furtif (headless) | Lance les bots sans afficher de fenêtres    |

---

## 📂 Contenu du dossier

- `ic3_kahoot_full.py` – Le script principal avec l’interface
- `start.sh` – Script de lancement rapide
- `glitch_music.mp3` – Musique de fond intégrée
- `README.md` – Ce fichier explicatif

---

## ✍️ Créé par

**IC3** – Passionné de projets glitch, dev, dark interface et hack design.

---

> Ce projet est là pour apprendre, s’amuser et découvrir. Ne l’utilise pas n’importe comment.
