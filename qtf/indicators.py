"""Mock indicators module"""

import numpy as np

class KDJ:
    @staticmethod
    def kdj(*args, **kwargs):
        n = len(args[0]) if args else 100
        return np.zeros(n), np.zeros(n), np.zeros(n)

class MACD:
    @staticmethod
    def macd(*args, **kwargs):
        n = len(args[0]) if args else 100
        return np.zeros(n), np.zeros(n), np.zeros(n)