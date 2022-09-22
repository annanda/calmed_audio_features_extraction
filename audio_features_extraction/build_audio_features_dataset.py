import os.path

import pandas as pd
import opensmile
from audio_features_extraction.conf import ANNOTATION_FILES_FOLDER


class AudioFeaturesExtraction:

    def __init__(self, session):
        self.session = session
        self.parts_of_a_session = ['session_01_01_01']
        self.session_annotation_folder = os.path.join(ANNOTATION_FILES_FOLDER, self.session)
        self.smile = opensmile.Smile(
            feature_set=opensmile.FeatureSet.eGeMAPSv02,
            feature_level=opensmile.FeatureLevel.Functionals,
        )

    def build_dataset(self):
        """ For each file of a given session, I need to create the audio working dataset of features
        """
        for part in self.parts_of_a_session:
            df_audio_features_per_part = None  # Create a dataframe and make intervals list a column with the values there to populate later with the features
            intervals = self.build_intervals_list(part)
            for interval in intervals:
                features = self.extract_audio_features(part + '.wav', interval, interval + 0.2)

    def build_intervals_list(self, annotation_file):
        annotation_df = pd.read_csv(os.path.join(self.session_annotation_folder, annotation_file + '.csv'))
        lst_intervals = list(annotation_df['time_of_video_seconds'])
        return lst_intervals

    def extract_audio_features(self, file, start, end):
        time_window_features = self.smile.process_file(file,
                                                       start=start,
                                                       end=end)
        return time_window_features


if __name__ == '__main__':
    audio_features = AudioFeaturesExtraction(session='session_01_01')
    audio_features.build_dataset()
    print('hi')
