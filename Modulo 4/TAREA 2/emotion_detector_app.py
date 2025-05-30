import cv2
import numpy as np
from tensorflow.keras.models import load_model

class EmotionDetectorApp:
    # constructor
    def __init__(self, model_path, labels):
        self.model = load_model(model_path)
        self.labels = labels
        self.face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    # Preprocesamiento de la imagen de la cara
    def preprocess_face(self, face):
        face = cv2.resize(face, (48, 48))
        face = face.astype('float32') / 255.0
        face = np.expand_dims(face, axis=0)
        face = np.expand_dims(face, axis=-1)
        return face

    # Método para ejecutar la camara
    def run(self):
        cap = cv2.VideoCapture(0)
        print("Presiona 'q' para salir.")
        while True:
            ret, frame = cap.read()
            if not ret:
                break
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) # Convertir a escala de grises
            faces = self.face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5) # Detectar caras
            
            # Procesar cada cara detectada
            for (x, y, w, h) in faces:
                face_img = gray[y:y+h, x:x+w]
                processed = self.preprocess_face(face_img)
                prediction = self.model.predict(processed)[0]
                emotion = self.labels[np.argmax(prediction)]
                confidence = round(np.max(prediction) * 100, 2)

                cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
                cv2.putText(frame, emotion, (x, y-10),
                cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)


            cv2.imshow('Detector de Emociones', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        cap.release()
        cv2.destroyAllWindows()
