import astra as aa
from ...detector import Parallel2D
from ...image import Image2D
from ...reconstruction.algorithm import FBP


def _get_algorithm_type(algorithm):
  if isinstance(algorithm, FBP):
    if algorithm.device.lower() == 'gpu':
      return 'FBP_CUDA'
    else:
      return 'FBP'
  raise ValueError("Unknown algorithm {}.".format(algorithm))


class ReconstructorParallel2D:
  def __init__(self, detector: Parallel2D, image: Image2D, algorithm: FBP):
    vol_geom = aa.creators.create_vol_geom(image.shape)
    proj_geom = aa.creators.create_proj_geom(
        'parallel', detector.sensor_width(), detector.nb_sensors,
        detector.views())
    self._proj_id = aa.creators.create_projector(detector.model().name,
                                                 proj_geom, vol_geom)
    self._sino_id = aa.data2d.create('-sino', proj_geom)
    self._image_id = aa.data2d.create('-vol', vol_geom)
    alg_cfg = {
        'type': _get_algorithm_type(algorithm),
        'ProjectionDataId': self._sino_id,
        'ReconstructionDataId': self._image_id,
        'FilterType': algorithm.filter
    }
    self._alg_id = aa.algorithm.create(alg_cfg)
    self._detector = detector
    self._image_spec = image
    self._algorithm = algorithm

  def reconstruct(self, sinogram, iterations=1):
    self._detector.check_data_capability(sinogram)
    aa.data2d.store(self._sino_id, sinogram)
    aa.algorithm.run(self._alg_id, iterations)
    result = aa.data2d.get(self._image_id)
    return result

  def clear(self):
    aa.data2d.delete(self._sino_id)
    aa.data2d.delete(self._image_id)
    aa.projector.delete(self._proj_id)
    aa.algorithm.delete(self._alg_id)