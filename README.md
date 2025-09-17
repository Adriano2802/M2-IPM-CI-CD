# TP1

## Construire l’image Docker :
docker build -t flask-docker-app .

## Lancer un conteneur (exercice 5):
docker run -d -p 5000:5000 flask-docker-app

## Tester dans le navigateur :
http://localhost:5000

## Pour arreter le conteneur :
docker stop <id|nom>

## Pour démarer un conteneur :
docker start <id|nom>