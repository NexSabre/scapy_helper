# Scapy helper
Several features that should help you use Scapy.

## TL;DR
```python
>>> from scapy_helper import *
>>> e = Ether() # Scapy Ether

# Dump frame hex
>>> hex = get_hex(e)

# Convert and print 
>>> show_hex(e)
ff ff ff ff ff ff e0 d5 5e e6 6c 8e 90 00

# Show the differences
#   can be result of get_hex() or string or frame
>>> second_ether = "ff ff fc ff ff fa e0 d5 5e e6 6c 8e 90 00" 
>>> show_diff(Ether(), second_ether)
__ __ ff __ __ ff __ __ __ __ __ __ __ __
__ __ fc __ __ fa __ __ __ __ __ __ __ __
```
