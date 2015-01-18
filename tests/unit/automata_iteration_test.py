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


  def test_run_one_iteration(self):
    expected_row = [
      True, True, True
    ]
    automaton = Engine(30)

    last_row = automaton.run(1)

    self.assertListEqual(last_row, expected_row)


  def test_run_two_iterations(self):
    expected_row = [
      True, True, False, False, True
    ]
    automaton = Engine(30)

    last_row = automaton.run(2)

    self.assertListEqual(last_row, expected_row)


  def test_run_three_iterations(self):
    expected_row = [
      True, True, False, True, True, True, True
    ]
    automaton = Engine(30)

    last_row = automaton.run(3)

    self.assertListEqual(last_row, expected_row)


  def test_retrieve_iteration(self):
    expected_first_row = [True]
    expected_second_row = [True, True, True]
    expected_third_row = [
      True, True, False, False, True
    ]
    automaton = Engine(30)
    automaton.run(10)

    first_row = automaton.retrieve(0)
    second_row = automaton.retrieve(1)
    third_row = automaton.retrieve(2)

    self.assertListEqual(first_row, expected_first_row)
    self.assertListEqual(second_row, expected_second_row)
    self.assertListEqual(third_row, expected_third_row)


  def test_user_provided_iteration_handler_one_iteration(self):
    received_rows = []
    def row_handler(row):
      received_rows.append(row)
    automaton = Engine(30)

    automaton.run(1, handler=row_handler)

    self.assertEqual(1, len(received_rows), "Row handler was not called")
    self.assertListEqual([True, True, True], received_rows[0])


  def test_user_provided_iteration_handler_many_iterations(self):
    received_rows = []
    def row_handler(row):
      received_rows.append(row)
    automaton = Engine(30)

    automaton.run(10, handler=row_handler)

    self.assertEqual(
      10, len(received_rows), 
      "Row handler was not called once for each new iteration output"
    )
    self.assertListEqual(
      [True, True, False, False, True, False, False, False, False, True, False, 
       True, True, True, True, False, True, True, False, False, True], 
      received_rows[9]
    )


  def test_tostring(self):
    expected_string = """Rule 30, 10 iterations:
          #          
         ###         
        ##  #        
       ## ####       
      ##  #   #      
     ## #### ###     
    ##  #    #  #    
   ## ####  ######   
  ##  #   ###     #  
 ## #### ##  #   ### 
##  #    # #### ##  #"""
    automaton = Engine(30)
    automaton.run(10)

    output_string = automaton.__str__()

    self.assertEquals(expected_string, output_string)

