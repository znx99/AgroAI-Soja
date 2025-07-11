from tensorflow.keras.models import load_model  # Usando tf.keras
from PIL import Image, ImageOps
import numpy as np

np.set_printoptions(suppress=True)
#Carregando o modelo e retornando ele em uma variavel
def load_keras_model(model_path):
    return load_model(model_path, compile=False)
#Carregando as classes do labels.txt
def load_class_labels(labels_path):
    with open(labels_path, "r") as f:
        return f.readlines()
#Preparando a imagem para o modelo poder classifica-la
def preprocess_image(image_path, target_size=(224, 224)):
    image = Image.open(image_path).convert("RGB")
    image = ImageOps.fit(image, target_size, Image.Resampling.LANCZOS)
    image_array = np.asarray(image, dtype=np.float32)
    normalized_image_array = (image_array / 127.5) - 1  # Normaliza para [-1, 1]
    return normalized_image_array
#Esta funcao esta sendo ultilizada na interface
def main(image_path):

    try:
        model = load_keras_model("keras_Model.h5")
        class_names = load_class_labels("labels.txt")
        
        processed_image = preprocess_image(image_path)
        input_data = np.expand_dims(processed_image, axis=0)
        
        prediction = model.predict(input_data)
        class_index = np.argmax(prediction)
        class_name = class_names[class_index].strip()
        confidence = prediction[0][class_index]

        print(f"Classe: {class_name}")
        print(f"Confiança: {confidence:.4f}")
        return class_name

    except Exception as e:
        print(f"ERRO: {e}")

