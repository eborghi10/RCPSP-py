# TODO List:

- Use Random Keys

- Implement Lévy Flights like Yang on their example of Cuckoo Search

- Use rk2al(). Some functions, like for generation of new solutions, should be modified.

- Test two generation methods independently. Later, test both together. If it's not better, left one.

- The RUR method is bullshit. Use another criteria to determine which solution is better.

- To end the algorithm, look when the best cost does not improve in 200 iterations (it could be a bigger or smaller number, depending on the problem). Analize for particular cases if that number can be setted automatically

- The MPE measures dispersion. Another unuseful parameter. In some cases, when the cost doesn't change in 200 iterations, the simulation can be finalized.

- Implement a comparison between the dispersion with the upper bound as a measurement parameter.

- Compare with a Genetic Algorithm.

- Improve performance using Numpy.

- Dynamic allocation of variables

- Merge functions into one library file (of load files)