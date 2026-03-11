import subprocess
import os
import sys

def main():
    print("Iniciando la instalación de la skill ui-ux-pro-max...")
    # 1. Instalar uipro-cli globalmente
    try:
        print("Ejecutando: npm install -g uipro-cli")
        res1 = subprocess.run("npm install -g uipro-cli", cwd=os.getcwd(), capture_output=True, text=True, shell=True)
        if res1.returncode != 0:
            print(f"Error instalando uipro-cli:\n{res1.stderr}")
            sys.exit(1)
        print("Instalación global finalizada con éxito.")
    except Exception as e:
        print(f"Excepción al instalar: {e}")
        sys.exit(1)

    # 2. Inicializar para antigravity
    try:
        print("Ejecutando: uipro init --ai antigravity")
        # uipro may need .cmd extension on Windows if called without shell
        res2 = subprocess.run("uipro init --ai antigravity", cwd=os.getcwd(), capture_output=True, text=True, shell=True)
        if res2.returncode != 0:
            print(f"Error inicializando skill uipro:\n{res2.stderr}\nSTDOUT:\n{res2.stdout}")
            sys.exit(1)
        print("Skill uipro-cli inicializada exitosamente.")
        print(f"Detalles:\n{res2.stdout}")
    except Exception as e:
        print(f"Excepción al inicializar: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
