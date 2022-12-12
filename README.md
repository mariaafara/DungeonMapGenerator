# DungeonMapGenerator

This project goal is to create a map generator that can generate a maze with a starting point, an ending point and a
treasure point. Such that, there should be a path that exists between the treasure point and the starting point; and the
starting point and the endpoint.

The map generator is made by using Q-learning to learn a QTable that must then be used to forge a path connecting the
three randomly produced places (the starting, finishing, and treasure point).

# Reinforcement Learning: Q learning

The environment for this problem is a 2D board.

An agent (the learner and decision maker) is placed somewhere in the maze. This somewhere would be the random generated
starting point. The agents' goal is to learn a path between the starting point and a treasure (located randomly in the
maze) i.e. crave a path to reach the treasure, and to also learn a path to reach the end point (randomly generated as
well) as quickly as possible.

To learn the paths, the agent moves through the maze in a succession of steps. For every step the agent must decide
which action to take. The options are move left, right, up or down.

For this purpose the agent is trained; it learns/fills a QTable which tells what is the best next move to make (Explore
or Exploit). With every step the agent incurs nothing or/and - when finally reaching the end - a reward.
