from __future__ import print_function
import httplib2
import os
from apiclient import discovery
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage
try:
    import argparse
    flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
except ImportError:
    flags = None

#url de servicio con permisos de lectura y escritura
SCOPES = 'https://www.googleapis.com/auth/contacts'
#credenciales de cliente sacada de ADMIN GOOGLE
CLIENT_SECRET_FILE = 'credentials.json'
APPLICATION_NAME = 'People API Python Quickstart'

#funcion para la utenticacion de la credenciales y la pestaña de concentimiento de google para la persona a autenticar
def get_credentials():

    home_dir = os.path.expanduser('./')
    credential_dir = os.path.join(home_dir, '.credentials')
    #se comprueba la existencia de la carpeta .credentials para la contencion de la autenticacion por medio de la pestaña de autenticacion
    if not os.path.exists(credential_dir):
        os.makedirs(credential_dir)
    credential_path = os.path.join(credential_dir,
                                   'people.googleapis.com-python-quickstart.json')

    store = Storage(credential_path)
    credentials = store.get()
    if not credentials or credentials.invalid:
        flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
        flow.user_agent = APPLICATION_NAME
        if flags:
            credentials = tools.run_flow(flow, store, flags)
        else:
            credentials = tools.run(flow, store)
        print('Storing credentials to ' + credential_path)
    return credentials

# funcion para la creacion de un contacto
def cargar(nickname,email):
     credentials = get_credentials()
     http = credentials.authorize(httplib2.Http())
     service = discovery.build('people', 'v1', http=http,
     discoveryServiceUrl='https://people.googleapis.com/$discovery/rest')
     #servicio para la creacion de un contacto enviandoles un body con la estructura y especificando la persona de autenticacion
     service.people().createContact(parent='people/me', body={
             "nicknames": [
                 {
                     "value": nickname
                 }
             ],
             "emailAddresses": [
                 {
                     "value": email
                 }

             ],
             "memberships": [
                 {
                       "contactGroupMembership": {
                      "contactGroupResourceName":"contactGroups/1bcec18a8d3b74d3"
                 }}
                     ]
         }).execute()


