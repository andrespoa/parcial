

from flask import Flask, render_template
import os
#5-importar archivo BD
import database as db
#6-ir al indrex y crear el formulario para los datos a ingresar 


#1-acceder al index para ser lanzado
# y unir src y template a la carpeta del proyecto 
template_dir = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))
template_dir = os.path.join(template_dir, "src", "templates")

#2-inicializar flask y renderizar para mostrar el html
app = Flask(__name__, template_folder = template_dir)

#rutas de la aplicación 
@app.route('/')
def home():
    return render_template('index.html')

#3-lanzar la aplicación
if __name__ == '__main__':
    app.run(debug=False, port=5000)


