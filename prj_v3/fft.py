import numpy as np
# from scipy.fft import fft2, fftshift, ifft2, ifftshift, dct, idct
from scipy import fft as fft2d
from image import Image


## FFT Functions for Images
class FFT2D(Image):
    def __init__(self, img: Image):
        self.data = fft2d.fft2(img.data)
        self.title = img.title
        self.dtype = "img"
        self.shifted = False
        self.axis_off = img.axis_off


class FFT2DShift(Image):
    def __init__(self, img: Image):
        self.data = fft2d.fftshift(fft2d.fft2(img.data))
        self.title = img.title
        self.dtype = "img"
        self.shifted = True
        self.axis_off = img.axis_off


class InvFFT2D(Image):
    def __init__(self, amp: Image, ang: Image=None):
        data = amp.data if ang is None else amp.data * np.exp(1j * ang.data)
        self.data = fft2d.ifft2(data)
        self.title = "Inverse FFT"
        self.dtype = "img"
        self.shifted = False
        self.axis_off = amp.axis_off


class InvFFT2DShift(Image):
    def __init__(self, amp: Image, ang: Image=None):
        data = amp.data if ang is None else amp.data * np.exp(1j * ang.data)
        self.data = fft2d.ifft2(fft2d.ifftshift(data))
        self.title = "Inverse FFT"
        self.dtype = "img"
        self.shifted = False
        self.axis_off = amp.axis_off


## DCT Functions for Images
class DCT2D(Image):
    def __init__(self, img: Image):
        self.data = fft2d.dct(fft2d.dct(img.data.T, type=2, norm='ortho').T, type=2, norm='ortho')
        self.title = img.title
        self.dtype = "img"
        self.is_shifted = False
        self.axis_off = img.axis_off


class InvDCT2D(Image):
    def __init__(self, img: Image):
        self.data = fft2d.idct(fft2d.idct(img.data.T, type=2, norm='ortho').T, type=2, norm='ortho')
        self.title = "Inverse DCT"
        self.dtype = "img"
        self.is_shifted = False
        self.axis_off = img.axis_off


## Math Functions for FFT of Images
class Amplitude(Image):
    def __init__(self, img: Image):
        self.data = np.abs(img.data)
        self.title = "Amplitude(FFT)"
        self.dtype = "amp"
        self.shifted = img.shifted
        self.axis_off = img.axis_off


class Phase(Image):
    def __init__(self, img: Image):
        self.data = np.angle(img.data)
        self.title = "Phase(FFT)"
        self.dtype = "ang"
        self.shifted = img.shifted
        self.axis_off = img.axis_off


## Math Functions for Images
class Abs(Image):
    def __init__(self, img: Image):
        self.data = np.abs(img.data)
        self.title = img.title
        self.dtype = img.dtype
        self.shifted = img.shifted
        self.axis_off = img.axis_off


class Log1p(Image):
    def __init__(self, img: Image):
        self.data = np.log1p(img.data)
        self.title = img.title
        self.dtype = img.dtype
        self.shifted = img.shifted
        self.axis_off = img.axis_off


class Log10(Image):
    def __init__(self, img: Image):
        self.data = np.log10(img.data)
        self.title = img.title
        self.dtype = img.dtype
        self.shifted = img.shifted
        self.axis_off = img.axis_off


class Real(Image):
    def __init__(self, img: Image):
        self.data = np.real(img.data)
        self.title = img.title
        self.dtype = img.dtype
        self.shifted = img.shifted
        self.axis_off = img.axis_off


if __name__ == "__main__":

    import skimage
    from image import Image
    from viewer import Viewer

    viewer = Viewer()
    img = Image(skimage.data.camera()).set_title("Original").info()

    if 1:
        fft1 = FFT2D(img)
        amp1 = Amplitude(fft1).info()
        ang1 = Phase(fft1).info()
        inv1 = Abs(InvFFT2D(amp1, ang1)).info()

        viewer.show(img, Log1p(amp1), ang1, inv1)

    if 1:
        fft2 = FFT2DShift(img)
        amp2 = Amplitude(fft2).info()
        ang2 = Phase(fft2).info()
        inv2 = Abs(InvFFT2DShift(amp2, ang2)).info()

        viewer.show(img, Log1p(amp2), ang2, inv2)