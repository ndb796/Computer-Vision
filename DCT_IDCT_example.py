from scipy.fft import dct, idct
import numpy as np

np.set_printoptions(suppress=True)

def dct2(block):
    return dct(dct(block.T, norm='ortho').T, norm='ortho')

def idct2(block):
    return idct(idct(block.T, norm='ortho').T, norm='ortho')

x = [
  [105, 202, 124, 198, 125, 102, 199, 205],
  [152, 190, 197, 180, 103, 202, 200, 122],
  [188, 144, 153, 165, 185, 134, 111, 123],
  [105, 202, 124, 198, 125, 102, 199, 205],
  [152, 190, 197, 180, 103, 202, 200, 122],
  [188, 144, 153, 165, 185, 134, 111, 123],
  [101, 203, 243, 111, 170, 198, 185, 203],
  [213, 202, 154, 144, 164, 195, 174, 152]
]

dct_result = dct2(np.array(x))
print(dct_result)

idct_result = idct2(dct_result)
print(idct_result)
