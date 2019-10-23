import unittest
from survey import AnonymousSurvey

# class TestAnonymousSurvey(unittest.TestCase):
#     """Test the function survey.py"""
#
#     def test_name_correctly(self):
#         question = "What age did you lose your virginity?"
#         test = AnonymousSurvey(question)
#         print_val = test.show_question()
#         print(print_val)
#         self.assertEqual("What age did you lose your virginity?", print_val)

class TestAnonymousSurvey(unittest.TestCase):
    """Tests for the class AnonymouSurvey"""

    def test_store_single_response(self):
        question = "What language did you first learn to speak?"
        my_survey = AnonymousSurvey(question)
        my_survey.store_response('English')

        self.assertIn('English', my_survey.responses)

    def test_store_three_responses(self):
        """Test that three individual responses are stored properly"""
        question = "What language did you first learn to speak?"
        my_survey = AnonymousSurvey(question)
        responses = ['English', 'Spanish', 'Mandarin']
        for response in responses:
            my_survey.store_response(response)
        self.assertIn('English', my_survey.responses)

        # for response in responses:
        #     self.assertIn(response, my_survey.responses)

unittest.main()
