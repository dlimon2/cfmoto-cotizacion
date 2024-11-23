# Cotización CFMOTO

Autor: Daniel Limón<br>
Email: dani@dlimon.net

Licencia de software pendiente.

Proyecto desarrollado con Flask para generar cotizaciones de motocicletas de la marca CFMOTO. Este repositorio y
sus despliegues no están relacionados directamente con la marca CFMOTO. Este proyecto es de caracter
demostrativo y se deben tener las siguientes consideraciones:

* La información mostrada es únicamente con fines ilustrativos.
* Los precios, modelos y especificaciones no son oficiales.
* Los cálculos financieros son aproximados y no constituyen una oferta real.
* Para información oficial, visite el sitio web oficial de <a hre="https://cfmotomx.com" target="_blank">CFMOTO México</a> o contacte con un distribuidor autorizado.

Este desarrollo es un ejercicio técnico y no debe ser considerado como fuente de información oficial de CFMOTO.

## Ejecución

Linux:
```bash
# Descargar y acceder al repositorio
$ git clone https://github.com/dlimon2/cfmoto-cotizacion
$ cd cfmoto-cotizacion

# Entorno virtual y dependencias
$ python3 -m venv .venv
$ . .venv/bin/activate
$ pip install -r requirements.txt

# Variables de entorno
$ mv .env.example .env

# Ejecución
$ flask run
```
Una vez que se ejecuta el servidor de desarrollo de Flask, el proyecto es accesible en el **puerto 5000** de **localhost** (127.0.0.1)
```bash
 * Serving Flask app 'main.py'
 * Debug mode: on
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:5000
Press CTRL+C to quit
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 250-428-620

```
> **IMPORTANTE:** Para desplegar este proyecto en servidor de producción, se recomienda usar **Gunicorn** o **Vercel** para manejar el despliegue, en lugar del servidor de desarrollo de Flask ($ flask run)

<a href="https://developers.redhat.com/articles/2023/08/17/how-deploy-flask-application-python-gunicorn" target="_blank">Desplegar aplicación de Flask usandio Gunicorn</a>

Cabe mencionar que desplegando esta app en <a href="https://vercel.com" target="_blank">Vercel</a> ahorra el paso de tener que gestionar el despliegue con Gunicorn o cualquier otro servidor WSGI. Se recomienda desplegar esta webapp en Vercel.
