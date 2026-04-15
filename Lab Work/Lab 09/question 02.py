from pgmpy.models import DiscreteBayesianNetwork
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination

model = DiscreteBayesianNetwork([
    ('Intelligence', 'Grade'),
    ('StudyHours', 'Grade'),
    ('Difficulty', 'Grade'),
    ('Grade', 'Pass')
])

cpd_intelligence = TabularCPD(
    variable='Intelligence',
    variable_card=2,
    values=[[0.7], [0.3]]
)

cpd_studyhours = TabularCPD(
    variable='StudyHours',
    variable_card=2,
    values=[[0.6], [0.4]]
)

cpd_difficulty = TabularCPD(
    variable='Difficulty',
    variable_card=2,
    values=[[0.4], [0.6]]
)

cpd_grade = TabularCPD(
    variable='Grade',
    variable_card=3,
    values=[
        [0.50, 0.70, 0.25, 0.40, 0.20, 0.35, 0.05, 0.15],  # A
        [0.30, 0.20, 0.35, 0.35, 0.35, 0.40, 0.25, 0.35],  # B
        [0.20, 0.10, 0.40, 0.25, 0.45, 0.25, 0.70, 0.50]   # C
    ],
    evidence=['Intelligence', 'StudyHours', 'Difficulty'],
    evidence_card=[2, 2, 2]
)

cpd_pass = TabularCPD(
    variable='Pass',
    variable_card=2,
    values=[
        [0.95, 0.80, 0.50],  # Yes
        [0.05, 0.20, 0.50]   # No
    ],
    evidence=['Grade'],
    evidence_card=[3]
)

model.add_cpds(cpd_intelligence, cpd_studyhours, cpd_difficulty, cpd_grade, cpd_pass)

print(model.check_model())

infer = VariableElimination(model)

q1 = infer.query(
    variables=['Pass'],
    evidence={'StudyHours': 0, 'Difficulty': 0}
)
print("P(Pass | StudyHours=Sufficient, Difficulty=Hard)")
print(q1)

q2 = infer.query(
    variables=['Intelligence'],
    evidence={'Pass': 0}
)
print("P(Intelligence | Pass=Yes)")
print(q2)
