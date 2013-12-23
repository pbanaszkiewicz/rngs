# import random as MersenneTwister
# from random import WichmannHill
# from random import SystemRandom

from random import gauss


class RandomNumberGenerator:
    """Base class for implementing random number generators."""

    def __init__(self):
        raise NotImplementedError

    def random(self):
        raise NotImplementedError


class Tausworth(RandomNumberGenerator):
    def __init__(self, seed1, seed2, seed3):
        assert 0 < seed1 < 2 ** 28
        assert 0 < seed2 < 2 ** 29
        assert 0 < seed3 < 2 ** 31

        b = ((seed1 << 9) - seed1) << 4
        seed1 = (seed1 << 4) - (b >> 28)
        b = ((seed2 << 2) - seed2) << 3
        seed2 = (seed2 << 3) - (b >> 29)
        b = ((seed3 << 6) - seed3) << 1
        seed3 = (seed3 << 1) - (b >> 31)

        self.seed1 = seed1
        self.seed2 = seed2
        self.seed3 = seed3

    def random(self):
        b = ((self.seed1 << 9) - self.seed1) << 4
        self.seed1 = (self.seed1 << 13) - (b >> 19)
        b = ((self.seed2 << 2) - self.seed2) << 3
        self.seed2 = (self.seed2 << 20) - (b >> 12)
        b = ((self.seed3 << 6) - self.seed3) << 1
        self.seed3 = (self.seed3 << 17) - (b >> 15)

        return (self.seed1 - self.seed2 - self.seed3) * 2.3283064365e-10


class Universal(RandomNumberGenerator):
    def __init__(self, seed1, seed2, seed3, seed4):
        assert 1 <= seed1 <= 178
        assert 1 <= seed2 <= 178
        assert 1 <= seed3 <= 178
        assert 0 <= seed4 <= 168
        assert seed1 != seed2 != seed3 != 1

        self.array = []
        self.ip, self.jp = 97, 33
        self.cc = 362436.0 / 16777216.0
        self.cd = 7654321.0 / 16777216.0
        self.cm = 16777213.0 / 16777216.0

        for i in xrange(98):
            s = 0
            t = 0.5

            for j in xrange(1, 25):
                m = (((seed1 * seed2) % 179) * seed3) % 179
                seed1, seed2, seed3 = seed2, seed3, m
                seed4 = (53 * seed4 + 1) % 169
                if ((seed4 * m) % 64 >= 32):
                    s += t
                t *= 0.5

            self.array.append(s)

    def random(self):
        rnd = self.array[self.ip - 1] - self.array[self.jp - 1]

        if (rnd < 0.0):
            rnd += 1

        self.array[self.ip - 1] = rnd

        self.ip -= 1
        if (self.ip == 0):
            self.ip = 97

        self.jp -= 1
        if (self.jp == 0):
            self.jp = 97

        self.cc -= self.cd
        if (self.cc < 0.0):
            self.cc += self.cm

        rnd -= self.cc
        if (rnd < 0.0):
            rnd += 1

        return rnd


class Gauss(RandomNumberGenerator):
    def __init__(self, mu, sigma):
        self.mu = mu
        self.sigma = sigma

    def random(self):
        return gauss(self.mu, self.sigma)
