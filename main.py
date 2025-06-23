from tensorflow.keras.models import load_model  # Usando tf.keras
from PIL import Image, ImageOps
import numpy as np

# Configuração do NumPy para evitar notação científica
np.set_printoptions(suppress=True)

def load_keras_model(model_path):
    """Carrega o modelo Keras"""
    return load_model(model_path, compile=False)

def load_class_labels(labels_path):
    """Carrega os rótulos das classes"""
    with open(labels_path, "r") as f:
        return f.readlines()

def preprocess_image(image_path, target_size=(224, 224)):
    """Pré-processa a imagem para predição"""
    image = Image.open(image_path).convert("RGB")
    image = ImageOps.fit(image, target_size, Image.Resampling.LANCZOS)
    image_array = np.asarray(image, dtype=np.float32)
    normalized_image_array = (image_array / 127.5) - 1  # Normaliza para [-1, 1]
    return normalized_image_array

def main(image_path):
    MODEL_PATH = "keras_Model.h5"
    LABELS_PATH = "labels.txt"
    IMAGE_PATH = image_path  # Substitua pelo seu arquivo

    try:
        model = load_keras_model(MODEL_PATH)
        class_names = load_class_labels(LABELS_PATH)
        
        processed_image = preprocess_image(IMAGE_PATH)
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

