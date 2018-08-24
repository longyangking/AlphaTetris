import numpy as np
from ai import AI

class SelfplayEngine:
    def __init__(self,
        state_shape,
        ai,
        verbose=False
    ):
        self.state_shape = state_shape
        self.ai = ai
        self.verbose = verbose

        # Training data
        self.states = list()
        self.boards = list()
        self.scores = list()
        self.actions = list()

    def update_states(self):

    def get_state(self):
        return self.states[-1]

    def play(self, action):

    def start(self, epsilon=0.5):

    
class TrainAI:
    def __init__(self,
        state_shape,
        action_dim,
        ai=None,
        verbose=False
    ):
        self.state_shape = state_shape
        self.action_dim = action_dim

        if ai is not None:
            self.ai = ai
        else:
            self.ai = AI(
                state_shape=state_shape,
                action_dim=action_dim,
                verbose=verbose
            )

        self.losses = list()

    def get_selfplay_data(self, n_round):

    def update_ai(self, dataset):

    def start(self, filename):
        