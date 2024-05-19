# mcapy

[![Documentation Status](https://readthedocs.org/projects/mcapy/badge/?version=latest)](https://mcapy.readthedocs.io/en/latest/?badge=latest)
[![Tests](https://github.com/wensheng/mcapy/actions/workflows/run-pytest.yml/badge.svg)](https://github.com/wensheng/mcapy/actions/workflows/run-pytest.yml)
<!---
[![PyPI - Downloads](https://img.shields.io/pypi/dm/mcapy)](https://pypi.org/project/mcapy/)
-->

Python reader and writer for Minecraft region MCA (aka [Anvil File Format](https://minecraft.wiki/w/Anvil_file_format)) files.

It only works for the files from Minecraft v1.18 onward.

# Installation
This project is available on [PyPI](https://pypi.org/project/mcapy/) and can be installed with pip
```
pip install mcapy
```
or directly from github
```
pip install git+https://github.com/wensheng/mcapy.git
```
# Usage
## Reading
```python
from mca import Region

region = Region.from_file('r.0.0.mca')
chunk = region.get_chunk(0, 0)
block = chunk.get_block(0, 0, 0)

print(block)
print(block.id)
print(block.properties)
```
## Making own regions
```python
from mca import Block, EmptyRegion
from random import choice

# Create a new region with the `EmptyRegion` class at 0, 0 (in region coords)
region = EmptyRegion(0, 0)

# Create `Block` objects that are used to set blocks
stone = Block('minecraft', 'stone')
dirt = Block('dirt')  # you can omit 'minecraft' namespace

# Make a 16x16x16 cube of either stone or dirt blocks
for y in range(16):
    for z in range(16):
        for x in range(16):
            region.set_block(choice((stone, dirt)), x, y, z)

# Save to a file
region.save('r.-1.-1.mca')
```

## Note

This project is originally forked from [anvil-parser](https://github.com/matcool/anvil-parser), which was archived by its author.

