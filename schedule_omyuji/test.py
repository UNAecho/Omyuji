import numpy as np
import time
from tasks.tools import bufferTools
# (train_data, train_labels), (test_data, test_labels) = imdb.load_data(num_words=10000)
train_data = [[1, 2, 2, 4, 5],[6, 7, 8, 9, 10]]
a = np.zeros((2, 3))
#
# def vectorize_sequences(sequences, dimension=11):
#     # Create an all-zero matrix of shape (len(sequences), dimension)
#     results = np.zeros((len(sequences), dimension))
#     for i, sequence in enumerate(sequences):
#         results[i, sequence] = 1.  # set specific indices of results[i] to 1s
#         print(sequence)
#         # print(results[i, sequence])
#     return results
#
# # Our vectorized training data
# x_train = vectorize_sequences(train_data)
# print(x_train)
# #
# # # Our vectorized test data
# # x_test = vectorize_sequences(test_data)

