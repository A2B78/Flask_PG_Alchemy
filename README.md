# 🚀 Flask_PG_Alchemy - API Flask avec PostgreSQL & JWT  

![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)  
![GitHub last commit](https://img.shields.io/github/last-commit/A2B78/Flask_PG_Alchemy?style=for-the-badge)
![GitHub issues](https://img.shields.io/github/issues/A2B78/Flask_PG_Alchemy?style=for-the-badge)
![GitHub forks](https://img.shields.io/github/forks/A2B78/Flask_PG_Alchemy?style=for-the-badge)
![GitHub stars](https://img.shields.io/github/stars/A2B78/Flask_PG_Alchemy?style=for-the-badge)
![GitHub license](https://img.shields.io/github/license/A2B78/Flask_PG_Alchemy?style=for-the-badge)  
![visitors](https://visitor-badge.glitch.me/badge?page_id=A2B78.Flask_PG_Alchemy)  

## 📌 Description  

Une **API RESTful** construite avec **Flask**, **SQLAlchemy** et **PostgreSQL**. Elle intègre une authentification sécurisée avec **JWT**, la gestion des utilisateurs (ajout, modification, suppression), la pagination et la révocation des tokens.  

## 📋 Fonctionnalités  

✅ **Authentification JWT** (Access & Refresh Tokens)  
✅ **Rafraîchissement automatique des tokens**  
✅ **Inscription et connexion des utilisateurs**  
✅ **Gestion des utilisateurs** (CRUD : création, modification, suppression)  
✅ **Promotion en administrateur**  
✅ **Révocation des tokens** (déconnexion sécurisée)  
✅ **Pagination des utilisateurs**  
✅ **Sécurisation avec rôles utilisateur/admin**  

---

## 🏗️ Installation  

### 1️⃣ Cloner le dépôt  
```bash
git clone https://github.com/A2B78/Flask_PG_Alchemy.git  
cd Flask_PG_Alchemy  
```

### 2️⃣ Créer un environnement virtuel et installer les dépendances  
```bash
python -m venv venv  
source venv/bin/activate  # Linux/macOS  
venv\\Scripts\\activate  # Windows  
pip install -r requirements.txt  
```

### 3️⃣ Configurer les variables d’environnement  
Créer un fichier `.env` à la racine du projet et ajouter :  
```env
DATABASE_URL=postgresql://user:password@localhost/dbname  
JWT_SECRET_KEY=supersecretkey  
ACCESS_TOKEN_EXPIRES=900  
REFRESH_TOKEN_EXPIRES=604800  
```

### 4️⃣ Initialiser la base de données  
```bash
flask db init  
flask db migrate -m "Initial migration"  
flask db upgrade  
```

### 5️⃣ Lancer le serveur  
```bash
python app.py  
```
L’API est maintenant accessible sur **http://127.0.0.1:5000**  

---

## 🔐 Endpoints Principaux  

### Authentification  
- `POST /auth/register` → Inscription d’un utilisateur  
- `POST /auth/login` → Connexion et récupération des tokens  
- `POST /auth/refresh` → Rafraîchir le token d’accès  
- `DELETE /auth/logout` → Révocation du token  

### Gestion des utilisateurs  
- `GET /users/` → Liste des utilisateurs (avec pagination)  
- `PUT /users/<id>` → Modifier un utilisateur  
- `DELETE /users/<id>` → Supprimer un utilisateur  
- **Promotion en admin** :  
  ```sql
  UPDATE user SET role='admin' WHERE username='testuser';
  ```

---

## 📊 Statistiques du projet  

![GitHub Stats](https://github-readme-stats.vercel.app/api?username=A2B78&show_icons=true&theme=tokyonight)  
![Top Langs](https://github-readme-stats.vercel.app/api/top-langs/?username=A2B78&layout=compact&theme=tokyonight)  
![Trophées GitHub](https://github-profile-trophy.vercel.app/?username=A2B78&theme=darkhub)  

---

## 🎯 Technologies Utilisées  
🔹 **Flask** - Framework web Python  
🔹 **Flask-JWT-Extended** - Gestion des tokens JWT  
🔹 **SQLAlchemy** - ORM pour PostgreSQL  
🔹 **Flask-Migrate** - Gestion des migrations  
🔹 **Dotenv** - Chargement des variables d’environnement  

---

## 🤝 Contribuer  
Les contributions sont les bienvenues ! Ouvrez une issue ou faites une pull request pour améliorer le projet.  

🚀 **N'oubliez pas de mettre une ⭐ si vous trouvez ce projet utile !** 🌟  