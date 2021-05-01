import unittest

class TestResult:
    def __init__(self):
        self.runCount = 0
        self.errorCount = 0
        # self.wasRun = None
    def testStarted(self):
        self.runCount = self.runCount + 1
    def testFailed(self):
        self.errorCount = self.errorCount + 1
    def summary(self):
        return "%d run, %d failed" % (self.runCount, self.errorCount)
        # return "1 run, 0 failed"

class TestCase:
    def __init__(self, name):
        self.name = name
        # self.wasRun = None
    def setUp(self):
        pass
    def tearDown(self):
        pass
    def run(self):
        result = TestResult()
        result.testStarted()
        self.setUp()
        try:
            method = getattr(self, self.name)
            method()
        except:
            result.testFailed()
        self.tearDown()
        return result
        # return TestResult()
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
    def testBrokenMethod(self):
        raise Exception("ERROR!!!")
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
    def testResult(self):
        test = WasRun("testMethod")
        result = test.run()
        assert("1 run, 0 failed" == result.summary())
    def testFailedResult(self):
        test = WasRun("testBrokenMethod")
        result = test.run()
        assert("1 run, 1 failed" == result.summary())
    def testFailedResultFormatting(self):
        result = TestResult()
        result.testStarted()
        result.testFailed()
        assert("1 run, 1 failed" == result.summary())

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

print(TestCaseTest("testTemplateMethod").run().summary())
print(TestCaseTest("testResult").run())
print(TestCaseTest("testFailedResult").run())
print(TestCaseTest("testFailedResultFormatting").run())

# TestCaseTest("testTemplateMethod").run()
# TestCaseTest("testResult").run()
# TestCaseTest("testFailedResult").run()
# TestCaseTest("testFailedResultFormatting").run()

# TestCaseTest("testRunning").run()
# TestCaseTest("testSetUp").run()

# test = WasRun("testMethod")
# print(test.wasRun)
# test.run()
# print(test.wasRun)
