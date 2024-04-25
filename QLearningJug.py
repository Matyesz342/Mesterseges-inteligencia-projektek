import random

class QLearningJug:
    def __init__(self, M1, M2, M3, target, learning_rate=0.1, discount_factor=0.9, exploration_prob=0.3):
        self.M1 = M1
        self.M2 = M2
        self.M3 = M3
        self.target = target
        self.learning_rate = learning_rate
        self.discount_factor = discount_factor
        self.exploration_prob = exploration_prob
        self.q_table = {}

    def get_q_value(self, state, action):
        return self.q_table.get((state, action), 0.0)

    def choose_action(self, state):
        if random.uniform(0, 1) < self.exploration_prob:
            return random.choice(self.get_possible_actions(state))
        else:
            return max(self.get_possible_actions(state), key=lambda a: self.get_q_value(state, a))

    def get_possible_actions(self, state):
        possible_actions = []
        for i in range(3):
            for j in range(3):
                if i != j and state[i] != 0 and state[j] != getattr(self, f'M{j+1}'):
                    possible_actions.append((i, j))
        #print(possible_actions)
        return possible_actions

    def update_q_value(self, state, action, reward, next_state):
        best_future_q = max(self.get_q_value(next_state, a) for a in self.get_possible_actions(next_state))
        current_q = self.get_q_value(state, action)
        new_q = current_q + self.learning_rate * (reward + self.discount_factor * best_future_q - current_q)
        self.q_table[(state, action)] = new_q

    def train(self, episodes):
        for episode in range(episodes):
            state = (0, 0, self.M3)
            total_reward = 0

            while state[1] != self.target and state[2] != self.target:
                action = self.choose_action(state)
                #print(action)
                next_state = self.perform_action(state, action)
                reward = -1 if next_state[1] != self.target or next_state[2] != self.target != self.target else 0  # -1 reward for each step, 0 at goal state
                self.update_q_value(state, action, reward, next_state)
                #print(next_state)
                state = next_state
                total_reward += reward

            print(f"Episode {episode + 1}, Total Reward: {total_reward}")

    def perform_action(self, state, action):
        i, j = action
        T = min([state[i], getattr(self, f'M{j+1}') - state[j]])
        new_state = list(state)
        new_state[i] -= T
        new_state[j] += T
        return tuple(new_state)

if __name__ == "__main__":
    jug_q_learning = QLearningJug(3, 5, 8, 4)
    jug_q_learning.train(100)

    # Test the learned policy
    state = (0, 0, 8)
    while state[1] != jug_q_learning.target and state[2] != jug_q_learning.target:
        action = jug_q_learning.choose_action(state)
        state = jug_q_learning.perform_action(state, action)
        print(f"Current state: {state}")
