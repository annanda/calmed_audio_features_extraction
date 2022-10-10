from audio_features_extraction.conf import RAW_FILES_FOLDER, MAIN_FOLDER, SESSION_PARTS

# smile = opensmile.Smile(
#     feature_set=opensmile.FeatureSet.eGeMAPSv02,
#     feature_level=opensmile.FeatureLevel.Functionals,
# )
# y = smile.process_file(os.path.join(RAW_FILES_FOLDER, 'session_01_01', 'session_01_01_01.wav'),
#                        start=0,
#                        end=0.4)
# y.to_csv(os.path.join(MAIN_FOLDER, 'output_opensmile', 'testing_session_01_01_01_beginning.csv'), index=False)
# print('hello')

for session in SESSION_PARTS.keys():
    # audio_features = AudioFeaturesExtraction(session, SESSION_PARTS[session])
    # audio_features.build_dataset()
    print(session)
    print(SESSION_PARTS[session])