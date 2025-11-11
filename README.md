## SpeechPerfect: Collaboration of Multiple Modules for Perfect Speech Synthesis
This project is an end-to-end speech reconstruction solution and aims to generate exactly the same speech as the given speech using features extracted from the input speech. The model is based on Microsoft's [FastSpeech 2: Fast and High-Quality End-to-End Text to Speech](https://arxiv.org/abs/2006.04558) and a multi-speaker [FastSpeech 2 model](https://github.com/ga642381/FastSpeech2), and an additional speaker characteristic extracting module is added to capture speaker-specific features.

## Dataset
Our model is trained on [VCTK](https://www.kaggle.com/datasets/pratt3000/vctk-corpus)

## Code Organization
folders:
- __audio__: contains utilities used in processing audios and extracting audio features such as f1 (will be used in predictor and variance adaptor).
- __config__: contains 2 config files, one for dataset and one for model hyperparameters.
- __data__: contains functions used in data preprocessing and dataset construction
- __records__: contains training logs
- __model__: contains the core fastspeech2 model and the training function
- __output__: contains synthesized output audio
- __scripts__: contains functions planned to be used in preprocessing data from each dataset (only VCTK is used finally)
- __text__: contains functions used in processing texts (VCTK's audio transcripts)
- __transformer__: contains transformer architecture that is used in the model
- __tmp__: contains checkpoints of models that are used in extracting speaker embedding
- __utils__: contains other unimportant functions that are used in preprocessing data and saving outputs

files:  
`preprocess.py`: performs data preprocessing  
`preprocess_speechembedding.py`: performs speech-specific characteristics (speaker embedding) extraction and preprocessing (Note that the output path is hardcoded and please remember to change it before running on your machine)  
`synthesize.py`: synthesize speech using a trained model  
`train.py`: model training  

## Setting config params
Configurations are set in __config__ folder, there are 2 files:
- dataset.yaml: configurations related to the dataset.
- hparams.py: configurations related to the model and training process.

Please remember to modify the dataset and mfa_path in `hparams.py` before running.

## Steps to Run on your machine
1. Download MFA and dataset
2. Perform data preprocessing
3. Start model training
4. Synthesize new audio!

## Step 1: Download MFA and dataset
MFA: Montreal-Forced-Aligner v1.0.1 is used, it can be accessed [here](https://github.com/MontrealCorpusTools/Montreal-Forced-Aligner/releases/tag/v1.0.1). A pre-trained acoustics model for English is also required and can be downloaded [here](https://github.com/MontrealCorpusTools/mfa-models/tree/main/acoustic)
Dataset: [VCTK](https://www.kaggle.com/datasets/pratt3000/vctk-corpus) is used

## Step 2: Perform data preprocessing
``` shell
python preprocess.py [WAV DIRECTORY] [TRANSCRIPT DIRECTORY] [OUTPUT DIRECTORY] --prepare_mfa --mfa --create_dataset
```
--prepare_mfa: to create mfa data
--mfa: to create textgrid files
--create_dataset: to perform dataset creation

## Step 3: Model training
By now, data preprocessing is finished and you should have a folder containing preprocessed data by `preprocess.py`.
``` shell
python train.py [PREPROCESSED DATA DIR]
```
Training logs will be saved in the __records__ folder

## Step 4: Synthesize new audio
``` shell
python synthesize.py --ckpt_path [MODEL CHECKPOINT PATH] --output_dir [OUTPUT DIR]
```
Synthesization is text-based and the content of the synthesized texts can be set inside `synthesize.py`


## Contributions
* This work is collaborated work with Jeihee Cho, Tong Jiao, Moukhik Misra, and Aarya Makwana
