#!/usr/bin/env python
"""
model tests
"""


import unittest

## import model specific functions and variables
from model import *

DATA_DIR = './cs-train'

class ModelTest(unittest.TestCase):
    """
    test the essential functionality
    """
        
    def test_01_train(self):
        """
        test the train functionality
        """

        ## train the model
        model_train(data_dir=DATA_DIR, test=False)
        self.assertTrue(os.path.exists('./models/sl-all-0.1.joblib'))

    def test_02_load(self):
        """
        test the train functionality
        """
                        
        ## train the model
        all_data, all_models = model_load(data_dir=DATA_DIR)
        print(all_models.keys())
        
        #self.assertTrue('all' in dir(all_models.keys()))
        self.assertTrue('hong_kong' in set(all_models.keys()))

       
    def test_03_predict(self):
        """
        test the predict function input
        """

        ## load model first
        all_data, all_models = model_load(data_dir=DATA_DIR)
    
        ## ensure that a list can be passed
        query = {'country': 'hong_kong', 'year': '2018', 'month':'07', 'day':'20'}

        result = model_predict(country=query['country'],
                               year=query['year'],
                               month=query['month'],
                               day=query['day'],
                               test=True,
                               all_models=all_models,
                               all_data=all_data)
        y_pred = result['y_pred']

        self.assertTrue(isinstance(y_pred[0], float))

          
### Run the tests
if __name__ == '__main__':
    unittest.main()
