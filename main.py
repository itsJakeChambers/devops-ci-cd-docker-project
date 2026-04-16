from fastapi import FastAPI

app = FastAPI()

donnees = {
    'lieux' : [
        'Paris',
        'Lyon',
        'Marseille',
        'Montpellier',
        'Toulon',
        'Lilles',
        'Nantes'
    ]
}

@app.get("/lieux")
async def get_lieux():

    # renvoyer nos données et code 200 (OK)
    return {'donnees': donnees}, 200

@app.post("/lieux")
async def post_lieux(lieu: str):
    # si le lieu est déjà présent, nous ne l'ajoutons pas aux données
    if lieu in donnees['lieux']:
        # donc retourner simplement la réponse avec un message disant qu'il existe déjà
        return {'donnees' : donnees, 'message' : "l'emplacement existe déjà"}
    
    # par contre s'il n'est pas présent, nous ajoutons le lieu aux données
    else:
        donnees['lieux'].append(lieu)
        #reponse de retour
        return {'donnees': donnees, 'message': "l'emplacement a été ajouté"}