![Test](https://github.com/NexSabre/scapy_helper/workflows/Test/badge.svg?branch=master)
![CodeQL](https://github.com/NexSabre/scapy_helper/workflows/CodeQL/badge.svg?branch=master)
[![PyPI version](https://badge.fury.io/py/scapy-helper.svg)](https://badge.fury.io/py/scapy-helper)

# Scapy helper (aka. Packet Helper) 
This micro library popularizes some handy tricks that make it easy usage of Scapy.

## TL;DR
```python
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
# Not equal at 11B

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

## Addons
Since version v0.5.1, to the _scapy_helper_ was added `chexdump` and `hexdump`. 
With v0.7.1 we introduce a `mac2int` and `int2mac`. 

### chexdump
```python
from scapy_helper import chexdump

packet = "\x00\x01".encode()

# chexdump as we know 
chexdump(packet)
# 0x00, 0x01

# with return 
val = chexdump("\x00\x01".encode(), dump=True)
# or if you need a list
val = chexdump("\x00\x01".encode(), dump=True, to_list=True)
```

### hexdump
```python
from scapy_helper import hexdump

packet = Ether(dst="ff:ff:ff:ff:ff:ff",
               src="00:00:00:00:00:00")

# chexdump as we know 
hexdump(packet)
# 0000   ff ff ff ff ff ff 00 00 00 00 00 00 08 00 45 00   ..............E.
# 0010   00 14 00 01 00 00 40 00 fb e8 00 00 00 00 7f 00   ......@.........
# 0020   00 01                                             ..

# with return 
val = hexdump(packet, dump=True)
# or if you need a list
val = hexdump(packet, dump=True, to_list=True)
```

### int2mac
Convert an integer value into mac address. Letters by the default are lower case. 
```python
from scapy_helper import int2mac

int2mac(73596036829, upper=True)
# "00:11:22:AA:66:DD"
```

### mac2int
Convert a mac address into integer value 
```python
from scapy_helper import mac2int

mac2int("00:11:22:AA:66:DD")
# 73596036829
```

### ip2int
Convert IP address string into int value
```python
from scapy_helper import ip2int

ip2int("0.0.0.0")
# 0
```

### int2mac
Convert an int value into IP address string
```python
from scapy_helper import int2ip

int2ip(0)
# 0.0.0.0
```

## Test case usage
### Extends test class using PacketAssert (since v0.3.1)
__Note: In the v0.3.0 this class was called HexEqual__

You can use assertHexEqual/assertHexNotEqual and assertBytesEqual/assertBytesNotEqual in the tests.
When the assertion fails, wrapper produces information about the frames (in hex).

```python
import unittest
from scapy_helper.test_case_extensions.packet_assert import PacketAssert

class TestExample(unittest.TestCase, PacketAssert):
    def test_example(self):
        self.assertHexEqual(Ether(), Ether("10.10.10.10"), "Frame should be the same")

    def text_example_negative(self):
        self.assertNotEqual(Ether(), Ether(), "Frame should be diffrent")

    def test_example_bytes(self):
        self.assertBytesEqual(Ether(), Ether(), "Bytes should be equal")
```


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
