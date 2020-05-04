import unittest


class TestRegistration(unittest.TestCase):
    """Check registration incompatibilities.

    ref https://github.com/stack-of-tasks/eigenpy/issues/83
    ref https://gitlab.laas.fr/loco-3d/curves/-/issues/6
    """
    def test_pinocchio_then_curves(self):
        import pinocchio
        import curves
        self.assertTrue(hasattr(pinocchio, 'Quaternion'))
        self.assertTrue(hasattr(curves, 'Quaternion'))

    def test_curves_then_pinocchio(self):
        import curves
        import pinocchio
        self.assertTrue(hasattr(pinocchio, 'Quaternion'))
        self.assertTrue(hasattr(curves, 'Quaternion'))


if __name__ == '__main__':
    unittest.main()
