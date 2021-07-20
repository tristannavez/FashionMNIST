# -*- coding: utf-8 -*-
"""fashion_mnist.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1sLHcBGQMAY5r4qpIEHuDTeV4Lvam4IIf
"""

import matplotlib.pyplot as plt
import tensorflow as tf
import numpy as np
import pandas as pd
import sys

"""Importation d'une bibliothèque (MNIST) de 60.000 images de vêtements depuis Zalando"""

fashion_mnist = tf.keras.datasets.fashion_mnist
(images, targets), (images_test, targets_test) = fashion_mnist.load_data()

images = images.astype(float)
images_test = images_test.astype(float)

images = images/255
images_test = images_test/255

print(images.shape)
print(targets.shape)

#affichage de la 15000e image de la bibliothèque
plt.imshow(images[15000])

targets_names= ["T-shirt", "Pantalon", "Pull", "Robe", "Manteau", "Sandale", "Chemise", "Sneaker", "Sac", "Bottes"]

"""Création du premier réseau de neuronnes 

"""

#Initialisation du modèle
model = tf.keras.models.Sequential()

#Ajout de la couche Flatten -> applatir les données -> image -> matrice -> vecteurs
model.add(tf.keras.layers.Flatten(input_shape=[28,28]))

#1ere couche avec 256 neuronnes
model.add(tf.keras.layers.Dense(256, activation="relu"))
#2e couche avec 128 neuronnes
model.add(tf.keras.layers.Dense(128, activation="relu"))
model.add(tf.keras.layers.Dense(10, activation="softmax"))

#résumé des couches qu'on obtient
model.summary()

#compilation du modèle
model.compile(
    loss="sparse_categorical_crossentropy",
    optimizer="adam",
    metrics=["accuracy"]
)

#on fit les images avec les catégories
#entrainement du modele
history = model.fit(images, targets, epochs=10, validation_split=0.2)

#schema d'évolution du modele
loss_curve = history.history["loss"]
acc_curve = history.history["accuracy"]

loss_val_curve = history.history["val_loss"]
acc_val_curve = history.history["val_accuracy"]

plt.plot(loss_curve, label="Train")
plt.plot(loss_val_curve, label="Val")
plt.legend(loc='upper left')
plt.title("Loss")
plt.show()

plt.plot(acc_curve, label="Train")
plt.plot(acc_val_curve, label="Val")
plt.legend(loc='upper left')
plt.title("Accuracy")
plt.show()

loss, acc = model.evaluate(images_test, targets_test)
print("Test Loss", loss)
print("Test Accuracy", acc)

"""Fasion MNIST avec CNN"""

fashion_mnist = tf.keras.datasets.fashion_mnist
data = tf.keras.datasets.fashion_mnist.load_data()

x_train = data[0][0]
y_train = data[0][1]

x_test = data[1][0]
y_test = data[1][1]

#Nos images sont sous la forme de vecteurs lignes, on va les mettre sous forme de vecteurs colonnes :

x_train = x_train.reshape(-1,28,28,1)
x_test = x_test.reshape(-1,28,28,1)

#On normalise nos pixels

x_train = x_train.astype('float')/255
x_test = x_test.astype('float')/255

model_cnn = tf.keras.Sequential()

model_cnn.add(tf.keras.layers.Conv2D(64, kernel_size=(4, 4),
                                     activation='relu',
                                     input_shape=(28, 28, 1)))

model_cnn.add(tf.keras.layers.MaxPooling2D(pool_size=(2, 2)))

model_cnn.add(tf.keras.layers.Flatten())

model_cnn.add(tf.keras.layers.Dense(128, activation='relu'))

model_cnn.add(tf.keras.layers.Dense(10, activation="softmax"))

model_cnn.summary()

model_cnn.compile(
    loss="sparse_categorical_crossentropy",
    optimizer="adam",
    metrics=["accuracy"]
)

history = model_cnn.fit(x_train,
                        y_train,
                        epochs=5,
                        validation_split = 0.2)

#schema d'évolution du modele
loss_curve = history.history["loss"]
acc_curve = history.history["accuracy"]

loss_val_curve = history.history["val_loss"]
acc_val_curve = history.history["val_accuracy"]

plt.plot(loss_curve, label="Train")
plt.plot(loss_val_curve, label="Val")
plt.legend(loc='upper left')
plt.title("Evolution de la fonction de perte")
plt.show()

plt.plot(acc_curve, label="Train")
plt.plot(acc_val_curve, label="Val")
plt.legend(loc='upper left')
plt.title("Evolution de la performance du modèle")
plt.show()

"""Calcul de la prédiction sur les données de test et matrice de confusion"""

model.predict(x_test)

predictions = []

prob_pred = model.predict(x_test)

for pred in prob_pred:
  predictions.append(np.argmax(pred))

prediction=np.array(predictions)

y_test

from sklearn.metrics import confusion_matrix
import seaborn as sns

sns.set()
mat = confusion_matrix(y_test, predictions)
sns.heatmap(mat.T, square=True, annot=True, fmt='d', cbar=False, xticklabels=targets_names, yticklabels=targets_names)
plt.xlabel('Categorie effective')
plt.ylabel('Categorie predite')

