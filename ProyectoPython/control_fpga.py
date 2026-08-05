#!/usr/bin/env python3
# ==========================================================
# control_fpga.py
#
# Biblioteca para controlar una Arty Z7 desde LabVIEW
# mediante SSH.
#
# Funciones:
#   conectar(ip)
#   desconectar()
#   ejecutar(comando)
#   leerRegistro(base,offset)
#   escribirRegistro(base,offset,valor)
#   tomarDatos(muestras)
#
# Autor: ChatGPT
# ==========================================================

import paramiko

# ----------------------------------------------------------
# Configuración
# ----------------------------------------------------------

USUARIO = "xilinx"
PASSWORD = "xilinx"

ssh = None


# ==========================================================
# Conectar
# ==========================================================

def conectar(host):

    global ssh

    try:

        ssh = paramiko.SSHClient()

        ssh.set_missing_host_key_policy(
            paramiko.AutoAddPolicy()
        )

        ssh.connect(
            hostname=host,
            username=USUARIO,
            password=PASSWORD,
            timeout=10
        )

        return "FPGA conectada"

    except Exception as e:

        return str(e)


# ==========================================================
# Desconectar
# ==========================================================

def desconectar():

    global ssh

    if ssh is not None:

        ssh.close()

        ssh = None

    return "FPGA desconectada"


# ==========================================================
# Ejecutar comando Linux
# ==========================================================

def ejecutar(comando):

    global ssh

    if ssh is None:

        return "No existe conexión."

    stdin, stdout, stderr = ssh.exec_command(comando)

    salida = stdout.read().decode()

    error = stderr.read().decode()

    if error != "":

        return error

    return salida


# ==========================================================
# Función privada
# Ejecuta código Python como ROOT
# ==========================================================

def _ejecutar_python(codigo):

    global ssh

    if ssh is None:
        raise Exception("No existe conexión con la FPGA.")

    stdin, stdout, stderr = ssh.exec_command(
        "sudo -S python3 -"
    )

    #
    # enviar password
    #

    stdin.write(PASSWORD + "\n")

    #
    # enviar código Python
    #

    stdin.write(codigo)

    stdin.flush()

    stdin.channel.shutdown_write()

    salida = stdout.read().decode()

    error = stderr.read().decode()

    if error != "":

        #
        # sudo normalmente imprime el password prompt
        #

        error = error.replace(
            "[sudo] password for xilinx:",
            ""
        ).strip()

        if error != "":

            raise Exception(error)

    return salida


# ==========================================================
# Leer un registro AXI
# ==========================================================

def leerRegistro(base, offset):

    codigo = f"""
import os
import mmap
import struct

BASE={base}
OFFSET={offset}
SIZE=0x10000

fd=os.open("/dev/mem",os.O_RDWR|os.O_SYNC)

mem=mmap.mmap(
    fd,
    SIZE,
    mmap.MAP_SHARED,
    mmap.PROT_READ|mmap.PROT_WRITE,
    offset=BASE
)

mem.seek(OFFSET)

dato=struct.unpack("<I",mem.read(4))[0]

print(dato)

mem.close()
os.close(fd)
"""

    salida = _ejecutar_python(codigo)

    return int(salida.strip())


# ==========================================================
# Escribir un registro AXI
# ==========================================================

def escribirRegistro(base, offset, valor):

    codigo = f"""
import os
import mmap
import struct

BASE={base}
OFFSET={offset}
VALOR={valor}
SIZE=0x10000

fd=os.open("/dev/mem",os.O_RDWR|os.O_SYNC)

mem=mmap.mmap(
    fd,
    SIZE,
    mmap.MAP_SHARED,
    mmap.PROT_READ|mmap.PROT_WRITE,
    offset=BASE
)

mem.seek(OFFSET)

mem.write(struct.pack("<I",VALOR))

mem.close()
os.close(fd)

print("OK")
"""

    salida = _ejecutar_python(codigo)

    return salida.strip()


# ==========================================================
# Leer XADC
# ==========================================================

def tomarDatos(muestras=50):

    codigo = f"""
import os
import mmap
import struct

BASE=0x43C00000
REG=0x244
SIZE=0x10000

fd=os.open("/dev/mem",os.O_RDWR|os.O_SYNC)

mem=mmap.mmap(
    fd,
    SIZE,
    mmap.MAP_SHARED,
    mmap.PROT_READ|mmap.PROT_WRITE,
    offset=BASE
)

for i in range({muestras}):

    mem.seek(REG)

    dato=struct.unpack("<I",mem.read(4))[0]

    adc=(dato>>4)&0x0FFF

    print(adc)

mem.close()

os.close(fd)
"""

    salida = _ejecutar_python(codigo)

    datos = []

    for linea in salida.splitlines():

        linea = linea.strip()

        if linea != "":

            datos.append(int(linea))

    return datos