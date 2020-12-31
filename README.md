# Quilter
## The composer of Matplotlib plots. Python implementation of the R package patchwork. 

This package overloads/creates operators for the matplotlib Figure class so that you can add and divide figures together into a new figure with subplots. 

Adding two figures together creates a new figure with the original figures side-by-side as subplots. Dividing will stack the figured on top of each other. 

Currently the package converts the input figures to images before reloading the images into the axes objects of the output figure. If anyone has a better way to copy actual axes objects to a new figure I'd loved help.

Here are some examples:

```
import matplotlib.pyplot as plt
import quilter # best to put this after your matplotlib import

fig1, ax1 = plt.subplots(figsize=(5,3))
ax1.plot([1, 2], label='my leg')
ax1.set_title("test")
ax1.legend()

fig2, ax2 = plt.subplots(figsize=(5,3))
ax2.plot([2, 2])
ax2.set_title("test 2")
```

Adding figures together
```
out = fig1 + fig2
```

Dividing figures
```
out = fig1 / fig2
```

More complex examples
```
out = (fig1 + fig2) / fig2

out = (fig1 + fig2) / (fig1 + fig2)
```
