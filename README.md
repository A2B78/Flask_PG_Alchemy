# 🚀 API Flask avec JWT, PostgreSQL et Gestion des Utilisateurs  

Une API RESTful construite avec **Flask**, utilisant **JWT** pour l’authentification, une **base de données PostgreSQL**, et proposant des fonctionnalités avancées comme la gestion des utilisateurs, la pagination et la révocation des tokens.  

## 📌 Fonctionnalités  
✅ **Authentification JWT** (Access & Refresh Tokens)  
✅ **Rafraîchissement automatique des tokens**  
✅ **Inscription et connexion des utilisateurs**  
✅ **Gestion des utilisateurs** (ajout, modification, suppression)  
✅ **Promotion en administrateur**  
✅ **Révocation des tokens** (déconnexion sécurisée)  
✅ **Pagination des utilisateurs**  
✅ **Sécurisation avec rôles utilisateur/admin**  

## 🏗️ Installation  

1️⃣ **Cloner le dépôt**  
```bash
git clone https://github.com/A2B78/Flask_PG_Alchemy.git  
cd Flask_PG_Alchemy  
```

2️⃣ **Créer un environnement virtuel et installer les dépendances**  
```bash
python -m venv venv  
source venv/bin/activate  # Linux/macOS  
venv\\Scripts\\activate  # Windows  
pip install -r requirements.txt  
```

3️⃣ **Configurer les variables d’environnement**  
Créer un fichier `.env` et ajouter :  
```env
DATABASE_URL=postgresql://user:password@localhost/dbname  
JWT_SECRET_KEY=supersecretkey  
ACCESS_TOKEN_EXPIRES=900  
REFRESH_TOKEN_EXPIRES=604800  
```

4️⃣ **Initialiser la base de données**  
```bash
flask db init  
flask db migrate -m "Initial migration"  
flask db upgrade  
```

5️⃣ **Lancer le serveur**  
```bash
flask run  
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
- `UPDATE user SET role='admin' WHERE username='testuser';` → Promotion en admin  

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

🚀 **Star ce projet si tu le trouves utile !** 🌟  