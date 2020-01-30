from __future__ import print_function
import pickle
import os.path
import json
from jsonpath_ng.ext import parse
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import re
from quickstart.CrearContact import cargar
from quickstart.Verif import verificar
from datetime import date, time

#url de direccionamiento para el consumo de la api de google con permisos de solo lectura
SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']


def main():
    #variable tiempo para capturar la fecha actual
    tiempo = date.today()
    print("Dia:",tiempo)
    tiempo = str(tiempo).replace("-", "/")
    #creds la variable que captura las credenciales cargando el pickle token
    creds = None
    #validacion de token pickle
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # validacion de token pickle
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)

        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    #biuld de tipo de servicio a utilizar, version y credenciales autenticadas
    service = build('gmail', 'v1', credentials=creds)
    #query es la variable de filtro de busqueda de mensajes por fecha
    query = 'after:'+tiempo
    Contador_correos=1
    #tamaño recive la lista json con los id de los mensajes de la fecha actual
    tamaño = service.users().messages().list(userId='me', q=query).execute()
    #sice captura el numero de mensajes recibidos
    sice = (match.value for match in parse('$.resultSizeEstimate').find(tamaño))
    if not tamaño:
        print('No mensaje ')
    else:
        #deserealiza el json
        sice = json.dumps(str(list(sice)))

        sice = sice.replace("\"[", "")
        sice = sice.replace("]\"", "")
        print("numero de correos:" + sice)
        print("--------------------------------------------")
        print("                 COMENZAR                   ")
    #recorre toda las lista de mensajes
    vector_vemsaje = 0
    while vector_vemsaje < int(sice):
        vector_vemsaje = str(vector_vemsaje)
        results = service.users().messages().list(userId='me', q=query).execute()

        #captura el id del mensaje que esta en la posicion recorrida
        serial = (match.value for match in parse('$.messages.[' + vector_vemsaje + '].id').find(results))
        if not results:
            print('No mensaje found.')
        else:
            print('ID_Mensajes:',Contador_correos)
            Contador_correos=Contador_correos+1
            # se deserializa y se limpia el string con replace
            id_mensaje2 = json.dumps(str(list(serial)))
            id_mensaje2 = id_mensaje2.replace("\"['", "")
            id_mensaje2 = id_mensaje2.replace("']\"", "")
            print(id_mensaje2)
            #results captura un json con toda la informacion de un mensaje especificado con su id de mensaje y el usuario autenticado

            results = service.users().messages().get(userId='gerencia@parrajimenezasesores.com.co', id=id_mensaje2).execute()


            #path captura los campos del json para identificar quien envio el mensaje
            path = (match.value for match in parse('$.payload.headers[?(@.name=="From")].value').find(results))

            if not results:
                print('No mensaje found.')
            else:

                print('Mensajes:')
                #se deserializa y se obtienen los datos con jsonpath como el nombre apellido y el correo electronico
                cadena = json.dumps(list(path))
                print(cadena)
                sub_cadena = re.search(r"[\w\-][\w\-\.]+@[\w\-][\w\-\.]+[a-zA-Z]{1,4}", cadena)
                email = sub_cadena.group()

                sub_cadena = re.search(r"[a-zA-Z]\w+\s[\w]\w+|[a-zA-Z]\w+", cadena)
                nickname = sub_cadena.group()
                print(email)
                print(nickname)
                #se llama la funcion verificar para comprobar que el email enviado no exista dentro de los contactos de la persona autenticada
                flag = verificar(email)
                #se termina de recorrer el vector sumandole 1 al contador
                vector_vemsaje = int(vector_vemsaje) + 1
                #flag recibe un boleano que comprueba la existencia del contacto
                if flag is True:
                    print("contacto ya existente")
                    print("--------------------------------------------")
                else:
                    #una vez se comprueba que no existe el correo se procede a crear los contactos enviando los nombres y el email especificado
                    cargar(nickname, email)

                    print("contacto creado")
                    print("--------------------------------------------")


if __name__ == '__main__':
    main()



