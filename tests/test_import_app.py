import importlib, sys, types, unittest


class TestImportApp(unittest.TestCase):
    def test_import_does_not_run_auto_push(self):
        # Insert a dummy `auto_push` module before importing `app` so we can
        # detect whether `auto_push.auto_push()` is invoked during import.
        dummy = types.ModuleType('auto_push')
        dummy.called = False

        def auto_push_fn():
            # If this is called during import, it will set the flag to True.
            dummy.called = True

        dummy.auto_push = auto_push_fn
        sys.modules['auto_push'] = dummy

        # Ensure `app` is not already imported in this process
        if 'app' in sys.modules:
            del sys.modules['app']

        # Import the app module; auto_push.auto_push() should NOT be called.
        importlib.import_module('app')

        # Clean up inserted dummy module
        if 'app' in sys.modules:
            del sys.modules['app']
        if 'auto_push' in sys.modules:
            del sys.modules['auto_push']

        self.assertFalse(dummy.called, "auto_push.auto_push() was called during import of app")


if __name__ == '__main__':
    unittest.main()
