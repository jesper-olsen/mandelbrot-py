mandelbrot-py
==============

Mandelbrot in Python. Three implementations:
* Regular python - for loops, sequential & parallel execution. 
* [numpy](https://numpy.org/) - vectorised.
* [jax](https://github.com/google/jax) - vectorised.

Other languages: 
* [Rust](https://github.com/jesper-olsen/mandelbrot-rs) 
* [Fortran](https://github.com/jesper-olsen/mandelbrot-f) 
* [Erlang](https://github.com/jesper-olsen/mandelbrot_erl) 
* [Mojo](https://github.com/jesper-olsen/mandelbrot-mojo)
* [Nushell](https://github.com/jesper-olsen/mandelbrot-nu)
* [Awk](https://github.com/jesper-olsen/mandelbrot-awk)
* [Tcl](https://github.com/jesper-olsen/mandelbrot-tcl)
* [R](https://github.com/jesper-olsen/mandelbrot-R)



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
  -n NWORKERS, --nworkers NWORKERS
```

```
% python mandelbrot.py --dim 1000 750 --xrange -1.2 -1.0  --yrange 0.2 0.35
Calculate 1000x750 mandelbrot
Saving output to mandelbrot.png
```
![PNG](https://raw.githubusercontent.com/jesper-olsen/mandelbrot-py/master/mandelbrot.png) 

Benchmark
---------

Below we will benchmark the time it takes to calculate a 5000x5000=25M pixel mandelbrot on a Macbook Air M1 (2020, 8 cores). All times are in seconds, and by the defaults it is the area with lower left {-1.20,0.20} and upper right {-1.0,0.35} that is mapped. Times include saving the result to file (png).

```
% time python mandelbrot.py --dim 5000 5000 
```

### Sequential 

| Time (real) | Time (user) | Speedup |
| ---------:  | ----------: | ------: |
| 177.2       | 177.3       |         |


### Worker Pool

Create a pool of #Workers which process individual rows concurrently.

| #Workers | Time (real) | Time (user) | Speedup |
| -------: | ---------:  | ----------: | ------: |
|  2       | 107.7       | 190.8       | 1.6     |
|  4       |  74.7       | 244.0       | 2.4     |
|  8       |  50.3       | 303.7       | 3.5     |
| 16       |  52.1       | 336.0       | 3.4     |
| 32       |  56.0       | 300.6       | 3.2     |
| 64       |  68.5       | 308.5       | 2.6     |


### Numpy & Jax - Vectorised

```
% time python mandelbrot_numpy.py --dim 5000 5000 
% time python mandelbrot_jax.py --dim 5000 5000 
```

|     | Time (real) | Time (user) | Speedup |
|-----| ---------:  | ----------: | ------: |
|Numpy| 55.1        | 34.3        |  3.3    |
|Jax  | 7.5         | 18.9        | 23.6    |

