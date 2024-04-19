import numpy as np


class Matrix:
    def __init__(self):
        num_rows = np.random.randint(2, 7)
        num_cols = np.random.randint(2, 7)
        self.matrix = np.random.rand(num_rows, num_cols)

    def print_matrix(self):
        print("Matrix:")
        print(self.matrix)

    def create_zero_matrix(self, n, m):
        return np.zeros((n, m))

    def create_ones_matrix(self, n, m):
        return np.ones((n, m))

    def create_identity_matrix(self, n):
        return np.eye(n)

    def get_column_with_min_sum(self):
        column_sums = np.sum(self.matrix, axis=0)
        min_sum_column_index = np.argmin(column_sums)
        return self.matrix[:, min_sum_column_index]

    def calculate_median(self, column):
        median_value = np.median(column)
        return median_value

    def calculate_median_manually(self, column):
        sorted_column = np.sort(column)
        n = len(sorted_column)
        if n % 2 == 0:
            median_value = (sorted_column[n // 2 - 1] + sorted_column[n // 2]) / 2
        else:
            median_value = sorted_column[n // 2]
        return median_value
    
    def calculate_mean(self, column):
        mean_value = np.mean(column)
        return mean_value

    def calculate_correlation_coefficients(self):
        corr_matrix = np.corrcoef(self.matrix, rowvar=False)
        return corr_matrix

    def calculate_variance(self, column):
        variance_value = np.var(column)
        return variance_value

    def calculate_std_deviation(self, column):
        std_deviation = np.std(column)
        return std_deviation


def task5_run():
    matrix = Matrix()
    matrix.print_matrix()

    zero_matrix = matrix.create_zero_matrix(3, 3)
    print('Zero matrix:')
    print(zero_matrix)

    ones_matrix = matrix.create_ones_matrix(2, 2)
    print('Ones matrix:')
    print(ones_matrix)
    
    identity_matrix = matrix.create_identity_matrix(4)
    print('Identity matrix:')
    print(identity_matrix)
    
    column = matrix.get_column_with_min_sum()
    print('Columm with min sum:')
    print(column)
    
    median = matrix.calculate_median(column)
    print(f'Column median(standart function): {median}')
    
    median_manual = matrix.calculate_median_manually(column)
    print(f'Column median(formule):{median_manual}')
    
    mean = matrix.calculate_mean(column)
    print("Column mean:", mean)
    
    corr_matrix = matrix.calculate_correlation_coefficients()
    print("Matrix correlation coefficients:") 
    print(corr_matrix)
    
    variance = matrix.calculate_variance(column)
    print(f"Column variance: {variance}")
    
    std_deviation = matrix.calculate_std_deviation(column)
    print("STD Deviation:", std_deviation)