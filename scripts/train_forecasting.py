import tensorflow as tf
from tensorflow.keras import layers, models
import pandas as pd
import numpy as np

df = pd.read_csv('transaksi_zakat.csv')
values = df['nominal_zakat'].values.reshape(-1, 1)

values = values / 1000.0

class HealthScoreCallback(tf.keras.callbacks.Callback):
    def on_epoch_end(self, epoch, logs = None):
        if logs.get('loss') < 0.01:
            print(f"\nLoss rendah di epoch {epoch}, menghentikan training!")
            self.model.stop_training = True

def build_forecasting_model():
    inputs = layers.Input(shape=(1, 1))
    x = layers.Dense(64, activation='relu')(inputs)
    x = layers.Dense(32, activation='relu')(x)

    outputs = layers.Dense(1)(x)

    model = models.Model(inputs=inputs, outputs=outputs)
    model.compile(optimizer='adam', loss='mae')
    return model

X_train = values[:-1].reshape(-1, 1, 1)
y_train = values[1:]

model = build_forecasting_model()
model.fit(X_train, y_train, epochs=100, callbacks=[HealthScoreCallback()])

model.save('model_forecasting_zakat.keras')
print("Model ZakatSight berhasil disimpan!")