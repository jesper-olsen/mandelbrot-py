mandelbrot-py
==============

Mandelbrot in Python. Three implementations:
* Regular python - for loops, sequential & parallel execution. 
* [numpy](https://numpy.org/) - vectorised.
* [jax](https://github.com/google/jax) - vectorised.


### Other Language Implementations

This project is part of a suite of mandelbrot implementations in different languages.

Single Thread/Multi-thread shows the number of seconds it takes to do a 5000x5000 calculation.


| Language    | Repository                                                           | Single Thread   | Multi-Thread | Simd | Multi-Thread + Simd |
| :--------   | :------------------------------------------------------------------- | ---------------:| -----------: | ----:| ------------------: |
| Awk         | [mandelbrot-awk](https://github.com/jesper-olsen/mandelbrot-awk)     |           146.3 |              |      |                     |
| Bash        | [mandelbrot-bash](https://github.com/jesper-olsen/mandelbrot-bash)   |         10187.3 |              |      |                     |
| C           | [mandelbrot-c](https://github.com/jesper-olsen/mandelbrot-c)         |             3.6 |          0.6 |  0.7 |               0.2   |
| C++         | [mandelbrot-cpp](https://github.com/jesper-olsen/mandelbrot-cpp)     |             3.7 |          0.6 |  0.7 |               0.2   |
| Erlang      | [mandelbrot_erl](https://github.com/jesper-olsen/mandelbrot_erl)     |            35.6 |          8.3 |      |                     |
| Fortran     | [mandelbrot-f](https://github.com/jesper-olsen/mandelbrot-f)         |             4.5 |              |      |                     |
| Go          | [mandelbrot-go](https://github.com/jesper-olsen/mandelbrot-go)       |             4.1 |          0.8 |  1.3 |               0.4   |
| Java        | [mandelbrot-java](https://github.com/jesper-olsen/mandelbrot-java)   |             3.9 |          0.8 |  1.4 |               0.5   |
| Lua         | [mandelbrot-lua](https://github.com/jesper-olsen/mandelbrot-lua)     |            33.2 |              |      |                     |
| Mojo        | [mandelbrot-mojo](https://github.com/jesper-olsen/mandelbrot-mojo)   |             3.8 |          1.2 |  0.7 |               0.4   |
| Nushell     | [mandelbrot-nu](https://github.com/jesper-olsen/mandelbrot-nu)       |   (est) 17186.6 |              |      |                     |
| Odin        | [mandelbrot-odin](https://github.com/jesper-olsen/mandelbrot-odin)   |             4.4 |              |      |                     |
| **Python**  | [mandelbrot-py](https://github.com/jesper-olsen/mandelbrot-py)       |     (pure) 93.3 | (jax)    5.9 |      |                     |
| R           | [mandelbrot-R](https://github.com/jesper-olsen/mandelbrot-R)         |           335.0 |              |
| Rust        | [mandelbrot-rs](https://github.com/jesper-olsen/mandelbrot-rs)       |             4.7 |          1.3 |  1.4 |               0.8   |
| Swift       | [mandelbrot-swift](https://github.com/jesper-olsen/mandelbrot-swift) |             4.5 |          1.2 |  1.3 |               0.7   |
| Tcl         | [mandelbrot-tcl](https://github.com/jesper-olsen/mandelbrot-tcl)     |           306.9 |              |      |                     |
| Zig         | [mandelbrot-zig](https://github.com/jesper-olsen/mandelbrot-zig)     |             4.9 |          0.9 |  0.7 |               0.3   |



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

Below we will benchmark the time it takes to calculate a 5000x5000=25M pixel mandelbrot on a Macbook Air M5 (4+6 cores). All times are in seconds, and by the defaults it is the area with lower left {-1.20,0.20} and upper right {-1.0,0.35} that is mapped. Times include saving the result to file (png).

```
% time python mandelbrot.py --dim 5000 5000 
```

### Sequential 

| Time (real) | Time (user) | Speedup |
| ---------:  | ----------: | ------: |
|  93.3       |  90.2       |         |


### Worker Pool

Create a pool of #Workers which process individual rows concurrently.

| #Workers | Time (real) | Time (user) | Speedup |
| -------: | ---------:  | ----------: | ------: |
|  2       |  59.0       |  90.2       | 1.6     |
|  4       |  36.2       | 111.8       | 2.6     |
|  8       |  26.3       | 154.0       | 3.5     |
| 16       |  22.3       | 169.8       | 4.2     |
| 32       |  22.3       | 169.8       | 3.2     |
| 64       |  23.5       | 189.6       | 4.0     |


### Numpy & Jax - Vectorised

```
% time python mandelbrot_numpy.py --dim 5000 5000 
% time python mandelbrot_jax.py --dim 5000 5000 
```

|     | Time (real) | Time (user) | Speedup |
|-----| ---------:  | ----------: | ------: |
|Numpy| 20.5        | 19.3        |  4.6    |
|Jax  | 5.9         | 10.7        | 15.8    |

