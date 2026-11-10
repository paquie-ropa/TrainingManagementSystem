# ============================================================
# 1.2 DESIGN PATTERN IMPLEMENTATION
# ============================================================

from abc import ABC, abstractmethod

# ============================================================
# 1. SINGLETON PATTERN
# Used for Application Configuration
# ============================================================
class AppConfig:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.app_name = "Training Management System"
            cls._instance.version = "1.0"
            cls._instance.support_email = "support@training.com"
        return cls._instance

    def display(self):
        print(f"App Name      : {self.app_name}")
        print(f"Version       : {self.version}")
        print(f"Support Email : {self.support_email}")


# ============================================================
# 2. FACTORY PATTERN
# Used to create different types of Support Tickets
# ============================================================
class SupportTicket:
    def __init__(self, ticket_id, learner_name, description, ticket_type):
        self.ticket_id = ticket_id
        self.learner_name = learner_name
        self.description = description
        self.ticket_type = ticket_type
        self.status = "Open"

    def __str__(self):
        return f"{self.ticket_type} (ID: {self.ticket_id}) - {self.learner_name}"


class TicketFactory:
    @staticmethod
    def create_ticket(ticket_type, ticket_id, learner_name, description):
        if ticket_type.lower() == "academic":
            return SupportTicket(ticket_id, learner_name, description, "AcademicTicket")
        elif ticket_type.lower() == "technical":
            return SupportTicket(ticket_id, learner_name, description, "TechnicalTicket")
        elif ticket_type.lower() == "registration":
            return SupportTicket(ticket_id, learner_name, description, "RegistrationTicket")
        else:
            return SupportTicket(ticket_id, learner_name, description, "GeneralTicket")


# ============================================================
# 3. STRATEGY PATTERN
# Used for different ways of calculating assessment results
# ============================================================
class AssessmentStrategy(ABC):
    @abstractmethod
    def calculate(self, score):
        pass


class PercentageStrategy(AssessmentStrategy):
    def calculate(self, score):
        return f"Percentage Result: {score}"


class ClassificationStrategy(AssessmentStrategy):
    def calculate(self, score):
        if score >= 80:
            result = "Distinction"
        elif score >= 70:
            result = "Merit"
        elif score >= 50:
            result = "Pass"
        else:
            result = "Fail"
        return f"Classification Result: {result}"


class PassFailStrategy(AssessmentStrategy):
    def calculate(self, score):
        result = "Pass" if score >= 40 else "Fail"
        return f"Pass/Fail Result: {result}"


class AssessmentCalculator:
    def __init__(self, strategy):
        self.strategy = strategy

    def set_strategy(self, strategy):
        self.strategy = strategy

    def evaluate(self, score):
        return self.strategy.calculate(score)


# ============================================================
# DEMONSTRATION
# ============================================================
print("=" * 60)
print("1.2 DESIGN PATTERN DEMONSTRATION")
print("=" * 60)

# ---------- SINGLETON ----------
print("\nSINGLETON PATTERN DEMONSTRATION")
print("-" * 60)

config1 = AppConfig()
config2 = AppConfig()

print(f"Config 1 ID: {id(config1)}")
print(f"Config 2 ID: {id(config2)}")

if config1 is config2:
    print("Singleton Successful: Same Instance")
else:
    print("Singleton Failed")

print("\nConfiguration Details:")
config1.display()

# ---------- FACTORY ----------
print("\n\nFACTORY PATTERN DEMONSTRATION")
print("-" * 60)

ticket1 = TicketFactory.create_ticket("Academic", "T001", "Thabo Mokoena", "Need assignment extension")
ticket2 = TicketFactory.create_ticket("Technical", "T002", "Aisha Patel", "Cannot login to the system")
ticket3 = TicketFactory.create_ticket("Registration", "T003", "Johan van Wyk", "Course not appearing")

print(f"Created: {ticket1.ticket_type}")
print(f"Created: {ticket2.ticket_type}")
print(f"Created: {ticket3.ticket_type}")

# ---------- STRATEGY ----------
print("\n\nSTRATEGY PATTERN DEMONSTRATION")
print("-" * 60)

calculator = AssessmentCalculator(PercentageStrategy())
print(calculator.evaluate(82))

calculator.set_strategy(ClassificationStrategy())
print(calculator.evaluate(82))

calculator.set_strategy(PassFailStrategy())
print(calculator.evaluate(35))

print("\n" + "=" * 60)
print("All Design Patterns executed successfully!")
print("=" * 60)