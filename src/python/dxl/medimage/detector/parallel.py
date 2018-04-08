from .base import Detector2D
import numpy as np


class Parallel2D(Detector2D):
  @classmethod
  def create_sensors(cls, nb_sensors, sensor_width=1.0):
    """
    Helper function to create sensors, locating at center of each periods.
    """
    return np.arange(nb_sensors) * sensor_width - \
      ((nb_sensors / 2 - 0.5) * sensor_width)

  @classmethod
  def create_views(cls, nb_views, view_range=None):
    if view_range is None:
      view_range = [0.0, np.pi]
    return np.linspace(view_range[0], view_range[1], nb_views, endpoint=False)

  def __init__(self, sensors=None, views=None):
    """
    """
    self._sensors = np.array(sensors)
    self._views = np.array(views)
    if self._sensors.ndim != 1:
      raise ValueError(
          'Sensor sensors spec is required to be one dimension, got {}.'.
          format(self._sensors.ndim))
    if self._views.ndim != 1:
      raise ValueError(
          'Sensor views spec is required to be one dimension, got {}.'.format(
              self._views.ndim))

  @property
  def nb_sensors(self):
    return len(self._sensors)

  @property
  def sensor_width(self):
    return np.mean(self._sensors[1:] - self._sensors[:-1])

  @property
  def sensors(self):
    return self._sensors

  @property
  def nb_views(self):
    return len(self._views)

  @property
  def views(self):
    return self._views

  def check_data_capability(self, data):
    if self.nb_views != data.shape[0] or self.nb_sensors != data.shape[1]:
      msg = "Shape of sinogram {} is not consisted with detector: nb_sensors: {}, nb_views: {}."
      raise ValueError(msg.format(data.shape, self.nb_sensors, self.nb_views))
