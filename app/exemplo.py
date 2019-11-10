# hug -f api.py
# localhost:8000/teste/2/21
# localhost:8000/endereco/59080000
# localhost/pic
import hug
import io
import requests
import json
from matplotlib import pyplot
from xml.etree import ElementTree

api = hug.get(on_invalid=hug.redirect.not_found)

@hug.get('/calc')
def imc_indice(valor: hug.types.float_number=1):
    return round(float(valor) / 2 , 2)

@api.urls('/teste/{page}/{id}')
def teste(page, id):
    return "Foi selecionada a pagina " + page + " do id " + id

@api.urls('/endereco/{cep}')
def endereco(cep):
    r = requests.get("https://viacep.com.br/ws/"+cep+"/json/")
    data = r.json()
    return data['localidade']

@hug.get('/pic',output=hug.output_format.png_image)
def plot():
    pyplot.plot([1, 2, 3, 4])
    pyplot.ylabel('some numbers')

    image_output = io.BytesIO()
    pyplot.savefig(image_output, format='png')
    image_output.seek(0)
    return image_output