from keras import layers
from keras import Sequential

class TransformerEncoder(layers.Layer):
    def __init__(self, embed_dim, dense_dim, num_heads, **kwargs):
        super().__init__(**kwargs)
        self.embed_dim = embed_dim
        self.dense_dim = dense_dim
        self.num_heads = num_heads
        # Multi-Head Attention layer
        self.attention = layers.MultiHeadAttention(
            num_heads=num_heads, key_dim=embed_dim)
        # Feed Forward layer
        self.dense_proj = Sequential(
            [layers.Dense(dense_dim, activation="relu"),
             layers.Dense(embed_dim),]
        )
        # Add&Norm layer1
        self.layernorm_1 = layers.LayerNormalization()
        # Add&Norm layer2
        self.layernorm_2 = layers.LayerNormalization()

    def call(self, inputs):
        # Multi-Head Attention layer
        attention_output = self.attention(inputs, inputs)
        # Add&Norm layer1
        proj_input = self.layernorm_1(inputs + attention_output)
        # Feed Forward layer
        proj_output = self.dense_proj(proj_input)
        # Add&Norm layer2
        return self.layernorm_2(proj_input + proj_output)

    def get_config(self):
        config = super().get_config()
        config.update({
            "embed_dim": self.embed_dim,
            "num_heads": self.num_heads,
            "dense_dim": self.dense_dim,
        })
        return config