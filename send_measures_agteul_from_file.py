#!/usr/bin/python3

'''
sobre inserts: https://www.w3schools.com/python/python_mongodb_insert.asp

como se ejecuta:  ******   python3 send_measures_agteul_from_file.py datos.txt   ******
ejemplo: python3 send_measures_agteul_from_file.py datos.txt
'''

__author__      = "Fabio Suarez"

from datetime import datetime
import os, logging, sys, requests, time


try:

    if len(sys.argv) >= 2:
        print("La cadena introducida tiene",len(sys.argv[1]),"caracteres")
    else:
        print("Este programa necesita parámetros")


    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s %(levelname)s %(message)s',
                        filename='/tmp/' + os.path.basename(__file__),
                        filemode='w')

    console = logging.StreamHandler()
    console.setLevel(logging.INFO)
    formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
    console.setFormatter(formatter)
    logging.getLogger('').addHandler(console)
    logger = logging.getLogger(__name__)


    logging.info('Inicia la ejecucion del script ' + os.path.basename(__file__) + ' a las ' + str(datetime.now()))

    vl_url_agente = 'https://<<URL>>'
    vl_fs = '<<FIWARE_SERVICE>>'
    vl_fsp = '/<<FIWARE_SERVICEPATH>>'
    vl_apikey = 'APIKEY'

    vl_device = ''
    vl_msj = ''
    lineas = []
    cant_insertados = 0
    vl_url = ''

    f = open (sys.argv[1],'r')

    mensaje = f.read()
    lineas = mensaje.split('\n')

    for l in lineas:
        vl_device, vl_msj = l.split(';')

        #EJEMPLO: vl_url_agente/iot/d?i=abcdef&k=vl_apikey&d=ts|2020-10-10T06:45:01.000Z|val|0|bat|127
        vl_url = vl_url_agente + '/iot/d?i=' + vl_device + '&k=' + vl_apikey + '&d=' + vl_msj
        response = requests.get(url=vl_url, headers = {"Fiware-Service": vl_fs, "Fiware-ServicePath": vl_fsp, "Content-Type": "application/json"}, verify=False)

        if response.status_code != 200:
            logging.info('Error en el script ' + os.path.basename(__file__) + ' a las ' + str(datetime.now()) + " -> " + str(response) + " -> " + " error al acceder al servicio")
            logging.error(response.json())
        else:
            print("vl_url:", vl_url)


        cant_insertados = cant_insertados +1
        time.sleep(1)


    print("cantidad insertados:", cant_insertados)
    logging.info('Finaliza la ejecucion del script ' + os.path.basename(__file__) + ' a las ' + str(datetime.now()))


except Exception as e:
    print("Error:", e, e.__doc__)
    logging.info('Error en el script ' + os.path.basename(__file__) + ' a las ' + str(datetime.now()) + " -> " + e.__doc__)

finally:
    try:
        f.close()
    except Exception:
        pass