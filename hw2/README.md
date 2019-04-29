# Train NN model to learn addition and subtraction
There are three notebooks here in homework 2.
Pleas read in the following order:
1. Addition
2. Subtraction
3. Mix\_add\_sub

The main comparing results about **different number of digits** and **training epochs** are in "Addition" notebook.<br>
And the **"Subtraction"** is compared to the **"Addition"**.<br>
The **"Mix\_add\_sub"** is compared to the **above two**.

## About multiplication:

#### Multiplication operation is hard to train
I tried to let my model learn multiplication, here is my result:<br>
![Multiplication](https://github.com/shihyuuuuuuu/DSAI/blob/master/hw2/output/mul.png)<br>
We can see that the multiplication operation is hard to learn by my model.<br>
The accuracy on testing data incresed very slow.<br>
**Even if I trained up to 340 epochs, the accuracy only reached 0.256.**
