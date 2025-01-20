from tensorflow.keras.layers import Input, Dense, Lambda
from tensorflow.keras.models import Model
from tensorflow.keras.losses import binary_crossentropy
from tensorflow.keras import backend as K

def vae_model(input_dim, latent_dim):
    # Encoder
    inputs = Input(shape=(input_dim,))
    hidden = Dense(128, activation='relu')(inputs)
    z_mean = Dense(latent_dim)(hidden)
    z_log_var = Dense(latent_dim)(hidden)

    # Sampling function
    def sampling(args):
        z_mean, z_log_var = args
        batch = K.shape(z_mean)[0]
        epsilon = K.random_normal(shape=(batch, latent_dim))
        return z_mean + K.exp(0.5 * z_log_var) * epsilon

    z = Lambda(sampling, output_shape=(latent_dim,))([z_mean, z_log_var])

    # Decoder
    decoder_hidden = Dense(128, activation='relu')
    decoder_out = Dense(input_dim, activation='sigmoid')
    decoded = decoder_out(decoder_hidden(z))

    # VAE model
    vae = Model(inputs, decoded)
    vae_loss = binary_crossentropy(inputs, decoded) * input_dim
    vae.add_loss(vae_loss)
    vae.compile(optimizer='adam')
    return vae

# Assuming we have prepared our input data `x_train`
vae = vae_model(input_dim=x_train.shape[1], latent_dim=50)
vae.fit(x_train, epochs=50, batch_size=32)


