import unittest
import puzzle


class TestPuzzle(unittest.TestCase):

    def test_simple(self):
        input_set_ok = ('a{{ a}} p{}--{}0',
                    '{{{{{{{{{{{{}}}}}}}}}}}}'
                    '{{}}{{}}',
                    '')

        input_set_fail = ('a{',
                    '{{{ ',
                    'aa{bb{ccc}',
                    '{{}}}')

        for s in input_set_ok:
            self.assertTrue(puzzle.check_brackets_simple(s), 'Test simpple: Input ' + s + ' failed.')
            self.assertTrue(puzzle.check_brackets_optimized(s), 'Test optimized: Input ' + s + ' failed.')

        for s in input_set_fail:
            self.assertFalse(puzzle.check_brackets_simple(s), 'Test simple: Input ' + s + ' failed.')
            self.assertFalse(puzzle.check_brackets_optimized(s), 'Test Optimized: Input ' + s + ' failed.')


    def test_complex(self):
        input_set_ok = ('a{{ a}} p{}--{}0',
                    '{{}}{{}}',
                    '',
                    '{[]}',
                    '[ { { } } ]',
                    '[{}]',
                    '')

        input_set_fail = ('a{',
                    '{{{{{{{{{{{{}}}}}}}}}}}}}',
                    'aa{bb{ccc}',
                    '{{}}}',
                    'a{',
                    '[]{',
                    '[{]}')

        for s in input_set_ok:
            self.assertTrue(puzzle.check_brackets_complex(s), 'Input ' + s + ' failed.')

        for s in input_set_fail:
            self.assertFalse(puzzle.check_brackets_complex(s), 'Input ' + s + ' failed.')




if __name__ == '__main__':
    unittest.main()
