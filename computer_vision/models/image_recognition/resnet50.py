import tensorflow as tf
from tensorflow.keras import layers
from tensorflow.keras.applications import ResNet50

# Load the pre-trained ResNet50 model
base_model = ResNet50(weights='imagenet', include_top=False)

# Add a global average pooling layer
x = layers.GlobalAveragePooling2D()(base_model.output)

# Add a dense layer with 1024 units and ReLU activation
x = layers.Dense(1024, activation='relu')(x)

# Add a dropout layer with a rate of 0.5
x = layers.Dropout(0.5)(x)

# Add a dense layer with the number of classes as the number of units and softmax activation
output = layers.Dense(num_classes, activation='softmax')(x)

# Create the model
model = tf.keras.Model(inputs=base_model.input, outputs=output)

# Compile the model
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
