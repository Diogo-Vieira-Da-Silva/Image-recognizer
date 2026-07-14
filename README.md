📝 Description: This project is a real-time computer vision application that uses a custom Image Classification model trained via Google's Teachable Machine. The system captures video from your webcam, processes each frame, and displays the predicted class along with the confidence percentage directly on the screen using OpenCV.

⚙️ How It Works: Model Loading: The system uses the `tf-keras` package to safely load the model (in the legacy `.h5` format), avoiding incompatibilities with modern Keras 3. Video Capture: OpenCV accesses the default webcam (index 0) and captures the video feed frame by frame. Pre-processing: Each frame is resized to $224 \times 224$ pixels and normalized to a range between $-1$ and $1$, matching the exact format expected by the model: (1, 224, 224, 3). Inference and Interface: The model analyzes the processed image. The class with the highest probability is extracted and displayed in real-time over the camera feed.

🚀 Setup and Installation

Prerequisites:

Python 3.10 or higher installed.

Trained model files (`keras_Model.h5` and `labels.txt`) from Teachable Machine (to obtain them: visit the site, click "Get Started," select "Image Project," then "Standard Image Mode." There, you can either upload files or record the classes you intend to use for training via your webcam. Afterward, click "Train Model." Once finished, click "Export Model," select "TensorFlow," and copy the code from the Keras section—you can use this as a base, though you may need to make modifications as I did. Additionally, download the model; a folder will be created containing the necessary files, which you should move into your project folder: `keras_model.h5` and `labels.txt`). 

Step-by-Step Commands: Open your VS Code terminal within the project folder and run the following commands:

- Create and activate a virtual environment (Recommended):
python -m venv venv
.\venv\Scripts\activate

- Install the necessary dependencies:
python -m pip install --upgrade pip
python -m pip install tensorflow tf-keras opencv-python pillow numpy

File Organization:

Ensure your project folder structure looks like this:

📁 your-folder-name/
├── 📄 images.py        (Your Python code)
├── 📄 keras_Model.h5  (The model file)
└── 📄 labels.txt      (The file containing class labels)

Run the application:

python images.py

Note: Press the 'Q' key while the video window is selected to safely exit the program.



--------------------------------------------------TRADUÇÃO-----------------------------------------

📝 DescriçãoEste projeto é uma aplicação de visão computacional em tempo real que utiliza um modelo de Classificação de Imagens personalizado, treinado no Teachable Machine do Google. O sistema captura o vídeo da sua webcam, processa cada quadro e exibe a classe prevista junto com a porcentagem de precisão diretamente na tela usando OpenCV.

⚙️ Como FuncionaCarregamento do Modelo: O sistema utiliza o pacote tf-keras para carregar o modelo antigo formato .h5 com segurança, evitando incompatibilidades com o Keras 3 moderno.Captura de Vídeo: O OpenCV acessa a webcam padrão (índice 0) e captura o feed de vídeo quadro a quadro.Pré-processamento: Cada quadro é redimensionado para $224 \times 224$ pixels e normalizado para um intervalo entre $-1$ e $1$, correspondendo exatamente ao formato esperado pelo modelo: (1, 224, 224, 3).Inferência e Interface: O modelo analisa a imagem tratada. A classe com maior probabilidade é extraída e desenhada em tempo real sobre o vídeo da câmera.

🚀 Configuração e Instalação

Pré-requisitos: 

Python 3.10 ou superior instalado.

Os arquivos do modelo treinado (keras_Model.h5 e labels.txt) do Teachable Machine(para instalar eles, apenas vá no site, clique em get started, depois em image project, então em Standar image mode, e lá poderá ou enviar arquivos ou gravar pela webcam as classes que irá usar para o treinamento do modelo, após isso, clique em train model, e depois de concluído, clique em export model, depois em Tensorflow e daí copie o código da sessão Keras, aí você usará ele de base para o código e poderá ter que fazer algumas modificações como eu fiz, mas além disso, faça download do modelo, será criada uma pasta e dentro dela, você deve pegar os arquivos dela e botar na pasta do projeto, serão criados o keras_model.h5 e o labels.text).

Comandos Passo a Passo:

Abra o terminal do seu VS Code dentro da pasta do projeto e execute os seguintes comandos:

- Criar e ativar um ambiente virtual (Recomendado):
python -m venv venv 
.\venv\Scripts\activate

- Instalar as dependências necessárias:
python -m pip install --upgrade pip
python -m pip install tensorflow tf-keras opencv-python pillow numpy

Organização dos Arquivos:

Certifique-se de que a estrutura da pasta do seu projeto esteja assim:

📁 nome-da-sua-pasta/
├── 📄 images.py        (O seu código Python)
├── 📄 keras_Model.h5  (O arquivo do modelo)
└── 📄 labels.txt      (O arquivo com as etiquetas das classes)

Executar a aplicação:

python images.py

Nota: Pressione a tecla 'Q' com a janela do vídeo selecionada para encerrar o programa com segurança.
---

