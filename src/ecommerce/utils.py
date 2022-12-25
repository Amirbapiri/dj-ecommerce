def convert_to_dot_notation(dict):
    """
    Making dictionary attributes accessable via dot notation
    """

    __getattr__ = dict.get
    __setattr__ = dict.__setitem__
    __delattr__ = dict.__delitem__
