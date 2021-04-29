import unittest

class TestCase:
    def __init__(self, name):
        self.name = name
        # self.wasRun = None
    def setUp(self):
        pass
    def tearDown(self):
        pass
    def run(self):
        self.setUp()
        method = getattr(self, self.name)
        method()
        self.tearDown()
        # self.log = self.log + "tearDown"

class WasRun(TestCase):
    def setUp(self):
        self.log = "setUp "
        # self.wasRun = None
        # self.wasSetUp = 1
    def testMethod(self):
        self.log = self.log + "testMethod "
        # pass
        # self.wasRun = 1
    def tearDown(self):
        self.log = self.log + "tearDown "
        # pass
        # self.wasRun = 1
    # def __init__(self, name):
        # pass
        # self.wasRun = None
        # self.name = name
        # super().__init__(name)
    # def run(self):
        # self.testMethod()
        # method = getattr(self, self.name)
        # method()

class TestCaseTest(TestCase):
    def testTemplateMethod(self):
        test = WasRun("testMethod")
        test.run()
        assert("setUp testMethod tearDown " == test.log)
        # self.test.run()
        # assert("setUp testMethod" == self.test.log)
        # assert("setUp testMethod" == test.log)
    # def setUp(self):
        # self.test = WasRun("testMethod")
    # def testRunning(self):
        # test = WasRun("testMethod")
        # assert(not test.wasRun)
        # test.run()
        # assert(test.wasRun)
        # self.test.run()
        # assert(self.test.wasRun)
    # def testSetUp(self):
        # test = WasRun("testMethod")
        # test.run()
        # assert(test.wasSetUp)
        # self.test.run()
        # assert("setUp" == self.test.log)
        # assert("setUp testMethod" == self.test.log)

TestCaseTest("testTemplateMethod").run()
# TestCaseTest("testRunning").run()
# TestCaseTest("testSetUp").run()

# test = WasRun("testMethod")
# print(test.wasRun)
# test.run()
# print(test.wasRun)
