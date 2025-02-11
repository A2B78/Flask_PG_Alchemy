📂 **Structure du projet**
```
/backend
│── app.py               # Point d'entrée principal
│── config.py            # Configuration de l'application
│── models.py            # Définition des modèles SQLAlchemy
│── extensions.py        # Initialisation des extensions (DB, JWT, etc.)
│── routes/
│   │── auth.py          # Routes d'authentification
│   │── users.py         # Gestion des utilisateurs (admin)
│── migrations/          # Dossier pour Flask-Migrate
│── .env                 # Variables d'environnement
│── requirements.txt     # Dépendances
│── README.md            # Tuto détaillé
```

### **1. .env (Fichier des variables d'environnement)**
```env
DATABASE_URL=postgresql://user:password@localhost/dbname
JWT_SECRET_KEY=supersecretkey
ACCESS_TOKEN_EXPIRES=900  # 15 minutes
REFRESH_TOKEN_EXPIRES=604800  # 7 jours
```

### **2. requirements.txt (Dépendances du projet)**
```txt
Flask
Flask-SQLAlchemy
Flask-Migrate
Flask-JWT-Extended
python-dotenv
Werkzeug
psycopg2-binary
```

### **3. README.md (Tuto détaillé pas à pas)**
```md
# 🚀 Backend Flask avec Authentification et PostgreSQL

## 1️⃣ Installation et configuration

### 📥 Cloner le projet
```bash
git clone https://github.com/A2B78/Flask_PG_Alchemy.git
cd Flask_PG_Alchemy
```

### 🏗️ Créer un environnement virtuel
```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
```

### 📦 Installer les dépendances
```bash
pip install -r requirements.txt
```

### ⚙️ Configurer les variables d'environnement
Créer un fichier `.env` à la racine du projet et ajouter :
```env
DATABASE_URL=postgresql://user:password@localhost/dbname
JWT_SECRET_KEY=supersecretkey
ACCESS_TOKEN_EXPIRES=900
REFRESH_TOKEN_EXPIRES=604800
```

## 2️⃣ Configuration de la base de données

### 🎲 Initialiser la base de données
```bash
flask db init
flask db migrate -m "Initial migration"
flask db upgrade
```

## 3️⃣ Lancer l'application
```bash
python app.py
```
L'API est maintenant accessible sur `http://127.0.0.1:5000`

## 4️⃣ Tester l'authentification

### 🔐 Inscription d'un utilisateur
```bash
curl -X POST http://127.0.0.1:5000/auth/register -H "Content-Type: application/json" -d '{"username":"testuser", "password":"testpass"}'
```

### 🔑 Connexion
```bash
curl -X POST http://127.0.0.1:5000/auth/login -H "Content-Type: application/json" -d '{"username":"testuser", "password":"testpass"}'
```

Cela retournera un **access token** et un **refresh token** que vous pourrez utiliser pour accéder aux routes protégées.

🎉 **Votre backend Flask avec authentification JWT et PostgreSQL est maintenant opérationnel !** 🚀
```