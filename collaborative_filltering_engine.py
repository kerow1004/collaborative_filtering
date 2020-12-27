import numpy as np
import pandas as pd
import tensorflow as tf

from RBM_model import recommender

out_dir='/Users/jinseongkim/PycharmProjects/collaborative_filtering/data/'


def inference(train_file, test_file, user_info_file, program_info_file):
    train_df = pd.read_csv(train_file)
    test_data = np.load(test_file)
    test_df = pd.DataFrame(test_data)
    test_df.columns = ['user_id','program_id','rating']

    if user_info_file != None:
        user_info_df = pd.read_csv(user_info_file)

    if program_info_file != None:
        program_info_df = pd.read_csv(program_info_file)
    df_result = test_df.merge(train_df, on=['user_id', 'program_id'])
    df_result['user_id'] = df_result['user_id'] + 1
    df_result['program_id'] = df_result['program_id'] + 1
    if user_info_file != None:
        df_result = df_result.merge(user_info_df, on=['user_id'])
    if program_info_file != None:
        df_result = df_result.merge(program_info_df, on=['program_id'])
    df_result.to_csv(out_dir + 'test_results.csv', index=False)

    print(f'output written to {out_dir}test_results.csv')
    test_rmse = (np.mean((df_result['rating'].values - df_result['predicted_rating'].values) ** 2)) ** 0.5
    print(f'test RMSE : {test_rmse}')


if __name__ == '__main__':
    # recommender_train = recommender(mode='train', train_file='/Users/jinseongkim/PycharmProjects/collaborative_filtering/data/train_data.npy', outdir='/Users/jinseongkim/PycharmProjects/collaborative_filtering/data/', num_hidden=5, epochs=1000)
    # recommender_train.main_process()

    inference('data/pred_all_recs.csv', 'data/test_data.npy', 'data/user_preprocess.csv', 'data/program.csv')