import time

learners_list = []

# Add 5000 learners to the list
for i in range(5000):
    learners_list.append({
        "id": f"L{i}",
        "name": f"Learner {i}"
    })

learners_dict = {}

# Add the same 5000 learners to the dictionary
for i in range(5000):
    learners_dict[f"L{i}"] = {
        "id": f"L{i}",
        "name": f"Learner {i}"
    }

# IDs we will search for
search_ids = [f"L{i}" for i in range(4500, 5000)]

# ---------------- LIST TEST ----------------

start = time.perf_counter()

for learner_id in search_ids:
    for learner in learners_list:
        if learner["id"] == learner_id:
            break

before_time = time.perf_counter() - start


# ---------------- DICTIONARY TEST ----------------

start = time.perf_counter()

for learner_id in search_ids:
    learner = learners_dict.get(learner_id)

after_time = time.perf_counter() - start


# ---------------- RESULTS ----------------

print("=" * 40)
print("PERFORMANCE IMPROVEMENT TEST")
print("=" * 40)

print("Learners in system : 5000")
print("Lookups performed  : 500")

print()

print(f"BEFORE (list)      : {before_time:.6f} seconds")
print(f"AFTER (dictionary) : {after_time:.6f} seconds")

if after_time > 0:
    print(f"Speed improvement  : {before_time / after_time:.1f}x faster")
else:
    print("Speed improvement  : Dictionary was too fast to measure")

print("=" * 40)