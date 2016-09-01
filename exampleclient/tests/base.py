from oslotest import base
import testscenarios

def cleanup_fun():
    print("cleanup!")

class BaseTestCase(testscenarios.WithScenarios, base.BaseTestCase):
    """Test base class."""

    def setUp(self):
        super(BaseTestCase, self).setUp()
        self.addCleanup(cleanup_fun)
