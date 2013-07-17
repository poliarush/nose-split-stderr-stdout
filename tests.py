import unittest
import sys
import nose
from nose.core import TextTestRunner
from nose.result import TextTestResult
from cStringIO import StringIO


class Tests(unittest.TestCase):

    def test_1(self):
        """Test 1"""
        print 'something'
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
        print 'something'
        raise AssertionError("error")
        self.assertEquals(1, 1)

if __name__ == '__main__':
    class MyTextTestResult(TextTestResult):

        def addError(self, test, err):
            print >> sys.stderr, "%r ... error\n\t%r" % (test, err)

        def addFailure(self, test, err):
            print >> sys.stderr, "%r ... failure\n\t%r" % (test, err)

        def addSuccess(self, test):
            print >> sys.stdout, "%r ... ok" % test

    class MyTextTestRunner(TextTestRunner):

        def __init__(self):
            TextTestRunner.__init__(self, stream=StringIO())

        def _makeResult(self):
            return MyTextTestResult(self.stream,
                                    self.descriptions,
                                    self.verbosity,
                                    self.config)

    nose.main(testRunner=MyTextTestRunner())
