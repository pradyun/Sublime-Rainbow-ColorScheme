"""Tests for compiler for theme definitions
"""

import yaml
import unittest

import builder


# ------------ Data Driven Testing ------------
def load_yaml_data(file_name):
    with open(file_name) as f:
        return yaml.load(f)


def data_driven_test_case(test_data):
    if not test_data:
        raise Exception("No test data!")
    elif type(test_data) not in (list, tuple):
        raise Exception("Expected a list or tuple.")

    def make_test_function(test):
        name = "test_" + test["name"]

        def func(self):
            self.template(test)
        func.__name__ = name

        return name, func

    def decorator(clazz):
        for test in test_data:
            name, func = make_test_function(test)
            assert not hasattr(clazz, 'test_{0}'.format(test["name"]))

            setattr(clazz, name, func)

        return clazz

    return decorator


# ------------ Tests ------------
@data_driven_test_case(load_yaml_data("test-conversion.yaml"))
class TestConversion(unittest.TestCase):
    longMessage = True

    def template(self, data):
        input_data = data["input"]
        name = input_data["name"]
        text = input_data["text"]
        uuid = input_data["uuid"]
        author = input_data["author"]

        expected_data = data["output"]

        output = builder.generate_color_scheme(name, text, uuid, author)

        self.assertEqual(output, expected_data, repr(text))

if __name__ == '__main__':
    unittest.main()
