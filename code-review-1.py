import unittest
import sys
import nose
from nose.core import TextTestRunner
from nose.result import TextTestResult
from cStringIO import StringIO
from unittest.runner import _WritelnDecorator


class Tests(unittest.TestCase):

    def test_1(self):
        """Test 1"""
        # print 'something'
        self.assertEquals(1, 1)

    def test_2(self):
        """Test 2"""
        self.assertEquals(1, 1)

    def test_3(self):
        """Test 3"""
        self.assertEquals(1, 1)

    def test_4(self):
        """Test 4"""
        self.assertEquals(1, 1)

    def test_5(self):
        """Test 5"""
        # print 'something'
        raise AssertionError("error")
        self.assertEquals(1, 1)

if __name__ == '__main__':

    class MyTextTestResult(TextTestResult):

        def addError(self, test, err):
            current_stream = self.stream
            self.stream = _WritelnDecorator(sys.stderr)
            TextTestResult.addError(self, test, err)
            self.stream = current_stream

        def addFailure(self, test, err):
            current_stream = self.stream
            self.stream = _WritelnDecorator(sys.stderr)
            TextTestResult.addFailure(self, test, err)
            self.stream = current_stream     

        def printErrors(self):
            current_stream = self.stream
            self.stream = _WritelnDecorator(sys.stderr)
            TextTestResult.printErrors(self)
            self.stream = current_stream


    class MyTextTestRunner(TextTestRunner):
        def __init__(self):
            TextTestRunner.__init__(self, stream=_WritelnDecorator(sys.stdout), verbosity=2)

        def _makeResult(self):
            return MyTextTestResult(self.stream,
                                    self.descriptions,
                                    self.verbosity,
                                    self.config)

    nose.run(testRunner=MyTextTestRunner(), argv=['nosetests', __file__, '-s', '-v'])
    # nose.run(argv=['nosetests', __file__, '-s', '-v', '--with-xunit', '--with-id'])
