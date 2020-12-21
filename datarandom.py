import pandas as pd
import openpyxl, random

# 유저 프로그램 선택 랜덤 생성
# program_hit = pd.read_excel('data/hilstation_data.xlsx', sheet_name='program_hit', engine='openpyxl')
# program_hit = program_hit[['user_id', 'program_id']]


# rating = []
# for i in range(1, 984):
#     rating.append(random.randint(1,5))
#
# program_hit['rating'] = rating
#
# for i in range(983, 100001):
#     program_hit.loc[i] = {'user_id': random.randint(201, 1000), 'program_id': random.randint(1, 145), 'rating': random.randint(1, 5)}
#     print(program_hit.loc[i])
#
# program_hit.to_csv('data/program_hit.csv', index=False)

# 프로그램 데이터 csv로 저장
# program = pd.read_excel('data/hilstation_data.xlsx', sheet_name='program', engine='openpyxl')
# program.rename(columns = {'id':'program_id', 'name':'program_name'}, inplace=True)
#
#
# program.drop(['Unnamed: 5'], axis=1, inplace=True)
# program[['program_id', 'program_name']].to_csv('data/program.csv')

# program_hit = pd.read_csv('data/program_hit.csv', index=False)
# program_hit.rename(columns = {'rank':'rating'}, inplace=True)
# print(program_hit)


# 정보 랜덤 생성
user = pd.read_excel('data/hilstation_data.xlsx', sheet_name='user', engine='openpyxl')
user.rename(columns = {'id':'user_id', 'name':'user_name'}, inplace=True)
user.drop(['Unnamed: 4', 'Unnamed: 5', 'Unnamed: 6'], axis=1, inplace=True)
user.to_csv('data/user_preprocess.csv')
