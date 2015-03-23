#!/usr/bin/env python
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

import sys
import time

from optparse import OptionParser

import automatatron

DEFAULT_RULE = 30

parser = OptionParser(
  usage="%prog [options]\n\nElementary Cellular Automata."
)

parser.add_option(
  "-r",
  "--rule_number",
  dest="rule_number",
  default=DEFAULT_RULE,
  help="Which elementary cellular automaton rule to run.")


def run(rule_number):
  automaton = automatatron.Engine(rule_number)
  def stream_handler(row, _):
    print automatatron.default_string_formatter(row)
    time.sleep(0.05)
  automaton.run(handler=stream_handler, width=101)


if __name__ == "__main__":
  (options, arguments) = parser.parse_args(sys.argv[1:])
  rule_number = int(options.rule_number)
  run(rule_number)