"""Main."""

from q_learner import QLearner

if __name__ == '__main__':
    q_learner = QLearner(4)
    q_learner.learn()
    qtable = q_learner.q_table

    dir_to_go = q_learner.get_dir_to_go()

    print("*" * 10)
    print(dir_to_go)
