# ============================================================
# 1.1 DOMAIN MODEL IMPLEMENTATION
# Training Management System
# ============================================================

from datetime import datetime

class Learner:
    def __init__(self, learner_id, name, email):
        if not learner_id or not name or not email:
            raise ValueError("Learner ID, name and email are required")
        
        self.learner_id = learner_id
        self.name = name
        self.email = email
        self.registrations = []

    def __str__(self):
        return f"Learner ID: {self.learner_id}, Name: {self.name}, Email: {self.email}"


class Course:
    def __init__(self, course_id, name, capacity):
        if capacity <= 0:
            raise ValueError("Capacity must be greater than 0")
        
        self.course_id = course_id
        self.name = name
        self.capacity = capacity
        self.enrolled_learners = []

    def is_full(self):
        return len(self.enrolled_learners) >= self.capacity

    def add_learner(self, learner):
        if self.is_full():
            return False
        if learner in self.enrolled_learners:
            return False
        self.enrolled_learners.append(learner)
        return True

    def __str__(self):
        return f"Course: {self.course_id} - {self.name} (Capacity: {self.capacity})"


class Registration:
    def __init__(self, registration_id, learner, course):
        self.registration_id = registration_id
        self.learner = learner
        self.course = course
        self.date = datetime.now().strftime("%Y-%m-%d")
        self.status = "Pending"

    def confirm(self):
        if self.course.add_learner(self.learner):
            self.status = "Confirmed"
            self.learner.registrations.append(self)
            return f"{self.learner.name} registered for {self.course.name}"
        else:
            self.status = "Failed"
            return f"Registration failed for {self.learner.name} - Course is full"

    def __str__(self):
        return f"Registration ID: {self.registration_id}, Status: {self.status}"


class Assessment:
    def __init__(self, assessment_id, learner, course, score):
        if score < 0 or score > 100:
            raise ValueError("Score must be between 0 and 100")
        
        self.assessment_id = assessment_id
        self.learner = learner
        self.course = course
        self.score = score
        self.result = "Pending"

    def __str__(self):
        return f"Assessment ID: {self.assessment_id}, Learner: {self.learner.name}, Score: {self.score}"


class SupportTicket:
    def __init__(self, ticket_id, learner, description):
        if not description:
            raise ValueError("Description is required")
        
        self.ticket_id = ticket_id
        self.learner = learner
        self.description = description
        self.status = "Open"
        self.created_date = datetime.now().strftime("%Y-%m-%d %H:%M")

    def close_ticket(self):
        self.status = "Closed"

    def __str__(self):
        return f"Ticket ID: {self.ticket_id}, Learner: {self.learner.name}, Status: {self.status}"


# ============================================================
# DEMONSTRATION
# ============================================================
print("=" * 60)
print("1.1 DOMAIN MODEL DEMONSTRATION")
print("=" * 60)

# Create Learners
learner1 = Learner("L001", "Thabo Mokoena", "thabo@email.com")
learner2 = Learner("L002", "Aisha Patel", "aisha@email.com")
print("\nLearners created:")
print(learner1)
print(learner2)

# Create Courses
course1 = Course("PY701", "Enterprise Python Development", 2)
course2 = Course("DB201", "Database Systems", 30)
print("\nCourses created:")
print(course1)
print(course2)

# Create Registrations
print("\nRegistrations:")
reg1 = Registration("R001", learner1, course1)
print(reg1.confirm())

reg2 = Registration("R002", learner2, course1)
print(reg2.confirm())

# This one should fail because capacity is 2
learner3 = Learner("L003", "Johan van Wyk", "johan@email.com")
reg3 = Registration("R003", learner3, course1)
print(reg3.confirm())

# Create Assessment
assessment1 = Assessment("A001", learner1, course1, 78)
print("\nAssessment created:")
print(assessment1)

# Create Support Ticket
ticket1 = SupportTicket("T001", learner1, "I cannot access the course materials")
print("\nSupport Ticket created:")
print(ticket1)

print("\n" + "=" * 60)
print("Domain Model executed successfully!")
print("=" * 60)