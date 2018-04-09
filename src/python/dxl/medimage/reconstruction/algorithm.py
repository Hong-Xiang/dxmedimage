class Algorithm:
  def __init__(self, device, backend):
    self._device = device
    self._backend = backend

  @property
  def device(self):
    return self._device

  @property
  def backend(self):
    return self._backend


class FBP(Algorithm):
  @classmethod
  def supported_filters(cls, backend):
    if backend == 'astra':
      return [
          'ram-lak',
          'shepp-logan',
          'cosine',
          'hamming',
          'hann',
          'none',
          'tukey',
          'lanczos',
          'triangular',
          'gaussian',
          'barlett-hann',
          'blackman',
          'nuttall',
          'blackman-harris',
          'blackman-nuttall',
          # 'flat-top',
          # 'kaiser',
          # 'parzen',
          # 'projection',
          # 'sinogram',
          # 'rprojection',
          # 'rsinogram'
      ]

  def __init__(self, device='gpu', backend='astra', filter_=None):
    super().__init__(device, backend)
    self._filter = filter_

  @property
  def filter(self):
    return self._filter
