import opensmile
import os.path
from audio_features_extraction.conf import RAW_FILES_FOLDER, MAIN_FOLDER

smile = opensmile.Smile(
    feature_set=opensmile.FeatureSet.ComParE_2016,
    feature_level=opensmile.FeatureLevel.Functionals,
)
y = smile.process_file(os.path.join(RAW_FILES_FOLDER, 'session_01_01', 'session_01_01_01.wav'))
y.to_csv(os.path.join(MAIN_FOLDER, 'output_opensmile', 'testing_session_01_01_01.csv'), index=False)
print('hello')


