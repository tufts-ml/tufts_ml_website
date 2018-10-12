import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

import sklearn.datasets

if __name__ == '__main__':
    ax = plt.gca()

    im_arr = mpimg.imread('tufts-elephant-logo.png')

    H, W, n_colors = im_arr.shape

    # blobs with varied variances
    x_ND, y_N = sklearn.datasets.make_moons(
        n_samples=2000, noise=.08, random_state=42)
    x_ND = np.dot(x_ND, np.diag([-2, 2]))
    theta = np.radians(10)
    c, s = np.cos(theta), np.sin(theta)
    rot_DD = np.asarray([[c,-s], [s, c]])
    x_ND = np.dot(x_ND, rot_DD)

    #x_ND, y_N = sklearn.datasets.make_blobs(
    #    n_samples=1000,
    #    cluster_std=[1.0, 2.5, 0.5],
    #    random_state=8675309)
    mean_D = np.mean(x_ND, axis=0)
    std_D = np.std(x_ND, axis=0)
    x_ND = (x_ND - mean_D[np.newaxis,:]) / std_D[np.newaxis,:]

    s_D = 1.5 * np.asarray([W, H]) / (2.0 * 3.0)
    #s_D[1] /= 1.2
    m_D = np.asarray([W, H]) / 2.0
    m_D[0] += 200
    x_ND = x_ND * s_D[np.newaxis,:] + m_D[np.newaxis,:]

    print x_ND.min(axis=0)
    print x_ND.max(axis=0)

    #color_list = ['#377eb8', '#ff7f00', '#4daf4a']
    color_list = ['#ff7f00', '#4daf4a']
    for kk in range(2):
        ax.plot(x_ND[y_N == kk,0], x_ND[y_N==kk,1], '.', markersize=13, color=color_list[kk], markeredgecolor='none', 
                alpha=0.2)
    ax.imshow(im_arr, origin='upper')
    ax.set_ylim([1150, -50])
    ax.set_xlim([0, 1200])
    ax.set_xticks([]); ax.set_yticks([])

    plt.savefig('tufts_ml_logo.png', bbox_inches='tight', pad_inches=0)
    plt.show()
