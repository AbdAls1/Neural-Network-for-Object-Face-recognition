# These are the the libraries needed from us to use Keras (Please see Arun's Vedio on how to install them):
 
import os
from keras.preprocessing.image import ImageDataGenerator
from keras import models
from keras import layers
from keras import optimizers
import numpy as np

# Folder locationOS library ( We need to creare a main folder that contains three folders train, test and validation within those three folders we can
add as many folders as wanted each folder will represent a class ):

base_dir = '/Users/TP042318/Desktop/Fruits'
train_dir = os.path.join(base_dir, 'train')
validation_dir = os.path.join(base_dir, 'validation')
test_dir = os.path.join(base_dir, 'test')


# Now Building  a CNN model using Keras functions:
model = models.Sequential()

# The sequental model is a linear stack of layers
# first layer :adding a 2dimensional convolutional layer that its window size is 3x3 and the window is a small area taken from the 
# bigger image and its filtered in 128 ways. 128 is a variable choosen by the programmer 
#depending on what works best with the current task.
#and the (3,3) is the kernal size (filters: Integer, the dimensionality of the output space 
#(i.e. the number of output filters in the convolution).
#kernel_size: An integer or tuple/list of 2 integers, specifying the height and width of the 2D.
#Lastly, input_shape is specified in the first layer. 
   
model.add(layers.Conv2D(128, (3,3), activation='relu', 
input_shape=(150, 150, 3)))
# the output comes out as a relu or a rectified linear unit meaning the output comes in a range of number between 0 and 1
model.add(layers.MaxPooling2D((2, 2)))# reduces the sampling by half to reduce computing power needed.
model.add(layers.Conv2D(128, (3, 3), activation='relu'))
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Conv2D(64, (3, 3), activation='relu'))
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Conv2D(32, (3, 3), activation='relu'))
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Flatten())# you need to convert the output of the convolutional part of the CNN into a 1D feature vector.
model.add(layers.Dropout(0.5))# Dropout: A Simple Way to Prevent Neural Networks from Overfitting
model.add(layers.Dense(1000, activation='relu')) # A dense layer is just a regular layer of neurons in a neural network. 
#Each neuron recieves input from all the neurons in the previous layer, thus densely connected, final layers that 
#classifies the features obtained from CNN layers.
model.add(layers.Dense(4, activation='softmax')) # Last layer has the number of outputs equals to the classes created 
#to make a classifications. here we used 4. 

# Compiling the model and specifying the loss and optimizer chosen to be used (if u have more than 2 classes use the loss function used here):
model.compile(loss='categorical_crossentropy',
optimizer=optimizers.RMSprop(lr=1e-4),
metrics=['acc'])

# Training data augmentation (only for training images) using ImageDataGenerator (if the number of images is low then try using this function
# to recreate images with different paramters):
train_datagen =ImageDataGenerator(rescale=1./255, 
    rotation_range=15,
                               width_shift_range=0.1,
                               height_shift_range=0.1,
                               shear_range=0.01,
                               zoom_range=[0.9, 1.25],
                               horizontal_flip=True,
                               vertical_flip=False,
                               fill_mode='reflect',
                               data_format='channels_last',
                               brightness_range=[0.5, 1.5])
# Rescaling Validation images using ImageDataGenerator (Very important to rescale pixels value the range of 0 to 1 otherwise the network wont learn):
validation_datagen = ImageDataGenerator(rescale=1./255) 

# Using Flow from directory to optimize the training set and validation set(in here we resize images into the size used in the 
# first layer of our model and depending on how much ram avalible and system power we choose the how many images the process should 
# grab at once how ever always better to keep it one next if color is important use rgb, lastly we name our classes:
train_generator = train_datagen.flow_from_directory(
                                                   train_dir,
                                                    target_size=(150, 150),
                                                    batch_size=1,
                                                    color_mode='rgb',
                                                    classes=['Potato', 'apple','capsicum','Broccoli'])
# Same for Validation: 
validation_generator = validation_datagen.flow_from_directory(
validation_dir,
target_size=(150, 150),
batch_size=1,
color_mode='rgb',
classes=['Potato', 'apple','capsicum','Broccoli'])


# Training process using Keras function:

history = model.fit_generator(
train_generator, # our training Data 
steps_per_epoch=200,# Number of images divieded by batch_size = steps_per_epoch, no of processing to finish one image
epochs=200, # Depends on how long you want to train for each one is a whole step that trains for all the images then dose it again, no of training for 1 image 

validation_data=validation_generator, Our validation Data
validation_steps=100) # Number of images divieded by batch_size = steps_per_epoch

# To save the trained neural network:
model.save('NAME OF THE MODEL.h5') 

#Note: You can re-train the same model by loading it into another file then using the new training and validation
#images using image data generator to optimize everything then just use the model.fit_generator function to train
#and lastly save the newer model. No need to build new layers or compile. 










