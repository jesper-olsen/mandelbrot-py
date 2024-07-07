import matplotlib.pyplot as plt
import numpy as np
import argparse
from multiprocessing import Pool


def escape_time(c, limit):
    z = c
    for i in range(limit):
        if abs(z) > 4:
            return i
        z = z * z + c
    return i


def mandelbrot_row(ll, ur, fwidth, fheight, width, height, y):
    row = np.empty(width)
    for x in range(width):
        c = complex(ll.real + x * fwidth / width, ur.imag - y * fheight / height)
        row[x] = 255 - escape_time(c, 255)
    return row


def mandelbrot(nworkers, ll, ur, width, height):
    print("#workers:", nworkers)
    fwidth, fheight = ur.real - ll.real, ur.imag - ll.imag

    pixels = np.empty((width, height))
    if nworkers == 1:
        for y in range(height):
            for x in range(width):
                c = complex(
                    ll.real + x * fwidth / width, ur.imag - y * fheight / height
                )
                pixels[x, y] = 255 - escape_time(c, 255)
    else:
        with Pool(nworkers) as pool:
            rows = pool.starmap(
                mandelbrot_row,
                [(ll, ur, fwidth, fheight, width, height, y) for y in range(height)],
            )

        for y, row in enumerate(rows):
            pixels[:, y] = row

    fig = plt.figure(frameon=False)
    fig.set_size_inches(width, height)
    ax = plt.Axes(fig, [0.0, 0.0, 1.0, 1.0])
    ax.set_axis_off()
    fig.add_axes(ax)
    plt.imshow(pixels.T, interpolation="nearest", cmap="gray", aspect="auto")
    fname = "mandelbrot.png"
    print(f"Saving to {fname}")
    plt.savefig(fname, bbox_inches="tight", pad_inches=0, dpi=1)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Calculate the mandelbrot set, and save it as a png file."
    )
    parser.add_argument("-x", "--xrange", nargs=2, type=float, default=[-1.2, -1.0])
    parser.add_argument("-y", "--yrange", nargs=2, type=float, default=[0.2, 0.35])
    parser.add_argument("-d", "--dim", nargs=2, type=int, default=[1000, 750])
    parser.add_argument("-n", "--nworkers", type=int, default=1)

    args = parser.parse_args()

    ll = complex(args.xrange[0], args.yrange[0])
    ur = complex(args.xrange[1], args.yrange[1])
    print(f"Calculate {args.dim[0]}x{args.dim[1]} mandelbrot")
    mandelbrot(args.nworkers, ll, ur, *args.dim)
