---
layout: post
title: Vector Fields
date: 2024-07-21 13:10 -0400
permalink: vf
categories: math cs
thumbnail: img/vf.webp
---

{% include youtubePlayer.html id='5kpwNamdE-I?si=dRErNj1zcpfNL0cP' %}

## A Quick Note

The following animations and scripts are inspired by the [Field Play repository by anvaka](https://github.com/anvaka/fieldplay) which has an [online component you can run in your browser!](https://anvaka.github.io/fieldplay)

I say *inspired* here because that's all I was aiming to do. This is not a recreation of the algorithms, I just used the online program and felt like I could give it a shot.

## What Is A Vector Field?

There's two important [components](https://www.grc.nasa.gov/www/k-12/airplane/vectpart.html) when we talk about a vector field.

Firstly, vectors.

1. Take a [field](https://mathworld.wolfram.com/FieldAxioms.html) $$F$$

2. Take an $$n$$ element list $$v = (v_1, v_2, ..., v_n)$$ with elements in $$F$$

3. Make sure the list $$v$$ [transforms like a vector](https://mathworld.wolfram.com/VectorSpace.html) (this was a joke, but really it just needs to act like elements in the field but with an extra scalar multiplication operation).

4. Congratulations, every $$v$$ you can make is a *vector* in $$F^n$$

So to make a vector field, we can take an arbitrary space (or a set endowed with some relationship between elements) and for each point in that space we assign a vector.

## Let's Make One

For our example, since our computer displays are effectively 2 dimensional, and we are looking to make art / visualize the vector field, let's take the classic vector field $$\mathbb{R}^2$$, over the same space. I.e. [the euclidean plane](https://mathworld.wolfram.com/EuclideanPlane.html).

We then define the vector field to be a function over the space. 
E.g. in our code snippet we use the following map from $$\mathbb{R}^2$$ the space to $$\mathbb{R}^2$$ the vector field:

$$
\begin{equation*}
(x, y) \mapsto

\begin{bmatrix}
    -y \\
    x
\end{bmatrix}
\end{equation*}
$$

Then we can make particles that will be pushed around our field, and we'll be sure to keep track of their positions.

We then update the velocities by adding the force vector.

Note we don't have to stick to 2 dimensions, or the euclidean space for that matter, but visualizations start becoming more difficult.

Here's an example:

```
import numpy as np      # pip install numpy
import cv2              # pip install opencv-python


# Let's make a subset of the euclidean plane
RESOLUTION = 500
X = np.linspace(-1, 1, RESOLUTION)
Y = np.linspace(-1, 1, RESOLUTION)

# Create a meshgrid
X, Y = np.meshgrid(X, Y)

# Define a vector field
def vector_field(V):
    
    # Get the x and y components of the vector field
    x, y = V.T

    # Define the vector field
    vx = -y
    vy = x

    return np.stack([vx, vy], axis=-1)



# Make particles to follow the vector field
N = 255
FORCE = 0.01
RESET_PROB = 0.01

particles = np.random.rand(N, 2)


def randomize_particles(idxs = None):
    if idxs is None:
        idxs = range(N)
    else:
        idxs = np.where(idxs)[0]
    particles[idxs] = np.random.rand(len(idxs), 2)
    particles[idxs, 0] = particles[idxs, 0] * (X.max() - X.min()) + X.min()
    particles[idxs, 1] = particles[idxs, 1] * (Y.max() - Y.min()) + Y.min()


randomize_particles()


# Make a function to update the particles
def update():
    global particles

    # Get the vector field at the current position of the particles
    v = vector_field(particles)

    # Update the particles
    particles += v * FORCE

    # If the particles go out of bounds, reset them
    out_of_bounds = (particles[:, 0] < X.min()) | (particles[:, 0] > X.max()) | (particles[:, 1] < Y.min()) | (particles[:, 1] > Y.max())
    randomize_particles(out_of_bounds)


    # We'll also randomly reset some particles
    reset_particles = np.random.rand(N) < RESET_PROB
    randomize_particles(reset_particles)


DECAY = 0.9

# We'll store the previous image to make the trails
prev_img = np.zeros((RESOLUTION, RESOLUTION, 3), dtype=np.uint8)

def draw():
    global prev_img
    # From the particles, we can get the indices of the pixels
    x = ((particles[:, 0] - X.min()) / (X.max() - X.min()) * RESOLUTION).astype(int)
    y = ((particles[:, 1] - Y.min()) / (Y.max() - Y.min()) * RESOLUTION).astype(int)

    # Create an image
    img = prev_img.copy()
    img = (img * DECAY).astype(np.uint8)

    # Draw the particles
    img[x, y] = 255

    # Update the previous image
    prev_img = img

    return img


# Main Loop
while True:
    # Update the particles
    update()

    img = draw()    

    # Show the image
    cv2.imshow("Particles", img)

    # Check if the user pressed a key
    key = cv2.waitKey(1)
    if key == ord('q') or cv2.getWindowProperty("Particles", cv2.WND_PROP_VISIBLE) < 1:
        break
```

## Gallery

{% include youtubePlayer.html id='VhZ1MtWQnfc' %}

{% include youtubePlayer.html id='Dehj_iG98so' %}

{% include youtubePlayer.html id='ZwE9PnuZ8UA' %}

{% include youtubePlayer.html id='jkplkK84EMc' %}

{% include youtubePlayer.html id='-l76pQOAyhw' %}