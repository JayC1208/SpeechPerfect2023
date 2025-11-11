import json
import os
from speechbrain.pretrained import EncoderClassifier
import torch
import numpy as np

import librosa


out_dir = "/home/jei/CMU/proj_idl/FastSpeech2-main/processed/VCTK/"

with open("/home/jei/CMU/proj_idl/FastSpeech2-main/processed/VCTK/metadata.json", "r", encoding="utf-8") as f:
    metadata = json.load(f)


train_meta = metadata["train"]
# print(train_meta)

# spk_model_name = "speechbrain/spkrec-xvect-voxceleb"
# speaker_model = EncoderClassifier.from_hparams(
#     source=spk_model_name,
#     run_opts={"device": "cuda"},
#     savedir=os.path.join("./tmp", spk_model_name),
# )
# speaker_model.eval()

# speaker_model = torch.hub.load('RF5/simple-speaker-embedding', 'gru_embedder')

# split = ["train","valid"]

# speaker_embedding_path = "/home/jei/CMU/proj_idl/FastSpeech2-main/processed/VCTK/speech/"
# new_meta = {"spker_table":metadata["spker_table"]}
# for split_path in split:
#     this_meta = metadata[split_path]
#     this_split = []
#     for idx in range(len(this_meta)):
#         audio_path = this_meta[idx]['wav']['path']  
#         split = audio_path.split("/")
#         folder_name = split[-2]
#         file_name = split[-1][:-4]
#         val, sr = librosa.load(audio_path)
#         val = torch.from_numpy(val)
#         file_path = speaker_embedding_path+folder_name
#         try:
#             os.mkdir(file_path)
#         except:
#             # print(file_path)
#             pass
        
#         speaker_embedding = speaker_model.encode_batch(val)
#         speaker_embedding = torch.nn.functional.normalize(speaker_embedding,dim=2)
#         speaker_embeddings = speaker_embedding.squeeze().cpu().numpy()

#         with open(file_path+"/"+file_name+".npy", "wb") as f:
#             np.save(f, speaker_embeddings)

#         temp = this_meta[idx]
#         temp["embed"] = {"path":file_path+"/"+file_name+".npy"}
#         this_split.append(temp)
#     new_meta[split_path] = this_split



# ### Save data ###
# with open(out_dir / "metadata_added.json", "w", encoding="utf-8") as f:
#     data = new_meta
#     json.dump(data, f, indent=4)


speaker_model = torch.hub.load('RF5/simple-speaker-embedding', 'convgru_embedder')
speaker_model.eval()
split = ["train","valid"]

speaker_embedding_path = "/home/jei/CMU/proj_idl/FastSpeech2-main/processed/VCTK/speech/"
new_meta = {"spker_table":metadata["spker_table"]}
for split_path in split:
    this_meta = metadata[split_path]
    this_split = []
    for idx in range(len(this_meta)):
        audio_path = this_meta[idx]['wav']['path']  
        split = audio_path.split("/")
        folder_name = split[-2]
        file_name = split[-1][:-4]
        val, sr = librosa.load(audio_path,sr=16000)
        val = torch.from_numpy(val)
        file_path = speaker_embedding_path+folder_name
        try:
            os.mkdir(file_path)
        except:
            # print(file_path)
            pass
        speaker_embedding = speaker_model(val[None])

        with open(file_path+"/"+file_name+".npy", "wb") as f:
            np.save(f, speaker_embedding.cpu().detach().numpy())

        temp = this_meta[idx]
        temp["embed"] = {"path":file_path+"/"+file_name+".npy"}
        this_split.append(temp)
    new_meta[split_path] = this_split

### Save data ###
with open(out_dir+"/metadata_added.json", "w", encoding="utf-8") as f:
    data = new_meta
    json.dump(data, f, indent=4)