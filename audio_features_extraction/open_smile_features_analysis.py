import os.path

import pandas as pd
from audio_features_extraction.conf import OUTPUT_OPENSMILE_FOLDER

# df_audio = pd.read_csv(os.path.join(OUTPUT_OPENSMILE_FOLDER, 'session_03_01', 'session_03_01_01_ComParE_2016_LowLevelDescriptors.csv'))
df_audio = pd.read_csv('/Users/annanda/PycharmProjects/audio_features_extraction/session_01_01_01.csv')
columns_names = df_audio.columns.values.tolist()

with open(os.path.join(OUTPUT_OPENSMILE_FOLDER, 'openface_columns.txt'), 'w') as file:
    for name in columns_names[2:]:
        file.write(f'{name}\n')
print('Hi!')

