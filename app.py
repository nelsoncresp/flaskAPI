from flask import Flask, jsonify, request
from models.personas_model import PersonasModel, Persona

app = Flask(__name__)

# Inicializa el modelo de personas
modelo_personas = PersonasModel()

# Rutas de la API
# Listar todas las personas
@app.route('/personas', methods=['GET'])
def get_personas():
    return jsonify({"personas": [persona.__dict__ for persona in modelo_personas.obtener_personas()]})

# Encontrar una persona por su id
@app.route('/personas/<int:id>', methods=['GET'])
def get_persona(id):
    persona = modelo_personas.obtener_persona_por_id(id)
    if not persona:
        return jsonify({"error": "Persona no encontrada"}), 404
    return jsonify({"persona": persona.__dict__})

# Añadir una nueva persona
@app.route('/personas', methods=['POST'])
def add_persona():
    nueva_persona_data = request.json
    nueva_persona = Persona(**nueva_persona_data)
    persona_agregada = modelo_personas.agregar_persona(nueva_persona)
    return jsonify({"message": "Persona añadida correctamente", "persona": persona_agregada.__dict__}), 201

# Actualizar una persona existente
@app.route('/personas/<int:id>', methods=['PUT'])
def update_persona(id):
    datos_actualizados = request.json
    persona_actualizada = modelo_personas.actualizar_persona(id, datos_actualizados)
    if not persona_actualizada:
        return jsonify({"error": "Persona no encontrada"}), 404
    return jsonify({"message": "Persona actualizada correctamente", "persona": persona_actualizada.__dict__})

# Eliminar una persona
@app.route('/personas/<int:id>', methods=['DELETE'])
def delete_persona(id):
    if modelo_personas.eliminar_persona(id):
        return jsonify({"message": "Persona eliminada correctamente"}), 200
    else:
        return jsonify({"error": "Persona no encontrada"}), 404

if __name__ == "__main__":
    app.run(debug=True, port=4000)
