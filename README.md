mandelbrot-py
==============

Mandelbrot in [Python](https://www.python.org/).
See [here](https://github.com/jesper-olsen/mandelbrot_erl) for an 
[Erlang](https://www.erlang.org/) version and [here](https://github.com/jesper-olsen/mandelbrot-rs) for a [Rust](https://www.rust-lang.org/) version.

Run
-----

```
% python mandelbrot.py -h 
Calculate the mandelbrot set, and save it as a png file.

options:
  -h, --help            show this help message and exit
  -x XRANGE XRANGE, --xrange XRANGE XRANGE
  -y YRANGE YRANGE, --yrange YRANGE YRANGE
  -d DIM DIM, --dim DIM DIM
```

```
% python mandelbrot.py --dim 1000 750 --xrange -1.2 -1.0  --yrange 0.2 0.35
Calculate 1000x750 mandelbrot
Saving output to mandelbrot.png
```
![PNG](https://raw.githubusercontent.com/jesper-olsen/mandelbrot-py/master/mandelbrot.png) 

Benchmark
---------

Below we will benchmark the time it takes to calculate a 25M pixel mandelbrot on a Macbook Air M1 (2020, 8 cores). All times are in seconds, and by the defaults it is the area with lower left {-1.20,0.20} and upper right {-1.0,0.35} that is mapped.

The image is calculated row by row - in multi-threaded mode 
[Rayon](https://docs.rs/rayon/latest/rayon/) farms the rows out to different threads.

```
% time python mandelbrot.py --dim 5000 5000 
```

### Sequential 

| Time (real) | Time (user) | Speedup |
| ---------:  | ----------: | ------: |
| 177.2       | 177.3       |         |

### Multi-process 

| Time (real) | Time (user) | Speedup |
| ---------:  | ----------: | ------: |
|             |             |         |

