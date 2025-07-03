# Re-import numpy and re-define necessary variables and functions after execution state reset
import numpy as np

# Support vectors, classes, alphas, and b
support_vectors = np.array([[0.2351, 0.4016], [-0.1764, -0.1916], [0.3057, -0.9394], [0.5590, 0.6353], [-0.6600, -0.1175]])
classes = np.array([1, 1, -1, -1, -1])
alphas = np.array([7.1655, 6.9060, 2.0033, 6.1144, 5.9538])
b = 0.3074

# Transformation function for a polynomial kernel of degree 2
def transform(x):
    return np.array([1, x[0]**2, np.sqrt(2)*x[0]*x[1], x[1]**2, np.sqrt(2)*x[0], np.sqrt(2)*x[1]])

# Transform support vectors
transformed_support_vectors = np.array([transform(sv) for sv in support_vectors])

print(transformed_support_vectors)

# # Query instance
# query_instance = np.array([0.90, 0.90])
# transformed_query = transform(query_instance)

# # Calculate the model's output
# output = sum(alphas[i] * classes[i] * np.dot(transformed_support_vectors[i], transformed_query) for i in range(len(support_vectors))) + b
# predicted_class = np.sign(output)

# output, predicted_class
