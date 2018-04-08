class Detector:
  def check_data_capability(self, data):
    """
    Check if data shape, content, e.t.c.
    Returns: 
      None
    Raises:
      ValueError, TypeError
    """
    pass


class Detector3D(Detector):
  ndim = 3


class Detector2D(Detector):
  ndim = 2
