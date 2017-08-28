from numpy import asarray, ndarray


class ndarray_listener(ndarray):
    def __new__(cls, input_array):
        obj = asarray(input_array).view(cls)

        if hasattr(input_array, '_listeners'):
            obj._listeners = input_array._listeners
        else:
            obj._listeners = []

        return obj

    def __array_finalize__(self, obj):
        if obj is None:
            return
        self._listeners = getattr(obj, '_listeners', [])

    def __setitem__(self, *args, **kwargs):
        super(ndarray_listener, self).__setitem__(*args, **kwargs)
        self.__notify()

    def __setattr__(self, *args, **kwargs):
        super(ndarray_listener, self).__setattr__(*args, **kwargs)
        if len(args) > 0 and args[0] == '_listeners':
            return
        self.__notify()

    def __getitem__(self, *args, **kwargs):
        v = super(ndarray_listener, self).__getitem__(*args, **kwargs)
        if isinstance(v, ndarray_listener):
            return v

        v = ndarray_listener(v)
        for l in self._listeners:
            v.talk_to(l)
        return v

    def talk_to(self, me):
        self._listeners.append(me)

    def __notify(self):
        for l in self._listeners:
            l(asarray(self))

    def itemset(self, *args, **kwargs):
        super(ndarray_listener, self).itemset(*args, **kwargs)
        self.__notify()
