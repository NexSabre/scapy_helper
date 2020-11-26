![Test](https://github.com/NexSabre/scapy_helper/workflows/Test/badge.svg?branch=master)   ![CodeQL](https://github.com/NexSabre/scapy_helper/workflows/CodeQL/badge.svg?branch=master)
# Scapy helper
Several features that should help you use Scapy.

## TL;DR
```python
from scapy.layers.inet import Ether
from scapy_helper import *

# Dump frame hex
hex_value = get_hex(Ether())
# hex_value: 
'ff ff ff ff ff ff 00 00 00 00 00 00 90 00'

# Convert and print 
show_hex(Ether())
# output: 
# ff ff ff ff ff ff 00 00 00 00 00 00 90 00

# Show the differences
#   can be result of get_hex() or string or frame
second_ether = "ff ff fc ff ff fa 00 00 00 00 00 00 90 00 11 11 00 22" 
show_diff(Ether(), second_ether)
# output: 
# WARN:: Frame len is not the same
# WARN:: Second row is longer by the 4B
#
# __ __ ff __ __ ff __ 00 00 00 00 00 __ __ XX XX XX XX | len: 14B
# __ __ fc __ __ fa __ 11 11 11 11 11 __ __ 11 11 00 22 | len: 18B
#
#Not equal at 11B

# You can add a index to it
show_diff(Ether(), second_ether, index=True)
# output: 
# __ __ ff __ __ ff __ 00 00 00 00 00 __ __ XX XX XX XX | len: 14B
# __ __ fc __ __ fa __ 11 11 11 11 11 __ __ 11 11 00 22 | len: 18B
#                                                       |
#       ^2       ^5    ^7 ^8 ^9 10 11       14 15 16 17 | position
#
# Not equal at 11B

# You can add a custom char to mark a missing elements
show_diff(Ether(), second_ether, index=True, empty_char="+")
# output: 
# __ __ ff __ __ ff __ 00 00 00 00 00 __ __ ++ ++ ++ ++ | len: 14B
# __ __ fc __ __ fa __ 11 11 11 11 11 __ __ 11 11 00 22 | len: 18B
#                                                       |
#       ^2       ^5    ^7 ^8 ^9 10 11       14 15 16 17 | position
```

## Test case usage
### hex_equal (since v0.1.11)
Return bool status of equality and print status if there is a difference between objects
```python
from scapy_helper import hex_equal

# hex_equal(first, second, show_inequalities=True, **options_for_show_diff):
assert hex_equal(Ether(), second_ether)
```

## Compare
### table_diff (tdiff as shortcut)
```text
from scapy_helper.compare import Compare
Compare(frame_1, frame_2).table_diff()

| Diff or header              | Element   | First             | Second            |
|-----------------------------|-----------|-------------------|-------------------|
| ###[ Ethernet ]###          |           |                   |                   |
|                             | dst       | 00:00:00:00:00:00 | 00:00:00:00:00:00 |
|                             | src       | 00:00:00:00:00:00 | 00:00:00:00:00:00 |
|                             | type      | IPv4              | IPv4              |
| ###[ IP ]###                |           |                   |                   |
|                             | version   | 4                 | 4                 |
|                             | ihl       | None              | None              |
|                             | tos       | 0x0               | 0x0               |
|                             | len       | None              | None              |
|                             | id        | 1                 | 1                 |
|                             | flags     |                   |                   |
|                             | frag      | 0                 | 0                 |
| 15 !=  20                   | ttl       | 15                | 20                |
|                             | proto     | udp               | udp               |
|                             | chksum    | None              | None              |
| 192.168.1.1 !=  192.168.1.2 | src       | 192.168.1.1       | 192.168.1.2       |
|                             | dst       | 192.168.1.20      | 192.168.1.20      |
| \options   \                |           |                   |                   |
| ###[ UDP ]###               |           |                   |                   |
|                             | sport     | domain            | domain            |
|                             | dport     | domain            | domain            |
|                             | len       | None              | None              |
|                             | chksum    | None              | None              |
|                             |           |                   |                   |

```