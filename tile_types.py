from typing import Tuple

import numpy as np # type: ignore

# Tile graphics structured type compatible with Console.tiles_rgb
graphic_dt = np.dtype(
  [
    ("ch", np.int32), # Unicode codepoint
    ("fg", "3B"),     # 3 unsigned bytes (for RGB colours)
    ("bg", "3B"),
  ]
)

# Tile struct used for statically defined tile data
tile_dt = np.dtype(
  [
    ("walkable", bool),    # #t if tile can be walked over  # Tutorial originally had np.bool, but error messages say that's an error
    ("transparent", bool), # #t if tiel doesn't block FOV   #  because np.bool is just a deprecated alias for builtin bool so this should work just fine
    ("dark", graphic_dt),     # graphics for when this tile is not in FOV
  ]
)

def new_tile(
  *,  #enforce the use of keywords so parameter order doesn't matter
  walkable: int,
  transparent: int,
  dark: Tuple[int, Tuple[int, int, int], Tuple[int, int, int]],
) -> np.ndarray:
  """Helper function for defining individual tile types"""
  return np.array((walkable, transparent, dark), dtype=tile_dt)

floor = new_tile(
  walkable=True, transparent=True,
  dark=(ord(" "), (255, 255, 255), (50, 50, 150)),
)
wall = new_tile(
  walkable=False, transparent=False,
  dark=(ord(" "), (255, 255, 255), (0, 0, 100)),
)