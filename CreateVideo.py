import cv2
import os

pasta_imagens = 'C:/Users/User/Desktop/meus aniversarios/Images'

arquivos_imagens = [os.path.join(pasta_imagens, arquivo) for arquivo in os.listdir(pasta_imagens) if arquivo.endswith('.jpg')]

largura = 1400
altura = 1400
fps = 0.5

codec = cv2.VideoWriter_fourcc(*'mp4v')
saida = cv2.VideoWriter('memorias.mp4', codec, fps, (largura, altura))

for imagem_path in arquivos_imagens:
    imagem = cv2.imread(imagem_path)
    if imagem is not None:
        Imagem_redimensionada = cv2.resize(imagem, (largura, altura))
        saida.write(Imagem_redimensionada)

saida.release()

print("Vídeo criado com sucesso!")