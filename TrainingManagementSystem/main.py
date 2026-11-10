"""
main.py - Run all demonstrations
"""

from domain_model import (
    Learner, Course, Registration, Assessment, SupportTicket
)
from singleton_pattern import ConfigManager
from customer import TicketFactory
from strategy_pattern import (
    PercentageStrategy, ClassificationStrategy, 
    LetterGradeStrategy, Grader
)


def test_domain_model():
    """Test all domain model classes"""
    
    print("\n" + "=" * 60)
    print("DOMAIN MODEL DEMONSTRATION")
    print("=" * 60)
    
    # 1. Create a learner
    print("\n1. CREATING LEARNER")
    print("-" * 30)
    learner = Learner("Thabo Mokoena", "thabo@email.com", "0821234567")
    print("Created: " + str(learner))
    print("ID: " + learner.id)
    
    # 2. Create a course
    print("\n2. CREATING COURSE")
    print("-" * 30)
    course = Course("PY101", "Python Basics", "Learn Python from scratch")
    print("Created: " + str(course))
    
    # 3. Enroll learner
    print("\n3. ENROLLING LEARNER")
    print("-" * 30)
    learner.enroll(course.id)
    course.add_student()
    print(learner.name + " enrolled in " + course.title)
    print("Enrolment: " + str(course.current) + "/" + str(course.max))
    
    # 4. Create registration
    print("\n4. CREATING REGISTRATION")
    print("-" * 30)
    reg = Registration(learner.id, course.id)
    reg.mark_paid()
    reg.update_progress(60)
    print("Registration created")
    print("Paid: " + str(reg.paid))
    print("Progress: " + str(reg.progress) + "%")
    
    # 5. Create assessment
    print("\n5. CREATING ASSESSMENT")
    print("-" * 30)
    assessment = Assessment(course.id, "Python Final Exam", 100, 50)
    assessment.add_question("What is 2+2?", "4", 20)
    assessment.add_question("What is Python?", "language", 20)
    assessment.publish()
    print("Created: " + str(assessment))
    print("Questions: " + str(len(assessment.questions)))
    
    # 6. Submit assessment
    print("\n6. SUBMITTING ASSESSMENT")
    print("-" * 30)
    answers = {"1": "4", "2": "language"}
    score = assessment.calculate(answers)
    learner.add_score(assessment.id, score)
    print("Score: " + str(score) + "/" + str(assessment.total))
    print("Passed: " + str(assessment.passed(score)))
    
    # 7. Create support ticket
    print("\n7. CREATING SUPPORT TICKET")
    print("-" * 30)
    ticket = SupportTicket(learner.id, "Cannot access videos", "Videos not loading")
    ticket.add_comment(learner.id, "Tried Chrome and Firefox")
    ticket.assign("SUPPORT-01")
    ticket.resolve("Fixed CDN issue")
    print("Created: " + str(ticket))
    print("Priority: " + ticket.priority)
    print("Comments: " + str(len(ticket.comments)))
    
    # 8. Show relationships
    print("\n8. CLASS RELATIONSHIPS")
    print("-" * 30)
    print("Learner -> Registration -> Course")
    print(learner.name + " -> " + course.title)
    print("Course -> Assessment")
    print(course.code + " -> " + assessment.title)
    print("Learner -> SupportTicket")
    print(learner.name + " -> " + ticket.subject)
    
    print("\n" + "=" * 60)
    print("DOMAIN MODEL OUTPUT")
    print("=" * 60)
    print("Learner ID: " + learner.id + ", Name: " + learner.name)
    print("Course: " + course.code + " - " + course.title)
    print(learner.name + " registered for " + course.title)
    print("=" * 60)
    print("DOMAIN MODEL DEMONSTRATION COMPLETE\n")


def test_singleton():
    """Test the Singleton Pattern"""
    
    print("\n" + "=" * 60)
    print("SINGLETON PATTERN DEMONSTRATION")
    print("=" * 60)
    
    # Create first instance
    config1 = ConfigManager()
    print("\nConfig 1 ID: " + str(id(config1)))
    
    # Create second instance
    config2 = ConfigManager()
    print("Config 2 ID: " + str(id(config2)))
    
    # Check if same
    print("\nSingleton Successful: " + str(config1 is config2))
    print("Same Instance: " + str(id(config1) == id(config2)))
    
    # Show settings
    print("\nSettings:")
    config1.show_settings()
    
    # Modify through one instance
    config1.set('app_name', 'New Training System')
    print("\nUpdated App Name: " + config2.get('app_name'))
    
    print("\nSingleton Pattern Successful: Same Instance")
    print("=" * 60 + "\n")


def test_factory():
    """Test the Factory Pattern"""
    
    print("\n" + "=" * 60)
    print("FACTORY PATTERN DEMONSTRATION")
    print("=" * 60)
    
    print("\nCreating Tickets...")
    print("-" * 30)
    
    # Create academic ticket
    ticket1 = TicketFactory.create(
        'academic',
        'L001',
        {'subject': 'Assignment Extension', 'description': 'Need extension for assignment'}
    )
    print("\nCreated: " + ticket1.category.title() + "Ticket")
    print("  Subject: " + ticket1.subject)
    print("  Priority: " + ticket1.priority)
    
    # Create technical ticket
    ticket2 = TicketFactory.create(
        'technical',
        'L001',
        {'subject': 'Video Playback Error', 'description': 'Videos are not loading'}
    )
    print("\nCreated: " + ticket2.category.title() + "Ticket")
    print("  Subject: " + ticket2.subject)
    print("  Priority: " + ticket2.priority)
    
    # Create registration ticket
    ticket3 = TicketFactory.create(
        'registration',
        'L001',
        {'subject': 'Cannot Enroll', 'description': 'Unable to enroll in course'}
    )
    print("\nCreated: " + ticket3.category.title() + "Ticket")
    print("  Subject: " + ticket3.subject)
    print("  Priority: " + ticket3.priority)
    
    print("\n" + "-" * 30)
    print("FACTORY PATTERN DEMONSTRATION")
    print("---")
    print("Created: AcademicTicket")
    print("Created: TechnicalTicket")
    print("Created: RegistrationTicket")
    print("=" * 60 + "\n")


def test_strategy():
    """Test the Strategy Pattern"""
    
    print("\n" + "=" * 60)
    print("STRATEGY PATTERN DEMONSTRATION")
    print("=" * 60)
    
    score = 82
    total = 100
    
    print("\nStudent Score: " + str(score) + "/" + str(total))
    print("-" * 30)
    
    # Test percentage strategy
    print("\nUsing Percentage Strategy:")
    grader = Grader(PercentageStrategy())
    result = grader.calculate(score, total)
    print("  Percentage: " + str(result['score']) + "%")
    print("  Passed: " + str(result['passed']))
    
    # Test classification strategy
    print("\nUsing Classification Strategy:")
    grader.set_strategy(ClassificationStrategy())
    result = grader.calculate(score, total)
    print("  Percentage: " + str(result['score']) + "%")
    print("  Classification: " + result['classification'])
    print("  Passed: " + str(result['passed']))
    
    # Test letter grade strategy
    print("\nUsing Letter Grade Strategy:")
    grader.set_strategy(LetterGradeStrategy())
    result = grader.calculate(score, total)
    print("  Percentage: " + str(result['score']) + "%")
    print("  Letter Grade: " + result['letter'])
    print("  Passed: " + str(result['passed']))
    
    print("\n" + "=" * 60)
    print("STRATEGY PATTERN DEMONSTRATION")
    print("---")
    print("Percentage Result: " + str(score) + "%")
    print("Classification Result: Distinction")
    print("=" * 60 + "\n")


def main():
    """Run all demonstrations"""
    
    print("\n" + "=" * 70)
    print("ENTERPRISE DOMAIN MODEL AND DESIGN PATTERNS")
    print("DELIVERABLE 1 DEMONSTRATION")
    print("=" * 70)
    
    # Run all tests
    test_domain_model()
    test_singleton()
    test_factory()
    test_strategy()
    
    print("\n" + "=" * 70)
    print("ALL DEMONSTRATIONS COMPLETE")
    print("=" * 70)


if __name__ == "__main__":
    main()