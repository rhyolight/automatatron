# The MIT License (MIT)
#
# Copyright (c) 2015 Matthew Taylor
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

import unittest
from automatatron import Engine

class Automata_Iteration_Test(unittest.TestCase):


  def test_automaton_creation_attaches_rule(self):
    expected_rule = [
      [True,  False, False],
      [False, True,  True],
      [False, True,  False],
      [False, False, True],
    ]
    automaton = Engine(30)
    self.assertListEqual(automaton.rule, expected_rule)


  def test_automaton_run_one_iteration(self):
    expected_row = [
      True, True, True
    ]
    automaton = Engine(30)
    last_row = automaton.run(1)
    self.assertListEqual(last_row, expected_row)


  def test_automaton_run_two_iterations(self):
    expected_row = [
      True, True, False, False, True
    ]
    automaton = Engine(30)
    last_row = automaton.run(2)
    self.assertListEqual(last_row, expected_row)


  def test_automaton_run_three_iterations(self):
    expected_row = [
      True, True, False, True, True, True, True
    ]
    automaton = Engine(30)
    last_row = automaton.run(3)
    self.assertListEqual(last_row, expected_row)
