# -*- coding: utf-8 -*-
# @Time    : 2018/10/15 0015 18:08
# @FileName: autograd_example.py
# @Software: PyCharm


import torch
x=torch.Tensor([1])
x.requires_grad=True
print(x.grad_fn)
print(x)
y = x + 2
print(y)
print(y.grad_fn)
z = y * y * 3
print(z.grad_fn)
print(z)
z.backward()
print(x.grad)