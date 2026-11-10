# Registration Processing Engine with Concurrency


import threading
from concurrent.futures import ThreadPoolExecutor, as_completed
import time
import random

# Lock to protect shared data
lock = threading.Lock()

# Courses dictionary
courses = {
    "CS101": {"name": "Introduction to Programming", "capacity": 5, "enrolled": []},
    "CS201": {"name": "Data Structures", "capacity": 4, "enrolled": []},
    "IT301": {"name": "Database Systems", "capacity": 3, "enrolled": []}
}

successful = []
failed = []

def process_registration(learner_id, learner_name, course_id):
    # Simulate some processing time
    time.sleep(random.uniform(0.05, 0.15))

    # Use lock so only one thread can change the data at a time
    with lock:
        # 1. Validation
        if learner_id == "" or learner_name == "" or course_id == "":
            result = f"[FAILED] {learner_name} - Missing information"
            failed.append(result)
            return result

        # 2. Check if course exists
        if course_id not in courses:
            result = f"[FAILED] {learner_name} - Course {course_id} does not exist"
            failed.append(result)
            return result

        course = courses[course_id]

        # 3. Prevent duplicate registration
        if learner_id in course["enrolled"]:
            result = f"[FAILED] {learner_name} - Already registered for {course_id}"
            failed.append(result)
            return result

        # 4. Check capacity
        if len(course["enrolled"]) >= course["capacity"]:
            result = f"[FULL]   {learner_name} - Course {course_id} is full"
            failed.append(result)
            return result

        # 5. Successful registration
        course["enrolled"].append(learner_id)
        result = f"[SUCCESS] {learner_name} registered for {course_id}"
        successful.append(result)
        return result


# ========== MAIN PROGRAM ==========
print("=" * 60)
print("REGISTRATION PROCESSING ENGINE (CONCURRENT)")
print("=" * 60)
print()

# List of registration requests (more than 10)
registrations = [
    ("L01", "Learner 1", "CS101"),
    ("L02", "Learner 2", "CS101"),
    ("L03", "Learner 3", "CS101"),
    ("L04", "Learner 4", "CS101"),
    ("L05", "Learner 5", "CS101"),
    ("L06", "Learner 6", "CS101"),      # Will be full
    ("L02", "Learner 2", "CS101"),      # Duplicate
    ("L07", "Learner 7", "CS201"),
    ("L08", "Learner 8", "CS201"),
    ("L09", "Learner 9", "CS201"),
    ("L10", "Learner 10", "CS201"),
    ("L11", "Learner 11", "CS201"),     # Will be full
    ("L12", "Learner 12", "IT301"),
    ("L13", "Learner 13", "IT301"),
    ("L14", "Learner 14", "IT301"),
    ("L15", "Learner 15", "IT301"),     # Will be full
    ("L16", "Learner 16", "CS999"),     # Invalid course
]

# Process many registrations at the same time using threads
with ThreadPoolExecutor(max_workers=6) as executor:
    futures = []
    for reg in registrations:
        learner_id, learner_name, course_id = reg
        future = executor.submit(process_registration, learner_id, learner_name, course_id)
        futures.append(future)

    # Print results as they finish
    for future in as_completed(futures):
        print(future.result())

# ========== SUMMARY ==========
print()
print("REGISTRATION SUMMARY")
print("-" * 60)
print(f"Total Requests      : {len(registrations)}")
print(f"Successful          : {len(successful)}")
print(f"Failed              : {len(failed)}")
print()

print("Successful Registrations:")
for s in successful:
    print("  " + s)

print()
print("Failed Registrations:")
for f in failed:
    print("  " + f)

print()
print("Course Capacity Status:")
for course_id, course in courses.items():
    print(f"  {course_id}: {len(course['enrolled'])}/{course['capacity']} enrolled")

print("=" * 60)
print("Concurrent processing completed successfully.")