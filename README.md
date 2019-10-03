# softeng19-a4

1. In our UML diagram, should Task be a class or should it simply be a string?  Why or why not?
        In the current UML design, Tasks should simply be a string. It has no methods or member variables in its current design, so there is no point in making it into anything more than a string. In addition, this allows us to build a basic version of the project that we can modify and add features to later.
1. What future enhancements might you add to this project next?  Does the answer to this question change your answer to the first question?
        We can add developers, detailed descriptions of tasks, and a way to track progress on a task.
        Adding these features would necessitate turning Tasks into a class, because then it would have member variables for each of these things, and it would most likely need ways of interacting with those member variables.
