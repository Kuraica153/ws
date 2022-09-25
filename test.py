from utils.converter import Converter
import base64
import yaml

data = 'LS0tDQogIG5hbWU6IENocmlzDQogIGhlaWdodDogMTg1DQogIHdlaWdodDogODgNCi0tLQ=='

data = base64.b64decode(data)

persona = Converter.convert_to_persona(data)


#imc = persona['weight'] / (persona['height'] ** 2)
