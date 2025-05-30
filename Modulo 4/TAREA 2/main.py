from emotion_model import EmotionModel
from emotion_detector_app import EmotionDetectorApp
import os

def main():
    # Ruta al dataset organizado por emoción
    data_dir = r"/Users/cesar/Documents/TEC DE CULIACAN/8 SEMESTRE TEC/IA/Modulo 4/TAREA 2/train"
    labels = ['angry', 'disgust', 'happy', 'sad', 'surprise']
    model_path = "emotion_model.h5"

    # Paso 1: Entrenar el modelo
    model_trainer = EmotionModel(data_dir, labels, model_path)
    model_trainer.build_model()
    model_trainer.train()

    # Paso 2: Detectar emociones en tiempo real
    detector = EmotionDetectorApp(model_path, labels)
    detector.run()

if __name__ == "__main__":
    main()
