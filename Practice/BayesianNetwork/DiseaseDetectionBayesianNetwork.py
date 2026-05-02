from pgmpy.models import DiscreteBayesianNetwork
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination

# define DAG
mymodel = DiscreteBayesianNetwork(
    [
    ('Disease','Fever'),
    ('Disease','Cough'),
    ('Disease','Test'),
    ]
)

# define CPTS

cpd_disease = TabularCPD(
    variable='Disease',
    values = [
        [0.99],   # P(disease=False) = 0.99
        [0.01]    # P(disease=True) = 0.01
    ],
    variable_card=2                    
)

cpd_fever = TabularCPD(
    variable ='Fever',
    values = [
        #D=F  D=T
        [0.8 , 0.2],    # fever = False
        [0.2 , 0.8]     # fever = True
    ],
    variable_card=2,
    evidence= ['Disease'],
    evidence_card=[2]                       
)

cpd_cough = TabularCPD(
    variable='Cough',
    values = [
        #D=F D=T
        [0.7,0.3],    # cough = F
        [0.3,0.7]     # cough = T
    ],
    variable_card=2,
    evidence=['Disease'],
    evidence_card = [2]
)

cpd_test = TabularCPD(
    variable ='Test',
    values = [
        #D=F D=T
        [0.9,0.1],   #Test=F
        [0.1,0.9]    #Test=T
    ],
    variable_card=2,
    evidence=['Disease'],
    evidence_card = [2]
)

mymodel.add_cpds(
    cpd_disease,
    cpd_fever,
    cpd_cough,
    cpd_test
    
)

assert mymodel.check_model() , "error"


inference = VariableElimination(mymodel)

result = inference.query(
    variables=['Disease'],
    evidence = {'Fever':1,'Cough':1,'Test':1}
)

print(result)
