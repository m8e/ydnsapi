# ydnsapi - YDNS API

ydns is a ip redirect provider.To use this api, you should register a account on [YDNS](https://ydns.io/) first.


## Update Machine IP to ydns

```python
import ydnsapi

ydns = ydnsapi.YDNS("username", "password")
state = ydns.autoUpdateIP("hostname")
print(state) # True if success

```