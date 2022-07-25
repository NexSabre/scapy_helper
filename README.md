[![push pipeline](https://github.com/NexSabre/scapy_helper/actions/workflows/pipeline.yml/badge.svg)](https://github.com/NexSabre/scapy_helper/actions/workflows/pipeline.yml)
[![PyPI version](https://badge.fury.io/py/scapy-helper.svg)](https://badge.fury.io/py/scapy-helper)
[![Downloads](https://pepy.tech/badge/scapy-helper)](https://pepy.tech/project/scapy-helper)

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
# scapy | __ __ ff __ __ ff __ 00 00 00 00 00 __ __ XX XX XX XX | len: 14B
# hex   | __ __ fc __ __ fa __ 11 11 11 11 11 __ __ 11 11 00 22 | len: 18B
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

Since version v0.5.1, to the _scapy_helper_ was added `chexdump` and `hexdump`. With v0.7.1 we introduce a `mac2int`
and `int2mac`. Version v0.10 bring `hstrip`. Version v0.11 adding `to_dict` & `to_list`.

### to_dict

Since v0.11, `to_dict(<packet>)` allows to dump a specific layer into a dict object.

```python
>> packet = Ether(dst="ff:ff:ff:ff:ff:ff", src="00:00:00:00:00:00") / IP() / TCP()

>> to_dict(packet)
{'Ethernet': {'src': '00:00:00:00:00:00', 'dst': 'ff:ff:ff:ff:ff:ff', 'type': 2048}}
```

You can specify id of layer to convert, by providing a `layer` key.

```python
>> packet = Ether(dst="ff:ff:ff:ff:ff:ff", src="00:00:00:00:00:00") / IP() / TCP()

>> to_dict(packet, layer=1)  # layer 1 is IP
{'IP': {'frag': 0, 'src': '0.0.0.0', 'proto': 6, 'tos': 0, 'dst': '127.0.0.1',
        'chksum': None, 'len': None, 'options': [], 'version': 4, 'flags': None,
        'ihl': None, 'ttl': 64, 'id': 1}}
```

### to_list

Since v0.11, `to_list(<packet>)` allows to dump entire frame into a List [ Dict ]

```python
>> packet = Ether(dst="ff:ff:ff:ff:ff:ff", src="00:00:00:00:00:00") / IP() / TCP()

>> to_list(packet)
[{'Ethernet': {'src': '00:00:00:00:00:00', 'dst': 'ff:ff:ff:ff:ff:ff', 'type': 2048}}, {
    'IP': {'frag': 0, 'src': '0.0.0.0', 'proto': 6, 'tos': 0, 'dst': '127.0.0.1', 'chksum': None, 'len': None,
           'options': [], 'version': 4, 'flags': None, 'ihl': None, 'ttl': 64, 'id': 1}}, {
     'TCP': {'reserved': 0, 'seq': 0, 'ack': 0, 'dataofs': None, 'urgptr': 0, 'window': 8192,
             'flags': None, 'chksum': None, 'dport': 80, 'sport': 20, 'options': []}}]
```

### hstrip

Since v0.10, allows to convert a Scapies hexdump into clean string-hex format. Select a hexdump and copy into clipboard.

```text
>>> f = Ether()/IP()/TCP()
>>> hexdump(f)
0000  FF FF FF FF FF FF 00 00 00 00 00 00 08 00 45 00  ..............E.
0010  00 28 00 01 00 00 40 06 7C CD 7F 00 00 01 7F 00  .(....@.|.......
0020  00 01 00 14 00 50 00 00 00 00 00 00 00 00 50 02  .....P........P.
0030  20 00 91 7C 00 00                                 ..|..
>>> 
```

In command line type `hstrip`

```text
FF FF FF FF FF FF 00 00 00 00 00 00 08 00 45 00
00 28 00 01 00 00 40 06 7C CD 7F 00 00 01 7F 00
00 01 00 14 00 50 00 00 00 00 00 00 00 00 50 02
20 00 91 7C 00 00
```

Voilà! You have in your clipboard striped version of hexdump. Now you can paste it
into [packetor.com](http://packetor.com)

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

### Use definition in Pytest
You can use functions in your pytest (if you do not use a unittest or do not want to inherit by the `PacketAssert`)
  * `assert_hex_equal`
  * `assert_hex_not_equal`
  * `assert_hex_len_equal` 
  * `assert_hex_len_not_equal`
  * `assert_bytes_equal`  
  * `assert_bytes_not_equal`

Example of usage:
```python
from scapy_helper import assert_hex_equal


class TestExample:
    def test_example(self):
        assert_hex_equal(Ether(), Ether("10.10.10.10"))
```


### Extends test class using PacketAssert (since v0.3.1)

__Note: In the v0.3.0 this class was called HexEqual__

You can use assertHexEqual/assertHexNotEqual and assertBytesEqual/assertBytesNotEqual in the tests. When the assertion
fails, wrapper produces information about the frames (in hex).

Example of usage: 
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
