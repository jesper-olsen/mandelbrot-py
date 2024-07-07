import numpy as np
import matplotlib.pyplot as plt
import argparse


def escape_time(c, fractal, max_iters=255):
    z = c
    for i in range(max_iters):
        z = z**2 + c
        diverged = np.abs(z) > 2
        diverging_now = diverged & (fractal == max_iters)
        fractal[diverging_now] = i
        z[diverged] = np.nan  # Prevent further overflow
    return max_iters - fractal


def cnt2char(n: int, max_iters: int) -> str:
    symbols = "MW2a_. "
    idx = round(n / max_iters * (len(symbols) - 1))
    return symbols[idx]


def print_ascii(pixels, max_iters):
    height, width = pixels.shape
    print("Mandelbrot ", height, "x", width)
    stepx = max(1, width // 50)
    stepy = max(1, height // 50)
    for y in range(height - 1, -1, -stepy):
        for x in range(0, width, stepx):
            val = int(pixels[y, x])
            print(cnt2char(val, max_iters), end="")
        print()


def save_as_png(pixels, width, height, fname="mandelbrot.png"):
    fig = plt.figure(frameon=False)
    fig.set_size_inches(width, height)
    ax = plt.Axes(fig, [0.0, 0.0, 1.0, 1.0])
    ax.set_axis_off()
    fig.add_axes(ax)
    plt.imshow(
        pixels, interpolation="nearest", cmap="gray", aspect="auto", origin="lower"
    )
    print(f"Saving to {fname}")
    plt.savefig(fname, bbox_inches="tight", pad_inches=0, dpi=1)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Calculate the mandelbrot set, and save it as a png file."
    )
    parser.add_argument("-x", "--xrange", nargs=2, type=float, default=[-1.2, -1.0])
    parser.add_argument("-y", "--yrange", nargs=2, type=float, default=[0.2, 0.35])
    parser.add_argument("-d", "--dim", nargs=2, type=int, default=[1000, 750])
    parser.add_argument("-i", "--max_iters", type=int, default=255)

    args = parser.parse_args()
    x_min, x_max = args.xrange
    y_min, y_max = args.yrange
    width, height = args.dim

    y, x = np.ogrid[y_min : y_max : height * 1j, x_min : x_max : width * 1j]
    c = x + y * 1j
    fractal = np.full(c.shape, args.max_iters, dtype=np.int16)
    escape_times = escape_time(c, fractal, args.max_iters)
    print_ascii(escape_times, args.max_iters)
    save_as_png(escape_times, width, height)
