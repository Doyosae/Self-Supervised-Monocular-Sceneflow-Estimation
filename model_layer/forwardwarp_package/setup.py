#!/usr/bin/env python3
from setuptools import setup, find_packages
from torch.utils.cpp_extension import BuildExtension, CUDAExtension

cxx_args = ['-std=c++14']

nvcc_args = [
    '-gencode', 'arch=compute_50,code=sm_50',
    '-gencode', 'arch=compute_52,code=sm_52',
    '-gencode', 'arch=compute_60,code=sm_60',
    '-gencode', 'arch=compute_61,code=sm_61',
    '-gencode', 'arch=compute_61,code=compute_61'
]

setup(
    name='forward_warp_cuda',
    ext_modules=[
        CUDAExtension('forward_warp_cuda', [
            'forward_warp_cuda.cpp',
            'forward_warp_cuda_kernel.cu',
        ], extra_compile_args={'cxx': cxx_args, 'nvcc': nvcc_args})
    ],
    cmdclass={
        'build_ext': BuildExtension
    })
