"""

    Word scheduling algos

"""

from .basicSR.four_levels_per_word import FourLevelsPerWord
from .basicSR.two_learning_cycles_per_word import TwoLearningCyclesPerWord



def get_scheduler(user):

    if user.has_feature("exercise_levels"):
        return FourLevelsPerWord
    else:
        return TwoLearningCyclesPerWord
