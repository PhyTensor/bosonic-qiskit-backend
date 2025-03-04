from typing import Any

from numpy import conjugate, ndarray, sqrt
from scipy.sparse import (coo_array, coo_matrix, csc_array, dia_array,
                          dia_matrix, eye, linalg, spdiags)

# class QOperators:
#     """Base class for bosonic quantum operators"""
#     def __init__(self, cutoff: int) -> None:
#         self.cutoff: int = cutoff # serves as Hilbert space dimension
#         # set the default operator that will be overwritten by subclasses
#         self.operator: csc_array | csc_matrix | coo_array | coo_matrix | dia_array | dia_matrix = eye(m=self.cutoff, n=self.cutoff, dtype=complex)
#
#
#     def as_matrix(self) -> ndarray:
#         """Return the operator as a matrix."""
#         return self.operator.toarray()
#
#
# class IdentityOperator(QOperators):
#     """Identity operator."""
#     def __init__(self, cutoff: int) -> None:
#         super().__init__(cutoff)
#         # A Sparse matrix with 1 on the main diagonal and 0 elsewhere
#         self.operator: csc_array | csc_matrix | coo_array | coo_matrix | dia_array | dia_matrix = eye(m=cutoff, n=cutoff)
#


class ContinuousVariableOperators:
    """Build operator matrices for continuously variable bosonic gates"""

    def identity(self, cutoff: int) -> coo_array | coo_matrix | dia_array | dia_matrix | Any:
        """Identity operator."""
        # A Sparse matrix with 1 on the main diagonal and 0 elsewhere
        return eye(m=cutoff, n=cutoff)

    def annihilation(self, cutoff: int) -> csc_array:
        """Annihilation operator."""
        a: range = range(cutoff)
        # create a numpy array [0, 1, sqrt{2}, sqrt{3}, sqrt{4}, ..., sqrt{cutoff - 1}]
        data: ndarray = sqrt(a)
        # specify diagonals
        A: dia_matrix = spdiags(data=data, diags=[1], m=len(data), n=len(data))
        # convert diagonal matrix to Compressed Sparse Column (CSC) format
        return A.tocsc()


    def creation(self, cutoff: int) -> csc_array:
        """Creation operator \hat{a}^\dagger."""
        a: csc_array = self.annihilation(cutoff)
        return a.conjugate().transpose().tocsc()

    def number(self, cutoff: int) -> csc_array | Any:
        """Number operator \hat{n} = a^\dagger a."""
        a: csc_array = self.annihilation(cutoff)
        a_dag: csc_array = self.creation(cutoff)
        return a_dag.dot(a)


    def rotation(self, theta: float, cutoff: int) -> csc_array:
        """
        Phase space rotation operator.

        Parameters:
            theta (float): The rotation angle.
            cutoff (int): The cutoff of the bosonic mode.

        Returns:
            ndarray: The rotation operator matrix.
        """
        arg: csc_array = 1j * theta * self.number(cutoff)
        return linalg.expm(arg)

    def displacement(self, alpha: float, cutoff: int) -> csc_array:
        """
        Displacement operator

        Parameters:
            alpha (float): The displacement parameter.
            cutoff (int): The cutoff of the bosonic mode.

        Returns:
            csc_matrix: The displacement operator matrix.
        """
        a: csc_array = alpha * self.creation(cutoff)
        a_dagger: csc_array = conjugate(alpha) * self.annihilation(cutoff)
        arg: csc_array = a - a_dagger
        return linalg.expm(arg)

    def squeezing_single(self, theta: float, cutoff: int) -> None:
        """Single-mode Squeezing operator"""
        pass


    def squeezing_double(self, theta: float) -> None:
        """Two-mode squeezing operator"""
        pass


    def squeezing_triple(self, theta: float) -> None:
        """Three-mode squeezing operator"""
        pass


