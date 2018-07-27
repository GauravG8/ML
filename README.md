# ML Adventures
Learning Machine Learning. Starting out the process of learning with my trusty sidekick, Raven.

#### 7th July, 2018: 
Starting out by understanding the [Rasa NLU](https://github.com/GauravG8/rasa_nlu)

https://medium.com/@gauravgpunjabi/getting-started-with-machine-learning-ea0dc29e3ff6

#### 8th July, 2018:
Compling the Raven Android project in Kotlin, the beginnings of an intelligent chatbot and a few resources for ML.

https://github.com/GauravG8/raven-kotlin

#### 9th July, 2018:
Exploring Jupyter Notebooks and Google Colaboratory (https://github.com/GauravG8/ML/blob/master/Hello%2C_Colaboratory.ipynb)

Added Reminders support to Dialogflow for Raven


#### 10th July, 2018
Understanding Neural Style transfer
https://www.youtube.com/watch?v=pQyzdwHBbqo

![Neural Style Transfer](https://github.com/GauravG8/ML/blob/master/neural-style-transfer/nst_2018-07-10_3.png)

[Neural Artistic Style Transfer: A Comprehensive Look - Medium](https://medium.com/artists-and-machine-intelligence/neural-artistic-style-transfer-a-comprehensive-look-f54d8649c199)

#### 11th July, 2018
Working on the Machine Learning Map. Discussions on ML to figure out the next path. Currently, chose to go with NLP.

#### 12th July, 2018
Understanding how to build a text summarizer (https://www.youtube.com/watch?v=ogrJaOIuBx4). Still a long way to go.
Terms to understand:
* Syntatic Parsing
* Pickle & Keras
* Word Vectors: word2vec & GloVe
* Sequence to sequence
* LSTM

#### 13th July, 2018
Conversations on ML regarding text and image processing. Laying out and undeerstanding what had been learnt so for. Understanding Numerical representations of data for Machine learning (word2vec & image matix representation)

#### 16th July, 2018
Concepts to explore:
* AlphaGo
* Deep Q
* Wavenet
* scikit-learn
* Gradient Descent Algorithm
* Neural Networks (Deep Learning)

[Basics of Linear Algebra](https://www.youtube.com/watch?v=kjBOesZCoqc&index=1&list=PLZHQObOWTQDPD3MizzM2xVFitgF8hE_ab)

[Natural Language Processing with Deep Learning](https://www.youtube.com/watch?v=OQQ-W_63UgQ&list=PL3FW7Lu3i5Jsnh1rnUwq_TcylNr7EkRe6)

#### 17th July, 2018
[Build a Chatbot - ML for Hackers #6](https://www.youtube.com/watch?v=5_SAroSvC0E)

* Retrieval Model - Hardcoded responses
* Generative Model - Trained with dataset

##### Neural Conversational Model (Torch & Lua)

1. Load dataset
2. Build Model - Sequence to Sequence Model (2 LSTMs)
3. Training Parameters - 
   * Negative Log Likelihood - to improve sentence predictions
   * Learning Rate & Momentum - help pace timesteps 
   * Decay Factor & Min Mean Error - helps improve learning rate while training
4. Enable CUDA
5. Train the model using backpropagation

##### LSTM - Long Short Term Memory Recurrent Neural Networks

LSTM can take an input sentence of variable length and convert it to a fixed dimensional vector representation called thought vector. The vector generated will help recognize the closeness of similar sentences.

#### 18th July, 2018
Understanding Chatbots with APIs and Tensorflow

* Feed Forward Neural Network
    * Data flows one way 
    * Takes a fixed data size (images or numbers), eg. predict if temperature is hot or cold
* Reccurrent Neural Networks
    * Sequence Learning
    * Feed data back to input while training in a recurring loop
    * useful for conversational training
    
#### 19th July, 2018
##### Selective Model
* Restricted pool of responses
* Customizable (Speak like a certain character)

 [A Neural Conversational Model using RNN](https://github.com/GauravG8/chatbot_tutorial)
 
In LSTM, memory is encoded by hidden states and weights is too small for long sequences (movies and books). The solution was to store multiple LSTM states and use an attention mechanism to choose between them.

##### A better solution: Dynamic Memory Network
* Neural network uses an external data structure as memory storage
* Learns where to retrieve the required memory from the memory bank in a supervised way
* Uses semantic and episodic memory

1. Extract data
2. Split data
3. Vectorise data

#### 21st July, 2018
Getting started with building a Telegram Bot. Discussions regarding ML, NLP and Rasa NLU.

#### 22nd July, 2018
Completed a basic echobot for Telegram. Deployed in Python Anywhere(Requires https).

#### 23rd July, 2018
Updated and deployed reverse echobot flask backend to CodeAnywhere and connected to telegram.

Bot can be accessed at [ReverseBot](https://t.me/NiohBot)

#### 24th July, 2018
AI Writer in Python (Lasagne)
* Load Image
    * Byte representation of image using numpy
    * Resize it so smallest dim = 256, preserve aspect ratio
* Run image through deep **Convolutional neural network (CNN)** to extract features
* Encode the image features into a multi-modal neural language model (based on **Unifying Visual Semantic Embeddings**)
    * Generates description for image using **LSTM RNN**
* Compute nearest neighbours
* Generate Skip Thought Vectors using **Gated Recurrent Units (GRUs) RNN** - Similar sentences
* Shift style of caption to the style of a book (trained using romance novels)
* Generate story based on shift (decoder using **RNN**)

#### 25th July, 2018
Connected Raven DialogFlow to Telegram [@RavenSnowBot](https://t.me/RavenSnowBot). Customized replies.

#### 26th July, 2018
**Bot Architecture** - Connecting different backends to frontends with varied processing pipelines.
* Backend
  * Python
  * Go
  * Node JS
* Processing (Handle Messages)
  * DialogFlow
  * Wit.ai
  * Recast.ai
  * Rasa NLU
  * Custom Model
* Frontend
  * Telegram
  * Command Line
  * Website
  * App
  
