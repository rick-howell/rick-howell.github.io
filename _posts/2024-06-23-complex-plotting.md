---
layout: post
title: Complex Plotting
date: 2024-06-23 23:35 -0400
permalink: /cplxplt/
categories: math
thumbnail: img/clog.webp
---

## The Main Bijection

When looking to plot complex functions, we'll use a fun and simple fact:

$$
\begin{aligned}
\mathbb{R} \times \mathbb{R} &\cong \mathbb{C} \\
(x, y) &\mapsto x+iy
\end{aligned}
$$


The obvious question then, how do we represent functions from 
$$\mathbb{C} \rightarrow \mathbb{C}$$
when we need two parameters to represent the input, and two more for the output?

We just make the inputs the regular complex plane, with the vertical axis corresponding to the imaginary part. Then, using HSL color space, we can make the hue correspond to the angle of the output at each point, and the lightness correspond to the magnitude:

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
    return np.log(z)
    

# Apply our function
fz = f(Z)


# Color the result
# We'll use HLS color space, where the hue is the angle of the complex number, and the saturation is the magnitude

angle = np.angle(fz)
magnitude = np.abs(fz)

# Normalize the angle
angle = 0.5 + angle / (2*np.pi)

# Normalize the magnitude
magnitude = magnitude / np.max(magnitude)

magnitude = 1 - magnitude

plot = np.zeros((RESOLUTION, RESOLUTION, 3), dtype=np.uint8)

plot[..., 0] = (angle * 180)
plot[..., 1] = (magnitude * 255)
plot[..., 2] = 100


# We'll clip the values between 0 and 255
plot = np.clip(plot, 0, 255).astype(np.uint8)


# Convert to BGR for OpenCV display
plot = cv2.cvtColor(plot, cv2.COLOR_HLS2BGR)


# Plot the result
cv2.imshow('f(z)', plot)
cv2.waitKey(0)

```

Doing this gives us the following result for $$f(z) = log(z)$$:
![log](/img/logwithmag.webp)


This is mathematically accurate, and entertaining in it's own right. 

That being said, I find myself much more intrigued by removing the magnitude all together, and just focusing on plotting the angle.


## Plots with only the angle

Technically we lose some information here, but for the sake of beauty, it isn't bad to do so.

Here is a new example script:

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
    # return z**3 - 1
    return np.log(z)
    


# Apply our function
fz = f(Z)


# Color the result

angle = np.angle(fz)


plot = np.zeros((RESOLUTION, RESOLUTION, 3), dtype=np.uint8)
plot[..., 0] = 255 * (1 + np.cos(angle)) / 2
plot[..., 1] = 255 * (1 + np.cos(angle + 2*np.pi/3)) / 2
plot[..., 2] = 255 * (1 + np.cos(angle + 4*np.pi/3)) / 2


# We'll clip the values between 0 and 255
plot = np.clip(plot, 0, 255).astype(np.uint8)


# Convert to BGR for OpenCV display
plot = cv2.cvtColor(plot, cv2.COLOR_RGB2BGR)


# Plot the result
cv2.imshow('f(z)', plot)
cv2.waitKey(0)

```

## Gallery

### $$f(z) = \sum z^4 + z$$
![mandelbrot4](/img/mandle.webp)

### $$f(z) = \log(z)$$
![log(z)](/img/clog.webp)

### $$z^3 - 1 = 0$$
![Third roots of unity](/img/3rootsofunity.webp)

### $$f(z) = \sum z^3 + z$$
![mandelbrot3](/img/mandel3.webp)