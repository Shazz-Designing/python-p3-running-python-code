#!/usr/bin/env python3

from os import path
import runpy
from io import StringIO
from unittest.mock import patch

class TestAppPy:
    '''
    app.py
    '''
    def test_app_py_exists(self):
        '''
        exists in lib directory
        '''
        assert(path.exists("lib/app.py"))

    def test_app_py_runs(self):
        '''
        is executable
        '''
        runpy.run_path("lib/app.py")

    def test_prints_hello_world(item):
        '''
        prints "Hello World! Pass this test, please."
        '''
        with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            try:
                runpy.run_path("lib/app.py")
            except SystemExit:
                pass
            except Exception as e:
                print(f"Caught an exception: {e}")
                raise

            captured_output = mock_stdout.getvalue()
            print("Captured Output:")
            print(captured_output)

            assert "Hello World! Pass this test, please." in captured_output

            if "Hello World! Pass this test, please." not in captured_output:
                print("Expected output not found!")

            if "ERROR" in captured_output.upper():
                print("Error detected in the output!")


