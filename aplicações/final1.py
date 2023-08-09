import subprocess
import threading
import time

# Caminho para a pasta platform-tools
platform_tools_path = r'C:\Users\engen\Documents\android\platform-tools'

# Função para executar comandos adb
def run_adb_command(command):
    result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, shell=True)
    return result.stdout


def open_smartgaga():
    try:
        # Insira o caminho completo para o executável do SmartGaGa
        smartgaga_path = "C:\\Program Files (x86)\\SmartGaGa\\ProjectTitan\\Engine\\Launcher.exe"

        subprocess.Popen(smartgaga_path)
        print("SmartGaGa foi aberto.")
    except Exception as e:
        print("Não foi possível abrir o SmartGaGa.")
        print(f"Erro: {str(e)}")

def open_app_with_adb():
    # Substitua com o caminho para o executável adb em seu sistema
    adb_path = r"C:\Users\engen\Documents\android\platform-tools\adb"  # Use "r" antes da string para interpretar as barras invertidas literalmente

    # Substitua com o nome do pacote e a atividade do aplicativo que deseja abrir
    app_package = "com.LoFe.BalanaEspacial"
    app_activity = "com.unity3d.player.UnityPlayerActivity"

    # Comando para abrir o aplicativo
    adb_command = [
        adb_path,
        "shell",
        "am",
        "start",
        "-n",
        f"{app_package}/{app_activity}"
    ]

    # Executa o comando no terminal para abrir o aplicativo
    subprocess.run(adb_command)

def run_adb_commands():
    # Caminho para a pasta platform-tools
    platform_tools_path = r'C:\Users\engen\Documents\android\platform-tools'

    # Função para executar comandos adb
    def run_adb_command(command):
        result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, shell=True)
        return result.stdout

if __name__ == "__main__":
    # Crie uma thread para a execução do SmartGaGa em primeiro plano
    smartgaga_thread = threading.Thread(target=open_smartgaga)
    smartgaga_thread.start()
    # Aguarde 12 segundos
    time.sleep(20)
     # Navega até a pasta platform-tools
    subprocess.run(f'cd /d {platform_tools_path}', shell=True)
    # Executa os comandos adb após abrir o SmartGaGa
    
    run_adb_command('adb kill-server')
    run_adb_command('adb start-server')
    devices_output = run_adb_command('adb devices')
    print(devices_output)
    
    open_app_with_adb()