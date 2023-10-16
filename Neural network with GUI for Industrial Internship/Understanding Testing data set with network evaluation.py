# Libraries needed: 
import os
from keras.models import load_model
from keras.preprocessing.image import ImageDataGenerator




# loading our trained AI:
model_3 = load_model('FF.h5')

# Folder location using os: 
base_dir = '/Users/TP042318/Desktop/Fruits'
test_dir = os.path.join(base_dir, 'test')


# rescaling:
# Normalised 0->1
test_datagen = ImageDataGenerator(rescale=1./255)

# Depending on the trained model choose your parameters:

test_batches= test_datagen.flow_from_directory(
    directory=test_dir,
    color_mode='rgb',
    target_size=(150, 150),
    batch_size= 20,
    classes =['Potato', 'apple','capsicum','Broccoli'],
    shuffle=False,
)



# function for predicting all the images in the test folder: 
#Parameter 1:  Data tested which is test_batches in this case. 
#Parameter 2: steps needed to test all the images in test_batches, which is total number of images in test folder / batch_size
#Parameter 3: always Zero 

# call AI function to test and for classification
predictions = model_3.predict_generator(test_batches, steps= 4 , verbose=0)

# This code is to evaluate our system performance showing overall accuracy and loss:  
loss, acc = model_3.evaluate_generator(test_batches, steps= 4, verbose=0)
print('loss = ',loss, 'Accuracy=',acc)

