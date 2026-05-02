## BAYESIAN NETWORK 
!pip install pgmpy

from pgmpy.models import DiscreteBayesianNetwork
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination

# define the DAG graph for BayesianNetwork
model = DiscreteBayesianNetwork([
    ('Burglary','Alarm'),   # burglary -> Alarm  (alarm depends on burglary)
    ('Earthquake','Alarm'), # Earthquake -> Alarm  (alarm depends on earthquake)
    ('Alarm','JohnCalls'),  # Alarm -> JohnCalls
    ('Alarm','MaryCalls')   # Alarm -> MaryCalls
])

# define CPTs (Conditional Probability Tables)
cpd_burglar = TabularCPD(
    variable = 'Burglary',
    variable_card =2,  # burglary has 2 states
    values = [[0.999],[0.001]]   # P(burglary=False) = 0.999, P(burglary=True) = 0.001

)

cpd_earthquake = TabularCPD(
    variable='Earthquake',
    variable_card=2,
    values = [[0.998],[0.002]]
)


cpd_alarm = TabularCPD(
    variable = 'Alarm',
    variable_card=2,
    values = [
        # B,E
        # FF     FT   TF   TT
        [0.999,0.71,0.06,0.05],   # alarm = False
        [0.001,0.29,0.94,0.95]   # alarm = True 
    ],
    evidence = ['Burglary','Earthquake'],
    evidence_card=[2,2]

    # this whole thing tells
    # P(Alarm | burglary,Earthquake)                  
)

cpd_john = TabularCPD(
    variable = 'JohnCalls',
    variable_card = 2 ,

    values = [
       #  A=F   A=T 
         [ 0.95, 0.10],         # johncalls = False
         [ 0.05, 0.90]         # johncalls = True
    ],
    evidence = ['Alarm'],
    evidence_card=[2]
# this gives
# P(Johncalls | Alarm)
                      
)

cpd_mary = TabularCPD(
    variable = 'MaryCalls',
    variable_card = 2 , 
    values = [
        [0.99,0.30],   # marrycalls = False
        [0.01,0.70]    # marrycalls = True
    ],
    evidence = ['Alarm'],
    evidence_card=[2]

)


# Add all the CPTs to our model

model.add_cpds(
    cpd_burglar,
    cpd_earthquake,
    cpd_alarm,
    cpd_john,
    cpd_mary
               
)
# now we have attached the probabilities to the graph 


assert model.check_model(), 'Model is incorrect'


# INFERENCE ENGINE 
inference = VariableElimination(model)

result = inference.query(
    variables = ['Burglary'],
    evidence = {'JohnCalls':1,'MaryCalls':1}
                        
)

print(result)
