from utils.converter import Converter
import yaml
import base64

class PersonaService():
    
    def get_imc(data):
        
        data = base64.b64decode(data)
        
        persona = Converter.convert_to_persona(data)
        
        imc = persona.weight / (persona.height ** 2)
        
        return imc