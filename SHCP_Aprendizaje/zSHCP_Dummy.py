#------------------------------------------------------------------------------------------------------------------------------------------
#   INTRODUCCIÓN A FASTAPI 
#------------------------------------------------------------------------------------------------------------------------------------------
# --¿Qué es FastAPI?.
# FastAPI es un “framework” web moderno y de alto rendimiento diseñado para construir APIs con Python (a partir de Python 3.7.+), 
# es de fácil manejo y con un rendimiento excepcional.

# --Framework.
# Un “Framework” o “Marco de Trabajo” (por su traducción del inglés) es un esquema o “estructura” que se establece para desarrollar y 
# organizar un software de una forma determinada.
# Esta definición en principio puede resultar compleja, pero si la resumimos podríamos decir que 
# “Es un Entorno pensado para facilitar las labores de desarrollo.
# Un Framework platica muchas ventajas para los Desarrolladores, ya que los Framework automatizan muchos procesos que en su ausencia 
# serían muy repetitivos, como puede ser; las conexiones a las Bases de Datos o el llamado a Servicios Web.

# --Librería vs Framework.
# • Librería: Es un conjunto de funciones y métodos que puedes importar y usar en tu código para realizar tareas específicas. 
#     Por ejemplo, requests es una librería en Python que puedes importar para realizar solicitudes HTTP.
# • Framework: Es una estructura más amplia que proporciona un esqueleto o una arquitectura para desarrollar aplicaciones. 
#     Un framework define cómo organizar y estructurar tu aplicación, proporcionando componentes básicos y herramientas para facilitar 
#     el desarrollo.

# --API.
# Una API (“Application Programing Interface”) es una interfaz por la cuál permite a diferentes sistemas informáticos pueden 
# comunicarse entre sí y compartir datos o funcionalidades de manera estandarizada y segura.
# Para explicarlo de la mejor manera posible, pongamos un ejemplo: 
# “Imaginemos que queremos desarrollar una aplicación tipo UBER , una aplicación que ofrezca servicios de transporte, en donde 
# se haga seguimiento de los vehículos que se encuentran en la ciudad dando el servicio en tiempo real. Para llevar acabo una aplicación 
# así, necesitaríamos de Mapas y Geolocalización, debemos tener mapas de la ciudad, crearlos desde cero costaría demasiado dinero y 
# tiempo, así que lo mejor sería conectarnos a una aplicación como “Google Maps” la cuál ya tiene toda una infraestructura cartográfica 
# muy desarrollada y avanzada, ya que ellos han invertido millones en imágenes territoriales provenientes de satelitales, de aviones, 
# de helicópteros, de carros, de gente con cámaras en la cabeza. Por lo tanto podríamos aprovechar todo este desarrollo llevado acabo 
# por Google Maps para poner en marcha nuestra aplicación.” Razones por las que una API puede ser beneficiosa para el desarrollo de una 
# aplicación.
# • Reutilización de funcionalidades:
#     Al conectarse a través de una API a otras aplicaciones o servicios, puedes aprovechar las funcionalidades existentes en lugar de 
#     desarrollarlas desde cero. Esto ahorra tiempo y recursos en el desarrollo de tu propia aplicación.
# • Acceso a datos externos:
#     Las API te permiten acceder a datos externos que pueden ser útiles para tu aplicación, como información meteorológica, 
#     datos de ubicación, información de usuarios, etc. Esto enriquece la funcionalidad de tu aplicación y mejora la experiencia 
#     del usuario.
# • Escalabilidad y flexibilidad:
#     Al construir tu aplicación sobre una infraestructura de API, tienes la flexibilidad de escalar y adaptar tu aplicación fácilmente 
#     según sea necesario. Puedes agregar o eliminar funcionalidades simplemente conectándote o desconectándote de diferentes APIs.
# • Mejora del rendimiento y la seguridad:
#     Al utilizar APIs de empresas reconocidas, puedes confiar en su experiencia y enfoque en la seguridad y el rendimiento. Esto puede 
#     mejorar la calidad y la fiabilidad de tu propia aplicación.
# En resumen, las APIs son herramientas poderosas que pueden potenciar el desarrollo de aplicaciones al permitir la integración con otras
# plataformas y servicios, ampliando así las capacidades y el alcance de tu propia aplicación.
#------------------------------------------------------------------------------------------------------------------------------------------

#------------------------------------------------------------------------------------------------------------------------------------------
#   INSTALACIÓN DE FASTAPI
#------------------------------------------------------------------------------------------------------------------------------------------
# --Instalación del FastAPI:
# FastAPI es compatible con varios servidores ASGI, pero Uvicorn es el más comúnmente utilizado en el desarrollo. 
# Puedes instalar ambos usando pip desde la Consola de Comandos/Símbolo del Sistema con la siguiente instrucción: 

#                     pip install fastapi uvicorn

# --Uvicorn: 
# Es un servidor web de tipo “ASGI” (Asynchronous Server Gateway Interface / Interfaz de Pasarela de Servidor Asincrónica) de alto rendimiento 
# diseñado para admitir operaciones asíncronas (operaciones que ejecutan múltiples tareas de forma concurrente, permitiendo que el código 
# continúe ejecutándose mientras se espera la finalización de operaciones de entrada/salida u otras tareas bloqueantes) y aplicaciones web en 
# tiempo real en Python. Fue desarrollado para admitir aplicaciones web modernas que utilizan asincronía para manejar solicitudes de manera 
# eficiente.
#------------------------------------------------------------------------------------------------------------------------------------------

#-----------------------------------------------------------------------------------------------------------------------------------------
#   ANALISIS DE LOS COMPONENTES BÁSICOS DE UNA APLICACIÓN EN FASTAPI
#-----------------------------------------------------------------------------------------------------------------------------------------
# --Framework: proporciona una infraestructura completa para construir APIs web rápidas y modernas
#
#                     from fastapi import FastAPI
#
# --Instancia FastaPI: Cuando creas una instancia de “FastAPI”, estás creando la aplicación web en sí. Todo lo que hagas para configurar tu 
#   aplicación se define a partir de esta instancia,.actúa como el punto de entrada principal para tu aplicación. Es el objeto a través del cual 
# defines y configuras todos los aspectos de la aplicación, desde las rutas hasta la configuración de seguridad y la gestión de errores.
#
#                     app = FastAPI()
#
# --Declaración de un Endpoint: 
#   •   Decorador: los decoradores en FastAPI son una forma elegante y declarativa de definir rutas (endpoints) y cómo se manejan las solicitudes 
#       HTTP dentro de tu aplicación.
#
#                           @app
#
#   •   Endpoint: La combinación de una ruta y un método HTTP
#
#                         .get("/")
#
#   •   Métodos de petición “HTTP”: FastAPI utiliza los metódos HTTP estándar para definir cómo interactuán los clientes con la API.
#       Aquí están los principales métodos HTTP y su función en FastAPI:
#       --Método “GET”: Método cuya función es SOLICITAR / OBTENER / RECUPERAR información o datos de un “recurso”.
#       --Método “POST“: Método cuya función es ENVIAR nueva información o datos de a un “recurso”.
#       --Método “PUT”: Método cuya función es ACTUALIZAR la información o datos de un “recurso”.
#       --Método “PATCH”: Método cuya función es ACTUALIZAR PARCIALMENTE la información o datos de un “recurso”.
#       --Método “DELETE”: Método cuya función es ELIMINAR la información o datos de un “recurso”.
#
#                         .get("/")
#
#   •   Ruta: es la parte de una URL que identifica un recurso específico en tu aplicación web. Por ejemplo, en la URL "https://tudominio.com/productos", 
#       "/productos" es la ruta que indica que estás accediendo a la página de productos en el servidor. En estos primeros ejemplos manejaremos la 
#       denominada “Ruta Raíz”.
#       
#       ?   Ruta Raíz: es la ruta predeterminada que te lleva al recurso por default
#
#                            "/"
#       
#       ?   Ruta: es la ruta que definimos, te lleva a un recurso en especifíco      
#                           
#                          "/about"
# 
#       Hay otros tipos de ruta, como “Parámetros de Ruta” o “Rutas de Consulta” que eventualmente conoceremos.
#  
#   •   Función Operación de Ruta o Función Manejadora: esta función se encarga de manejar las solicitudes HTTP que llegan a una ruta específica, procesando 
#       cualquier parámetro de la URL necesario, ejecutando la lógica de negocio correspondiente (como consultar una base de datos o realizar cálculos), y 
#       finalmente devolviendo una respuesta adecuada, la cual FastAPI convierte automáticamente en un formato compatible (generalmente JSON) para ser enviado 
#       de vuelta al cliente que realizó la solicitud.
#
#                      def read_root():
#
#                          return {"Hello": "World"}
# 
#   •   JSON (JavaScript Object Notation): es un formato de intercambio de datos ligero y fácil de leer que se utiliza para transmitir datos estructurados entre 
#       un servidor y un cliente, o entre diferentes componentes de una aplicación. Es ampliamente utilizado en el desarrollo de aplicaciones web y APIs debido a
#       su simplicidad y facilidad de uso.
#
#                     {"Hello": "World"}
# 
#------------------------------------------------------------------------------------------------------------------------------------------

# #------------------------------------------------------------------------------------------------------------------------------------------
# #   PRIMER APLICACIÓN
# #-----------------------------------------------------------------------------------------------------------------------------------------

# # Empezamos importando nuestro framework FastAPI en el programa, cabe aclarar que esto es un framework y no una clase.    
# from fastapi import FastAPI

# # Creamos una instancia del framework FastAPI llamada "app"
# app = FastAPI()

# # Usamos el decorador @app.get para definir una ruta GET en "/"
# @app.get("/")
# # Definimos la función read_root que se ejecutará cuando se haga una solicitud GET a "/"
# def read_root():
#     # Retorna un String
#     return "Hello"

# #------------------------------------------------------------------------------------------------------------------------------------------
# #   IMPORTANTE!!!
# #------------------------------------------------------------------------------------------------------------------------------------------

# # Debemos siempre decorar una función Cuando usas un decorador como @app.get("/"), estás registrando una ruta para el método HTTP GET en la ruta raíz ("/").
# # El término "decorar" se usa en un sentido más general en Python, pero en el contexto de FastAPI, estamos específicamente registrando rutas y asociándolas con 
# # funciones que manejan las solicitudes a esas rutas.
# #
# #                      @app.get("/")
# #
# # ¿Qué pasa si no "decoramos" una función

# from fastapi import FastAPI

# app = FastAPI()

# def read_root():
#     return "Hello"

# # Si no decoras una función en una aplicación FastAPI, esa función no estará asociada a ninguna ruta y, por lo tanto, no se ejecutará en respuesta a una solicitud HTTP.
# # En otras palabras, la función existirá en tu código, pero FastAPI no sabrá cuándo ni cómo llamarla, ya que no está registrada como un manejador de rutas.

# #------------------------------------------------------------------------------------------------------------------------------------------
# # Devolviendo un diccionrio
# #------------------------------------------------------------------------------------------------------------------------------------------

# from fastapi import FastAPI

# app = FastAPI()

# @app.get("/")
# def read_root():
#     # La función devuelve un diccionario que será automáticamente convertido a JSON
#     return {"Hello": "World"}

# #------------------------------------------------------------------------------------------------------------------------------------------
# # Devolviendo un diccionario con un diccionario dentro 
# #------------------------------------------------------------------------------------------------------------------------------------------

# from fastapi import FastAPI

# app = FastAPI()

# @app.get("/")
# def read_root():
#     # En este ejemplo devolvemos un diccionario con la clave "data" y el valor {"Hello": "World"}
#     return {"data": {"Hello": "World"}}

# #------------------------------------------------------------------------------------------------------------------------------------------
# # Devolviendo una lista dentro 
# #------------------------------------------------------------------------------------------------------------------------------------------

# from fastapi import FastAPI

# app = FastAPI()

# @app.get("/")
# def read_root():
#     # Devolvemos una lista de elementos
#     return ["Elemento 1", "Elemento 2", "Elemento 3"]

# # ------------------------------------------------------------------------------------------------------------------------------------------
# # Devolviendo un un Json con una lista dentro 
# # ------------------------------------------------------------------------------------------------------------------------------------------

# from fastapi import FastAPI

# app = FastAPI()

# @app.get("/")
# def read_root():
#     # Devolvemos un diccionario con una clave "data" que contiene una lista de elementos
#     return {"data": ["Elemento 1", "Elemento 2", "Elemento 3"]}

# #------------------------------------------------------------------------------------------------------------------------------------------
# # Cambiando la ruta de un endpoint para convertirlo en otro endpoint
# #------------------------------------------------------------------------------------------------------------------------------------------

# from fastapi import FastAPI

# app = FastAPI()

# @app.get("/")
# def read_root():
#     # Devolvemos un diccionario con una clave "data" que contiene una lista de elementos
#     return {"data": ["Elemento 1", "Elemento 2", "Elemento 3"]}

# # Aquí por primera vez cambiamos la Ruta Raíz, usamos el decorador @app.get para definir una ruta GET en "/ruta_2"
# @app.get("/ruta_2")
# def read_root():
#     # Devolvemos un diccionario con una clave "data" que contiene a otro diccionario 
#     return {"data_2": {"Elemento 1", "Elemento 2"}}

# #------------------------------------------------------------------------------------------------------------------------------------------
# # Caso con el mismo nombre 
# #------------------------------------------------------------------------------------------------------------------------------------------

# from fastapi import FastAPI

# app = FastAPI()

# @app.get("/")
# def read_root():
#     # Devolvemos un diccionario con una clave "data" que contiene una lista de elementos
#     return {"data": ["Elemento 1", "Elemento 2", "Elemento 3"]}

# # Aquí por primera vez cambiamos la Ruta Raíz, usamos el decorador @app.get para definir una ruta GET en "/ruta_2"
# @app.get("/")
# def read_root():
#     # Devolvemos un diccionario con una clave "data" que contiene a otro diccionario 
#     return {"data_2": {"Elemento 1", "Elemento 2"}}

# # En este código hay un problema: ambas funciones decoradoras tienen la misma ruta y el mismo nombre read_root. 
# # La segunda definición sobrescribirá a la primera, lo que puede llevar a un comportamiento inesperado o errores. Entonces debemos correfir los nombres de las funciones
# # decoradoras y si se puede de las funciones, para que no se sobreescriban:

# from fastapi import FastAPI

# app = FastAPI()

# @app.get("/")
# def read_root():
#     # Devolvemos un diccionario con una clave "data" que contiene una lista de elementos
#     return {"data": ["Elemento 1", "Elemento 2", "Elemento 3"]}

# # Aquí por primera vez cambiamos la Ruta Raíz, usamos el decorador @app.get para definir una ruta GET en "/ruta_2"
# @app.get("/about")
# def read_root_2():
#     # Devolvemos un diccionario con una clave "data" que contiene a otro diccionario 
#     return {"data_2": {"Elemento 1", "Elemento 2"}}

# #------------------------------------------------------------------------------------------------------------------------------------------
# # Tres Endpoints con mismo endpoint y mismo nombre de función
# #------------------------------------------------------------------------------------------------------------------------------------------

# # Si tenemos el siguiente caso:

# from fastapi import FastAPI

# app = FastAPI()

# @app.get("/")
# def read_root():
#     # Devolvemos un diccionario con una clave "data" que contiene una lista de elementos
#     return {"data": ["Elemento 1"]}

# @app.get("/")
# def read_root():
#     # Devolvemos un diccionario con una clave "data" que contiene una lista de elementos
#     return {"data": ["Elemento 1", "Elemento 2"]}

# @app.get("/")
# def read_root():
#     # Devolvemos un diccionario con una clave "data" que contiene una lista de elementos
#     return {"data": ["Elemento 1", "Elemento 2", "Elemento 3"]}

# # Como tal s+olo ejecutará sólo la primer función decoradora 

# #------------------------------------------------------------------------------------------------------------------------------------------
# # Extendiendo ruta
# #------------------------------------------------------------------------------------------------------------------------------------------

# from fastapi import FastAPI

# app = FastAPI()

# # Podemos extender la ruta lo más que queramos 
# @app.get("/extendiendo/la_ruta")
# def abc():
#     return {'data':"Luis"}

# # Recordar que debemos acompletar el link "127.0.0.0.1:8000/exteniendo/la_ruta" 

# #------------------------------------------------------------------------------------------------------------------------------------------
# # IMPORTANTISÍMOOO!!!
# #------------------------------------------------------------------------------------------------------------------------------------------

# from fastapi import FastAPI

# app = FastAPI()

# # Ruta que termina en "/"
# @app.get("/extendiendo/la_ruta/")
# def abc():
#     return {'data':"Luis"}

# # Ruta que termina sin "/"
# @app.get("/extendiendo/la_ruta")
# def abc():
#     return {'data':"Luis"}

# # Serán diferentes rutas por el sólo hecho de tener un "/" de diferencia

# #------------------------------------------------------------------------------------------------------------------------------------------
# # Enrutado Dinámico 
# #------------------------------------------------------------------------------------------------------------------------------------------

# from fastapi import FastAPI

# app = FastAPI()

# # Cuando escribamos la ruta, podremos escribir los que sea en el parámetro de ruta "{enrutado_dinamicos}" y de todos modos nos devolverá el Json "{ data:Luis }"
# @app.get("/ruta/{enrutado_dinamicos}")
# def abc():
#     return {'data':"Luis"}

# #------------------------------------------------------------------------------------------------------------------------------------------
# # Enrutado Dinámico, en diferente orden
# #------------------------------------------------------------------------------------------------------------------------------------------

# from fastapi import FastAPI

# app = FastAPI()

# # Cuando escribamos la ruta, podremos escribir los que sea en el parámetro de ruta "{enrutado_dinamicos}" y de todos modos nos devolverá el Json "{ data:Luis }"
# @app.get("/{enrutado_dinamicos}/ruta/")
# def abc():
#     return {'data':"Luis"}

# #------------------------------------------------------------------------------------------------------------------------------------------
# # Recordar
# #------------------------------------------------------------------------------------------------------------------------------------------
# from fastapi import FastAPI

# app = FastAPI()

# @app.get("/{enrutado_dinamicos}/ruta/")
# def ruta_con_barra(enrutado_dinamicos: str):
#     return {"ruta": "con barra", "valor": enrutado_dinamicos}

# @app.get("/{enrutado_dinamicos}/ruta")
# def ruta_sin_barra(enrutado_dinamicos: str):
#     return {"ruta": "sin barra", "valor": enrutado_dinamicos}

# #------------------------------------------------------------------------------------------------------------------------------------------
# # Enrutado Dinámico con Parámetro Abreviado 
# #------------------------------------------------------------------------------------------------------------------------------------------

# from fastapi import FastAPI

# app = FastAPI()

# # 
# @app.get("/ruta/{enr_din}")
# def abc(enr_din):
#     return {'data': enr_din}

# # ------------------------------------------------------------------------------------------------------------------------------------------
# # Enrutado Dinámico con Parámetro de Ruta de Tipo `int`
# # ------------------------------------------------------------------------------------------------------------------------------------------

# from fastapi import FastAPI

# app = FastAPI()

# # 
# @app.get("/blog/{paramtr}")
# def abc(paramtr : int):
#     return {'data': paramtr}

# # Como lo definios de tipo "int", si en la ruta ponemos un string nos dará error

# # ------------------------------------------------------------------------------------------------------------------------------------------
# # Enrutado Dinámico con Parámetro de Ruta de Tipo `str`
# # ------------------------------------------------------------------------------------------------------------------------------------------

# from fastapi import FastAPI

# app = FastAPI()

# # 
# @app.get("/blog/{paramtr}")
# def abc(paramtr : str):
#     return {'data': paramtr}

# # Como lo definios de tipo "str", si en la ruta ponemos un int nos dará error

# # ------------------------------------------------------------------------------------------------------------------------------------------
# # Dividiendo y taggeando metódos en segmentos, creando un aplicación que devuelve un HTML básico
# # ------------------------------------------------------------------------------------------------------------------------------------------

# from fastapi import FastAPI, HTTPException
# from typing import Optional 
# from fastapi.responses import HTMLResponse

# # Lista Ejemplo:
# movies = [
#     {"id": 1, "title": "STARWARS", "overview": "while my guitar gently weeps", "year": "2009", "rating": "7.8", "category": "Acción"},
#     {"id": 2, "title": "Avatar", "overview": "Rocketman", "year": "2009", "rating": "7.8", "category": "Acción"},
#     {"id": 3, "title": "Platoon", "overview": "while", "year": "2009", "rating": "7.8", "category": "Acción"},
#     {"id": 4, "title": "Alien", "overview": "China Girl", "year": "2009", "rating": "7.8", "category": "Acción"},
#     {"id": 5, "title": "Foundation of Decay", "let it flood, let it wash away": "morning ray", "it conforts me much more": "2022", "rating": "7.8", "get up": "cowaaard!!! "},
#     ]

# app = FastAPI()

# app.title = "Mi Aplicación"
# app.version = "3.3.0"

# @app.get("/blogz", tags=["Home"])
# def index(limit: int = 10, published: bool = True, sort: Optional[str] = None):
#     return {'data': f'{limit} pus {published}'}

# @app.get('/blog/{id}/comments', tags=['Home'])
# def comments(id: int = 23, limit: int = 10):
#     return {'data': f'{limit} pus {id}'}

# @app.get('/html', tags=['Home'])
# def html_f():
#     return HTMLResponse('<h1>Still my guitar gently weeps!!!</h1>')

# @app.get('/Consulta/{id}', tags=['Consulta'])
# def query1(id: int):
#     for movie in movies:
#         if movie['id'] == id:
#             return movie
#     return []
#     # raise HTTPException(status_code=404, detail="Movie not found")

# @app.get('/Consulta2', tags=['Consulta_2'])
# def query2(id2: int):
#     id2-=3
#     return movies[id2]

# # ------------------------------------------------------------------------------------------------------------------------------------------
# # Manejo de Rutas Duplicadas y Prioridad en FastAPI
# # ------------------------------------------------------------------------------------------------------------------------------------------

# from fastapi import FastAPI

# app = FastAPI()

# # Cuando tenemos dos endpoint con la misma ruta de enrutamiento dinámico  

# @app.get("/blog/{paramtr}")
# def abc():
#     return {'data': "adios"}

# @app.get("/blog/{paramtr}")
# def abc():
#     return {'data': "bye"}

# # Sólo ejecutará la primer opción

# #--------------------------------------------------------------------

# # Pero que pasa cuando tenermos una ruta definida

# @app.get("/blog/ruta")
# def abc():
#     return {'data': "au revoir"}

# # Si en la ruta del navegador escribimos esta ruta: "----/blog/ruta", ejecutará este
# # último enpoint, pero si escribimos algo diferente, ejecutará el primer endpoint

# # ------------------------------------------------------------------------------------------------------------------------------------------
# # Conflicto de Rutas con Parámetros Dinámicos y Rutas Específicas
# # ------------------------------------------------------------------------------------------------------------------------------------------

## Ahora bien, si nuestro parámetro fue usado como parámetro de la función 

# from fastapi import FastAPI

# app = FastAPI()

# @app.get("/")
# def abc():
#     return {'data': "Hola"}

# @app.get("/blog/{id}")
# def abc(id: int):
#     return {'id': id}

# @app.get("/blog/unpubliz")
# def abc():
#     return {'data': "all unpublished blogs"}

# # Si ejecutamos el último endpoint "----/blog/unpubliz", nos dará error, lo que pasa es que FastAPI se queda en el anterior endpoint 
# # "----/blog/{id}", e interpreta que queremos meter el valor "unpubliz" al parámetro "{id}" y entonces no pasa de dicho endpoint el cuál
# # habiamos definido como int y por eso malinterpreta el string "unpubliz" y no lo deja pasar

# #------------------------------------------------------------------------------------------------------------------------------------------
# # Enrutado Dinámico con Parámetro Opcional
# #------------------------------------------------------------------------------------------------------------------------------------------

# from fastapi import FastAPI
# from typing import Optional

# app = FastAPI()

# # Definimos un endpoint GET con un parámetro de ruta opcional
# # Si no se proporciona "paramtr", tomará el valor por defecto "default"
# @app.get("/items/{paramtr}")
# def read_item(paramtr: Optional[str] = "default"):
#     return {"data": paramtr}

# #------------------------------------------------------------------------------------------------------------------------------------------
# # Enrutado con Rutas Anidadas
# #------------------------------------------------------------------------------------------------------------------------------------------

# from fastapi import FastAPI

# app = FastAPI()

# # Definimos rutas anidadas para gestionar recursos relacionados
# # La ruta incluye dos parámetros dinámicos: "user_id" e "item_id"
# @app.get("/users/{user_id}/items/{item_id}")
# def read_user_item(user_id: int, item_id: int):
#     return {"user_id": user_id, "item_id": item_id}

# #------------------------------------------------------------------------------------------------------------------------------------------
# # Manejo de Errores con Excepciones Personalizadas
# #------------------------------------------------------------------------------------------------------------------------------------------

# from fastapi import FastAPI, HTTPException

# app = FastAPI()

# # Definimos un endpoint que lanza una excepción personalizada si el parámetro es incorrecto
# @app.get("/items/{item_id}")
# def read_item(item_id: int):
#     # Si el parámetro "item_id" no es 1, se lanza una excepción HTTP 404
#     if item_id != 1:
#         raise HTTPException(status_code=404, detail="Item not found")
#     return {"item_id": item_id, "name": "Item One"}

# #------------------------------------------------------------------------------------------------------------------------------------------
# # Uso de Parámetros de Consulta Básicos
# #------------------------------------------------------------------------------------------------------------------------------------------

# from fastapi import FastAPI

# app = FastAPI()

# # Definimos un endpoint que acepta un parámetro de consulta (query parameter)
# @app.get("/items/")
# def read_items(item_name: str):
#     """
#     item_name: el nombre del ítem a buscar
#     """
#     # Retornamos el nombre del ítem proporcionado
#     return {"item_name": item_name}

#------------------------------------------------------------------------------------------------------------------------------------------
# Uso de Cuerpo de Solicitud (Request Body) Básico
#------------------------------------------------------------------------------------------------------------------------------------------

# from fastapi import FastAPI
# from pydantic import BaseModel

# app = FastAPI()

# # Definimos un modelo Pydantic para el cuerpo de la solicitud
# class Item(BaseModel):
#     name: str
#     description: str

# # Definimos un endpoint que acepta un cuerpo de solicitud
# @app.post("/items/")
# def create_item(item: Item):
#     """
#     item: el objeto del cuerpo de la solicitud que contiene nombre y descripción del ítem
#     """
#     # Retornamos el ítem proporcionado
#     return item

# #------------------------------------------------------------------------------------------------------------------------------------------
# # Otro ejemplo de (Request Body) Básico
# #------------------------------------------------------------------------------------------------------------------------------------------

# from fastapi import FastAPI
# #Importamos BaseModel de Pydantic para hacer un Modelo Pydantic
# from pydantic import BaseModel
# from typing import Optional

# app = FastAPI()

# # Definimos un modelo Pydantic para el cuerpo de la solicitud
# class Blog(BaseModel):
#     # pass         #Lo podemos poner en modo espera si no estamos definiendo nada en la clase
#     title: str  
#     body: str
#     published_at: Optional[bool]    #Este será "Opcional", porque no siempre requeriremos el nombre de donde se publicará

# # Definimos un endpoint que acepta un cuerpo de solicitud
# @app.post("/blog")
# def create_blog(request: Blog):

#     # Nos creará un "request" con todos los atributos o estructura de la clase blog
#     # return request
#     # 
#     return {'data': "Blog is created with title as {request.title}"}

# #------------------------------------------------------------------------------------------------------------------------------------------
# # Cambiando el Puerto
# #------------------------------------------------------------------------------------------------------------------------------------------

# # Si queremos programar un cambio de puerto dentro del código, lo hacemos así

# # Importamos "uvicorn"
# import uvicorn

# #Código que ejecutará, pero esta parte no nos interesa por ahora: -------------------------------------------------------------------------------
# from fastapi import FastAPI
# from pydantic import BaseModel
# from typing import Optional

# app = FastAPI()

# # Definimos un modelo Pydantic para el cuerpo de la solicitud
# class Blog(BaseModel):
#     # pass         #Lo podemos poner en modo espera si no estamos definiendo nada en la clase
#     title: str  
#     body: str
#     published_at: Optional[bool]    #Este será "Opcional", porque no siempre requeriremos el nombre de donde se publicará

# # Definimos un endpoint que acepta un cuerpo de solicitud
# @app.post("/blog")
# def create_blog(request: Blog):
#     return {'data': "Blog is created with title as {request.title}"}
# #------------------------------------------------------------------------------------------------------------------------------------------------

# # Este bloque de código solo se ejecutará si este archivo se ejecuta directamente,  se usa para asegurarse de que un determinado bloque de 
# # código solo se ejecute cuando el script se ejecuta directamente, y no cuando se importa como un módulo en otro script.
# if __name__ == "__main__":
#     # Se ejecutará en el puerto "9000"
#     uvicorn.run(app, host="127.0.0.1", port='9000') 

# #------------------------------------------------------------------------------------------------------------------------------------------
# # Debugging Básico
# #------------------------------------------------------------------------------------------------------------------------------------------

# from fastapi import FastAPI

# app = FastAPI()

# # Definimos un endpoint que usa print para debugging
# @app.get("/debug/")
# def debug_example(value: str):
#     """
#     value: el valor a imprimir para debugging
#     """
#     # Imprimimos el valor para debugging
#     print(f"Debugging value: {value}")
#     return {"debugged_value": value}

# #------------------------------------------------------------------------------------------------------------------------------------------
# # CRUD usando FastAPI para un Blog
# #------------------------------------------------------------------------------------------------------------------------------------------

# # --Primera Parte 1
# # Puedes usar FastAPI para Bases de Datos Relacionales, podemos usar SQLAlchemy el cuál contiene dos entidades que nos serán de mucha ayuda
# # --Definición de Toolkit
# # Un toolkit es un conjunto de herramientas, bibliotecas o componentes que se utilizan para facilitar el desarrollo de software. 
# # Estas herramientas ayudan a los desarrolladores a realizar tareas comunes de manera más eficiente y efectiva. Por ejemplo, un toolkit de 
# # desarrollo web puede incluir utilidades para manejar solicitudes HTTP, formularios, autenticación de usuarios y más.

# # --Definición de Object Relational Mapper (ORM)
# # Un Object Relational Mapper (ORM) es una herramienta que permite a los desarrolladores interactuar con bases de datos relacionales utilizando 
# # objetos de programación en lugar de escribir directamente consultas SQL. Los ORM convierten automáticamente los datos de las tablas de la base 
# # de datos en objetos que pueden ser manipulados en el código y viceversa. Esto simplifica el trabajo con bases de datos y reduce la cantidad de 
# # código SQL que se necesita escribir.

# # Bien veamos:
# # Creamos una nueva carpeta a la que llamaremos "blog", dentro crearemos un archivo que se llamará "__init__.py", luego creamos un -requirement file-
# # el cuál llamaremos "requirements.txt". después necesitamos crear un ambiente virtual, usando esta intrucción en la Terminal "python -m venv blog-env",
# # se creará una carpeta de nombre "blog-env"
# # (archivo de requisitos) tal archivo el cuál es un archivo de texto que lista todas las dependencias necesarias para que el proyecto funcione. 
# # Sirve para gestionar y compartir las bibliotecas y versiones específicas que tu proyecto necesita para ejecutarse correctamente. Lo llamaremos:
# # "requirements.txt", después ejecutaremos este otro comando "pip install -r requirements.txt", creamos un nuevo archivo main.py dentro de nuestra
# # carpeta "blog" y empezamos a programar
# from fastapi import FastAPI

# app = FastAPI()

# @app.post('/blog')
# def create():
#     return 'creating'

# # para ejecutar el anterior código, como tenemos este main.py dentro de la carpeta blog, debemos ejecutarlo en la terminal así: uvicorn blog.main:app
# #----------------------------------------------------------------------------------------------------------------------------------------------------------

# #------------------------------------------------------------------------------------------------------------------------------------------
# # Uso Básico de Esquemas Pydantic
# #------------------------------------------------------------------------------------------------------------------------------------------

# from fastapi import FastAPI
# from pydantic import BaseModel # type: ignore
# from typing import Optional

# app = FastAPI()

# # Definimos un modelo Pydantic
# class Blog(BaseModel):
#     title: str
#     body: str
#     published_at: Optional[bool]
#     username: str
#     email: str

# @app.post('/blog')
# def create_blog(request: Blog):
#     return request

# #------------------------------------------------------------------------------------------------------------------------------------------
# # Uso Básico de Esquemas Pydantic - Caso 2 -
# #------------------------------------------------------------------------------------------------------------------------------------------

# from fastapi import FastAPI
# from pydantic import BaseModel

# # Definimos un modelo Pydantic
# class User(BaseModel):
#     username: str
#     email: str

# app = FastAPI()

# # Definimos un endpoint que acepta y retorna un esquema Pydantic
# @app.post("/user/")
# def create_user(user: User):
#     """
#     user: el objeto del cuerpo de la solicitud que contiene nombre de usuario y correo electrónico
#     """
#     # Retornamos el usuario proporcionado
#     return user

# #------------------------------------------------------------------------------------------------------------------------------------------
# # Conexión Básica a la Base de Datos con SQLAlchemy
# #------------------------------------------------------------------------------------------------------------------------------------------

# from sqlalchemy import create_engine

# # Conexión a una base de datos SQLite en memoria
# DATABASE_URL = "sqlite:///./test.db"
# engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

# #------------------------------------------------------------------------------------------------------------------------------------------
# # Creación de Modelo y Tablas con SQLAlchemy
# #------------------------------------------------------------------------------------------------------------------------------------------

# from sqlalchemy import Column, Integer, String, create_engine, Base

# # Conexión a la base de datos
# DATABASE_URL = "sqlite:///./test.db"
# engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

# # Definimos una base para nuestros modelos
# Base = declarative_base()

# # Definimos un modelo para un blog
# class Blog(Base):
#     __tablename__ = "blogs"
#     id = Column(Integer, primary_key=True, index=True)
#     title = Column(String, index=True)
#     content = Column(String)

# # Creamos las tablas en la base de datos
# Base.metadata.create_all(bind=engine)

# #------------------------------------------------------------------------------------------------------------------------------------------
# # Almacenar un Blog en la Base de Datos
# #------------------------------------------------------------------------------------------------------------------------------------------

# from sqlalchemy.orm import Session
# from fastapi import FastAPI, Depends

# app = FastAPI()

# # Dependencia para obtener la sesión de la base de datos
# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()

# # Definimos un endpoint para crear un blog
# @app.post("/blogs/")
# def create_blog(title: str, content: str, db: Session = Depends(get_db)):
#     """
#     title: el título del blog
#     content: el contenido del blog
#     """
#     new_blog = Blog(title=title, content=content)
#     db.add(new_blog)
#     db.commit()
#     db.refresh(new_blog)
#     return new_blog

# #------------------------------------------------------------------------------------------------------------------------------------------
# # Obtener un Blog de la Base de Datos
# #------------------------------------------------------------------------------------------------------------------------------------------

# @app.get("/blogs/{blog_id}")
# def read_blog(blog_id: int, db: Session = Depends(get_db)):
#     """
#     blog_id: el ID del blog a obtener
#     """
#     return db.query(Blog).filter(Blog.id == blog_id).first()

# #------------------------------------------------------------------------------------------------------------------------------------------
# # Manejo de Excepciones y Códigos de Estado
# #------------------------------------------------------------------------------------------------------------------------------------------

# from fastapi import HTTPException

# @app.get("/blogs/{blog_id}")
# def read_blog(blog_id: int, db: Session = Depends(get_db)):
#     """
#     blog_id: el ID del blog a obtener
#     """
#     blog = db.query(Blog).filter(Blog.id == blog_id).first()
#     if blog is None:
#         raise HTTPException(status_code=404, detail="Blog not found")
#     return blog

# #------------------------------------------------------------------------------------------------------------------------------------------
# # Eliminar un Blog de la Base de Datos
# #------------------------------------------------------------------------------------------------------------------------------------------

# @app.delete("/blogs/{blog_id}")
# def delete_blog(blog_id: int, db: Session = Depends(get_db)):
#     """
#     blog_id: el ID del blog a eliminar
#     """
#     blog = db.query(Blog).filter(Blog.id == blog_id).first()
#     if blog is None:
#         raise HTTPException(status_code=404, detail="Blog not found")
#     db.delete(blog)
#     db.commit()
#     return {"detail": "Blog deleted"}

# #------------------------------------------------------------------------------------------------------------------------------------------
# # Uso de Modelos de Respuesta con Pydantic
# #------------------------------------------------------------------------------------------------------------------------------------------

# from pydantic import BaseModel

# # Definimos un modelo Pydantic para la respuesta
# class BlogResponse(BaseModel):
#     title: str
#     content: str

# @app.get("/blogs/{blog_id}", response_model=BlogResponse)
# def read_blog(blog_id: int, db: Session = Depends(get_db)):
#     """
#     blog_id: el ID del blog a obtener
#     """
#     blog = db.query(Blog).filter(Blog.id == blog_id).first()
#     if blog is None:
#         raise HTTPException(status_code=404, detail="Blog not found")
#     return blog

# #------------------------------------------------------------------------------------------------------------------------------------------
# # Crear un Usuario en la Base de Datos
# #------------------------------------------------------------------------------------------------------------------------------------------

# from pydantic import BaseModel

# # Definimos un modelo Pydantic para el usuario
# class User(BaseModel):
#     username: str
#     email: str

# # Definimos un modelo SQLAlchemy para el usuario
# class UserModel(Base):
#     __tablename__ = "users"
#     id = Column(Integer, primary_key=True, index=True)
#     username = Column(String, unique=True, index=True)
#     email = Column(String, unique=True, index=True)

# @app.post("/users/")
# def create_user(user: User, db: Session = Depends(get_db)):
#     """
#     user: el objeto del cuerpo de la solicitud que contiene nombre de usuario y correo electrónico
#     """
#     new_user = UserModel(username=user.username, email=user.email)
#     db.add(new_user)
#     db.commit()
#     db.refresh(new_user)
#     return new_user

# #------------------------------------------------------------------------------------------------------------------------------------------
# # Hash de Contraseña para Usuarios
# #------------------------------------------------------------------------------------------------------------------------------------------

# from passlib.context import CryptContext

# # Configuramos el contexto de PassLib para hashing
# pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# # Función para hashear una contraseña
# def get_password_hash(password: str):
#     """
#     password: la contraseña en texto plano a hashear
#     """
#     return pwd_context.hash(password)

# #------------------------------------------------------------------------------------------------------------------------------------------
# # Mostrar un Usuario desde la Base de Datos
# #------------------------------------------------------------------------------------------------------------------------------------------

# @app.get("/users/{user_id}")
# def show_user(user_id: int, db: Session = Depends(get_db)):
#     """
#     user_id: el ID del usuario a obtener
#     """
#     return db.query(UserModel).filter(UserModel.id == user_id).first()

# #------------------------------------------------------------------------------------------------------------------------------------------
# # Uso de Etiquetas de Documentación
# #------------------------------------------------------------------------------------------------------------------------------------------

# @app.get("/items/", tags=["items"])
# def read_items():
#     """
#     Este endpoint está etiquetado bajo 'items'
#     """
#     return {"message": "This is an item"}

# #------------------------------------------------------------------------------------------------------------------------------------------
# # Definición de Relaciones entre Modelos SQLAlchemy
# #------------------------------------------------------------------------------------------------------------------------------------------

# from sqlalchemy.orm import relationship

# # Definimos un modelo para el usuario
# class User(Base):
#     __tablename__ = "users"
#     id = Column(Integer, primary_key=True, index=True)
#     username = Column(String, unique=True, index=True)
#     email = Column(String, unique=True, index=True)
#     blogs = relationship("Blog", back_populates="owner")

# # Actualizamos el modelo del blog para incluir la relación
# class Blog(Base):
#     __tablename__ = "blogs"
#     id = Column(Integer, primary_key=True, index=True)
#     title = Column(String, index=True)
#     content = Column(String)
#     owner_id = Column(Integer, ForeignKey("users.id"))
#     owner = relationship("User", back_populates="blogs")

# #------------------------------------------------------------------------------------------------------------------------------------------
# # Uso de Routers para Organizar la API
# #------------------------------------------------------------------------------------------------------------------------------------------

# from fastapi import APIRouter

# # Creamos un router
# router = APIRouter()

# @router.get("/items/")
# def read_items():
#     """
#     Este endpoint está dentro del router
#     """
#     return {"message": "This is an item"}

# # Incluimos el router en la aplicación principal
# app.include_router(router)

# #------------------------------------------------------------------------------------------------------------------------------------------
# # Uso de Operadores de Ruta en Routers
# #------------------------------------------------------------------------------------------------------------------------------------------

# @router.get("/users/{user_id}")
# def read_user(user_id: int):
#     """
#     user_id: el ID del usuario a obtener
#     """
#     return {"user_id": user_id}

# #------------------------------------------------------------------------------------------------------------------------------------------
# # Repositorios para Blog y Usuario
# #------------------------------------------------------------------------------------------------------------------------------------------

# # Repositorio para Blogs
# class BlogRepository:
#     def __init__(self, db: Session):
#         self.db = db

#     def create_blog(self, title: str, content: str):
#         new_blog = Blog(title=title, content=content)
#         self.db.add(new_blog)
#         self.db.commit()
#         self.db.refresh(new_blog)
#         return new_blog

# # Repositorio para Usuarios
# class UserRepository:
#     def __init__(self, db: Session):
#         self.db = db

#     def create_user(self, username: str, email: str):
#         new_user = UserModel(username=username, email=email)
#         self.db.add(new_user)
#         self.db.commit()
#         self.db.refresh(new_user)
#         return new_user

# #------------------------------------------------------------------------------------------------------------------------------------------
# # Login y Verificación de Contraseña
# #------------------------------------------------------------------------------------------------------------------------------------------

# from fastapi import Depends

# # Función para verificar una contraseña
# def verify_password(plain_password: str, hashed_password: str):
#     """
#     plain_password: la contraseña en texto plano a verificar
#     hashed_password: la contraseña hasheada almacenada
#     """
#     return pwd_context.verify(plain_password, hashed_password)

# @app.post("/login/")
# def login(username: str, password: str, db: Session = Depends(get_db)):
#     """
#     username: el nombre de usuario
#     password: la contraseña en texto plano
#     """
#     user = db.query(UserModel).filter(UserModel.username ==

# #------------------------------------------------------------------------------------------------------------------------------------------
# # Generación de Token de Acceso JWT
# #------------------------------------------------------------------------------------------------------------------------------------------

# from datetime import datetime, timedelta
# from jose import JWTError, jwt

# SECRET_KEY = "secret"
# ALGORITHM = "HS256"

# # Función para crear un token de acceso
# def create_access_token(data: dict, expires_delta: timedelta = None):
#     """
#     data: los datos a incluir en el token
#     expires_delta: el tiempo de expiración del token
#     """
#     to_encode = data.copy()
#     if expires_delta:
#         expire = datetime.utcnow() + expires_delta
#     else:
#         expire = datetime.utcnow() + timedelta(minutes=15)
#     to_encode.update({"exp": expire})
#     encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
#     return encoded_jwt

# #------------------------------------------------------------------------------------------------------------------------------------------
# # Protección de Rutas con Autenticación JWT
# #------------------------------------------------------------------------------------------------------------------------------------------

# from fastapi.security import OAuth2PasswordBearer
# from jose import JWTError, jwt
# from fastapi import Depends, HTTPException

# oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# # Función para obtener el usuario actual a partir del token
# def get_current_user(token: str = Depends(oauth2_scheme)):
#     """
#     token: el token JWT a verificar
#     """
#     try:
#         payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
#         username: str = payload.get("sub")
#         if username is None:
#             raise HTTPException(status_code=401, detail="Invalid token")
#     except JWTError:
#         raise HTTPException(status_code=401, detail="Invalid token")
#     return {"username": username}

# @app.get("/users/me")
# def read_users_me(current_user: dict = Depends(get_current_user)):
#     """
#     current_user: el usuario actual obtenido a partir del token
#     """
#     return current_user

#------------------------------------------------------------------------------------------------------------------------------------------
# Despliegue de una Aplicación FastAPI
#------------------------------------------------------------------------------------------------------------------------------------------

# Guardamos el archivo main.py con nuestro código FastAPI

# Instalamos uvicorn si no está instalado
# pip install uvicorn

# Ejecutamos el servidor de desarrollo con el siguiente comando:
# uvicorn main:app --reload

# from fastapi import FastAPI, Path, Query
# from typing import Annotated

# app = FastAPI()

# @app.get("/items/{item_id}")
# async def read_items(
#     item_id: Annotated[int, Path(title="The ID of the item to get")],
#     q: Annotated[str | None, Query(alias="item-query")] = None,
# ):
#     results = {"item_id": item_id}
#     if q:
#         results.update({"q": q})
#     return results



# from fastapi import FastAPI, Path, Query
# from typing import Annotated

# app = FastAPI()

# fake_items_db = [ {"item_name: ":"uno"},
#                   {"item_name: ":"dos"},
#                   {"item_name: ":"tres"}

# ]

# @app.get('/items/')
# async def read_item(skip: int=0, limit: int=10):
#     return fake_items_db[skip: skip + limit]


# E:\luis_sanchezag\SHCP_Documentos\Python\FastAPI_LGSA
















