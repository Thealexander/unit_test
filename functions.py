import io
from datetime import datetime

def registrar_log(id,usuario,correo,ciudad):
    dia = datetime.today().isoformat()

    with open('creation.txt','a') as f:
        f.write(f'{id},{usuario},{correo},{ciudad},{dia}\n')