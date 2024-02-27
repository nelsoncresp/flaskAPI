import json

class Persona:
    def __init__(self, nombre, edad, ciudad):
        self.id = None  # El ID se asignará automáticamente al agregar la persona al modelo
        self.nombre = nombre
        self.edad = edad
        self.ciudad = ciudad

class PersonasModel:
    def __init__(self, archivo_json='bd/personas.json'):
        self.archivo_json = archivo_json
        self.personas = self.cargar_personas()

    def cargar_personas(self):
        try:
            with open(self.archivo_json, 'r') as file:
                personas_data = json.load(file)
                return [Persona(**data) for data in personas_data]
        except FileNotFoundError:
            return []
        except json.decoder.JSONDecodeError:
            return []

    def guardar_personas(self):
        personas_data = [{'nombre': persona.nombre, 'edad': persona.edad, 'ciudad': persona.ciudad} for persona in self.personas]
        with open(self.archivo_json, 'w') as file:
            json.dump(personas_data, file, indent=2)

    def obtener_personas(self):
        return self.personas

    def obtener_persona_por_id(self, persona_id):
        for persona in self.personas:
            if persona.id == persona_id:
                return persona
        return None

    def agregar_persona(self, nueva_persona):
        nuevo_id = len(self.personas) + 1
        nueva_persona.id = nuevo_id
        self.personas.append(nueva_persona)
        self.guardar_personas()
        return nueva_persona

    def actualizar_persona(self, persona_id, datos_actualizados):
        persona = self.obtener_persona_por_id(persona_id)
        if persona:
            for key, value in datos_actualizados.items():
                setattr(persona, key, value)
            self.guardar_personas()
        return persona

    def eliminar_persona(self, persona_id):
        personas_actualizadas = [persona for persona in self.personas if persona.id != persona_id]
        if len(personas_actualizadas) < len(self.personas):
            self.personas = personas_actualizadas
            self.guardar_personas()
            return True
        return False