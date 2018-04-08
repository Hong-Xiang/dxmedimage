import unittest
import numpy as np
from dxl.medimage.detector.parallel import Parallel2D


class TestParallel2D(unittest.TestCase):
  def test_sensors(self):
    sensors = Parallel2D.create_sensors(5, 2.0)
    np.testing.assert_array_equal(sensors, [-4., -2., 0., 2., 4.])
    sensors = Parallel2D.create_sensors(5)
    np.testing.assert_array_equal(sensors, [-2., -1., 0., 1., 2.])

  def test_views(self):
    views = Parallel2D.create_views(10)
    np.testing.assert_almost_equal(views, [
        0., 0.31415927, 0.62831853, 0.9424778, 1.25663706, 1.57079633,
        1.88495559, 2.19911486, 2.51327412, 2.82743339
    ])
