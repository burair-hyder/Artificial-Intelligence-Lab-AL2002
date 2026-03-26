# Task 7
from ortools.sat.python import cp_model
n = 4
model = cp_model.CpModel()

queens = [model.NewIntVar(0, n - 1, f"q{i}") for i in range(n)]

model.AddAllDifferent(queens)
model.AddAllDifferent([queens[i] + i for i in range(n)])
model.AddAllDifferent([queens[i] - i for i in range(n)])

solver = cp_model.CpSolver()
status = solver.Solve(model)

if status == cp_model.OPTIMAL or status == cp_model.FEASIBLE:
    for i in range(n):
        row = ["_"] * n
        row[solver.Value(queens[i])] = "Q"
        print(" ".join(row))
else:
    print("No solution found.")
