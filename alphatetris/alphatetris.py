'''
Main process for AlphaMineSweeper
'''
import numpy as np 
import argparse

__version__ = "0.0.1"
__author__ = "Yang Long"
__info__ = "Play Tetris Game with AI"

__default_board_shape__ = 15, 40
__default_state_shape__ = *__default_board_shape__, 1
__default_action_dim__ = 5
__filename__ = 'model.h5'

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__info__)
    parser.add_argument("--retrain", action='store_true', default=False, help="Re-Train AI")
    parser.add_argument("--train",  action='store_true', default=False, help="Train AI")
    parser.add_argument("--verbose", action='store_true', default=False, help="Verbose")
    parser.add_argument("--play", action='store_true', default=False, help="Play game")
    parser.add_argument("--playai", action='store_true', default=False, help="Play game with AI")
    parser.add_argument("--playnaiveai", action='store_true', default=False, help="Play game with naive AI")

    args = parser.parse_args()
    verbose = args.verbose

    if args.train:
        if verbose:
            print("Contiune to train AI with state shape: {0}".format(__default_state_shape__))

        from train import TrainAI
        from ai import AI

        ai = AI(
            state_shape=__default_state_shape__,
            action_dim=__default_action_dim__,
            verbose=verbose
        )

        if verbose:
            print("Loading AI model from file: [{0}] ... ".format(__filename__),end="")
        ai.load_nnet(__filename__)
        if verbose:
            print("OK!")

        trainai = TrainAI(
            state_shape=__default_state_shape__,
            ai=ai,
            verbose=verbose
        )
        trainai.start(__filename__)

        if verbose:
            print("End of training and the latest model is saved as file [{0}]".format(__filename__))
        
    if args.retrain:
        if verbose:
            print("Start to re-train AI with state shape: {0}".format(__default_state_shape__))

        from train import TrainAI

        trainai = TrainAI(
            state_shape=__default_state_shape__,
            verbose=verbose
        )
        trainai.start(__filename__)

        if verbose:
            print("End of re-train and the model is saved as file [{0}]".format(__filename__))

    if args.playai:
        if verbose:
            print("Visualize AI performance with state shape: {0}".format(__default_state_shape__))

        #from game2048 import VisualizeAI
        from ai import AI

        ai = AI(
            state_shape=__default_state_shape__,
            action_dim=__default_action_dim__,
            verbose=verbose
        )

        if verbose:
            print("Loading latest AI model from file: [{0}] ...".format(__filename__),end="")
        ai.load_nnet(__filename__)
        if verbose:
            print("OK!")

        visualizer = VisualizeAI(
            state_shape=__default_state_shape__,
            ai=ai,
            verbose=verbose
        )
        
        visualizer.start() # Run a game to get result
        visualizer.view()  

    if args.playnaiveai:
        if verbose:
            print("Watch naive AI to play game. Please close game in terminal after closing window (i.e, Press Ctrl+C).")

        from tetris import Tetris, NaiveAI
        tetris = Tetris(
            state_shape=__default_state_shape__,
            player=NaiveAI(verbose=verbose),
            verbose=verbose
        )

        tetris.start()

    if args.play:
        print("Play game. Please close game in terminal after closing window (i.e, Press Ctrl+C).")
        # from game2048 import Game2048, Human

        # game2048 = Game2048(state_shape=__default_state_shape__, player=Human(), verbose=verbose)
        # game2048.start()