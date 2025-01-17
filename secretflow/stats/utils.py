# Copyright 2022 Ant Group Co., Ltd.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


import numpy as np
import jax.numpy as jnp


def newton_matrix_inverse(x: np.ndarray, iter_round: int = 20):
    """
    computing the inverse of a matrix by newton iteration.
    https://aalexan3.math.ncsu.edu/articles/mat-inv-rep.pdf
    """
    assert x.shape[0] == x.shape[1], "x need be a (n x n) matrix"
    E = jnp.identity(x.shape[0])
    a = (1 / jnp.trace(x)) * E
    for _ in range(iter_round):
        a = jnp.matmul(a, (2 * E - jnp.matmul(x, a)))
    return a
