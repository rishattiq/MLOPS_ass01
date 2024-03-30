import numpy as np
import matplotlib.pyplot as plt
from keras.models import Sequential
from keras.layers import Dense, Activation, Dropout
from keras.datasets import mnist
from keras.utils import to_categorical
from keras.utils import plot_model

# load dataset
(x_train, y_train), (x_test, y_test) = mnist.load_data()

# count the number of unique train labels
unique_train, counts_train = np.unique(y_train, return_counts=True)
print("Train labels: ", dict(zip(unique_train, counts_train)))

# count the number of unique test labels
unique_test, counts_test = np.unique(y_test, return_counts=True)
print("Test labels: ", dict(zip(unique_test, counts_test)))

# sample 25 mnist digits from train dataset
indexes = np.random.randint(0, x_train.shape[0], size=25)
images = x_train[indexes]
labels = y_train[indexes]

# plot the 25 mnist digits
plt.figure(figsize=(5, 5))
for i in range(len(indexes)):
    plt.subplot(5, 5, i + 1)
    image = images[i]
    plt.imshow(image, cmap="gray")
    plt.axis("off")

plt.show()

# convert to one-hot vector
num_labels = len(np.unique(y_train))
y_train = to_categorical(y_train, num_labels)
y_test = to_categorical(y_test, num_labels)

# image dimensions (assumed square)
image_size = x_train.shape[1]
input_size = image_size * image_size

# resize and normalize
x_train = np.reshape(x_train, [-1, input_size]).astype("float32") / 255
x_test = np.reshape(x_test, [-1, input_size]).astype("float32") / 255

# network parameters
batch_size = 128
hidden_units = 256
dropout = 0.45
num_classes = 10  # Number of classes in the MNIST dataset

# Model architecture
model = Sequential()
model.add(Dense(hidden_units, input_dim=input_size))
model.add(Activation("relu"))
model.add(Dropout(dropout))
model.add(Dense(hidden_units))
model.add(Activation("relu"))
model.add(Dropout(dropout))
model.add(Dense(num_classes))
model.add(Activation("softmax"))

# Compile the model
model.compile(loss="categorical_crossentropy", optimizer="adam", metrics=["accuracy"])

model.summary()

# Plot the model architecture
plot_model(model, to_file="mlp-mnist.png", show_shapes=True)

# Train the model
model.fit(x_train, y_train, epochs=20, batch_size=batch_size)

# Evaluate the model
loss, acc = model.evaluate(x_test, y_test, batch_size=batch_size)
print("\nTest accuracy: %.1f%%" % (100.0 * acc))