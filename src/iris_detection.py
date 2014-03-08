#!/usr/bin/env python2.7

# Imported from https://gitorious.org/hough-circular-transform
# License: GPLv3
# Date: Fri, Mar 7 2014

import matplotlib.pyplot as plt
import matplotlib.patches as plt_patches
import houghcirculartransform as hct
import numpy as np

def detect_iris(filename):
    """
   Example function call:
       For a trickier example, load 'test2.png'!
       (Can't fint the circle? Try the debug mode!)
       ((Pro tip: try lowering the threshold...))
    """
    CH = hct.CircularHough()

    raw_image = plt.imread(filename)
    raw_image = raw_image[:,:,0] # get the first channel
    print "[DEBUG] Image shape is: " + str(raw_image.shape)

    accumulator, radii = CH(raw_image, radii=np.arange(70, 95, 3), threshold=0.01, binary=True, method='fft')

    """
    maxima = []
    max_positions = []
    for i, r in enumerate(radii):
        max_positions.append(np.unravel_index(accumulator[i].argmax(), accumulator[i].shape))
        maxima.append(accumulator[i].max())
        print "Maximum signal for radius %d: %d %s" % (r, maxima[i], max_positions[i])

    # Identify maximum:
    max_index = np.unravel_index(accumulator.argmax(), accumulator.shape)

    print "Maximum correlation found for radius %d at position (%d, %d)." % \
          (radii[max_index[0]], max_index[2], max_index[1])

    # Make a fancy figure:
    fig = plt.figure(1)
    fig.clf()
    subplots = []
    for n in xrange(8):
        subplots.append(fig.add_subplot(3, 3, n+1))
        plt.imshow(accumulator[n, :, :])
        plt.title('Radius: %d, Signal: %s' % (radii[n], accumulator[n].max()))

    # Add original to figure:
    subplots.append(fig.add_subplot(339))
    """
    
    print "[DEBUG] Calling imshow"
    plt.imshow(raw_image)

    plt.title('Raw image (inverted)')

    # Add appropriate circular patch to figure (thanks to MZ!):
    for i, r in enumerate(radii):
        # [Vitor] where i is the accumulator index and r is the radius
        # accumulator a list of points
        point = np.unravel_index(accumulator[i].argmax(), accumulator[i].shape)
        try:
            blob_circ = plt_patches.Circle((point[1], point[0]), r, fill=False, ec='red')
            plt.gca().add_patch(blob_circ)
        except ValueError:
            print point, r
            continue
    # Fix axis distortion:
    plt.axis('image')

    plt.show()

if __name__ == '__main__':
    detect_iris("../working-db/003L_3.png")
    
