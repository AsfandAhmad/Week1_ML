import numpy as np

x = np.array([[1, 2],
               [3, 4],
               [5, 6]])

w = np.array([0.5, 1.5])

y = np.array([2, 3, 4])

elementWise = (x*w)

prediction = x @ w
prediction2 = np.dot(x, w)

print("Element-wise:\n", elementWise)
print("Dot product predictions by using @ :\n", prediction)
print("Dot product predictions by using function :\n", prediction2)

xT = x.T
xTx = xT @ x

xTx_inv = np.linalg.inv(xTx)
xTy = xT @ y
w = xTx_inv @ xTy

print("Weights using normal equation:", w)

cov_matrix = np.cov(x.T)
diagonal = np.diag(cov_matrix)
diagonal_sum = np.sum(diagonal)

print("Covariance Matrix:\n", cov_matrix)
print("Diagonal Elements (Variances):", diagonal)
print("Sum of Diagonal Elements:", diagonal_sum)

A = np.array([[2, 1],
              [1, 3]])

b = np.array([3, 4])

x = np.linalg.solve(A, b)
print("Solution [x, y]:", x)

np.random.seed(42)
random_values = np.random.rand(5)
print("Random values with seed 42:", random_values)

x_Rand = np.random.random((3, 2))
print("Random decimal features:\n", x_Rand)

x_int = np.random.randint(1, 10, (3, 2)) 

data = np.array([10, 20, 30, 40, 50])
selected = np.random.choice(data, size=3, replace=False)

print("Randomly selected values (no repeat):", selected)

weights = np.array([0.5, 1.2, -0.8])
np.save("model_weights.npy", weights)
loaded_weights = np.load("model_weights.npy")
print("Loaded Weights:", loaded_weights)

x_rand2 = np.random.rand(5, 2)
y = np.array([10, 20, 30, 40, 50])

np.savetxt("features.txt", x_rand2)
np.savetxt("labels.txt", y)

x_loaded = np.loadtxt("features.txt")
y_loaded = np.loadtxt("labels.txt")

print("Loaded Features:\n", x_loaded)
print("Loaded Labels:", y_loaded)

np.savez("full_data.npz", features=x_Rand, labels=y, weights=weights)
data = np.load("full_data.npz")


print("Features from .npz:\n", data["features"])
print("Labels from .npz:\n", data["labels"])
print("Weights from .npz:\n", data["weights"])

data = np.array([[60, 70],
                 [80, 90],
                 [75, 85],
                 [50, 65],
                 [90, 95]])

mean = np.mean(data, axis=0)
std = np.std(data, axis=0)
normalized = (data - mean) / std

print("Mean:", mean)
print("Std Deviation:", std)
print("Normalized Data:\n", normalized)

features = np.arange(10).reshape(10, 1)
labels = np.arange(10) * 2

indices = np.arange(len(features))
np.random.shuffle(indices)

split = int(0.8 * len(indices))
train_idx, test_idx = indices[:split], indices[split:]

x_train, x_test = features[train_idx], features[test_idx]
y_train, y_test = labels[train_idx], labels[test_idx]


print("Train Features:\n", x_train)
print("Test Features:\n", x_test)

bonus_data = np.array([[1, 2], [3, 4]])


choice = input("Choose format to save: 1 for .npy, 2 for .txt, 3 for .npz: ")

if choice == '1':
    np.save("mydata.npy", data)
    print("Data saved as mydata.npy")

elif choice == '2':
    np.savetxt("mydata.txt", data)
    print("Data saved as mydata.txt")

elif choice == '3':
    np.savez("mydata.npz", array=data)
    print("Data saved as mydata.npz")

else:
    print("Invalid choice.")