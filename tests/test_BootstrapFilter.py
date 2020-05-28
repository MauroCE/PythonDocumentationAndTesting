import unittest
from BootstrapFilter.BootstrapFilter import BootstrapFilter
import numpy as np


class MyTestCase(unittest.TestCase):
    """Test for Bootstrap Filter."""
    def test_initial_sampler(self):
        """Simply tests the type of `initial_sampler` output."""
        model = BootstrapFilter(lambda n: np.random.normal(),
                                lambda: np.random.normal(),
                                lambda: np.random.normal(),
                                1,
                                np.array([[1.0], [2.0]]))
        self.assertEqual(type(model.initial_sampler()), type((lambda x: np.random.normal())(1)))

    def test_string(self):
        """Test the string representation."""
        model = BootstrapFilter(lambda n: np.random.normal(),
                                lambda: np.random.normal(),
                                lambda: np.random.normal(),
                                1,
                                np.array([[1.0], [2.0]]))
        self.assertEqual(model.__str__(), "Object of Class BootstrapFilter implementing a basic SMC algorithm.")


if __name__ == '__main__':
    unittest.main()
