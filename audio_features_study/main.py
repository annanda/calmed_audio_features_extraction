import pandas as pd
import os.path
from audio_features_extraction.conf import MAIN_FOLDER

audio_df_all = pd.read_csv(os.path.join(MAIN_FOLDER, 'output_opensmile', 'testing_session_01_01_01.csv'))
audio_df = pd.read_csv(os.path.join(MAIN_FOLDER, 'output_opensmile', 'testing_session_01_01_01_beginning.csv'))
print('hi')
