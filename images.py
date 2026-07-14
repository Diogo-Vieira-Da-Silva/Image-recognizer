import numpy as np
import cv2
# Usando o motor de compatibilidade que resolveu o problema
import tf_keras as keras

# Desativa a notação científica para clareza
np.set_printoptions(suppress=True)

print("Carregando o modelo de IA... Aguarde.")
model = keras.models.load_model("keras_Model.h5", compile=False)
print("Modelo carregado com sucesso!")

# Carrega as classes do arquivo labels.txt
class_names = open("labels.txt", "r").readlines()

# Limpa os nomes das classes (remove o número e o espaço do começo: "0 Class 1" vira "Class 1")
classes = [line.split(" ", 1)[1].strip() for line in class_names]

# Cria o array com o formato correto para o modelo (1, 224, 224, 3)
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

print("Iniciando a webcam... Pressione 'Q' na janela da imagem para sair.")
# Inicia a captura da webcam (0 é geralmente a webcam integrada)
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    raise RuntimeError("Não foi possível abrir a webcam. Verifique se ela está conectada ou sendo usada por outro app.")

while True:
    success, img = cap.read()
    if not success or img is None:
        print("Erro ao capturar imagem da webcam.")
        break

    # 1. Redimensiona a imagem para 224x224 (o tamanho que o modelo exige)
    img_s = cv2.resize(img, (224, 224))
    image_array = np.asarray(img_s)
    
    # 2. Normaliza a imagem exatamente como o Teachable Machine pede
    normalized_image_array = (image_array.astype(np.float32) / 127.5) - 1
    data[0] = normalized_image_array
    
    # 3. Faz a previsão em tempo real
    prediction = model.predict(data, verbose=0)
    index_val = int(np.argmax(prediction))
    confidence_score = prediction[0][index_val]

    # 4. Cria o texto com o resultado e a porcentagem de certeza
    texto_resultado = f"{classes[index_val]} ({confidence_score * 100:.1f}%)"

    # 5. Desenha o texto na tela da webcam
    cv2.putText(img, texto_resultado, (20, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    
    # Show a imagem na tela
    cv2.imshow("Detector IA em Tempo Real", img)

    # SE APERTAR A TECLA 'Q', O PROGRAMA FECHA
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# Finaliza tudo corretamente para não travar a câmera
cap.release()
cv2.destroyAllWindows()
print("Programa encerrado.")