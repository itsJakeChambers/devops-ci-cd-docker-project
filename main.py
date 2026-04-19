from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from pydantic import BaseModel

app = FastAPI()

class Lieu(BaseModel):
    nom: str

donnees = {
    'lieux' : [
        'Paris',
        'Lyon',
        'Marseille',
        'Montpellier',
        'Toulon',
        'Lille',
        'Nantes'
    ]
}

@app.get("/", response_class=HTMLResponse)
async def home():
    return """
    <html>
        <head>
            <title>DevOps Deployment Service</title>
            <style>
                body {
                    font-family: Arial, sans-serif;
                    text-align: center;
                    padding: 50px;
                    background-color: #0f172a;
                    color: white;
                }
                h1 {
                    font-size: 3em;
                    margin-bottom: 10px;
                }
                p {
                    font-size: 1.2em;
                    color: #cbd5f5;
                }
                .btn {
                    display: inline-block;
                    margin: 10px;
                    padding: 15px 25px;
                    border-radius: 8px;
                    text-decoration: none;
                    font-weight: bold;
                }
                .primary {
                    background-color: #3b82f6;
                    color: white;
                }
                .secondary {
                    background-color: #1e293b;
                    color: white;
                    border: 1px solid #3b82f6;
                }
                .container {
                    max-width: 800px;
                    margin: auto;
                }
            </style>
        </head>
        <body>
            <div class="container">
                <h1>🚀 Deploy your app like a pro</h1>
                
                <p>
                Je déploie vos applications avec une infrastructure complète :
                <br><br>
                ✔️ Docker & containerisation  
                ✔️ CI/CD (GitHub Actions)  
                ✔️ Serveur cloud (VPS)  
                ✔️ Domaine + HTTPS sécurisé  
                ✔️ Reverse proxy (Nginx)
                </p>

                <br>

                <a class="btn primary" href="mailto:kjeanmarie01@gmail.com">
                    📩 Me contacter
                </a>

                <a class="btn secondary" href="/docs">
                    📚 Voir l'API
                </a>

                <br><br>

                <p>
                Déploiement rapide • Setup propre • Infrastructure scalable
                </p>
            </div>
        </body>
    </html>
    """

@app.get("/lieux")
async def get_lieux():

    # renvoyer nos données et code 200 (OK)
    return {'donnees': donnees}, 200

@app.post("/lieux")
async def post_lieu(lieu: str):
    # si le lieu est déjà présent, nous ne l'ajoutons pas aux données
    if lieu in donnees['lieux']:
        # donc retourner simplement la réponse avec un message disant qu'il existe déjà
        return {'donnees' : donnees, 'message' : "l'emplacement existe déjà"}
    
    # par contre s'il n'est pas présent, nous ajoutons le lieu aux données
    else:
        donnees['lieux'].append(lieu)
        #reponse de retour
        return {'donnees': donnees, 'message': "l'emplacement a été ajouté"}
    

@app.delete("/lieux/")
async def delete_lieu(lieu: str):
    # si le lieu est présent on le supprime 
    if lieu in donnees['lieux']:
        donnees['lieux'].remove(lieu)
        # réponse de retour confirmant la suppression
        return {'donnees': donnees, 'message': "l'emplacement a été supprimé"}
    
    # s'il n'est pas présent, renvoyez simplement la réponse
    else:
        return {'donnees': donnees, 'message': "le lieu n'existe pas"}
    
