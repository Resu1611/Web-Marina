# Directiva: Instalación de Skill UI UX Pro Max

## Objetivo
Instalar la herramienta CLI `uipro-cli` globalmente mediante npm y activarla para el agente local (antigravity) en el proyecto actual. Esto proveerá plantillas y directrices de UI/UX inteligentemente generadas.

## Requisitos Previos
- Node.js y npm deben estar instalados.
- Python 3.x (para el motor de la skill).
- Estar ejecutando dentro de un directorio de proyecto (ej. `Marina`).

## Entradas
- Carpeta raíz del proyecto.

## Salidas
- La instalación global del paquete `uipro-cli` en npm.
- La confirmación de inicialización (`uipro init --ai antigravity`).
- Presencia de scripts o archivos generados por `uipro` en las carpetas destinadas por dicha skill a `antigravity`.

## Lógica y Pasos Recomendados
1.  **Ejecución de Comando 1:** `npm install -g uipro-cli` para disponer del comando uipro de forma global.
2.  **Ejecución de Comando 2:** En el directorio raíz de la app, ejecutar `uipro init --ai antigravity` para inyectar la skill.
3.  **Verificación:** Asegurarse de que no ocurran errores de permisos (en Windows típicamente es permisivo para instalar globales, pero pueden saltar alertas de ejecución de scripts powershell. Si ocurre con Powershell, invocar usando cmd o `.cmd`).

## Trampas Conocidas, Restricciones y Casos Borde
-   *Permisos en Windows:* En algunos sistemas, un alias global de npm puede fallar por políticas de ejecución de PowerShell. Si falla, hay que invocar directamente `npx` o `uipro.cmd`.
-   *Rutas:* `npm i -g` requiere acceso de escritura a la carpeta AppData de Node.js.
-   *Disponibilidad de Python:* El comando `uipro init` requiere Python. Si el comando `python` falla con "Python was not found" en Windows, debe instalarse vía `winget install Python.Python.3.12 --accept-package-agreements --accept-source-agreements`. Posteriormente, al ejecutar scripts `.py`, si el PATH no se ha actualizado en la misma consola, se debe invocar usando la ruta absoluta completa, por ejemplo: `C:\Users\Javier\AppData\Local\Programs\Python\Python312\python.exe`.
-   *Directorio local:* `uipro init` asume que se está en la raíz de un proyecto para generar los archivos de asistente.
