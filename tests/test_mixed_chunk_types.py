from pytest import mark
from mca import Chunk, EmptyChunk, EmptyRegion, Block, Region
import random

def test_mixed_chunk_types():
    colors = ['stone', 'dirt', 'grass', 'water']

    region = EmptyRegion(0, 0)

    chunk = EmptyChunk(0, 0)
    empty_chunk = EmptyChunk(1, 0)
    for i, color in enumerate(colors):
        chunk.set_block(Block(color), i, 0, 0)
        empty_chunk.set_block(Block(color), i, 0, 0)

    region.add_chunk(Chunk(chunk.save()))
    region.add_chunk(empty_chunk)
    #region.add_chunk(Chunk(empty_chunk.save()))

    region = Region(region.save())

    for i in range(2):
        chunk = region.get_chunk(i, 0)
        for i, color in enumerate(colors):
            assert chunk.get_block(i, 0, 0).id == color
