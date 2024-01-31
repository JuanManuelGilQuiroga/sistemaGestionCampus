camper=[
    {
        "Nombre":"Miguel",
        "Apellido":"Castro",
        "Edad":15
    },
    {
        "Nombre":"Maria",
        "Apellido":"Del barrio",
        "Edad":13
    }
]
def save(data):
    camper.append(data)

def getAll():
    return camper