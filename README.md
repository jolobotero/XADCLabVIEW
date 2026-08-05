{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "bce20739",
   "metadata": {},
   "source": [
    "# Crear archivo *.bin"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "7ad5014b",
   "metadata": {},
   "source": [
    "Aunque el vivado puede crear el archivo *.bin, las diferentes versiones de vivado y las versiones del linux o el petalinux instalado en la FPGA pueden no ser compatibles, por tanto es más seguro crear el archivo *.bin desde el simbolo del sistema en windows (CMD). \n",
    "Abrimos CMD en windows en la carpeta donde generamos el bitstream (*.bit) y en un block de notas creamos el archivo download.bif y copiamos dentro:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "a80e2678",
   "metadata": {},
   "outputs": [],
   "source": [
    "all:\n",
    "{\n",
    "    xadc_axiLite.bit\n",
    "}"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "27245cea",
   "metadata": {},
   "source": [
    "en este caso \"xadc_axiLite.bit\" es el nombre del bitstream generado por vivado."
   ]
  },
  {
   "cell_type": "markdown",
   "id": "23d0acc8",
   "metadata": {},
   "source": [
    "# Comprobar que existe la herramienta BOOTGEN"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "da240bf1",
   "metadata": {},
   "source": [
    "Comprobar que existe la herramienta bootgen en windows"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "9eb464a8",
   "metadata": {},
   "outputs": [],
   "source": [
    "</> cmd\n",
    "bootgen -help"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "85898479",
   "metadata": {},
   "source": [
    "o"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "dd23d643",
   "metadata": {},
   "outputs": [],
   "source": [
    "</> cmd\n",
    "bootgen -version"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "44a37a09",
   "metadata": {},
   "source": [
    "si se obtiene algo como:\n",
    "\n",
    "\"bootgen\" no se reconoce como un comando interno o externo,\n",
    "programa o archivo por lotes ejecutable.\n",
    "\n",
    "Entonces, bootgen no esta instalado o en algunas versiones de vivado, se debe cargar primero el entorno desde AMD/Xilinx Command Promp o ejecutar: "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "e013768d",
   "metadata": {},
   "outputs": [],
   "source": [
    "</> cmd\n",
    "C:\\Xilinx\\Vitis\\2022.2\\settings64.exe"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "e4420982",
   "metadata": {},
   "source": [
    "La ruta puede cambiar según la versión de Vivado. Ya en este caso se repite la comprobación de bootgen"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "ab3d52b2",
   "metadata": {},
   "outputs": [],
   "source": [
    "</> cmd\n",
    "bootgen -help"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "0e2b521c",
   "metadata": {},
   "source": [
    "# Ejecutar bootgen\n",
    "\n",
    "Abrir una consola CMD donde se encuentran los archivos *.bit y download.bif y ejecutar el comando"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "25a4bd78",
   "metadata": {},
   "outputs": [],
   "source": [
    "</> cmd\n",
    " bootgen -image download.bif -arch zynq -process_bitstream bin -w -o nombre_archivo.bin\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "5a2815cc",
   "metadata": {},
   "source": [
    "****** Xilinx Bootgen v2022.2.0\n",
    "\n",
    "  **** Build date : Oct 13 2022-12:22:51\n",
    "\n",
    "    ** Copyright 1986-2022 Xilinx, Inc. All Rights Reserved.\n",
    "\n",
    "\n",
    "[INFO]   : Bootimage generated successfully"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "a49c7417",
   "metadata": {},
   "source": [
    "Ahora en la carpeta hay un nuevo archivo nombre_archivo.bit.bin\n",
    "\n",
    "### Renombrar el archivo"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "5bb5e862",
   "metadata": {},
   "outputs": [],
   "source": [
    "</>  cmd\n",
    "ren nombre_archivo.bit.bin nuevo_nombre.bin"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "852b14c9",
   "metadata": {},
   "source": [
    "# Copiar archivo a la ARTY\n",
    "password = xilinx"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "4af2ef62",
   "metadata": {},
   "source": [
    "</> cmd \n",
    "scp nombre_archivo.bin xilinx@IP_DE_LA_ARTY:/home/xilinx/"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "726a9c9a",
   "metadata": {},
   "source": [
    "## Conectarse a la FPGA ARTY \n",
    "\n",
    "el password es xilinx"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "d440eb5f",
   "metadata": {},
   "outputs": [],
   "source": [
    "</> cmd\n",
    "ssh xilinx@IP_DE_LA_ARTY"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "df068234",
   "metadata": {},
   "source": [
    "En la arty, copiar el archivo *.bin al directorio /lib/firmware/"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "12014740",
   "metadata": {},
   "outputs": [],
   "source": [
    "</> bash (ARTY) \n",
    "sudo cp /home/xilinx/nombre_archivo.bin /lib/firmware/"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "920b70c3",
   "metadata": {},
   "source": [
    "# Programar la FPGA"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "9aea21c5",
   "metadata": {},
   "outputs": [],
   "source": [
    "</> bash (ARTY)\n",
    "\n",
    "echo nombre_archivo.bin | sudo tee /sys/class/fpga_manager/fpga0/firmware\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "f3ab1465",
   "metadata": {},
   "source": [
    "### Comprobar el resultado"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "bf60937e",
   "metadata": {},
   "outputs": [],
   "source": [
    "</> bash (ARTY)\n",
    "\n",
    "dmesg | tail -20\n",
    "\n",
    "cat /sys/class/fpga_manager/fpga0/state"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "d775e35e",
   "metadata": {},
   "source": [
    "operating"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "50f90ebf",
   "metadata": {},
   "source": [
    "## Comunicacion con la FPGA"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "ca6654ec",
   "metadata": {},
   "source": [
    "para comunicarse con la fPGA y sus diferentes registros, debemos conocer las direcciones de los registros, en este caso el programa desarrollado solo tiene el módulo xadc conectado por un bus axiLite\n",
    "\n",
    "            * xadc_wiz_0/S_axi_lite                  0x43C00000           64K        0x43C0FFFF\n",
    "\n",
    "eso quiere decir que hay reservados 64K de memoria para el xadc_wiz_0 y que se encuentra entre las posiciones 0x43C00000 y 0x43C0FFFF.\n",
    "\n",
    "Vamos a escribir un script en python que permita hacer la comunicación, pero, el script será escrito de tal forma que permita llamarlo desde LabVIEW.\n",
    "\n",
    "## LabVIEW y Python \n",
    "\n",
    "No cualquier versión de LabVIEW sirve para llamar un script de python, cada version de LabVIEW tiene versiones de python con la que es compatible. así:\n",
    "\n",
    "    *   LabVIEW 2018                        Python 2.7   3.6\n",
    "    *   LabVIEW 2019                        Python 2.7   3.6   3.7\n",
    "    *   LabVIEW 2020                        Python 3.6   3.7   3.8\n",
    "    *   LabVIEW 2021                        Python 3.6   3.7   3.9\n",
    "    *   LabVIEW 2022 Q1                     Python 3.8   3.9\n",
    "    *   LabVIEW 2022 Q3                     Python 3.9\n",
    "    *   LabVIEW 2023 Q1                     Python 3.9   3.10\n",
    "    *   LabVIEW 2023 Q3                     Python 3.9   3.10  3.11\n",
    "    *   LabVIEW 2024                        Python 3.10  3.11\n",
    "    *   LabVIEW 2025                        Python 3.11  y más recientes\n",
    "    \n",
    " Tambien debe coincidir la arquitectura, ambos deben tener la misma arquitectura, de 32 bits o 64 bits.\n",
    " \n",
    "### Python\n",
    "\n",
    "Ver versiones instaladas de python."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "a6eda657",
   "metadata": {},
   "outputs": [],
   "source": [
    "</> cmd\n",
    "\n",
    "py --list"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "db41f19c",
   "metadata": {},
   "source": [
    "Si es necesario, en la página oficial de python, descarga la versión que mejor se adapte a tu LabVIEW, junto con su arquitectura 32 o 64 bits.\n",
    "\n",
    "se debe instalar paramiko, para poder hacer una comunicación SSH desde python, pero antes se debe actualizar la herramienta pip, pero en la versión donde se va a trabajar (en mi caso la version de python es 3.9 de 32 bits)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "24435911",
   "metadata": {},
   "outputs": [],
   "source": [
    "</> cmd\n",
    "\n",
    "py -3.9-32 -m pip install --ipgrade pip"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "4449587a",
   "metadata": {},
   "source": [
    "Y luego instalamos paramiko"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "150a1a70",
   "metadata": {},
   "outputs": [],
   "source": [
    "</> cmd\n",
    "\n",
    "py -3.9-32 -m pip install paramiko"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "023580c9",
   "metadata": {},
   "source": [
    "Por tratarse de diferentes versiones de python puede ser que se presenten problemas al instalar paramiko, si es una versión anterior de python, es mejor tratar de instalar una version compatible de paramiko y para evitar errores, instalar una version correspondiente de cryptography, programa necesario para instalar paramiko.\n",
    "\n",
    "### Instalar Cryptography \n",
    "\n",
    "Para mi caso python 3.9-32"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "9ea0647a",
   "metadata": {},
   "outputs": [],
   "source": [
    "</> cmd\n",
    "\n",
    "py -3.9-32 -m pip install \"cryptography==41.0.7\""
   ]
  },
  {
   "cell_type": "markdown",
   "id": "5e0a1705",
   "metadata": {},
   "source": [
    "### Instalar Paramiko"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "33f0de85",
   "metadata": {},
   "outputs": [],
   "source": [
    "</> cmd\n",
    "\n",
    "py -3.9-32 -m pip install \"paramiko==3.4.0\""
   ]
  },
  {
   "cell_type": "markdown",
   "id": "7de0037f",
   "metadata": {},
   "source": [
    "### Creacion del script de python\n",
    "\n",
    "shebang, su función es indicar al sistema operativo linux que este archivo se ejecuta con el interprete Python3, por esta razón el programa se puede ejecutar solo con ./nombre_archivo.py"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "09c17e5a",
   "metadata": {},
   "outputs": [],
   "source": [
    "</> python\n",
    "\n",
    "#!/usr/bin/env python3"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "f555c6b4",
   "metadata": {},
   "source": [
    "paramiko es la biblioteca que implementa el protocolo SSH"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "4dbc1c4b",
   "metadata": {},
   "outputs": [],
   "source": [
    "</> python\n",
    "\n",
    "import paramiko"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "3e3a1889",
   "metadata": {},
   "source": [
    "Para conectarse a la ARTY el login es \"xilinx\" y el password es \"xilinx\", se definen estas variables globales"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "7551219f",
   "metadata": {},
   "outputs": [],
   "source": [
    "</> python\n",
    "\n",
    "USUARIO = \"xilinx\"\n",
    "PASSWORD = \"xilinx\"\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "6c164d2d",
   "metadata": {},
   "source": [
    "SSH contendrá el objeto que representa la conexión con la FPGA (None = aún no hay ninguna conexión)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "e99c1e40",
   "metadata": {},
   "outputs": [],
   "source": [
    "</> python\n",
    "\n",
    "ssh = None"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "78cc2512",
   "metadata": {},
   "source": [
    "### Definicion de la función \"conectar(host)\"\n",
    "\n",
    "LabVIEW accede al script de python a través de funciones, por eso el script sera un conjunto de funciones que desarrollan una tarea particular y que pueden o no retornar una variable como resultado de la tarea particular. En este caso conectar es una funcion que recibe el parametro host que es un string y representa la dirección IP donde se encuentra conectada la FPGA"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "dec4a53e",
   "metadata": {},
   "outputs": [],
   "source": [
    "</> python\n",
    "\n",
    "def conectar(host):\n",
    "\n",
    "    global ssh\n",
    "\n",
    "    try:\n",
    "\n",
    "        ssh = paramiko.SSHClient()\n",
    "\n",
    "        ssh.set_missing_host_key_policy(\n",
    "            paramiko.AutoAddPolicy()\n",
    "        )\n",
    "\n",
    "        ssh.connect(\n",
    "            hostname=host,\n",
    "            username=USUARIO,\n",
    "            password=PASSWORD,\n",
    "            timeout=10\n",
    "        )\n",
    "\n",
    "        return \"FPGA conectada\"\n",
    "\n",
    "    except Exception as e:\n",
    "\n",
    "        return str(e)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "0c07a3bc",
   "metadata": {},
   "source": [
    "global ssh          define ssh como una variable global, ssh mantiene la información de la conexión, dirección IP, puerto, usuraio, contraseña autenticada, canal SSH abierto.\n",
    "\n",
    "ssh = paramiko.SSHClient()       se creea un objeto de la clase SSHClient, aun no se ha conectado\n",
    "\n",
    "ssh.set_missing_host_key_policy(\n",
    "        paramiko.AutoAddPolicy()\n",
    " )\n",
    "\n",
    "SSH trabaja con criptográfias. Cuando se abre una nueva conección a un servidor, puede aparecer el siguiente mensaje:\n",
    "\n",
    "The authenticity of host can't be established.\n",
    "Are you sure?\n",
    "\n",
    "Normalmente la respuesta es:\n",
    "\n",
    "yes\n",
    "\n",
    "la libreria paramiko hace lo mismo con la instruccion AutoAddPolicity()\n",
    "\n",
    "ssh.connect(\n",
    "    hostname=host,\n",
    "    username=USUARIO,\n",
    "    password=PASSWORD,\n",
    "    timeout=10\n",
    ")\n",
    " \n",
    "Esta instrucción es la que abre la conexión, es similar a hacer ssh xilinx@IP_DIRECTION_FPGA\n",
    "depues envía \n",
    "\n",
    "password: \n",
    "\n",
    "Y responde automatico \"xilinx\"\n",
    "\n",
    "si todo es correcto la funcion devuelve una variable de string con el mensaje\n",
    "\n",
    "\"FPGA conectada\"\n",
    "\n",
    "### Funcion desconectar()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "99bb2c11",
   "metadata": {},
   "outputs": [],
   "source": [
    "</> python\n",
    "\n",
    "def desconectar():\n",
    "\n",
    "    global ssh\n",
    "\n",
    "    if ssh is not None:\n",
    "\n",
    "        ssh.close()\n",
    "\n",
    "        ssh = None\n",
    "\n",
    "    return \"FPGA desconectada\"\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "916d983d",
   "metadata": {},
   "source": [
    "esta funcion desconecta la FPGA y retorna el string \"FPGA desconectada\"\n",
    "\n",
    "### Funcion ejecutar(comando)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "680793d5",
   "metadata": {},
   "outputs": [],
   "source": [
    "</> python\n",
    "\n",
    "def ejecutar(comando):\n",
    "\n",
    "    global ssh\n",
    "\n",
    "    if ssh is None:\n",
    "\n",
    "        return \"No existe conexión.\"\n",
    "\n",
    "    stdin, stdout, stderr = ssh.exec_command(comando)\n",
    "\n",
    "    salida = stdout.read().decode()\n",
    "\n",
    "    error = stderr.read().decode()\n",
    "\n",
    "    if error != \"\":\n",
    "\n",
    "        return error\n",
    "\n",
    "    return salida\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "28122a9d",
   "metadata": {},
   "source": [
    "la funcon ejecuta un comando propio de linux a través del parámetro \"comando\".\n",
    "\n",
    "ejemplo\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "c59a7739",
   "metadata": {},
   "outputs": [],
   "source": [
    "</> python\n",
    "\n",
    "ejecutar(\"ls\")"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "e7f2a490",
   "metadata": {},
   "source": [
    "global ssh        se refiere a la conexión ssh con la FPGA\n",
    "\n",
    "if ssh is None:\n",
    "   return \"No existe conexión\"\n",
    "\n",
    "comprueba que exista una conexión ssh con la FPGA, si no hay conexión, la función retorna el string \"No existe conexión\"\n",
    "\n",
    "stdin, stdout, stderr = ssh.exec_command(comando) \n",
    "\n",
    "La anterior línea ejecuta el comando como si el usario lo hubiera escrito en una terminal SSH, exec_command() devuelve tres objetos, stdin, stdout, stderr\n",
    "\n",
    "#### stdin\n",
    "\n",
    "Es la entrada estándar, escribe información al programa remoto, por ejemplo, sudo espera un password, este password se envía por stdin\n",
    "\n",
    "#### stdout\n",
    "\n",
    "Es la salida estándar, lo que aparece en la pantalla del terminal, ejemplo"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "8e69544a",
   "metadata": {},
   "outputs": [],
   "source": [
    "</> SSH FPGA\n",
    "\n",
    "$ pwd\n",
    "\n",
    "/home/xilinx"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "384f734f",
   "metadata": {},
   "source": [
    "#### stderr\n",
    "\n",
    "es la salida de errores\n",
    "\n",
    "salida = stdout.read().decode()      \n",
    "\n",
    "Lee la salida en bytes (stdout.read()) y luego los convierte en texto (.decode())\n",
    "\n",
    "error = stderr.read().decode() de igual manera lee el error, si lo hubo.\n",
    "\n",
    "if error != \"\":\n",
    "        return error\n",
    "    return salida\n",
    "\n",
    "si existio error, la función retorna el error, si no, retorna lo que hay en salida.\n",
    "\n",
    "### Funcion _ejecutar_python(codigo)\n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "8d7aef56",
   "metadata": {},
   "outputs": [],
   "source": [
    "</> python\n",
    "\n",
    "def _ejecutar_python(codigo):\n",
    "\n",
    "    global ssh\n",
    "\n",
    "    if ssh is None:\n",
    "        raise Exception(\"No existe conexión con la FPGA.\")\n",
    "\n",
    "    stdin, stdout, stderr = ssh.exec_command(\n",
    "        \"sudo -S python3 -\"\n",
    "    )\n",
    "\n",
    "    #\n",
    "    # enviar password\n",
    "    #\n",
    "\n",
    "    stdin.write(PASSWORD + \"\\n\")\n",
    "\n",
    "    #\n",
    "    # enviar código Python\n",
    "    #\n",
    "\n",
    "    stdin.write(codigo)\n",
    "\n",
    "    stdin.flush()\n",
    "\n",
    "    stdin.channel.shutdown_write()\n",
    "\n",
    "    salida = stdout.read().decode()\n",
    "\n",
    "    error = stderr.read().decode()\n",
    "\n",
    "    if error != \"\":\n",
    "\n",
    "        #\n",
    "        # sudo normalmente imprime el password prompt\n",
    "        #\n",
    "\n",
    "        error = error.replace(\n",
    "            \"[sudo] password for xilinx:\",\n",
    "            \"\"\n",
    "        ).strip()\n",
    "\n",
    "        if error != \"\":\n",
    "\n",
    "            raise Exception(error)\n",
    "\n",
    "    return salida"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "a74f24b5",
   "metadata": {},
   "source": [
    "Es la función que le permitirá a LabVIEW ejecutar código python directamente dentro de la FPGA con permisos de admiistrador (ROOT). Gracias a ella puede aaceder a /dev/mem y, por tanto, controlar cualquier IP del diseño.\n",
    "\n",
    "el parametro código es lo que se va a enviar a la FPGA.\n",
    "\n",
    "global ssh\n",
    "\n",
    "if ssh is None:\n",
    "    raise Exception(\"No existe conexión con la FPGA.\")\n",
    "    \n",
    "las líneas anteriores chequean que exista una comunicación SSH con la FPGA\n",
    "\n",
    "stdin, stdout, stderr = ssh.exec_command(\n",
    "    \"sudo -S python3 -\"\n",
    ")\n",
    "\n",
    "envia el comando \"sudo -S python3 -\" \n",
    "\n",
    "\"sudo\" se usa para administrar el programa como administrador\n",
    "\n",
    "-S Normalmente sudo pide la contraseña por teclado, de esta forma la contraseña será leída desde stdin, lo mismo para python3 -\n",
    "\n",
    "se envia \"sudo -S\" sudo espera Password\n",
    "\n",
    "stdin.write(PASSWORD + \"\\n\")\n",
    "\n",
    "escribe el password (xilinx)\n",
    "\n",
    "luego se escribe \"python3 -\" y luego se envia el codigo\n",
    "\n",
    "stdin.write(codigo)\n",
    "\n",
    "el signo \"-\" es para indicar que es un codigo, no un archivo *.py\n",
    "\n",
    "    * También es posible crear un script de python, guardarlo en la FPGA y solo ejecutarlo desde LabVIEW usando este mismo sistema.\n",
    "    \n",
    "stdin.flush()    forzar el envío, python guarda temporalmente los datos eb un búffer con flush() se obliga a enviar inmediatamente todo el contenido\n",
    "\n",
    "stdin.channel.shutdown_write()   Le indica al interprete remoto que ya se terminó de enviar el programa\n",
    "\n",
    "salida = stdout.read().decode()\n",
    "error = stderr.read().decode()\n",
    "\n",
    "leen la salida y el error si lo hay y lo convierte a en cadena de caracteres en cualquiera de ambos casos.\n",
    "\n",
    "if error != \"\":\n",
    "        error = error.replace(\n",
    "            \"[sudo] password for xilinx:\",\n",
    "            \"\"\n",
    "        ).strip()\n",
    "\n",
    "if error != \"\":\n",
    "    raise Exception(error)\n",
    "return salida\n",
    "\n",
    "Si no hay error retorna lo que hay en salida.\n",
    "\n",
    "### Funcion leerRegistro(base, offset)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "6059b1e7",
   "metadata": {},
   "outputs": [],
   "source": [
    "</> python\n",
    "\n",
    "def leerRegistro(base, offset):\n",
    "\n",
    "    codigo = f\"\"\"\n",
    "import os\n",
    "import mmap\n",
    "import struct\n",
    "\n",
    "BASE={base}\n",
    "OFFSET={offset}\n",
    "SIZE=0x10000\n",
    "\n",
    "fd=os.open(\"/dev/mem\",os.O_RDWR|os.O_SYNC)\n",
    "\n",
    "mem=mmap.mmap(\n",
    "    fd,\n",
    "    SIZE,\n",
    "    mmap.MAP_SHARED,\n",
    "    mmap.PROT_READ|mmap.PROT_WRITE,\n",
    "    offset=BASE\n",
    ")\n",
    "\n",
    "mem.seek(OFFSET)\n",
    "\n",
    "dato=struct.unpack(\"<I\",mem.read(4))[0]\n",
    "\n",
    "print(dato)\n",
    "\n",
    "mem.close()\n",
    "os.close(fd)\n",
    "\"\"\"\n",
    "\n",
    "    salida = _ejecutar_python(codigo)\n",
    "\n",
    "    return int(salida.strip())\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "f43e2d57",
   "metadata": {},
   "source": [
    "Esta funcion lee un registro en la direccion = base + offset\n",
    "\n",
    "codigo = f\"\"\"                  \"\"\"   le pasa a codigo una cadena de texto que lleva el programa de python\n",
    "\n",
    "#### programa en python\n",
    "\n",
    "Este es el código que será pasado al parámetro \"codigo\"\n",
    "\n",
    "import os\n",
    "\n",
    "permite acceder /dev/mem\n",
    "\n",
    "import map\n",
    "\n",
    "permite mapear una región de memoria física\n",
    "\n",
    "import struct\n",
    "\n",
    "convierte bytes en enteros\n",
    "\n",
    "BASE={base}\n",
    "OFFSET={offset}\n",
    "SIZE=0x10000\n",
    "\n",
    "define los parametros, dirección a ser leída = BASE + OFFSET\n",
    "\n",
    "fd=os.open(\"/dev/mem\",os.O_RDWR|os.O_SYNC)\n",
    "\n",
    "abre \"/dev/mem\" , obteniendo acceso a la memoria física del ZYNQ, el resultados es fd (file descriptor)\n",
    "\n",
    "mem=mmap.mmap(\n",
    "    fd,\n",
    "    SIZE,\n",
    "    mmap.MAP_SHARED,\n",
    "    mmap.PROT_READ|mmap.PROT_WRITE,\n",
    "    offset=BASE\n",
    ")\n",
    "\n",
    "se crea una ventana de memoria, la variable mem representa esa ventana\n",
    "\n",
    "mem.seek(OFFSET)\n",
    "\n",
    "ir al registro, el registro leído es BASE + OFFSET\n",
    "\n",
    "dato=struct.unpack(\"<I\",mem.read(4))[0]\n",
    "\n",
    "lee el registro, mem.read(4) lee un registro AXI completo (32 bits)\n",
    "\n",
    "struct.unpack(\"<I\",mem.read(4)) convierte esos 4 bytes en un entero de 32 bits, además, devuelve una tupla, por eso se toma el primer elemento de esa tupla [0]\n",
    "\n",
    "dato=struct.unpack(\"<I\",mem.read(4))[0]\n",
    "\n",
    "mem.close()\n",
    "\n",
    "cierra el mapeo\n",
    "\n",
    "os.close(fd)\n",
    "\n",
    "cierra acceso a /dev/mem\n",
    "\n",
    "salida = _ejecutar_python(codigo)\n",
    "\n",
    "ejecuta el programa python guardado en el parámetro \"codigo\"\n",
    "\n",
    "return int(salida.strip())\n",
    "\n",
    "Quita los saltos de línea y convierte la salida a entero, y ese dato es la sallida del programa.\n",
    "\n",
    "### Funcion escribirRegistro(base, offset, valor)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "a3f1c5a8",
   "metadata": {},
   "outputs": [],
   "source": [
    "</> python\n",
    "\n",
    "def escribirRegistro(base, offset, valor):\n",
    "\n",
    "    codigo = f\"\"\"\n",
    "import os\n",
    "import mmap\n",
    "import struct\n",
    "\n",
    "BASE={base}\n",
    "OFFSET={offset}\n",
    "VALOR={valor}\n",
    "SIZE=0x10000\n",
    "\n",
    "fd=os.open(\"/dev/mem\",os.O_RDWR|os.O_SYNC)\n",
    "\n",
    "mem=mmap.mmap(\n",
    "    fd,\n",
    "    SIZE,\n",
    "    mmap.MAP_SHARED,\n",
    "    mmap.PROT_READ|mmap.PROT_WRITE,\n",
    "    offset=BASE\n",
    ")\n",
    "\n",
    "mem.seek(OFFSET)\n",
    "\n",
    "mem.write(struct.pack(\"<I\",VALOR))\n",
    "\n",
    "mem.close()\n",
    "os.close(fd)\n",
    "\n",
    "print(\"OK\")\n",
    "\"\"\"\n",
    "\n",
    "    salida = _ejecutar_python(codigo)\n",
    "\n",
    "    return salida.strip()\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "73b415a7",
   "metadata": {},
   "source": [
    "Funciona de forma identica a la funcion leerRegistro descrita anteriormente, la única función diferente es:\n",
    "\n",
    "mem.write(struct.pack(\"<I\",VALOR))\n",
    "\n",
    "que escribe en la dirección BASE + OFFSET el valor del parámetro \"VALOR\"\n",
    "\n",
    "### Funcion tomarDatos(muestras)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "e8e676f9",
   "metadata": {},
   "outputs": [],
   "source": [
    "</> python\n",
    "\n",
    "def tomarDatos(muestras=50):\n",
    "\n",
    "    codigo = f\"\"\"\n",
    "import os\n",
    "import mmap\n",
    "import struct\n",
    "\n",
    "BASE=0x43C00000\n",
    "REG=0x244\n",
    "SIZE=0x10000\n",
    "\n",
    "fd=os.open(\"/dev/mem\",os.O_RDWR|os.O_SYNC)\n",
    "\n",
    "mem=mmap.mmap(\n",
    "    fd,\n",
    "    SIZE,\n",
    "    mmap.MAP_SHARED,\n",
    "    mmap.PROT_READ|mmap.PROT_WRITE,\n",
    "    offset=BASE\n",
    ")\n",
    "\n",
    "for i in range({muestras}):\n",
    "\n",
    "    mem.seek(REG)\n",
    "\n",
    "    dato=struct.unpack(\"<I\",mem.read(4))[0]\n",
    "\n",
    "    adc=(dato>>4)&0x0FFF\n",
    "\n",
    "    print(adc)\n",
    "\n",
    "mem.close()\n",
    "\n",
    "os.close(fd)\n",
    "\"\"\"\n",
    "\n",
    "    salida = _ejecutar_python(codigo)\n",
    "\n",
    "    datos = []\n",
    "\n",
    "    for linea in salida.splitlines():\n",
    "\n",
    "        linea = linea.strip()\n",
    "\n",
    "        if linea != \"\":\n",
    "\n",
    "            datos.append(int(linea))\n",
    "\n",
    "    return datos"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "52dfe1ac",
   "metadata": {},
   "source": [
    "esta función es muy parecida a las dos anteriores, en esta funcion se lee el registro 0x04C00000 + 0x0244 = 0x04C00244, que corresponde al canal A0 en la FPGA Arty. y lo hace el número de veces indicado en el parámetro \"muestras\"  \n",
    "\n",
    "for i in range({muestras}):\n",
    "    mem.seek(REG)\n",
    "    dato=struct.unpack(\"<I\",mem.read(4))[0]\n",
    "    adc=(dato>>4)&0x0FFF\n",
    "    print(adc)\n",
    "\n",
    "print(adc) envía un número que se envía por SSH hacia el computador\n",
    "\n",
    "salida = _ejecutar_python(codigo)\n",
    "\n",
    "datos = []\n",
    "\n",
    "for linea in salida.splitlines():\n",
    "    linea = linea.strip()\n",
    "    if linea != \"\":\n",
    "        datos.append(int(linea))\n",
    "return datos\n",
    "\n",
    "ejecuta el programa, se separan las lineas, divide la cadena en una lista y la convierte a enteros."
   ]
  },
  {
   "cell_type": "markdown",
   "id": "b7c9e9e1",
   "metadata": {},
   "source": [
    "# Labview"
   ]
  },
  {
   "attachments": {
    "image-2.png": {
     "image/png": "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"
    },
    "image-3.png": {
     "image/png": "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"
    },
    "image-4.png": {
     "image/png": "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"
    },
    "image-5.png": {
     "image/png": "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ARIgARIgARIggZoTYBtW8zsAp18XApwnCZAACZAACZAACZBAcQiwDSvOWrASEiABEqgaAc6HBEiABEiABEgglQDbsFQsHCQBEiABEiABEigrAdZNAiRAAsUnwDas+GvECkmABEiABEiABEiABIpOgPWRQF8E2Ib1hYvGJEACJEACJEACJEACJDBsAs8999yTTz75zDPPPP3000899RT2n3jiiccff/xU6/bYY4+dfvrpP+x2e8UrXtHN5IcFt/nfrdsPfvCD73//+9/73ve++93vNhqNO+644+abb968efOw18Y1X7sNW+52Qwq7SaChTQDC8ot8LGCCYfIJQFh+kY8FTDBMPgEIyy/ysYAJhsknAGH5RT4WMMEw+QQgLL/IxwImGO6Fz49//GN0YpAXX3wR9ug6TjvttJ/wb6e1bmawdVTN32aO2EK+/vWvf+UrX7n//vv/8R//8Ytf/OKPfvQjtKbYBlgTv8AtMRYfGKZNuw0b63ZDWd1MxmgjIyKfQfNJj0fO6Vxao+TTIpH+m3zSubRGyadFIv03+aRzaY2ST4tE+m/ySefSGq0zn5daN7RhMXnhhReef/55nCjDKbLWiaJR/t6Rw+348eOY0ne+852TJ09++9vffvDBB7/xjW/g/tD0b4YNdrEDOK37S/w37ONDieNh2rTbMGSlkAAJkAAJ9ECAJiRAAiRAAiRAAlYCfzXo27nnnmtNVloF27DSLh0LJwESIAESqBcBzpYESIAESKA6BNiGVWctORMSIAESIAESIAESGDQBxiOBQRJoNpt9hevXvq/gozVmGzZa/sxOAiRAAiRAAiRAAiRAAgMnsLBzKrxtmVsy8TEY7puRHrZw8iP17xkPjp6XOJImAAAQAElEQVSq0WhgG1ekHOshWMJe71Xxh21YFVeVcyIBEiABEiABEiABEqg7gYnN++dx279Z7dnRasQkJui3kq3Wws4ZNYso87Ore4tiyxD2VOissG8zC8dhA8vwsHo7bMMKuaYsigRIgARIgARIgARIgAQGQWB8+op1R+++Nzgh1mfEhcMH162d1E6Tl21WrlFUrKdCf4URHdXyAy1sLMqKDLMNq8hCchokMAACDEECJEACJEACJFATAktzW/xLDbHZuYA541TYzEF1dM+GqSn/GEOQpZPHJlatwA5k/MzVR48/ip1+JbWnQpeF8dRQGIc2VVWlweG1YfPbV26fD9HhaP3Nj7QOcRTRtUZ7/g33lStXRuL17NnN8JGb1yPyypWTk5MZ4qO+PIrrVjz1JEACJFAKAiySBEiABEggTwJLc7cenLjogvFojoWdG/as9q81nN+/+djMlrmlyW3zs+uUfx3jtsmoKfdzIjC8Nmzqkstv+1yrD3vk2ANq8dNfCPowHHnnrHad4fz2K2+7/BMnThz4w7NcQ6T7oQd766d/454TuC0sLHzivIeOpdtxlARIgARIgARIoGwEWC8JVJ+Af2prako3XLunO7ownORSwbWGyr9m0eksV08EhVNbOOUFbSwKRjAeG6zk4fDaMLX6HO+BY6bxeuQLnz7vuutU0NfgSP3G27P0UBmaOOuqPnLz1uvO+0S7t5vasWPKakwFCZAACZAACZAACZAACXQjMFS9f2pLf7qG++mt6IWI6N3CCxR7nEfXngodF2zCaNjHSHhY7Z12G7bc7QYQ3UyWJZtX/PJbn//rA/fB5tEDf/38v/rlM1be9jef0hHv/8riyjNeofc+9UH/EsCVKydn711evm/XpSs/6FsEukt33Yc9PazNJidnP7UMjytvU4vXvXWlUfpOWosf+Pr1wObSD37w0pU6mN7f9SkEhl4fI5i+4HBlyx3xjdx34K8X159/njlAzSrY0xnDaPpAB8LPBz8V5grjByUtP/Yj9fzj9+ukyNUabMVL/PbjJEY7B2jTySN+RD5xIp3H5NPJI35EPnEincfk08kjfkQ+cSKdx+TTySN+RD5xIp3HNeeD6Q9M0F2pg4f1W8KU0tcsts6MJROsWDURGC7cvkfFLm1MmkdHeuyp0HfBEo7YYh87GaXzXtM+Qtj2gWVvmDbtNmys2w1ldTMZE23Of9Mbv/a9p2Bz8nsvf+/683/7PZefOPXc2NgD9x24/D2/7Yf+7Y+e8G+fWH/gv9/13Plb/9PlB+57wNf4Vv9p6/ljD3zsvfe811woeKO69a43f/TEJy5X3nX3nLgTSq3d9cZP+DHuue7ENVff/qgaG/vpV6qvnfg3e06c+Ohv+/u7bv0pHMDvwDWT1//UnoWFBex/bdengkwm38/91Mu9f/Nmf/+5u65G+zQ5efVdqNaP0Io2FhZ8+YFbw1xB/Huue/mu60MXM7hw4/p4Ij9FdCMyDAxpE4Cw/CIfC5hgmHwCEJZf5GMBEwyTTwDC8ot8LGCCYfIJQFh+kY8FTDBccz6Y/uBkcpt+S9iUvm24+6L92/x3g02uXedfxxj5iA41Pr17Vs1ouxk1G7u0USqnr54K3Vdf9lJihSf/wR0m9gtesZHk4TBt2m0YsuYtwdvD7v37285bfZZSq89Rn/7CIx1vDJvfjhNLK1deecCUEjjgYP5zD1y3aUopWPvnvmA2ec2BxeCyRhj4orWXXwIzHJ31hx+4fPGRk9iDeJGLHr3rdvnvIkNw1RrX+w8EV0zC3Egr+ll/eGBh4cbLzaDetryw3yr4NuwH0orvF9AqsDV4wdsuV4lEgSN/5UWAcUmABEiABEiABEigZgQmt80nu6bIIPorfb0iftpmUON43jRlIa9gND4c6lN30FmljtsG+7W3xSnR+FDbMDRe3gPH7j3+LdMqnfX231APfeELn269MeyRm9dfqfxTWfds/WXDcGrTdQ987OZHHrn5Yw+0Gyn9eRw44aXPYuX3dq2zVp/XtV+KFHydZwqObnVTGD3mPgmQQK0IcLIkQAIkQAIkQAIkYCMw3DZMN17XXbNLBR+LiFbntuuuW/RPjaHAYw8tms/aeOQLn/8ajrVoj0/v3fvp8z7gn8FScFG3oTHTuuSPrw0+jhGt222Xv+2CpFGPI+gA1XVvFT9HP1LwpxfDsK1PgHzkC59eNP1mqOIOCZAACZAACeRLgNFJgARIgARKQWC4bZhCV+WpX37H288ycPS1gCpsVUzjs3Llyq0PvS44G6a0h7rttvOCKw2Vmtpxz3Voj2A1OTkZ/SYyP6LWPnAllCtX6s+a3+HehSHzHx448Qllgk1OXvNAcC2jn8dsIgWf1z4b5p330FZdwVuvO+8T+Z2tMxVwSwIkQAIkQAIkQAKjJ8AKSIAE+iUw5DZM6fdZ/cVlZ7XKnNpx4kS7VYHyhL4d2DHzF39hzn6ZbihiEwzArHVRImK0P1ZeJ4BOSzgYNehlv1UcfsNchzqBXK1wGGrthskO7Nhx4MBlK+Cg5ZxNB3ynsOqoywU7Bv8FZzopf0iABEiABEiABEiABEhg5AR+7/d+758GfbNNqtTjw27DSg2LxZMACZAACZAACZAACZDASAg0m82X/NsLL7zwYuv2ta997ejRo9/85jcfeuihRx555J8LcHviiSeO5HDDzL73ve+dOnXq6aeffu655154QUMAD5DAttnUcJrNZok+6oNt2EgeRwNJyiAkQAIkQAIkQAIkQAK1IHDaaae98MILzz///Oc///lDhw793d/93Wc/+9m77rrrxIkTx1s3tGF1EDNdTHxpaek73/nOD37wA/RmzzzzDHqwl73sZS9/+cvLcodgGzbYlYpefzjYyIxGAgUhwDJIgARIgARIgASGTeBVr3rV+Pj4z//8z/+7f/fvLrvsst/93d/9vd/7vcv924bW7R3veMcV3W6ltvn9xO3KK6/cuHHjH/zBH7zzne98//vf/8EPfvDjH//4sNfGNR/bMFdy9CMBEiABEhgeAWYiARIgARIggUoRYBtWqeXkZEiABEiABEiABAZHgJFIgARIIC8C7TZsudsNJXQzWX7uueeefPLJZ5555umnn37qqaew/8QTTzz++OOnWrfHHnvs9NNP/2G32yte8YpuJj+kjYyIfMjHRoD3DRsZM04+hoNtSz42MmacfAwH25Z8bGTMOPkYDrZtbfikAODcQyj/u3X7wQ9+8P3vf/973/ved7/73Uajcccdd9x8882bN2+2NSy99DLDtGm3YWPdbiirm8nYj3/8Y3RikBdffBH2IHLaaaf9hH87rXUzg60j/iYBEiABEiABEiABEiABEiCB7gRMH4Et5Otf//pXvvKV+++//x//8R+/+MUv/uhHP8LpH2xtDQt6E5sqHB+mTbsNQ9bs8lLrhjYsJubTXXCiDKfIWk1s2m+OkQAJkAAJkAAJkAAJkAAJkEAnge985zsnT5789re//eCDD37jG99A59L0b6b/wC520IBgvBQy4DasFHNmkSSQQoBDJEACJEACJEACJEACJDAsAmzDhkWaeUiABEggSYAjJEACJEACJEACtSTANqyWy85JkwAJkAAJ1JkA504CJEACJDBqAhVuw5bmtkyZ286FAPPCTjMwtWVuKTYkjQSm/EUCJEACJEACJEACJOBKgH4kQAIRAhVuwx4984p5fdu/+diM34gtzZ1cqwfm52dX79nhN2ILO2fUrB4TRiK0uEsCJEACJEACJEACJEACJFAiAkUttcJt2OTkpE99/MzV/m81Pj1tRtSKVRP+0MLhg+vW+mOTl21Wd9+7pJIjviE3JEACJEACJEACJEACJEACJDAoAhVuw1qI2p1Va0Q9evzo6jPH1dLJYxOrVphRNGtHjz+aHDHa5HZfSW4skwRIgARIgARI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"
    },
    "image.png": {
     "image/png": "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"
    }
   },
   "cell_type": "markdown",
   "id": "e818e28a",
   "metadata": {},
   "source": [
    "El programa en LabvIEW es muy simple, solo se debe acceder al script de python (descrito anteriormente paso por paso) a la funcion que se desea  desarrollar.\n",
    "\n",
    "### Inicializar python\n",
    "\n",
    "![image.png](attachment:image.png)\n",
    "\n",
    "al modulo \"Open python Session\" se le asigna la versión del python usado, en este caso \"3.9.12\" y la dirección donde se encuentra la versión de python que se usará, si solo se tiene una versión de python, no es necesario pasarle la dirección.\n",
    "\n",
    "### Conectar a la FPGA\n",
    "\n",
    "![image-2.png](attachment:image-2.png)\n",
    "\n",
    "El módulo \"Python Node\" se encarga de llamar la funcion y pasarle los parametros necesarios.\n",
    "\n",
    "Debe tener la ruta donde se encuentra el archivo *.py, luego el nombre de la función, en nuestro caso \"conectar\" a la entrada de color gris con el nombre \"abc\" se le conecta el tipo de variable que se espera retorne la función. la siguiente entrada son los parametros, en el caso de la función \"conectar\" se le debe ingresar el host (dirección IP) = \"192.168.1.58\". la funcion retorna la variable \"return value\"\n",
    "\n",
    "### Leer los datos\n",
    "\n",
    "![image-3.png](attachment:image-3.png)\n",
    "\n",
    "El módulo \"Python Node\" llama la funcion \"tomarDatos\" cómo parámetro se le envia la cantidad de muestras, y el tipo de variable que retorna es\n",
    "un array (vector o lista) de enteros que pasan a la gráfica de labview \n",
    "\n",
    "#### Diagrama de bloques\n",
    "\n",
    "![image-4.png](attachment:image-4.png)\n",
    "\n",
    "#### Panel\n",
    "\n",
    "![image-5.png](attachment:image-5.png)\n",
    "\n",
    "\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "1e02e1cb",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
