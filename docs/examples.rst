Examples
========
The following example demonstrates how to initialize the status handler for the
base application status page.

.. code:: python

    import tornado.ioloop
    import tornado.web
    from sprockets.handlers import status


    application = tornado.web.Application([
        ('/status', status.StatusHandler),
    ])

    if __name__ == '__main__':

        # Set the application name to the local package
        status.set_application('mypackage')

        application.listen(8888)
        tornado.ioloop.IOLoop.current().start()

You can change the status by setting the ``status`` attribute on
``RequestHandler.application``, but note this does it for the single
running process and should be coordinated across all backends using an
external synchronization mechanism.

The following example uses Consul to determine if a request is in maintenance
mode.

.. code:: python

    import json
    import socket

    from tornado import gen
    from tornado import httpclient
    from sprockets.handlers import status

    class ConsulStatusHandler(status.StatusHandler):

        HEALTH_URL_FORMAT = 'http://localhost:8500/v1/health/node/{0}

        @gen.coroutine
        def prepare(self):
            result = yield self._maintenance_enabled()
            if result:
                setattr(self.application, 'status', status.MAINTENANCE)
            else:
                setattr(self.application, 'status', status.OK)

        @gen.coroutine
        def _maintenance_enabled(self)
            client = httpclient.AsyncHTTPClient()
            url = self.HEALTH_URL_FORMAT.format(socket.gethostname())
            result = yield client.fetch()
            return self._in_maintenance(json.loads(result.body))

        @staticmethod
        def _in_maintenance(self, checks):
            for check in checks:
                 if check['CheckID'] == '_node_maintenance':
                    return check['Status'] == 'critical'
            return False
