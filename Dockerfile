# Utilise une image Python officielle
FROM python:3.10-slim

# Crée un dossier de travail dans le conteneur
WORKDIR /app

# Copie les fichiers nécessaires
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY app.py app.py

# Expose le port
EXPOSE 5000

# Commande pour démarrer l'application
CMD ["python", "app.py"]