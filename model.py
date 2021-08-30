import pickle
import os
import numpy as np
from sklearn.linear_model import LinearRegression

cwd = os.getcwd()


model_dir = cwd + "/linear_regression.pkl"

# [[humidity, time passed since drying started]]
sample_input = np.asarray([[80.0, 0]])

print("AAAAAAAAAAAAAA: {}".format(sample_input.shape))

saved_model = pickle.load(open(model_dir, 'rb'))
results = saved_model.predict(sample_input)
print("model output: {} seconds to dry".format(results[0].round()))