import numpy as np 
import pandas as pd
np.random.seed(1)

dice = pd.DataFrame([1, 2, 3, 4, 5, 6])
sum_of_dice = dice.sample(3, replace=True).sum().loc[0]
print("Sum of three dice is : ", sum_of_dice)

# 50 trials then print the first 10 observations
trial = 50
result = [dice.sample(3, replace=True).sum().loc[0] for i in range (trial)]
print("The first 10 observations are : \n", result[:10])
