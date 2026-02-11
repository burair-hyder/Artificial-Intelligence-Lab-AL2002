# question 06:
import random

class Environment:
    def __init__(self):
        self.actions = ['Play', 'Rest']
        self.rewards = {'Play': 5, 'Rest': 1}

    def get_reward(self, action):
        return self.rewards[action]

class Agent:
    def __init__(self, environment):
        self.env = environment
        self.q_table = {}
        for action in self.env.actions:
            self.q_table[action] = 0
        self.alpha = 0.5

    def choose_action(self):
        return random.choice(self.env.actions)

    def update_q(self, action, reward):
        self.q_table[action] = self.q_table[action] + self.alpha * (reward - self.q_table[action])

def run_agent(iterations):
    env = Environment()
    agent = Agent(env)
    for step in range(1, iterations + 1):
        action = agent.choose_action()
        reward = env.get_reward(action)
        print("Step", step, ": Action", action, "Reward", reward)
        agent.update_q(action, reward)
        if step % 5 == 0:
            print("Q-table Updated")
            print("Q-values:", agent.q_table)

run_agent(10)
