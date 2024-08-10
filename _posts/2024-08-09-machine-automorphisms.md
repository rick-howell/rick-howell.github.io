---
layout: post
title: Machine Automorphisms
date: 2024-08-09 10:24 -0400
permalink: machine-automorphisms
categories: music
thumbnail: img/aut(m).webp
---

{% include youtubePlayer.html id='5xoiDZP0ljQ?si=YOSgdFxOXUZ86GK0' %}

\
Machine Automorphisms is a new journal entry into my life. [You can listen to it through bandcamp here](https://rickhowell.bandcamp.com/album/machine-automorphisms), or on all of your other favorite music streaming platforms.

The tracks took a lot of direction from idm, techno, and video game artists, but also from the synthesizers themselves. The process of patching my synthesizers together gives them their own language of sorts while acting as a peripheral of my brain in the same sense an arm or a leg does. It's as if I was thinking in English while writing in Latin with hardly an understanding of the latter. 

# The Title And Cover

The string 'Machine Automorphisms' is in reference to [the algebraic structure](https://en.wikipedia.org//wiki/Automorphism). I like to think of patching like 'the machine acting on itself', so the title is in reference to that.

A lot of my recent personal explorations happen on a torus, so I knew I had to include it as a big part of this (if we're thinking of the album as a snapshot into my life). The script I used to generate it was pretty simple, utilizing the [parameterized equations](https://en.wikipedia.org/wiki/Torus#Geometry):

```
import numpy as np
import cv2

# This file generates an image of a discrete torus.
SCREEN_SIZE = 4000

n = 16

theta = np.linspace(0, 2.*np.pi, n)
phi = np.linspace(0, 2.*np.pi, n)
theta, phi = np.meshgrid(theta, phi)
c, a = 2, 0.8
x = (c + a*np.cos(theta)) * np.cos(phi)
y = (c + a*np.cos(theta)) * np.sin(phi)
z = a * np.sin(theta)

x = SCREEN_SIZE/2 + x * SCREEN_SIZE/8
y = SCREEN_SIZE/2 + y * SCREEN_SIZE/8

# We'll perform a perspective projection
f = 8
x = f * x / (z + f)
y = f * y / (z + f)


img = np.zeros((SCREEN_SIZE, SCREEN_SIZE, 3), dtype=np.uint8)
for i in range(n):
    for j in range(n):
        radius = z[i, j]
        radius = (radius + 2) * 20
        cv2.circle(img, (int(x[i, j]), int(y[i, j])), int(radius), (255, 255, 255), int(z[i, j] + 1 + radius // 2))

cv2.imshow('Torus', img)
cv2.waitKey(0)
```

We then did some simple image processing in [GIMP](https://www.gimp.org/) to get the final cover!

![Machine Automorphisms webp](/img/aut(m).webp)


# Individual Tracks

__Q8__ is a reference to the [Quaternion Group](https://en.wikipedia.org/wiki/Quaternion_group) because it has a very special property: the [commuting probability](https://en.wikipedia.org/wiki/Commuting_probability) of Q8 is 5/8. Since the song is in 5 / 8 time, and algebra is an important subject to me, I felt it to be a fitting name.

__Immutable__ was named as such because most of the sounds were generated using [Mutable Instruments](https://pichenettes.github.io/mutable-instruments-documentation/) modules- and this is a take on that. Coincidentally it's also a [big topic in cs](https://en.wikipedia.org/wiki/Immutable_object) so it's like a double entendre. 

__Blame Steiner-Parker__ is obviously a callback to the [synthacon](https://en.wikipedia.org/wiki/Steiner-Parker_Synthacon). The 'drums' in this track utilized the Steiner-Parker filter on the [Minibrute 2S](https://www.arturia.com/products/hardware-synths/minibrute-2s/overview). 

__Rings, Clouds, and Nomads__ is a take on the [eurorack classic](https://www.perfectcircuit.com/signal/rings-into-clouds), but with the inspiration of [Outer Wilds](https://www.mobiusdigitalgames.com/outer-wilds.html). 

__CR Noise__ stands for 'Curits Roads'. [His influence](https://mitpress.mit.edu/9780262681544/microsound/) helped shape granular synthesis to be what it is today. I used the [Nebulae V2](https://www.qubitelectronix.com/shop/p/nebulae) for all of the noise and textures in this track, so the name 'CR Noise' is pretty literal.


# Tools and Synths

![The Machine](/img/synthjpg.jpg)

Pretty much every [pad](https://music.stackexchange.com/questions/44060/what-is-the-definition-of-a-pad) or texture was made with the [Nebulae](https://www.qubitelectronix.com/shop/p/nebulae). I rarely use it for anything else, but it is really quite good at that one thing. Pairing this with [Rings](https://pichenettes.github.io/mutable-instruments-documentation/modules/rings/) is usually my go-to, either by recording Rings in the Nebulae's buffer and playing it back, or by using the Nebulae to generate impulses that I then feed into Rings. 

The amount of work that the [Meng Qi Low Pass Gate](https://www.mengqimusic.com/shop-base/dplpg) put into this album is insane.  Every pluck you hear in the album was made using this. I haven't had an analog low pass gate before this album and damn- what a game changer. Pretty much every main sound source used this as the *VCA*, unless I specifically needed snappy / brighter sounds.

The [Vintage Phaser](https://www.image-line.com/fl-studio/plugins/vintage-phaser-) from FL Studio sounds amazing and made its way into a few effect chains.

The main Reverb / Delay / Chorus / Other Delay Effects were made using [Valhalla Supermassive](https://valhalladsp.com/shop/reverb/valhalla-supermassive/). This thing being free is ridiculous. If they turned this into a Eurorack Module, I would sell my FL Studio license and do *everything* dawless.