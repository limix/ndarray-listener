# ndarray-listener

Implementation of the [Observer pattern](https://en.wikipedia.org/wiki/Observer_pattern) for NumPy arrays.

## Example

```python
from numpy import array
from ndarray_listener import ndl

a = ndl(array([-0.5, 0.1, 1.1]))

class Observer(object):
  def __init__(self):
    self.called_me = False

  def __call__(self, _):
    self.called_me = True

o = Observer()
a.talk_to(o)
print(o.called_me)
a[0] = 1.2
print(o.called_me)
```

The output should be

```
False
True
```

## Install

From command line, enter

```bash
pip install ndarray-listener
```

## Running the tests

Install dependencies

```bash
pip install pytest
```

then run

```python
python -c "import ndarray_listener; ndarray_listener.test()"
```

## Documentation

[Documentation](https://ndarray-listener.readthedocs.io/en/latest/)

## Authors

* [Danilo Horta](https://github.com/horta)


## License

This project is licensed under the [MIT License](https://raw.githubusercontent.com/limix/ndarray-listener/master/LICENSE.md).
