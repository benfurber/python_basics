class Airport:
    '''
    Following the steps of: https://github.com/makersacademy/airport_challenge
    '''

    def __init__(self, name):
        self.name = name
        self.hanger = []
        print('Initialising {}'.format(self.name))
