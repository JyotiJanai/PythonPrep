import numpy as np

speed = [99, 86, 87, 88, 111, 86, 103, 87, 94, 78, 77, 85, 86]
x = np.mean(speed)
print(x)

y = np.median(speed)
print(y)

from scipy import stats

x = stats.mode(speed)
print(x)

x = np.std(speed)
print(x)

import numpy as np

speed = [32, 111, 138, 28, 59, 77, 97]
x = np.var(speed)
x1 = np.percentile(speed, 60)
print(x)
print(x1)

# What is the speed that 90% of the speeds are lower than?
x = np.percentile(speed, 80)
print(x)
