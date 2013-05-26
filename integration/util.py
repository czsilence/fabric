from fabric.api import env


class Integration(object):
    def setup(self):
        if not env.host_string: # Allow runtime selection
            env.host_string = "127.0.0.1"

    def teardown(self):
        # Just so subclasses can super() us w/o fear. Meh.
        pass
