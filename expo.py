import numpy as np

def get_exponential_distributed_number(l):
    return -np.log(np.random.uniform()) / l
 # x = np.random.uniform(low=0, high=1)
 # return transform_uniform_to_exponential_distribution(x, l)


# f(p) definieren uniform -> exponential distribution
def transform_uniform_to_exponential_distribution(p, l):
    return -(1. / l) * np.log(p)