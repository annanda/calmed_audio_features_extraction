import os.path

import pandas as pd
import opensmile
from audio_features_extraction.conf import ANNOTATION_FILES_FOLDER, MAIN_FOLDER, RAW_FILES_FOLDER


class AudioFeaturesExtraction:

    def __init__(self, session, parts_of_a_session):
        self.session = session
        self.parts_of_a_session = parts_of_a_session
        self.session_annotation_folder = os.path.join(ANNOTATION_FILES_FOLDER, self.session)
        self.output_folder = os.path.join(MAIN_FOLDER, 'output_opensmile', self.session)
        self.smile = opensmile.Smile(
            feature_set=opensmile.FeatureSet.ComParE_2016,
            feature_level=opensmile.FeatureLevel.Functionals,
        )

    def build_dataset(self):
        """ For each file of a given session, I need to create the audio working dataset of features
        """
        for part in self.parts_of_a_session:
            intervals = self.build_intervals_list(part)
            df_audio_features_per_part = pd.DataFrame(intervals, columns=['frametime'])
            features_dfs = []
            for interval in intervals:
                path_audio = os.path.join(RAW_FILES_FOLDER, self.session, part + '.wav')
                final_interval = interval + 0.2
                features = self.extract_audio_features(path_audio, interval, final_interval)
                features['frametime'] = interval
                features_dfs.append(features)
            # features.to_csv(os.path.join(MAIN_FOLDER, 'output_opensmile', f'result_features_{part}_{interval}.csv'))
            features_from_part = pd.concat(features_dfs)
            merged = df_audio_features_per_part.merge(features_from_part, on='frametime', how='outer')
            merged.to_csv(os.path.join(self.output_folder, f'{part}.csv'))

    def build_intervals_list(self, annotation_file):
        annotation_df = pd.read_csv(os.path.join(self.session_annotation_folder, annotation_file + '.csv'))
        lst_intervals = list(annotation_df['time_of_video_seconds'])
        return lst_intervals

    def extract_audio_features(self, file, start, end):
        print(f'Calling OpenSMILE for {file}. From: {start} - to: {end}')
        print('.')
        print('.')
        print('.')
        time_window_features = self.smile.process_file(file,
                                                       start=start,
                                                       end=end)
        return time_window_features


if __name__ == '__main__':
    parts_session = ['session_03_02_01',
                     'session_03_02_02',
                     'session_03_02_03',
                     'session_03_02_04',
                     'session_03_02_05',
                     'session_03_02_06']
    audio_features = AudioFeaturesExtraction('session_03_02', parts_session)
    audio_features.build_dataset()
    # print('hi')
