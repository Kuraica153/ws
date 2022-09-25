from pydantic import BaseModel

#Entidades que se reciben o regresar, POST y GET
class Persona(BaseModel):
    name: str
    height: float
    weight: float

