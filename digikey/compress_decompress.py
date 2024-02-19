import lzstring
import json

lz = lzstring.LZString()


compressed_string = 'N4IgrCBcoA5QjAGhDOl4AYMF9tA'


decompressed_string = lz.decompressFromEncodedURIComponent(compressed_string)

# print(decompressed_string)


import lzstring
import json

lz = lzstring.LZString()

data = {"5": {"p": 1, "pp": 100}}
"""N4IgrCBcAEoA5WgRgCwCYA00RwTJADAQL7FA страница  142
N4IgrCBcAEoA5WgRgAxvQGmiOCapQF9Cg страница  1000000
N4IgrCBcAEoA5WgRgDTRHBMkAYcF98g страница  1"""
json_string = json.dumps(data)
lz = lzstring.LZString()
compressed_string = lz.compressToEncodedURIComponent(json_string)
print(compressed_string)



