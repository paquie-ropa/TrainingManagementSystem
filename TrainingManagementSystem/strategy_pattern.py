"""
strategy_pattern.py - Strategy Pattern for Grading
"""


class GradingStrategy:
    """Base class for grading strategies"""
    
    def grade(self, score, total):
        pass


class PercentageStrategy(GradingStrategy):
    """Simple percentage grade"""
    
    def grade(self, score, total):
        if total == 0:
            percentage = 0
        else:
            percentage = (score / total) * 100
        
        return {
            'type': 'percentage',
            'score': round(percentage, 1),
            'passed': percentage >= 50
        }


class ClassificationStrategy(GradingStrategy):
    """Classification grade: Distinction, Merit, Pass, Fail"""
    
    def grade(self, score, total):
        if total == 0:
            percentage = 0
        else:
            percentage = (score / total) * 100
        
        if percentage >= 80:
            classification = "Distinction"
        elif percentage >= 65:
            classification = "Merit"
        elif percentage >= 50:
            classification = "Pass"
        else:
            classification = "Fail"
        
        return {
            'type': 'classification',
            'score': round(percentage, 1),
            'classification': classification,
            'passed': classification != "Fail"
        }


class LetterGradeStrategy(GradingStrategy):
    """Letter grade: A, B, C, D, F"""
    
    def grade(self, score, total):
        if total == 0:
            percentage = 0
        else:
            percentage = (score / total) * 100
        
        if percentage >= 90:
            letter = "A"
        elif percentage >= 75:
            letter = "B"
        elif percentage >= 60:
            letter = "C"
        elif percentage >= 50:
            letter = "D"
        else:
            letter = "F"
        
        return {
            'type': 'letter',
            'score': round(percentage, 1),
            'letter': letter,
            'passed': letter != "F"
        }


class Grader:
    """Context class that uses a grading strategy"""
    
    def __init__(self, strategy):
        self.strategy = strategy
    
    def set_strategy(self, strategy):
        self.strategy = strategy
    
    def calculate(self, score, total):
        return self.strategy.grade(score, total)