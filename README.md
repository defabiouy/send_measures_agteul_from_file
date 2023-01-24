
# send_measures_agteul_from_file

Este script tiene como objetivo enviar mediciones al **FIWARE IoT Agent For Ultralight 2.0** (https://fiware-iotagent-ul.readthedocs.io/en/latest/index.html) a partir de un archivo con mediciones obtenidas de kafka.
Para ello, primero se formatea el archivo y luego para cada uno de los mensajes se invoca al agente UL.

Consta de los siguientes pasos:

**1 - obtener el archivo con las mediciones desde kafka**

**2 - ejecutar el script limpiar.sh para darle formato al archivo**
    Cada línea del script está comentada una a una que es lo que hace.
    Como se ejecuta: `limpiar.sh ./datos/datos.txt`
    
   La salida del script es el mismo archivo datos.txt, modificado.
    
**3 - ejecutar el script send_measures_agteul_from_file.py**
    Como se ejecuta: `python3 send_measures_agteul_from_file.py datos.txt`


**Notas:** 
 - El script limpiar.sh debe ejecutarse desde linux ya que es un shell
   bash.
- Tiene un sleep de 1 segundo entre llamado y llamado al agente, para no sobrecargarlo.
