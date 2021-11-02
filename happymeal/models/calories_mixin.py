
class CaloriesMixin:
    '''
        This is a mixin that can be included in classes that need the
        calories getter method
    '''

    def calories(self):
        return self._calories