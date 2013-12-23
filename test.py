from rngs import Tausworth, Universal, Gauss
import time


class TestTausworth:

    @classmethod
    def setup_class(cls):
        cls.rng = Tausworth(int(time.time() / 1000), int(time.time() / 100),
                            int(time.time() / 10))

    def test_output_type(self):
        assert isinstance(self.rng.random(), float)

    def test_multiple_output_equality(self):
        assert self.rng.random() != self.rng.random() != self.rng.random()


class TestUniversal:

    @classmethod
    def setup_class(cls):
        cls.rng = Universal(12, 34, 56, 78)

    def test_output_type(self):
        assert isinstance(self.rng.random(), float)

    def test_multiple_output_equality(self):
        assert self.rng.random() != self.rng.random() != self.rng.random()


class TestGauss:

    @classmethod
    def setup_class(cls):
        cls.rng = Gauss(10, 10)

    def test_output_type(self):
        assert isinstance(self.rng.random(), float)

    def test_multiple_output_equality(self):
        assert self.rng.random() != self.rng.random() != self.rng.random()
