import numpy as np
import pandas as pd
import argparse

def process_file(infile_path):
    infile = pd.read_csv(infile_path)
    # print(infile.head())
    # infile.columns = ['user_id','program_id','rating']
    print(infile)
    users = list(np.unique(infile.user_id.values))
    programs = list(np.unique(infile.program_id.values))

    test_data = []
    ratings_matrix = np.zeros([len(users)+1,len(programs),5])
    # print(len(users),len(programs))
    count = 0
    total_count = len(infile)
    for i in range(len(infile)):
        rec = infile[i:i+1]
        user_index = int(rec['user_id']-1)
        program_index = int(rec['program_id']-1)
        rating_index = int(rec['rating']-1)
        # print(user_index)
        # print(program_index)
        # print(rating_index)
        a = np.random.uniform(0,1)
        if a < 0.2 :
            # print(a)
            test_data.append([user_index,program_index,int(rec['rating'])])
        else:
            # print([user_index, program_index, rating_index])
            # print(ratings_matrix[user_index, program_index, rating_index])
            ratings_matrix[user_index,program_index,rating_index] = 1

        count +=1
        if (count % 100000 == 0) & (count>= 100000):
            print('Processed ' + str(count) + ' records out of ' + str(total_count))

    np.save('data/train_data',ratings_matrix)
    np.save('data/test_data',np.array(test_data))


if __name__ == '__main__':

    process_file('data/program_hit.csv')