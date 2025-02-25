from flask import Flask, render_template, request

app = Flask(__name__)


cursos = [
    'Ingeniería en sistemas computacionales', 
    'Ingeniería industrial', 
    'Ingeniería civil', 
    'Ingeniería mecatrónica', 
    'Ingeniería electrónica'
]


@app.route('/')
def index():
    data = {
        'titulo': 'OrientaTec Zapopan',
        'bienvenida': 'OrientaTec Zapopan',
        'cursos': cursos,
        'numero_cursos': len(cursos),
    }

    
    preguntas = [
        {'texto': '¿Disfrutas resolviendo problemas lógicos y creando soluciones mediante la tecnología?', 'respuestas': ['Sí', 'No']},
        {'texto': '¿Te interesa trabajar en proyectos colaborativos?', 'respuestas': ['Sí', 'No']},
        {'texto': '¿Te gusta diseñar y construir estructuras como edificios, puentes o carreteras?', 'respuestas': ['Sí', 'No']},
        {'texto': '¿Te apasiona la robótica y la automatización de procesos mediante sistemas mecánicos y electrónicos?', 'respuestas': ['Sí', 'No']},
        {'texto': '¿Te interesa la electrónica y cómo funcionan los circuitos, sensores y dispositivos tecnológicos?', 'respuestas': ['Sí', 'No']},
        {'texto': '¿Te gustaría trabajar desarrollando software, bases de datos o sistemas computacionales?', 'respuestas': ['Sí', 'No']},
        {'texto': '¿Te motiva diseñar estrategias para mejorar la producción y reducir los costos en una fábrica?', 'respuestas': ['Sí', 'No']},
        {'texto': '¿Prefieres un trabajo donde puedas supervisar construcciones y gestionar materiales de obra?', 'respuestas': ['Sí', 'No']},
        {'texto': '¿Te gustaría diseñar sistemas automatizados que combinen mecánica y electrónica?', 'respuestas': ['Sí', 'No']},
        {'texto': '¿Te interesa desarrollar dispositivos electrónicos innovadores para distintas aplicaciones?', 'respuestas': ['Sí', 'No']},
        {'texto': '¿Te gusta la programación y el desarrollo de aplicaciones para solucionar problemas?', 'respuestas': ['Sí', 'No']},
        {'texto': '¿Te interesa analizar datos y tomar decisiones para mejorar procesos productivos?', 'respuestas': ['Sí', 'No']},
        {'texto': '¿Disfrutas trabajar con planos y modelado de estructuras para mejorar procesos productivos?', 'respuestas': ['Sí', 'No']},
        {'texto': '¿Disfrutas trabajar con planos y modelado de estructuras físicas en computadora?', 'respuestas': ['Sí', 'No']},
        {'texto': '¿Te llama la atención la fabricación de robots o vehículos autónomos?', 'respuestas': ['Sí', 'No']},
        {'texto': '¿Te gustaría diseñar sistemas de telecomunicaciones o trabajar en redes eléctricas?', 'respuestas': ['Sí', 'No']},
        {'texto': '¿Te interesa la inteligencia artificial y el aprendizaje automático?', 'respuestas': ['Sí', 'No']},
        {'texto': '¿Te gusta trabajar con maquinaria industrial y optimizar su rendimiento?', 'respuestas': ['Sí', 'No']},
        {'texto': '¿Te gustaría participar en el diseño de infraestructuras urbanas sostenibles?', 'respuestas': ['Sí', 'No']},
        {'texto': '¿Te interesan las energías renovables y el desarrollo de nuevas tecnologías eléctricas?', 'respuestas': ['Sí', 'No']}
    ]

    return render_template('index.html', data=data, preguntas=preguntas)


@app.route('/resultados', methods=['POST'])
def resultados():
    respuestas_usuario = request.form.to_dict()  

    
    respuestas_carreras = {
        'Ingeniería en sistemas computacionales': ['Sí', 'Sí', 'No', 'No', 'No', 'Sí', 'No', 'No', 'No', 'No', 'Sí', 'No', 'No', 'No', 'No', 'Sí', 'No', 'No', 'No', 'No'],
        'Ingeniería industrial': ['No', 'Sí', 'No', 'No', 'No', 'No', 'Sí', 'No', 'No', 'No', 'No', 'Sí', 'No', 'No', 'No', 'Sí', 'Sí', 'No', 'No', 'No'],
        'Ingeniería civil': ['No', 'No', 'Sí', 'No', 'No', 'No', 'No', 'Sí', 'No', 'No', 'No', 'No', 'Sí', 'No', 'No', 'No', 'No', 'Sí', 'No', 'No'],
        'Ingeniería mecatrónica': ['No', 'No', 'No', 'Sí', 'Sí', 'No', 'No', 'No', 'Sí', 'Sí', 'No', 'No', 'No', 'Sí', 'No', 'Sí', 'No', 'Sí', 'Sí', 'No'],
        'Ingeniería electrónica': ['No', 'No', 'No', 'No', 'Sí', 'No', 'No', 'No', 'No', 'Sí', 'No', 'No', 'No', 'No', 'Sí', 'No', 'Sí', 'No', 'Sí', 'Sí']
    }

    
    respuestas_ordenadas = [respuestas_usuario.get(f"respuesta_{i}") for i in range(1, len(respuestas_carreras['Ingeniería en sistemas computacionales']) + 1)]

    
    puntuaciones = {}
    for carrera, respuestas_carrera in respuestas_carreras.items():
        puntuacion = 0
        for i, respuesta in enumerate(respuestas_ordenadas):
            if respuesta == respuestas_carrera[i]:
                puntuacion += 1
        puntuaciones[carrera] = puntuacion

  
    carrera_recomendada = max(puntuaciones, key=puntuaciones.get)

    
    return render_template('resultados.html', carrera_recomendada=carrera_recomendada, resultados=puntuaciones)


carreras = [
    {
        "nombre": "Ingeniería en Sistemas Computacionales",
        "descripcion": "Forma profesionales capaces de diseñar, desarrollar e implementar software, gestionar bases de datos, y administrar sistemas de redes. También se capacita en ciberseguridad y áreas de inteligencia artificial.",
        "habilidades": ["Programación", "Desarrollo web", "Análisis de sistemas", "Administración de redes", "Ciberseguridad", "Inteligencia Artificial"],
        "areas_interes": ["Desarrollo de software", "Redes y comunicaciones", "Seguridad informática", "Big Data", "Inteligencia Artificial"],
        "salidas_profesionales": ["Desarrollador de software", "Administrador de redes", "Ingeniero de sistemas", "Analista de datos", "Especialista en ciberseguridad"]
    },
    {
        "nombre": "Ingeniería Industrial",
        "descripcion": "Prepara profesionistas capacitados para optimizar sistemas de producción y gestión de recursos en las industrias. Estudia la eficiencia en el uso de recursos, la mejora de procesos y la calidad.",
        "habilidades": ["Gestión de procesos", "Optimización de recursos", "Control de calidad", "Gestión de proyectos", "Análisis de operaciones"],
        "areas_interes": ["Producción y operaciones", "Logística", "Gestión de calidad", "Gestión empresarial", "Optimización de procesos"],
        "salidas_profesionales": ["Gerente de operaciones", "Ingeniero de procesos", "Consultor en mejora continua", "Especialista en logística", "Gerente de planta"]
    },
    {
        "nombre": "Ingeniería Civil",
        "descripcion": "Forma profesionales capacitados para diseñar, construir y supervisar proyectos de infraestructura, como carreteras, puentes, edificios y obras hidráulicas, garantizando la seguridad y el cumplimiento de normas.",
        "habilidades": ["Diseño estructural", "Construcción de obras civiles", "Cálculo estructural", "Gestión de proyectos", "Geotecnia"],
        "areas_interes": ["Construcción", "Gestión de proyectos", "Urbanismo", "Infraestructura hidráulica", "Topografía"],
        "salidas_profesionales": ["Ingeniero civil", "Director de obras", "Especialista en gestión de proyectos", "Consultor en construcción", "Inspector de obras"]
    },
    {
        "nombre": "Ingeniería Mecatrónica",
        "descripcion": "Combina la ingeniería mecánica, electrónica, informática y de control para diseñar, fabricar y mantener sistemas automatizados y robots. Se enfoca en la creación de soluciones tecnológicas innovadoras.",
        "habilidades": ["Diseño de sistemas automatizados", "Robótica", "Mecánica", "Electrónica", "Programación de controladores", "Análisis de sistemas"],
        "areas_interes": ["Robótica", "Automatización industrial", "Sistemas embebidos", "Inteligencia artificial aplicada", "Control de procesos"],
        "salidas_profesionales": ["Ingeniero en robótica", "Diseñador de sistemas automatizados", "Ingeniero en control de procesos", "Desarrollador de sistemas embebidos", "Consultor en automatización"]
    },
    {
        "nombre": "Ingeniería Electrónica",
        "descripcion": "Se enfoca en el diseño, desarrollo y mantenimiento de circuitos electrónicos, sistemas de comunicaciones, dispositivos y equipos electrónicos. Además, abarca áreas como la automatización y la instrumentación.",
        "habilidades": ["Diseño de circuitos electrónicos", "Sistemas de comunicación", "Instrumentación", "Electrónica de potencia", "Automatización", "Microcontroladores"],
        "areas_interes": ["Diseño de circuitos", "Telecomunicaciones", "Electrónica industrial", "Sistemas embebidos", "Electrónica de consumo"],
        "salidas_profesionales": ["Ingeniero en telecomunicaciones", "Diseñador de circuitos electrónicos", "Ingeniero en sistemas embebidos", "Especialista en automatización", "Consultor en electrónica"]
    }
]


@app.route('/informacion')
def informacion():
    return render_template('informacion.html', carreras=carreras)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
