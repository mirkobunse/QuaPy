import unittest
from sklearn.linear_model import LogisticRegression

from quapy.method import AGGREGATIVE_METHODS, BINARY_METHODS
from quapy.method.aggregative import *
import inspect


class HierarchyTestCase(unittest.TestCase):

    def test_aggregative(self):
        lr = LogisticRegression()
        for m in AGGREGATIVE_METHODS:
            self.assertEqual(isinstance(m(lr), AggregativeQuantifier), True)

    def test_inspect_aggregative(self):

        import quapy.method.aggregative as aggregative

        members = inspect.getmembers(aggregative)
        classes = set([cls for name, cls in members if inspect.isclass(cls)])
        quantifiers = [cls for cls in classes if issubclass(cls, BaseQuantifier)]
        quantifiers = [cls for cls in quantifiers if issubclass(cls, AggregativeQuantifier)]
        quantifiers = [cls for cls in quantifiers if not inspect.isabstract(cls) ]

        for cls in quantifiers:
            self.assertIn(cls, AGGREGATIVE_METHODS)

    def test_binary(self):
        lr = LogisticRegression()
        for m in BINARY_METHODS:
            self.assertEqual(isinstance(m(lr), BinaryQuantifier), True)

    def test_inspect_binary(self):

        import quapy.method.base as base
        import quapy.method.aggregative as aggregative
        import quapy.method.non_aggregative as non_aggregative
        import quapy.method.meta as meta

        members = inspect.getmembers(base)
        members+= inspect.getmembers(aggregative)
        members += inspect.getmembers(non_aggregative)
        members += inspect.getmembers(meta)
        classes = set([cls for name, cls in members if inspect.isclass(cls)])
        quantifiers = [cls for cls in classes if issubclass(cls, BaseQuantifier)]
        quantifiers = [cls for cls in quantifiers if issubclass(cls, BinaryQuantifier)]
        quantifiers = [cls for cls in quantifiers if not inspect.isabstract(cls) ]

        for cls in quantifiers:
            self.assertIn(cls, BINARY_METHODS)

    def test_probabilistic(self):
        lr = LogisticRegression()
        for m in [CC(lr), ACC(lr)]:
            self.assertEqual(isinstance(m, AggregativeCrispQuantifier), True)
            self.assertEqual(isinstance(m, AggregativeSoftQuantifier), False)
        for m in [PCC(lr), PACC(lr)]:
            self.assertEqual(isinstance(m, AggregativeCrispQuantifier), False)
            self.assertEqual(isinstance(m, AggregativeSoftQuantifier), True)


if __name__ == '__main__':
    unittest.main()

