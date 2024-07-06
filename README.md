# cim_converter
simple python scripts to extract/compress `.png` files from/into `.cim` files. (the skin format used by [beatoraja](https://github.com/exch-bms2/beatoraja))
* cim2png.py - extracts PNGs from CIMs
* png2cim.py - compress PNGs into CIMs
## Usage
To convert CIMs to PNGs:
```
cim2png.py file1.cim file2.cim file3.cim ...
```
To convert PNGs to CIMs:
```
png2cim.py file1.png file2.png file3.png ...
```
or you could just drag & drop the files onto the executable(script).  
The script requires `zlib`, `numpy`, so you might want to do `pip install zlib` and `pip install numpy` first.
