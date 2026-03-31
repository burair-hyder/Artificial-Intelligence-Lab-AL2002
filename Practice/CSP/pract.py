# parh letay pheley.
# pr yeh pher bhe nhi hota
# mujh sy bhe nhi hoa 

!pip install ortools
from ortools.sat.python import cp_model


class printer(cp_model.CpSolverSolutionCallback):
  def __init__(self,var):
    super().__init__()
    self.count =0
    self.var = var
  
  def on_solution_callback(self):
    self.count+=1
    for v in self.var:
      print(f"{v}={self.value(v)}")
    print()


def csp_solve():

  model = cp_model.CpModel()

  upper = max(50,45,37)
  x = model.new_int_var(0,upper,"x")
  y = model.new_int_var(0,upper,"y")
  z = model.new_int_var(0,upper,"z")

#constraints
  model.add(2 *x + 7*y + 3*z <= 50)
  model.add(3*x-5*y +7*z <=45)
  model.add(5 * x + 2 * y - 6 * z <= 37)

  # objective func
  model.maximize(2*x + 2*y +3*z)
# it will maximize this func while fullfilling constaints
  printer1 = printer([x,y,z])
  solver = cp_model.CpSolver()
  solver.parameters.enumerate_all_solutions = True
  status = solver.solve(model,printer1)

csp_solve()
