import automatatron

# Print the first 10 rows of all possible automaton:
for rule in range(1,257):
  automaton = automatatron.Engine(rule)
  automaton.run(10)
  print automaton

# Print the first 50 rows of Rule 30
automaton = automatatron.Engine(30)
automaton.run(50)
print automaton


def row_handler(row):
  print row

# Run the next 10 iterations, and pass results into specified handler.
automaton.run(10, handler=row_handler)