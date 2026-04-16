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