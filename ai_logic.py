import random
 
RETOS = {
    "fácil": [
        "Lista todos los archivos de la carpeta actual",
        "Muestra en qué carpeta estás ahora mismo",
        "Crea una carpeta llamada 'mis_archivos'",
        "Entra en la carpeta 'mis_archivos'",
        "Muestra el contenido del archivo 'notas.txt'",
        "Crea un archivo vacío llamado 'prueba.txt'",
        "Borra el archivo 'prueba.txt'",
        "Muestra los últimos 5 comandos que usaste",
        "Vuelve a la carpeta anterior",
        "Muestra el manual del comando 'ls'",
        "Limpia la pantalla del terminal",
        "Muestra la fecha y hora actual",
        "Crea una carpeta llamada 'backup'",
        "Lista archivos con sus tamaños en formato legible",
        "Muestra quién eres (tu usuario actual)",
    ],
    "medio": [
        "Lista todos los archivos incluyendo los ocultos",
        "Copia el archivo 'datos.txt' a la carpeta 'backup'",
        "Busca todos los archivos .txt en la carpeta actual",
        "Muestra las primeras 10 líneas de un archivo llamado 'log.txt'",
        "Muestra las últimas 10 líneas de un archivo llamado 'log.txt'",
        "Cambia los permisos de 'script.sh' para que sea ejecutable",
        "Muestra el espacio libre en disco",
        "Renombra el archivo 'viejo.txt' a 'nuevo.txt'",
        "Muestra el tamaño de la carpeta 'proyectos'",
        "Cuenta cuántas líneas tiene el archivo 'datos.txt'",
        "Muestra los procesos activos del sistema",
        "Busca la palabra 'error' dentro del archivo 'log.txt'",
        "Crea un archivo con el texto 'Hola Mundo' dentro",
        "Muestra las últimas líneas de un archivo en tiempo real",
        "Ordena el contenido del archivo 'lista.txt' alfabéticamente",
    ],
    "difícil": [
        "Busca la palabra 'error' dentro de todos los archivos .log",
        "Comprime la carpeta 'proyectos' en un archivo .tar.gz",
        "Muestra los procesos que más CPU están usando",
        "Crea un enlace simbólico de 'config.txt' llamado 'config_link'",
        "Muestra todas las conexiones de red activas",
        "Encuentra archivos modificados en las últimas 24 horas",
        "Muestra el uso de memoria RAM del sistema",
        "Extrae el archivo 'backup.tar.gz'",
        "Muestra las variables de entorno del sistema",
        "Busca archivos de más de 100MB en el sistema",
        "Redirige la salida de 'ls' a un archivo llamado 'lista.txt'",
        "Ejecuta un comando y muestra solo las líneas que contienen 'ok'",
        "Muestra el historial de conexiones SSH",
        "Cambia el propietario del archivo 'config.txt' a tu usuario",
        "Muestra los puertos abiertos en el sistema",
    ]
}
 
RESPUESTAS = {
    "Lista todos los archivos de la carpeta actual": ["ls", "ls -l"],
    "Muestra en qué carpeta estás ahora mismo": ["pwd"],
    "Crea una carpeta llamada 'mis_archivos'": ["mkdir mis_archivos"],
    "Entra en la carpeta 'mis_archivos'": ["cd mis_archivos"],
    "Muestra el contenido del archivo 'notas.txt'": ["cat notas.txt"],
    "Crea un archivo vacío llamado 'prueba.txt'": ["touch prueba.txt"],
    "Borra el archivo 'prueba.txt'": ["rm prueba.txt"],
    "Muestra los últimos 5 comandos que usaste": ["history 5"],
    "Vuelve a la carpeta anterior": ["cd ..", "cd -"],
    "Muestra el manual del comando 'ls'": ["man ls"],
    "Limpia la pantalla del terminal": ["clear"],
    "Muestra la fecha y hora actual": ["date"],
    "Crea una carpeta llamada 'backup'": ["mkdir backup"],
    "Lista archivos con sus tamaños en formato legible": ["ls -lh", "ls -lah"],
    "Muestra quién eres (tu usuario actual)": ["whoami"],
    "Lista todos los archivos incluyendo los ocultos": ["ls -a", "ls -la", "ls -al"],
    "Copia el archivo 'datos.txt' a la carpeta 'backup'": ["cp datos.txt backup", "cp datos.txt backup/"],
    "Busca todos los archivos .txt en la carpeta actual": ["find . -name '*.txt'", "find . -name \"*.txt\""],
    "Muestra las primeras 10 líneas de un archivo llamado 'log.txt'": ["head log.txt", "head -10 log.txt", "head -n 10 log.txt"],
    "Muestra las últimas 10 líneas de un archivo llamado 'log.txt'": ["tail log.txt", "tail -10 log.txt", "tail -n 10 log.txt"],
    "Cambia los permisos de 'script.sh' para que sea ejecutable": ["chmod +x script.sh", "chmod 755 script.sh"],
    "Muestra el espacio libre en disco": ["df -h", "df"],
    "Renombra el archivo 'viejo.txt' a 'nuevo.txt'": ["mv viejo.txt nuevo.txt"],
    "Muestra el tamaño de la carpeta 'proyectos'": ["du -sh proyectos", "du -h proyectos"],
    "Cuenta cuántas líneas tiene el archivo 'datos.txt'": ["wc -l datos.txt"],
    "Muestra los procesos activos del sistema": ["ps aux", "ps", "top"],
    "Busca la palabra 'error' dentro del archivo 'log.txt'": ["grep error log.txt", "grep 'error' log.txt"],
    "Crea un archivo con el texto 'Hola Mundo' dentro": ["echo 'Hola Mundo' > archivo.txt", "echo \"Hola Mundo\" > archivo.txt"],
    "Muestra las últimas líneas de un archivo en tiempo real": ["tail -f archivo.txt"],
    "Ordena el contenido del archivo 'lista.txt' alfabéticamente": ["sort lista.txt"],
    "Busca la palabra 'error' dentro de todos los archivos .log": ["grep 'error' *.log", "grep error *.log"],
    "Comprime la carpeta 'proyectos' en un archivo .tar.gz": ["tar -czf proyectos.tar.gz proyectos"],
    "Muestra los procesos que más CPU están usando": ["top", "htop"],
    "Crea un enlace simbólico de 'config.txt' llamado 'config_link'": ["ln -s config.txt config_link"],
    "Muestra todas las conexiones de red activas": ["netstat", "ss -tuln", "netstat -tuln"],
    "Encuentra archivos modificados en las últimas 24 horas": ["find . -mtime -1", "find . -mtime 0"],
    "Muestra el uso de memoria RAM del sistema": ["free -h", "free"],
    "Extrae el archivo 'backup.tar.gz'": ["tar -xzf backup.tar.gz"],
    "Muestra las variables de entorno del sistema": ["env", "printenv"],
    "Busca archivos de más de 100MB en el sistema": ["find / -size +100M"],
    "Redirige la salida de 'ls' a un archivo llamado 'lista.txt'": ["ls > lista.txt"],
    "Ejecuta un comando y muestra solo las líneas que contienen 'ok'": ["comando | grep ok", "comando | grep 'ok'"],
    "Muestra el historial de conexiones SSH": ["last", "who"],
    "Cambia el propietario del archivo 'config.txt' a tu usuario": ["chown $USER config.txt"],
    "Muestra los puertos abiertos en el sistema": ["ss -tuln", "netstat -tuln"],
}
 
PISTAS = {
    "Lista todos los archivos de la carpeta actual": "El comando empieza por 'l'",
    "Muestra en qué carpeta estás ahora mismo": "Son 3 letras: 'p', 'w', 'd'",
    "Crea una carpeta llamada 'mis_archivos'": "Usa 'mkdir' seguido del nombre",
    "Entra en la carpeta 'mis_archivos'": "Usa 'cd' seguido del nombre de la carpeta",
    "Muestra el contenido del archivo 'notas.txt'": "Usa 'cat' seguido del nombre del archivo",
    "Crea un archivo vacío llamado 'prueba.txt'": "El comando es 'touch'",
    "Borra el archivo 'prueba.txt'": "El comando es 'rm'",
    "Muestra los últimos 5 comandos que usaste": "Usa 'history' seguido de un número",
    "Vuelve a la carpeta anterior": "Usa 'cd' con dos puntos '..'",
    "Muestra el manual del comando 'ls'": "Usa 'man' seguido del comando",
    "Limpia la pantalla del terminal": "El comando es 'clear'",
    "Muestra la fecha y hora actual": "El comando es 'date'",
    "Crea una carpeta llamada 'backup'": "Usa 'mkdir' seguido del nombre",
    "Lista archivos con sus tamaños en formato legible": "Usa 'ls' con las opciones '-lh'",
    "Muestra quién eres (tu usuario actual)": "El comando es 'whoami'",
    "Lista todos los archivos incluyendo los ocultos": "Usa 'ls' con la opción '-a'",
    "Copia el archivo 'datos.txt' a la carpeta 'backup'": "Usa 'cp origen destino'",
    "Busca todos los archivos .txt en la carpeta actual": "Usa 'find . -name' con comodín '*'",
    "Muestra las primeras 10 líneas de un archivo llamado 'log.txt'": "El comando es 'head'",
    "Muestra las últimas 10 líneas de un archivo llamado 'log.txt'": "El comando es 'tail'",
    "Cambia los permisos de 'script.sh' para que sea ejecutable": "Usa 'chmod +x'",
    "Muestra el espacio libre en disco": "Usa 'df' con la opción '-h'",
    "Renombra el archivo 'viejo.txt' a 'nuevo.txt'": "Usa 'mv origen destino'",
    "Muestra el tamaño de la carpeta 'proyectos'": "Usa 'du -sh'",
    "Cuenta cuántas líneas tiene el archivo 'datos.txt'": "Usa 'wc' con la opción '-l'",
    "Muestra los procesos activos del sistema": "Usa 'ps aux' o 'top'",
    "Busca la palabra 'error' dentro del archivo 'log.txt'": "Usa 'grep palabra archivo'",
    "Crea un archivo con el texto 'Hola Mundo' dentro": "Usa 'echo' con '>' para redirigir",
    "Muestra las últimas líneas de un archivo en tiempo real": "Usa 'tail' con la opción '-f'",
    "Ordena el contenido del archivo 'lista.txt' alfabéticamente": "El comando es 'sort'",
    "Busca la palabra 'error' dentro de todos los archivos .log": "Usa 'grep' con '*.log'",
    "Comprime la carpeta 'proyectos' en un archivo .tar.gz": "Usa 'tar -czf nombre.tar.gz carpeta'",
    "Muestra los procesos que más CPU están usando": "El comando es 'top' o 'htop'",
    "Crea un enlace simbólico de 'config.txt' llamado 'config_link'": "Usa 'ln -s origen destino'",
    "Muestra todas las conexiones de red activas": "Usa 'netstat' o 'ss -tuln'",
    "Encuentra archivos modificados en las últimas 24 horas": "Usa 'find . -mtime -1'",
    "Muestra el uso de memoria RAM del sistema": "Usa 'free' con la opción '-h'",
    "Extrae el archivo 'backup.tar.gz'": "Usa 'tar -xzf archivo.tar.gz'",
    "Muestra las variables de entorno del sistema": "El comando es 'env' o 'printenv'",
    "Busca archivos de más de 100MB en el sistema": "Usa 'find / -size +100M'",
    "Redirige la salida de 'ls' a un archivo llamado 'lista.txt'": "Usa '>' para redirigir la salida",
    "Ejecuta un comando y muestra solo las líneas que contienen 'ok'": "Usa '|' (pipe) con 'grep'",
    "Muestra el historial de conexiones SSH": "El comando es 'last' o 'who'",
    "Cambia el propietario del archivo 'config.txt' a tu usuario": "Usa 'chown $USER archivo'",
    "Muestra los puertos abiertos en el sistema": "Usa 'ss -tuln' o 'netstat -tuln'",
}
 
 
def generar_reto(nivel, retos_usados=[]):
    nivel = nivel.lower()
    if nivel not in RETOS:
        nivel = "fácil"
    disponibles = [r for r in RETOS[nivel] if r not in retos_usados]
    if not disponibles:
        disponibles = RETOS[nivel]
    return random.choice(disponibles)
 
 
def corregir_comando(reto, respuesta):
    respuesta = respuesta.strip()
    correctas = RESPUESTAS.get(reto, [])
    correcto = any(respuesta.lower() == c.lower() for c in correctas)
    if correcto:
        explicacion = f"✅ ¡CORRECTO! '{respuesta}' es el comando adecuado."
    else:
        if correctas:
            explicacion = f"❌ NO ES CORRECTO. El comando era: '{correctas[0]}'"
        else:
            explicacion = "❌ NO ES CORRECTO. Inténtalo de nuevo."
    return correcto, explicacion
 
 
def obtener_pista(reto):
    return PISTAS.get(reto, "Piensa qué tipo de operación necesitas hacer en Linux.")