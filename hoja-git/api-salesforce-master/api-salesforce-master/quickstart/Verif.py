from __future__ import print_function
import json
from googleapiclient.discovery import build
from jsonpath_ng.ext import parse
from quickstart.CrearContact import get_credentials




#url de permisos de solo lectura
SCOPES = ['https://www.googleapis.com/auth/contacts.readonly']
#funcion de comprobante de existencia del email
def verificar(email):

    service = build('people', 'v1', credentials=get_credentials())
    token=None
    #contadores para poder concretar una exelente paginacion
    contador = 1
    personas=2001
    while  contador <= int(personas):
      #result captura la respuesta del servicio de lista de contactos (solo permite un maximo de 2000 por paginacion)
      results = service.people().connections().list(
        resourceName='people/me',
        pageSize=2000,
        personFields='names,emailAddresses',
        pageToken=token).execute()
      #se obtiene el token de paginacion y se limpia
      path = (match.value for match in parse('$.nextPageToken').find(results))
      personas = (match.value for match in parse('$.totalPeople').find(results))
      personas = json.dumps(list(personas))
      personas = personas.replace("[", "")
      personas = personas.replace("]", "")
      cadena = json.dumps(list(path))
      cadena = cadena.replace("[\"", "")
      cadena = cadena.replace("\"]", "")
      #se carga el token de paginacion
      token =cadena


      connections = results.get('connections', [])
      #se obtiene los email dentro de people
      flag = False
      for person in connections:
        contador = contador + 1
        names = person.get('emailAddresses', [])
        # se verifica la existencia de los email
        if names:
            name = names[0].get('value')
            if email == name:
             flag=True
    #se retorna el booleano
    return flag



