import subprocess

# Função para executar o executável
def run_executable(executable_path):
    while True:
        try:
            subprocess.run([executable_path])
        except Exception as e:
            print("Erro ao executar o executável:", e)

# Caminho para o executável
executable_path = r"C:\Users\engen\Desktop\dist\video.exe"

# Loop infinito para manter o programa em execução
while True:
    # Chama a função para executar o executável
    run_executable(executable_path)


