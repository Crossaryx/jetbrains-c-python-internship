import unittest
import sys
import argparse
from tool.tool import SharedLibPath, get_native_functions

# Generic tool test
# Shared library object as well as expected native functions
# are passed as arguments
parser = argparse.ArgumentParser()
parser.add_argument("--lib", type=SharedLibPath)
parser.add_argument("--expected_functions", type=str)
args, unknown = parser.parse_known_args() 

class TestTool(unittest.TestCase):
    def test(self) -> None:
        result = get_native_functions(args.lib)
        expected_functions = args.expected_functions.split(",")
        expected_functions.sort()
        self.assertEqual(result,expected_functions)
if __name__ == "__main__":
    unittest.main(argv=[sys.argv[0]] + unknown)
