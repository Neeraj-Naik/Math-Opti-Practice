from pyomo.environ import SolverFactory

solvers = ["highs", "cbc", "glpk", "scip", "ipopt"]
IsInstalled = False

print("\n\n### SOLVER CHECKS ###")
print("     Currently Installed :     ", end="")

for solver in solvers:
    if SolverFactory(solver).available(False):
        IsInstalled = True
        print(solver, end=", ")

print("\n")

if not IsInstalled:
    print(f"None of the Solvers in {solvers} are currently installed !!")

