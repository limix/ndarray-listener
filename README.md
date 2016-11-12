# ndarray_listener

[![PyPI](https://img.shields.io/pypi/v/ndarray_listener.svg)](https://pypi.python.org/pypi/ndarray-listener/)\

[![Anaconda-Server Badge](https://anaconda.org/conda-forge/ndarray_listener/badges/version.svg)](https://anaconda.org/conda-forge/ndarray_listener)

[![Anaconda-Server Badge](https://anaconda.org/conda-forge/ndarray_listener/badges/installer/conda.svg)](https://conda.anaconda.org/conda-forge)



NumPy ``ndarray`` that notifies listeners for data change

## Getting Started

Watch for ``ndarray`` changes

```python
>>> from numpy import array
>>>
>>> from ndarray_listener import ndarray_listener
>>>
>>> a = array([-0.5, 0.1, 1.1])
>>> b = ndarray_listener(a)
>>> c = ndarray_listener(array([-0.5, 0.1, 1.1]))
>>>
>>> class Watcher(object):
...
...     def __init__(self):
...             self.called_me = False
...
...     def __call__(self, _):
...             self.called_me = True
>>>
>>> w = Watcher()
>>> b.talk_to(w)
>>>
>>> w.called_me
False
>>> b[0] = 1.2
>>> w.called_me
True
>>>
>>> w = Watcher()
>>> b.talk_to(w)
>>>
>>> w.called_me
False
>>> b[:] = 1
>>> w.called_me
True
>>>
>>> w = Watcher()
>>> c.talk_to(w)
>>>
>>> w.called_me
False
>>> c[:] = c + c
>>> w.called_me
True
```

### Installing

Via pip
```
pip install ndarray_listener
```

or via [Conda](http://conda.pydata.org/docs/index.html)
```
conda install -c conda-forge ndarray_listener
```

## Running the tests

After installation, you can test it
```
python -c "import ndarray_listener; ndarray_listener.test()"
```

## Authors

* **Danilo Horta** - [https://github.com/Horta](https://github.com/Horta)

## License

This project is licensed under the MIT License - see the
[LICENSE](LICENSE) file for details
