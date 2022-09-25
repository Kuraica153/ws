from schemas.persona import Persona


class Converter:
    '''
    Get the string data and convert it to a dictionary of the Persona class
    '''
    def convert_to_persona(data) -> Persona:
        data = data.__str__()
        data = data.split('\\r\\n ')

        persona = {}

        for i in range(1, len(data)):
            item = data[i].split(': ')
            persona[item[0].replace(' ','')] = item[1].replace("\\r\\n---'",'')

            if(i >= 2):
                persona[item[0].replace(' ','')] = float(persona[item[0].replace(' ','')])

        return Persona(**persona)