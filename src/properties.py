DATA_DIR = '/Users/alankar/Documents/cmu/Spring-2018/NN for ' \
           'NLP/Project/Assignment-1/vanGAN/data/'
EN_WORD_TO_VEC = 'EN.200K.cbow1_wind5_hs0_neg10_size300_smpl1e-05.txt'
IT_WORD_TO_VEC = 'IT.200K.cbow1_wind5_hs0_neg10_size300_smpl1e-05.txt'
<<<<<<< HEAD:src/properties.py
VALIDATION_FILE = 'OPUS_en_it_europarl_test.txt'
=======
EVAL_EUROPARL = 'OPUS_en_it_europarl_test.txt'
>>>>>>> a2ee1ef8a73237fead0f788402073c3d10d3b339:properties.py

# Model Hyper-Parameters
# TODO: Add all these as program parameters

g_input_size = 300     # Random noise dimension coming into generator, per output vector
g_hidden_size = 50   # Generator complexity
g_output_size = 300    # size of generated output vector
d_input_size = 300   # cardinality of distributions
d_hidden_size = 50   # Discriminator complexity
d_output_size = 1    # Single dimension for 'real' vs. 'fake'
mini_batch_size = 32
dropout_rate = 0.1

d_learning_rate = 2e-4  # 2e-4
g_learning_rate = 2e-4
optim_betas = (0.9, 0.999)
<<<<<<< HEAD:src/properties.py
num_epochs = 10
=======
num_epochs = 20
>>>>>>> a2ee1ef8a73237fead0f788402073c3d10d3b339:properties.py
print_interval = 200
d_steps = 1  # 'k' steps in the original GAN paper. Can put the discriminator on higher training freq than generator
g_steps = 1
