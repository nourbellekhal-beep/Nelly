# 🏛️ Rapport de Projet : Judicia Luxe
**Objet** : Modernisation du système de gestion d'un Cabinet Judiciaire de Prestige.

---

## 1. Vision du Projet
Le projet **Judicia Luxe** est un environnement web haut de gamme conçu pour répondre aux besoins spécifiques d'un cabinet juridique d'excellence. L'objectif principal était de concilier une interface utilisateur (UI) prestigieuse avec une architecture logicielle robuste et évolutive (MariaDB/MySQL).

## 2. Architecture Technique (Architecture Django Full-Stack)
Le projet repose sur le framework **Django 4.2 LTS** organisé selon le pattern **MVT (Model-View-Template)** et structuré en trois applications modulaires :

*   📦 **App `base`** : Point d'entrée de l'application, incluant le moteur de rendu de la page d'accueil avec un design "Hero" immersif et un panneau de statistiques clés.
*   ⚖️ **App `services`** : Module complexe de gestion des expertises juridiques. Utilise des modèles de données interdépendants (`Category`, `Service`) permettant une structuration dynamique de l'offre du cabinet (Fusions-Acquisitions, Droits Patrimoniaux, etc.).
*   🤝 **App `clients`** : Système de gestion du portefeuille client, sécurisé et offrant une vue panoramique des dossiers et coordonnées, avec un tableau de bord élégant.

## 3. Direction Artistique & UX "Luxe"
Afin de refléter l'excellence du cabinet, une charte graphique luxueuse a été appliquée :
*   **Palette de Prestige** : Duo de couleurs **Bleu Nuit (`#0A192F`)** et **Or Raffiné (`#D4AF37`)**.
*   **Typographie de Marque** : Choix de polices à empattements (*Playfair Display*) pour souligner l'aspect statutaire et historique de l'institution.
*   **Design Glassmorphism** : Utilisation d'effets de calque transparents et de flou (backdrop-filter) pour une sensation de profondeur et de modernité "State-of-the-art".

## 4. Défis Techniques & Solutions (Spécificités Professeur)
*   **Interopérabilité MariaDB (XAMPP)** : Transition réussie de SQLite vers MariaDB (v10.4). Utilisation de `pymysql` pour bypasser les limitations de versions et assurer une compatibilité totale avec les environnements serveurs communs.
*   **Admin Premium (Jazzmin)** : Refonte complète de l'interface d'administration pour transformer le back-office standard en un véritable outil de gestion décisionnelle professionnel.
*   **Système de Données Faker** : Développement d'une commande personnalisée (`python manage.py fake_data`) permettant le déploiement instantané d'un environnement de démonstration crédible et structuré pour la présentation finale.

## 5. Guide de Maintenance
*   **Backend** : Python 3.13 / Django 4.2.29
*   **Front-end** : Vanilla CSS 3 / HTML 5 / FontAwesome 6
*   **Database** : MariaDB via XAMPP

---
*Réalisé pour la présentation de fin de cycle - Judicia Luxe 2026*
