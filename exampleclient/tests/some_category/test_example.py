import exampleclient

from exampleclient.tests import base

class TestExample(base.BaseTestCase):

    def setUp(self):
        super(TestClients, self).setUp()
        print("Setup TestExample")

    def test_hello(self):
        exampleclient.example.hello()

    def test_goodbye(self):
        exampleclient.example.goodbye()
