import exampleclient
import exampleclient.example

from exampleclient.tests import base

class TestExample(base.BaseTestCase):

    def setUp(self):
        super(TestExample, self).setUp()
        print("Setup TestExample")

    def test_hello(self):
        exampleclient.example.hello()

    def test_goodbye(self):
        exampleclient.example.goodbye()
