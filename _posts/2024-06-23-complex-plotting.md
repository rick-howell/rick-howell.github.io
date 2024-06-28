---
layout: post
title: Complex Plotting
date: 2024-06-23 23:35 -0400
permalink: /cplxplt/
categories: math
thumbnail: img/clog.webp
---

A [complex](https://mathworld.wolfram.com/ComplexNumber.html) function is any function $$f: A \rightarrow \mathbb{C}$$, for some domain $$A$$. There are many [exciting things](https://www.britannica.com/science/fundamental-theorem-of-algebra) to talk about with complex functions, and maybe we'll get to that in the future, but today we're just going to try and figure out how to actually *look* at them. 

## The Main Bijection

When looking to plot complex functions, we'll use a fun and simple fact:

$$
\begin{aligned}
\mathbb{R} \times \mathbb{R} &\cong \mathbb{C} \\
(x, y) &\mapsto x+iy
\end{aligned}
$$


So looking at an arbitrary function, $$f: \mathbb{C} \rightarrow \mathbb{C}$$, we notice each complex coordinate needs two real values to represent it, and so that effectively makes viewing our [graph](https://en.wikipedia.org/wiki/Graph_of_a_function) a 4 dimensional problem... 

\
One way to overcome this is to make the inputs the regular complex plane, with the vertical axis corresponding to the imaginary part.

 Then, using HSL color space, we can make the hue correspond to the angle of the output at each point, and the lightness correspond to the magnitude.

Putting it all together, here's a simple script we can use.

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

\
Doing this gives us the following result for $$f(z) = \log(z)$$
![log](/img/logwithmag.webp)


This is mathematically accurate, and entertaining in it's own right. But that being said, there's nothing to say your representation of the function has to be *correct*, or include all available information. 

\
Before we move on however, let's actually digest this picture.

Note the 'black hole' in the middle. This should be intuitive from the many times we've encountered log defined over $$\mathbb{R}$$, but often our intuition fails to hold when we start climbing into new domains.

We first make note though that $$\forall z \in \mathbb{C}$$, $$\nexists z : \exp(z) = 0$$, and so we'll color the point at $$z=0$$ black.

Then remembering how $$\log(x)$$ from $$\mathbb{R_+} \rightarrow \mathbb{R}$$ is strictly decreasing as we approach zero, we can fix the imaginary component and see we are lessening in magnitude the closer we get towards the center.

\
Now what's with the line through the negative real axis?

We call this a *branch cut*, and to see why it exists, we can look at each $$z \in \mathbb{C}$$ in polar form as $$z = re^{i\theta}$$, and then we get $$\log(z) = \log(r) + i\theta$$.

Remembering that $$\theta = 2\pi n\theta$$, $$\forall n \in \mathbb{Z}$$, we can compute:

$$
\begin{aligned}
\log(-1) = \log(1) + i\pi = i\pi = 3i\pi = 5i\pi = \dots = (2n+1)i\pi \\
\end{aligned}
$$

So let's fix $$r$$, and put $$\theta \in (-\pi, \pi]$$. We see 

$$
\begin{aligned}
\lim_{\theta \rightarrow \pi^-} &= i\pi \\

\lim_{\theta \rightarrow -\pi^+} &= -i\pi \\
\end{aligned}
$$

The difference in color then is the angle difference as we approach $$\pi$$ from either side of the cut!

## Plotting With Style

Let's explore different ways of coloring the domain.

Here is a new example script for the colorful plot shown in the thumbnail:

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