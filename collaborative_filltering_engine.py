import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
import ast
from scipy import stats
from ast import literal_eval
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn.metrics.pairwise import linear_kernel, cosine_similarity

user = pd.read_csv('data/user_preprocess.csv')
program = pd.read_csv('data/program_preprocess.csv')
program_hits = pd.read_csv('data/program_hits_preprocess.csv')