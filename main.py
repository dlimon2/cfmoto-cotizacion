# app.py
from flask import Flask, render_template, request, jsonify
from decimal import Decimal
from dotenv import load_dotenv
import json

load_dotenv()
app = Flask(__name__)

# Datos de ejemplo de motos CFMoto (estos datos deberían venir de una base de datos en producción)
MOTOS = {
    '450NK': {
        'nombre': '450NK',
        'precio_base': 89990,
        'categoría': 'Naked',
        'cilindrada': '450cc',
        'colores': ['Negro', 'Azul', 'Blanco'],
        'imagen_base': '450nk.jpeg'
    },
    '450SR': {
        'nombre': '450SR',
        'precio_base': 159990,
        'categoría': 'Sport',
        'cilindrada': '450cc',
        'colores': ['Gris', 'Negro', 'Rojo'],
        'imagen_base': '450sr.jpeg'
    }
}

# Configuraciones de financiamiento
PLAZOS = [12, 24, 36, 48]
TASA_INTERES = 0.16  # 16% anual

@app.route('/')
def index():
    return render_template('index.html', motos=MOTOS)

@app.route('/obtener-moto/<modelo>')
def obtener_moto(modelo):
    if modelo in MOTOS:
        return jsonify(MOTOS[modelo])
    return jsonify({'error': 'Modelo no encontrado'}), 404

@app.route('/calcular-financiamiento', methods=['POST'])
def calcular_financiamiento():
    datos = request.json
    modelo = datos.get('modelo')
    plazo = int(datos.get('plazo'))
    enganche = float(datos.get('enganche'))
    
    if modelo not in MOTOS:
        return jsonify({'error': 'Modelo no encontrado'}), 404
    
    precio = MOTOS[modelo]['precio_base']
    monto_financiar = precio - enganche
    
    # Cálculo de pagos mensuales (usando fórmula de amortización)
    tasa_mensual = TASA_INTERES / 12
    factor = (tasa_mensual * (1 + tasa_mensual)**plazo) / ((1 + tasa_mensual)**plazo - 1)
    pago_mensual = monto_financiar * factor
    
    return jsonify({
        'pago_mensual': round(pago_mensual, 2),
        'monto_total': round(pago_mensual * plazo + enganche, 2),
        'plazo': plazo
    })

if __name__ == '__main__':
    app.run(debug=True)