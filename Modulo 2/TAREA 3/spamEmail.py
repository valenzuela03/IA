import numpy as np
import pandas as pd
import tkinter as tk
from tkinter import ttk, messagebox
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from nltk.corpus import stopwords

# Cargar dataset
dataset = pd.read_csv("/Users/cesar/Documents/TEC DE CULIACAN/8 SEMESTRE TEC/IA/Modulo 2/TAREA 3/spam_assassin.csv")

# Función para limpiar correos
def limpiar_texto(texto, stop_words):
    # Convertir a minúsculas y eliminar caracteres no alfanuméricos 
    texto = texto.lower()
    texto = ''.join([c if c.isalnum() or c.isspace() else ' ' for c in texto])
    return ' '.join(word for word in texto.split() if word not in stop_words)

# Preparar los datos aplicando limpieza de texto
stop_words = set(stopwords.words('spanish')).union(stopwords.words('english'))
ds_clean = dataset.drop_duplicates(subset="text").copy()
ds_clean['text'] = ds_clean['text'].apply(lambda x: limpiar_texto(x, stop_words))

# Dividir en conjuntos de entrenamiento y prueba
# 80% para entrenamiento y 20% para prueba
x_train, x_test, y_train, y_test = train_test_split(ds_clean['text'], ds_clean['target'], test_size=0.20, random_state=42)

# Vectorización
# Convertir los correos a vectores de frecuencia de palabras
vectorizer = CountVectorizer()
x_train_count = vectorizer.fit_transform(x_train)
x_test_count = vectorizer.transform(x_test)

# Implementación manual de Bayes
# Probabilidad previa de spam y no spam
p_spam = np.mean(y_train)
p_no_spam = 1 - p_spam

# Calcular la probabilidad de cada palabra en el vocabulario dado spam o no spam
# Utilizamos Laplace smoothing (sumando +1) para evitar probabilidades nulas
x_train_array = x_train_count.toarray()
total_spam = x_train_array[y_train == 1].sum()
total_no_spam = x_train_array[y_train == 0].sum()
p_palabra_dado_spam = (x_train_array[y_train == 1].sum(axis=0) + 1) / (total_spam + len(vectorizer.get_feature_names_out()))
p_palabra_dado_no_spam = (x_train_array[y_train == 0].sum(axis=0) + 1) / (total_no_spam + len(vectorizer.get_feature_names_out()))

# Función para predecir si un correo es spam(1) o no spam(0) usando implementación manual
def predecir(email):
    # Convertir el correo a un vector de frecuencia de palabras
    email_vector = vectorizer.transform([email]).toarray()[0]
    # Calcular la probabilidad posterior para spam y no spam
    log_prob_spam = np.log(p_spam) + np.sum(email_vector * np.log(p_palabra_dado_spam))
    log_prob_no_spam = np.log(p_no_spam) + np.sum(email_vector * np.log(p_palabra_dado_no_spam))
    return 1 if log_prob_spam > log_prob_no_spam else 0

# Implementación con MultinomialNB de sklearn para Bayes
# Crear y entrenar el modelo de Naive Bayes de sklearn
modelo_sklearn = MultinomialNB()
modelo_sklearn.fit(x_train_count, y_train)

#Creacion de interfaz
def crear_interfaz():
    def verificar_spam():
        asunto = entrada_asunto.get()
        if not asunto.strip():
            messagebox.showwarning("Advertencia", "Por favor ingresa un asunto para verificar")
            return
        
        resultado = predecir(asunto)
        if resultado == 1:
            etiqueta_resultado.config(text="SPAM", foreground="red")
        else:
            etiqueta_resultado.config(text="NO ES SPAM", foreground="green")
    
    # Crear ventana principal
    ventana = tk.Tk()
    ventana.title("Clasificador de Spam")
    ventana.geometry("500x300")
    ventana.resizable(False, False)
    
    # Estilo de la interfaz
    estilo = ttk.Style()
    estilo.configure('TFrame', background='#f0f0f0')
    estilo.configure('TLabel', background='#f0f0f0', font=('Arial', 10))
    estilo.configure('TButton', font=('Arial', 10))
    
    # Crear marco principal
    marco = ttk.Frame(ventana, padding="20")
    marco.pack(fill=tk.BOTH, expand=True)
    
    titulo = ttk.Label(marco, text="Clasificador de Correos Spam", font=('Arial', 14, 'bold'))
    titulo.pack(pady=10)
    
    instrucciones = ttk.Label(marco, text="Ingresa el asunto del correo electrónico para verificar si es spam:", wraplength=400)
    instrucciones.pack(pady=10)
    
    entrada_asunto = ttk.Entry(marco, width=50, font=('Arial', 10))
    entrada_asunto.pack(pady=10)
    entrada_asunto.focus()
    
    boton_verificar = ttk.Button(marco, text="Verificar", command=verificar_spam)
    boton_verificar.pack(pady=10)
    
    etiqueta_resultado = ttk.Label(marco, text="", font=('Arial', 12, 'bold'))
    etiqueta_resultado.pack(pady=20)
    
    ventana.mainloop()

if __name__ == "__main__":
    crear_interfaz()


#correo = input("Introduce el asunto del correo para saber si es spam o no: ")
#print("El correo es spam" if predecir(correo) == 1 else "El correo no es spam")