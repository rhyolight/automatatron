import automatatron
import time

print "EXAMPLE 1:"
print "Print the first 10 rows of all possible automaton:"
for rule in range(1,257):
  automaton = automatatron.Engine(rule)
  automaton.run(10)
  print automaton

print "EXAMPLE 2:"
print "Print the first 50 rows of Rule 30"
automaton = automatatron.Engine(30)
automaton.run(50)
print automaton

print "EXAMPLE 3:"
print "Run the next 10 iterations, and pass results into specified handler."
def row_handler(row, _):
  print row
automaton.run(10, handler=row_handler)

print "EXAMPLE 4:"
print "Stream the middle 101 columns to stdout"
automaton = automatatron.Engine(30)
def stream_handler(row, _):
  print automatatron.default_string_formatter(row)
  time.sleep(0.05)
automaton.stream(stream_handler, width=101)
