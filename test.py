import unittest
import numpy as np
from keras.models import Sequential
from keras.layers import Dense, Activation, Dropout
from keras.datasets import mnist
from keras.utils import to_categorical


class TestMNISTModel(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Load MNIST dataset
        (cls.x_train, cls.y_train), (cls.x_test, cls.y_test) = mnist.load_data()
        # Preprocess data
        num_labels = len(np.unique(cls.y_train))
        cls.y_train = to_categorical(cls.y_train, num_labels)
        cls.y_test = to_categorical(cls.y_test, num_labels)
        image_size = cls.x_train.shape[1]
        input_size = image_size * image_size
        cls.x_train = np.reshape(cls.x_train, [-1, input_size]).astype("float32") / 255
        cls.x_test = np.reshape(cls.x_test, [-1, input_size]).astype("float32") / 255
        # Create model
        cls.model = Sequential()
        cls.model.add(Dense(256, input_dim=input_size))
        cls.model.add(Activation("relu"))
        cls.model.add(Dropout(0.45))
        cls.model.add(Dense(256))
        cls.model.add(Activation("relu"))
        cls.model.add(Dropout(0.45))
        cls.model.add(Dense(10))
        cls.model.add(Activation("softmax"))
        cls.model.compile(
            loss="categorical_crossentropy", optimizer="adam", metrics=["accuracy"]
        )
        cls.model.fit(cls.x_train, cls.y_train, epochs=5, batch_size=128, verbose=0)

    def test_model_accuracy(self):
        loss, accuracy = self.model.evaluate(self.x_test, self.y_test, verbose=0)
        self.assertGreaterEqual(accuracy, 0.9, "Model accuracy is less than 90%")


if name == "main":
    unittest.main()