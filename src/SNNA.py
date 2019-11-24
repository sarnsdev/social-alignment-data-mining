class SNNA(object):
    """docstring for SNNA."""
    def __init__(self, arg):
        super(SNNA, self).__init__()
        self.arg = arg
        self.generator = None
        self.discriminator = None

    """
    Inputs:
        - alpha = learning rate
        - c = clipping weight
        - m = minimal training batch size
        - n = the number of discriminator training in each loop
        - lam_c = the annotated guided weight
    """
    def train(self, lambda=0.0001, c=0.01, m=256, n=5, lam_c=0.2):
        pass
