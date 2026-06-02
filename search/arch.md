## Outline

## Task Env

(search applies to atomic states. Factored and structured states requie far more complex method to achieve effective goal)
Input:
-> problem (state space)
-> Initial state
-> Goal state
-> Action domain(All possible actions)
-> Transition model (change of state due to an action)

Output:
path from initial to goal/ just the goal. Or failure.

## Data structures
-> Node: represents a state
    It contains some properties to keep track of it
    ----> state, parent, action, path-cost

-> Queue: represents the Frontier(fringe)
    contains
    -----> push, pop, front, is_empty

### Best First Search
