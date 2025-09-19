# TP1

## Construire l’image Docker :
docker build -t flask-docker-app .

## Lancer un conteneur (exercice 5):
docker run -d -p 5000:5000 flask-docker-app

## Lancer les conteneurs (exercice 6) :
docker-compose up --build

## Tester dans le navigateur :
http://localhost:5000

## Pour arreter le conteneur :
docker stop <id|nom>

## Pour démarer un conteneur :
docker start <id|nom>

## Vérifier directement dans MongoDB (exercice 6) :
docker exec -it mongo_db mongosh

## Et ensuite exécuter ça pour afficher les documents :
use testdb
db.messages.find()


# TP2

## Etape 1
##### Problème identifié = Builds non reproductibles

    original =  FROM node:latest

    actuel =    FROM node:18-alpine


## Etape 2
##### Problème identifié = Mauvaise gestion du cache

    original =  COPY . /app
                RUN npm install

    actuel =    COPY package*.json ./
                RUN npm ci --only=production
                COPY . .


## Etape 3
##### Problème identifié = Sécurité et poids de l’image

    original =  COPY node_modules
                apt-get install
                USER root

    actuel =    USER node


## Etape 4
#### Problème identifié = Exposition et environnement

#### original =  EXPOSE 3000 4000 5000
    ENV NODE_ENV=development

#### actuel =    EXPOSE 3000
    ENV NODE_ENV=production