---
layout: post
title: Complex Plotting
date: 2024-06-23 23:35 -0400
categories: math
thumbnail: img/complexlog.webp
---

## The Main Bijection

When looking to plot complex functions, we'll use a fun and simple fact:

$$
\begin{aligned}
\mathbb{R} \times \mathbb{R} &\cong \mathbb{C} \\
(x, y) &\mapsto x+iy
\end{aligned}
$$


Here is an example script with OpenCV and NumPy:

```
import numpy as np
import cv2


RESOLUTION = 1000


# Make the grid
grid = np.linspace(-2, 2, RESOLUTION)


# Make a complex grid
X, Y = np.meshgrid(grid, grid)
Z = X + 1j*Y


# Define our function
def f(z):
    #return z**2 + 1
    return np.log(z)


# Apply our function
fz = f(Z)


# Color the result
plot = np.zeros((RESOLUTION, RESOLUTION, 3), dtype=np.uint8)
plot[..., 0] = 255 * (1 + np.cos(np.angle(fz))) / 2
plot[..., 1] = 255 * (1 + np.cos(np.angle(fz) + 2*np.pi/3)) / 2
plot[..., 2] = 255 * (1 + np.cos(np.angle(fz) + 4*np.pi/3)) / 2


plot = cv2.cvtColor(plot, cv2.COLOR_RGB2BGR)


# Plot the result
cv2.imshow('f(z) = z^2 + 1', plot)
cv2.waitKey(0)

```