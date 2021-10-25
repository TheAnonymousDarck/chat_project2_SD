import os
import socket
import struct


def recibirTamArchivo(sck: socket.socket):
    # Esta función se asegura de que se reciban los bytes
    # que indican el tamaño del archivo que será enviado,
    # que es codificado por el cliente vía struct.pack(),
    # función la cual genera una secuencia de bytes que
    # representan el tamaño del archivo.
    formato = "<Q"
    bytes_esperados = struct.calcsize(formato)
    bytes_recibidos = 0
    buffer = bytes()
    while bytes_recibidos < bytes_esperados:
        tam_recv = sck.recv(bytes_esperados - bytes_recibidos)
        buffer += tam_recv
        bytes_recibidos += len(tam_recv)
    tam_archivo = struct.unpack(formato, buffer)[0]
    return tam_archivo


def recibirArchivo(sck: socket.socket, nombre_archivo):
    # Leer primero del socket la cantidad de
    # bytes que se recibirán del archivo.
    tam_archivo = recibirTamArchivo(sck)
    # Abrir un nuevo archivo en donde guardar
    # los datos recibidos.
    with open(nombre_archivo, "wb") as f:
        bytes_recibidos = 0
        # Recibir los datos del archivo en bloques de
        # 1024 bytes hasta llegar a la cantidad de
        # bytes total informada por el cliente.
        while bytes_recibidos < tam_archivo:
            buffer = sck.recv(1024)
            if buffer:
                f.write(buffer)
                bytes_recibidos += len(buffer)


def enviarArchivo(sck: socket.socket, nombre_archivo):
    # Obtener el tamaño del archivo a enviar.
    tam_archivo = os.path.getsize(nombre_archivo)
    # Informar primero al servidor la cantidad
    # de bytes que serán enviados.
    sck.sendall(struct.pack("<Q", tam_archivo))
    # Enviar el archivo en bloques de 1024 bytes.
    with open(nombre_archivo, "rb") as f:
        while leer_bytes := f.read(1024):
            sck.sendall(leer_bytes)