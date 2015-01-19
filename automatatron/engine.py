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
import math


def default_string_formatter(row, width=0):
  side_padding = int(math.floor((width - len(row) )/ 2)) * " "
  out = side_padding
  for v in row:
    if v:
      cell = "#"
    else:
      cell  = " "
    out += cell
  out += side_padding
  return out


class Engine(object):

  # I'm sure there's a clever programmatic way to generate these rules, but I'm
  # lazy.
  rules = [
    [True,  True,  True],
    [True,  True,  False],
    [True,  False, True],
    [True,  False, False],
    [False, True,  True],
    [False, True,  False],
    [False, False, True],
    [False, False, False],
  ]

  @classmethod
  def get_rule(cls, number):
    rules_to_apply = [bool(int(i)) for i in list('{0:08b}'.format(number))]
    rules = []
    for i, rule in enumerate(rules_to_apply):
      if rule:
        rules.append(cls.rules[i])
    return rules


  def __init__(self, rule_number):
    self.rule_number = rule_number
    self.rule = self.get_rule(rule_number)
    self.rows = [[True]]


  def step(self):
    next_row = []
    last_row = list(self.rows[-1])
    # Pad the row with two false values on each side. This allows us to more
    # easily match the expected state with the upward row (which is now padded).
    for i in xrange(2):
      last_row.insert(0, False)
      last_row.append(False)

    for index, value in enumerate(last_row):
      # skip first and last values (because of the padding)
      if index == 0 or index == len(last_row) - 1:
        continue
      # Upward state is the three cells above this one.
      upward_state = last_row[index - 1 : index + 2]
      match = upward_state in self.rule
      next_row.append(match)
    self.rows.append(next_row)
    return next_row


  def retrieve(self, number):
    return self.rows[number]


  def run(self, iterations, handler=None):
    last_row = None
    for i in xrange(iterations):
      last_row = self.step()
      if handler:
        handler(last_row, i)
    return last_row


  def stream(self, handler, width=None):
    while (True):
      row = self.step()
      if width is not None:
        # Pad the row till it reaches the specified width
        if width > len(row):
          padding = int((width - len(row)) / 2)
          for i in xrange(0, padding):
            row.insert(0, False)
            row.append(False)
        # Trim the row to the center rows
        half = int(math.floor(width/2))
        midpoint = int(math.floor(len(row)/2))
        row = row[midpoint - half : midpoint + half + 1]
      handler(row, len(self.rows)-1)


  def __str__(self, formatter=default_string_formatter):
    out = "Rule %i, %i iterations:" % (self.rule_number, len(self.rows) - 1)
    width = len(self.rows[-1])
    for row in self.rows:
      out = "%s\n%s" % (out, formatter(row, width))
    return out
