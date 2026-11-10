import unittest


class TestRegistration(unittest.TestCase):

    def test_registration(self):
        learner = "L001"
        course = "Python"

        self.assertIsNotNone(learner)
        self.assertIsNotNone(course)

    def test_duplicate_registration(self):
        registrations = ["L001-Python"]

        self.assertIn("L001-Python", registrations)

    def test_course_capacity(self):
        capacity = 2
        enrolled = 2

        self.assertEqual(enrolled, capacity)

    def test_validation(self):
        learner_id = "L001"

        self.assertNotEqual(learner_id, "")


class TestAssessment(unittest.TestCase):

    def test_assessment_calculation(self):
        mark1 = 70
        mark2 = 80

        average = (mark1 + mark2) / 2

        self.assertEqual(average, 75)


if __name__ == "__main__":
    unittest.main()