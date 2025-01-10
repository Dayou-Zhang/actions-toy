import numpy as np
import toy.dot_product.calc_dot as d
#  import toy.dot_product.ddot as d


def dot(vec1, vec2):
    v1 = np.asarray(vec1, dtype=np.float64)
    v2 = np.asarray(vec2, dtype=np.float64)
    n = len(v1)
    if n != len(v2):
        raise ValueError("Vectors must be of the same length")
    return d.calc_dot(v1, v2)
