import sys
import time
import random

import os
import shutil
import logging

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from_dir = "/Users/Kuttimma/Downloads"

# Classe Gerenciadora de Eventos
class FileEventHandler(FileSystemEventHandler):

    #1_on_created
    def on_created(self_event):
        print(f'ola, {event.scr_path} foi criado')

    #2_on_deleted
    def on_deleted(self_event):
        print(f'opa, alguem excluiu {event.scr_path}!')

    #3_on_modified
    def on_modified(self_event):
        print(f'ola!, {event.scr_path} foi modificado')

    #4_on_moved
    def on_moved(self_event):
        print(f'alguem moveu {event.scr_path} para {event.dest_path}')



        


# Inicialize a Classe Gerenciadora de Eventos
event_handler = FileEventHandler()

# Inicialize o Observer
observer = Observer()

# Agende o Observer
observer.schedule(event_handler, from_dir, recursive=True)


# Inicie o Observer
observer.start()


#5_Escreva uma exceção para keyboardInterrupt
try:
    while True:
        time.sleep(2)
        print("executando...")
except KeyboardInterrupt:
        print("interrompido!")
        observer.stop()






