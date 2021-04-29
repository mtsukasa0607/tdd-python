import unittest

class TestCase:
    # pass
    def __init__(self, name):
        # self.wasRun = None
        self.name = name
    def setUp(self):
        pass
    def run(self):
        self.setUp()
        method = getattr(self, self.name)
        method()

class WasRun(TestCase):
    # pass
    # def __init__(self, name):
        # pass
        # self.wasRun = None
        # self.name = name
        # super().__init__(name)
    def setUp(self):
        self.wasRun = None
        self.wasSetUp = 1
    # def run(self):
        # self.testMethod()
        # method = getattr(self, self.name)
        # method()
    def testMethod(self):
        # pass
        self.wasRun = 1

class TestCaseTest(TestCase):
    def setUp(self):
        self.test = WasRun("testMethod")
    def testRunning(self):
        # test = WasRun("testMethod")
        # assert(not test.wasRun)
        # test.run()
        # assert(test.wasRun)
        self.test.run()
        assert(self.test.wasRun)
    def testSetUp(self):
        # test = WasRun("testMethod")
        # test.run()
        # assert(test.wasSetUp)
        self.test.run()
        assert(self.test.wasSetUp)

TestCaseTest("testRunning").run()
TestCaseTest("testSetUp").run()

# test = WasRun("testMethod")
# print(test.wasRun)
# test.run()
# print(test.wasRun)
