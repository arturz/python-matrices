from unittest import mock
from unittest.mock import patch
import io


def make_list(data):
    return list(map(str.strip, data.strip().splitlines()))


def mock_input(texts):

    def decorator(function):

        def wrapper(*args, **kwargs):
            texts_copy = texts[:]
            original_input = mock.builtins.input
            mock.builtins.input = lambda: texts_copy.pop(0)
            result = function(*args, **kwargs)
            assert len(texts_copy) == 0
            mock.builtins.input = original_input
            return result
        return wrapper
    return decorator


def assert_output(texts):

    def decorator(function):

        @patch('sys.stdout', new_callable=io.StringIO)
        def wrapper(self, mock_stdout, *args, **kwargs):
            result = function(self, *args, **kwargs)

            mocked_lines = mock_stdout.getvalue().strip().splitlines()
            assert len(mocked_lines) == len(texts), "Different numbers of lines printed than given"
            for i, name in enumerate(mocked_lines):
                assert texts[i] == name

            return result
        return wrapper
    return decorator
