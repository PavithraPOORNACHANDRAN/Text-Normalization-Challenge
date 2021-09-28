# Text-Normalization-Challenge---English-Language

It is Kaggle competition challenge to automate the process of developing text normalization grammars via machine learning focusing on English language. 
 It is funded by Google’s Text Normalization Research Group, which conducts research and develops tools for the identification, normalization and denormalization of non-standard terms, such as abbreviations, numbers or currency expressions, measuring phrases, addresses or dates, representing unique entities that are semantically limited.
 
 However, one of the biggest challenges when developing a TTS or ASR system for a new language is to develop and test the grammar for all these rules. This project presents a challenge to the community given a large corpus of written text aligned to its normalized spoken form. We have applied three different algorithms with different approaches to predict normalized text, such as XGBoost, Sequence-to-Sequence, Long Term Short Memory (LSTM). Our approach takes very long time to train and to evaluate the model. We present different model experiments and results with various parameter settings.
 
# Description of the data
Our training dataset contains a total of 9 million observations and our testing dataset contains 10 million observations. You can download the dataset from the following link:
https://www.kaggle.com/c/text-normalization-challenge-english-language

# Model 
Our approach involves modelling the problem as classification. We have used 3 distinct models for our project with different activation functions and optimization techniques.
- XGBoost
- Sequence-to-Sequence model
- LSTM

