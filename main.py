from flask import Flask, render_template, url_for
from templates.modules.logica import gen_pass
import random

app = Flask(__name__)

facts_list = ["Elon Musk afirma que las redes sociales están diseñadas para mantenernos dentro de la plataforma, de modo que pasemos el mayor tiempo posible viendo contenidos.", 
            "Según un estudio realizado en 2018, más del 50% de las personas de entre 18 y 34 años se consideran dependientes de sus smartphones.", 
            "Las redes sociales tienen aspectos positivos y negativos, y debemos ser conscientes de ambos cuando utilicemos estas plataformas.", 
            "El estudio de la adicción tecnológica es una de las áreas más relevantes de la investigación científica moderna."]

@app.route('/')
def index():
    return render_template('index.html')



@app.route('/random_facts')
def facts():
    choice_randoms = random.choice(facts_list)
    return render_template('modules/random_fact.html', choice = choice_randoms)

@app.route('/password')
def mostrar_contraseña():
    contraseña = gen_pass(16)
    return render_template('contraseña.html', contraseña=contraseña)
    

if __name__ == '__main__':
    app.run(debug = True)