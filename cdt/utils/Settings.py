"""
Settings file for CGNN algorithm
Defining all global variables
Authors : Anonymous Author
Date : 8/05/2017
"""
import ast
import os


class ConfigSettings(object):
    __slots__ = ("NB_JOBS",  # Number of parallel jobs runnable
                 "GPU",  # True if GPU is available
                 "NB_GPU",  # Number of available GPUs (Not used if autoset)
                 "GPU_OFFSET",  # First index of GPU (Not used if autoset)
                 "GPU_LIST"  # List of CUDA_VISIBLE_DEVICES
                 "autoset_config"
                 "verbose",
                 "r_is_available")

    def __init__(self):  # Define here the default values of the parameters

        self.NB_JOBS = 2
        self.GPU = True
        self.NB_GPU = 2
        self.GPU_OFFSET = 0
        self.GPU_LIST = [i for i in range(
            self.GPU_OFFSET, self.GPU_OFFSET + self.NB_GPU)]
        self.autoset_config = True
        self.verbose = True
        self.r_is_available = False

        if self.autoset_config:
            self = autoset_settings(self)


class CGNNSettings(object):
    __slots__ = ("h_layer_dim",
                 "train_epochs",
                 "test_epochs",
                 "NB_RUNS",
                 "NB_MAX_RUNS",
                 "learning_rate",
                 "init_weights",
                 "ttest_threshold",
                 "nb_run_feature_selection",
                 "regul_param",
                 "threshold_UMG",
                 "nb_epoch_train_feature_selection",
                 "nb_epoch_eval_weights",
                 "use_Fast_MMD",
                 "nb_vectors_approx_MMD",
                 "complexity_graph_param",
                 "max_nb_points")

    def __init__(self):
        super(object, self).__init__()
        self.NB_RUNS = 8
        self.NB_MAX_RUNS = 32
        self.learning_rate = 0.01
        self.init_weights = 0.05
        self.max_nb_points = 1500
        self.h_layer_dim = 30
        self.use_Fast_MMD = False
        self.nb_vectors_approx_MMD = 100

        # CGNN
        self.train_epochs = 1000
        self.test_epochs = 500
        self.complexity_graph_param = 0.0005
        self.ttest_threshold = 0.05

        # specific for FSGNN
        self.nb_run_feature_selection = 1
        self.regul_param = 0.004
        self.threshold_UMG = 0.15
        self.nb_epoch_train_feature_selection = 2000
        self.nb_epoch_eval_weights = 500


def autoset_settings(set_var):
    """
    Autoset GPU parameters using CUDA_VISIBLE_DEVICES variables. Return default config if variable not set.
    :param set_var: Variable to set. Must be of type ConfigSettings 
    """
    try:
        devices = ast.literal_eval(os.environ["CUDA_VISIBLE_DEVICES"])
        if len(devices) != 0:
            set_var.GPU_LIST = os.environ["CUDA_VISIBLE_DEVICES"]
            print("Detecting CUDA devices : {}".format(devices))
        else:
            raise KeyError
    except KeyError:
        warnings.warn("No GPU automatically detected.
                      Switching back to default settings")
    return set_var


SETTINGS = ConfigSettings()
CGNN_SETTINGS = CGNNSettings()
