import pyglet
import imageio
import os

def play_video(video_path):
    # Carrega o vídeo usando a biblioteca imageio
    video = imageio.get_reader(video_path)

    # Obtém as informações do vídeo
    fps = video.get_meta_data()['fps']

    # Cria uma janela vazia
    window = pyglet.window.Window()

    # Obtém as dimensões do vídeo
    width, height = video.get_meta_data()['source_size']

    # Calcula a escala necessária para ajustar o vídeo à janela
    scale = min(window.width / width, window.height / height)

    # Calcula as coordenadas para centralizar o vídeo na janela
    video_x = (window.width - width * scale) / 2
    video_y = (window.height - height * scale) / 2

    # Variável para controlar o número do frame atual
    current_frame = 0

    # Função de callback para o evento de fechamento da janela
    @window.event
    def on_close():
        pyglet.app.exit()

    # Função de callback para o evento de desenho da janela
    @window.event
    def on_draw():
        window.clear()

        # Exibe o frame atual do vídeo com a transformação de rotação e dimensionamento
        video_frame = video.get_data(current_frame)
        texture = pyglet.image.ImageData(width, height, 'RGB', video_frame, -width * 3).get_texture()
        texture.width, texture.height = int(width * scale), int(height * scale)
        texture.blit(video_x, video_y)

    # Função para atualizar o frame do vídeo
    def update(dt):
        nonlocal current_frame

        # Verifica se o vídeo chegou ao final
        if current_frame == video.get_length() - 1:
            current_frame = 0  # Reinicia o vídeo
        else:
            current_frame += 1  # Incrementa o número do frame atual

    # Agendamento da função de atualização do frame
    pyglet.clock.schedule_interval(update, 1/fps)

    # Inicia a aplicação do Pyglet
    pyglet.app.run()

# Caminho para o diretório contendo o vídeo
video_directory = r"C:\Users\engen\Documents\videos"

# Lista os arquivos do diretório
files = os.listdir(video_directory)

# Filtra os arquivos com extensão .mp4
video_files = [f for f in files if f.endswith(".mp4")]

# Verifica se há pelo menos um arquivo de vídeo
if len(video_files) > 0:
    # Escolhe o primeiro arquivo de vídeo encontrado
    video_path = os.path.join(video_directory, video_files[0])

    # Loop infinito para manter o programa em execução
    while True:
        # Chama a função para reproduzir o vídeo
        play_video(video_path)
else:
    print("Nenhum arquivo de vídeo encontrado no diretório.")
