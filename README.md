# Equirectangular-rotate

## Theory
### Transform Longitute-Latitute into Spherical Coordinate
![](./docs-img/equirect2sphere.png)
### Transform Spherical Coordinate into Longitute-Latitute
![](./docs-img/spherical2equirect.png)

## Usage
```
positional arguments:
  file_path          file path
  X                  x rotation value
  Y                  y rotation value
  Z                  z rotation value
  outfile_name       output file name

optional arguments:
  -h, --help         show this help message and exit
  --isInverse ISINVERSE  Inverse Transformation. True or False
  --unit UNIT        degree or rad, default unit is degree
```

```
python main.py [-h] [--isInverse ISINVERSE] [--unit UNIT] file_path X Y Z outfile_name
```

for example
```
python main.py equirect-test.png 45 45 45 out_img.png
```

`main_with_time.py` is provided in `/testbench/` folder

## Performance
- **Original Image**
![](./testbench/equirect-test.png)

- **x - 45°, y - 45°, z - 45°**
![](./testbench/out.png)

- **x - 180°, y - 0, z - 0**
![](testbench/x180.png)