"""
Step 1: Load and Inspect the Data
First, we need to load your dataset and inspect it to understand the structure
 and types of data available. This will help us decide how to handle categorical and numerical data.
"""

import pandas as pd

# Load the dataset
data = pd.read_csv('/path/to/your/SampleSuperstore(in).csv')

# Display the first few rows of the dataframe
print(data.head())

# Display general information about the dataframe
print(data.info())


"""
Step 2: Data Preprocessing

Based on the initial inspection, let's assume the dataset includes both categorical and numerical 
columns. We will preprocess these by encoding categorical columns and scaling numerical columns.
"""
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline

# Identify categorical and numerical columns
categorical_cols = data.select_dtypes(include=['object']).columns  # Adjust if necessary
numerical_cols = data.select_dtypes(include=['float64', 'int64']).columns  # Adjust if necessary

# Create a column transformer to apply different preprocessing to different columns
preprocessor = ColumnTransformer(
    transformers=[
        ('num', StandardScaler(), numerical_cols),
        ('cat', OneHotEncoder(), categorical_cols)
    ])

# Fit and transform the data
data_processed = preprocessor.fit_transform(data)

"""
Step 3: Setting Up the VAE

Now that we have preprocessed the data, we can set up a simple VAE.
 I'll provide a simplified version here suitable for your dataset.
"""

import numpy as np
from tensorflow.keras.layers import Input, Dense, Lambda, Layer, Concatenate
from tensorflow.keras.models import Model
from tensorflow.keras.losses import mse
from tensorflow.keras import backend as K

def sampling(args):
    z_mean, z_log_var = args
    batch = K.shape(z_mean)[0]
    epsilon = K.random_normal(shape=(batch, latent_dim))
    return z_mean + K.exp(0.5 * z_log_var) * epsilon

# VAE model parameters
original_dim = data_processed.shape[1]
intermediate_dim = 256
latent_dim = 2

# Encoder setup
inputs = Input(shape=(original_dim,))
x = Dense(intermediate_dim, activation='relu')(inputs)
z_mean = Dense(latent_dim)(x)
z_log_var = Dense(latent_dim)(x)
z = Lambda(sampling, output_shape=(latent_dim,))([z_mean, z_log_var])

# Decoder setup
decoder_h = Dense(intermediate_dim, activation='relu')
decoder_mean = Dense(original_dim, activation='sigmoid')
h_decoded = decoder_h(z)
x_decoded_mean = decoder_mean(h_decoded)

# VAE model
vae = Model(inputs, x_decoded_mean)
encoder = Model(inputs, z_mean)

# Loss function
xent_loss = mse(inputs, x_decoded_mean) * original_dim
kl_loss = -0.5 * K.sum(1 + z_log_var - K.square(z_mean) - K.exp(z_log_var), axis=-1)
vae_loss = K.mean(xent_loss + kl_loss)

vae.add_loss(vae_loss)
vae.compile(optimizer='adam')

"""
Step 4: Train the VAE
With the VAE set up, we train it using the preprocessed data:
"""

vae.fit(data_processed, epochs=30, batch_size=128)


"""
Step 5: Generate New Data
After training, the VAE can be used to generate new data samples by sampling from the latent space:
"""

# Sampling from the latent space to generate new data
n_samples = 10
z_sample = np.random.normal(size=(n_samples, latent_dim))
samples = decoder.predict(z_sample)
