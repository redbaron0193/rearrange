#!/usr/bin/env python3

from rearrange_name import rearrange_name
import unittest

class TestRearrange(unittest.TestCase):
    def test_basic(self):
        testcase = "Schulberg, Jason"
        expected = "Jason Schulberg"
        self.assertEqual(rearrange_name(testcase), expected)

    def test_empty(self):
        TestCase = ""
        expected = ""
        self.assertEqual(rearrange_name(TestCase), expected)

    def test_double_name(self):
        testcase = "Hopper, Grace M."
        expected = "Grace M. Hopper"
        self.assertEqual(rearrange_name(testcase), expected)

    def test_one_name(self):
        testcase = "James"
        expected = "James"
        self.assertEqual(rearrange_name(testcase), expected)

unittest.main()
