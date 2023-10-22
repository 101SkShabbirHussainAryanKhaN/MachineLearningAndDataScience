import numpy as n
one_dim =n.array([[1,1,1],[1,1,1],[1,1,1]]) 
print(one_dim)
print(one_dim.dtype)

# by data is float
ones_dims = n.ones((3,4))
# print(ones_dims.__dir__())

one = n.ones((3,5), dtype=int)


"""['__new__', '__repr__', '__str__', '__lt__', '__le__', '__eq__', '__ne__', '__gt__', 
'__ge__', '__iter__', '__add__', '__radd__', '__sub__', '__rsub__', '__mul__', '__rmul__',
'__mod__', '__rmod__', '__divmod__', '__rdivmod__', '__pow__', '__rpow__', '__neg__',
 '__pos__', '__abs__', '__bool__', '__invert__', '__lshift__', '__rlshift__', '__rshift__',
  '__rrshift__', '__and__', '__rand__', '__xor__', '__rxor__', '__or__', '__ror__', 
'__int__', '__float__', '__iadd__', '__isub__', '__imul__', '__imod__', '__ipow__', 
'__ilshift__', '__irshift__', '__iand__', '__ixor__', '__ior__', '__floordiv__', 
'__rfloordiv__', '__truediv__', '__rtruediv__', '__ifloordiv__', '__itruediv__', 
'__index__', '__matmul__', '__rmatmul__', '__imatmul__', '__len__', '__getitem__',
 '__setitem__', '__delitem__', '__contains__', '__array__', '__array_prepare__',
  '__array_finalize__', '__array_wrap__', '__array_ufunc__', '__array_function__',
   '__sizeof__', '__copy__', '__deepcopy__', '__reduce__', '__reduce_ex__',
    '__setstate__', 'dumps', 'dump', '__complex__', '__format__', 
    '__class_getitem__', 'all', 'any', 'argmax', 'argmin',
     'argpartition', 'argsort', 'astype', 'byteswap', 'choose',
      'clip', 'compress', 'conj', 'conjugate', 'copy', 'cumprod',
       'cumsum', 'diagonal', 'dot', 'fill', 'flatten', 'getfield',
        'item', 'itemset', 'max', 'mean', 'min', 'newbyteorder', 
        'nonzero', 'partition', 'prod', 'ptp', 'put', 'ravel', 
        'repeat', 'reshape', 'resize', 'round', 'searchsorted', 
        'setfield', 'setflags', 'sort', 'squeeze', 'std', 'sum',
         'swapaxes', 'take', 'tobytes', 'tofile', 'tolist', 'tostring', 
         'trace', 'transpose', 'var', 'view', '__dlpack__', '__dlpack_device__',
          'ndim', 'flags', 'shape', 'strides', 'data', 'itemsize', 'size',
           'nbytes', 'base', 'dtype', 'real', 'imag', 'flat', 'ctypes', 
           'T', '__array_interface__', '__array_struct__',
            '__array_priority__', '__doc__', '__hash__', '__getattribute__', 
            '__setattr__', '__delattr__',
 '__init__', '__getstate__', '__subclasshook__', '__init_subclass__', '__dir__', '__class__']"""
print(ones_dims)
print(ones_dims.dtype)
print(one)

zero_matrix = n.zeros((3,3))
print(zero_matrix)

zeros_matrix = n.zeros((3,3) ,dtype=bool )
print(zeros_matrix)

zerostr_matrix = n.zeros((3,3) ,dtype=str )
print(zerostr_matrix)

empty = ''
print(bool(empty))

em_matrix = n.empty((3,3))
print(em_matrix)

