import numpy as np
import os
import sys

class Parameters():
    def __init__(self, workers_num):
        # hyperparameters
        self.seed = 1234

        self.max_exploration_episodes = 500
        self.batch_size       = 256      # batch size during training
        self.rm_size          = 1000000    # memory replay maximum size
        self.gamma            = 0.99     # Discount factor
        self.critic_lr        = 0.001    # Learning rate for critic
        self.actor_lr         = 0.0001   # Learning rate for actor

        self.tau              = 0.001    # moving average for target network

        self.max_episodes     = 50000

        self.valid_freq       = 100
        self.train_steps      = 5

        self.train = True
        self.continue_training=False

        # self.env_name         = 'Pendulum-v0'   # 'MountainCarContinuous-v0'
        self.env_name = 'MountainCarContinuous-v0'

        self.summary_dir = './tboard_ddpg'  # Directory for storing tensorboard summary results
        self.save_dir = './model_ddpg'      # Directory for storing trained model

        self.parameter_servers = ["localhost:2222"]
        self.workers = []
        for i in range(workers_num):
            self.workers.append("localhost:"+str(2223+i))
        self.workers_num      = workers_num
