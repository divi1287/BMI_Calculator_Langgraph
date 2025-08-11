from langgraph.graph import StateGraph, START, END
from typing import TypedDict

"""Creating class"""

class BMI(TypedDict):
    height_cm: float
    weight_kg: float
    bmi: float
    category: str

def calculate_bmi(state:BMI)->BMI:
  weight=state['weight_kg']
  height=state['height_cm']
  bmi=weight/(height/100)**2
  state['bmi'] = round(bmi,2)
  return state

def label_bmi(state:BMI)->BMI:
  bmi=state['bmi']
  if bmi<18.5:
    state['category']='Underweight'
  elif bmi>=18.5 and bmi<25:
    state['category']='Normal'
  elif bmi>=25 and bmi<30:
    state['category']='Overweight'
  else:
    state['category']='Obese'
  return state

"""Create graph and add nodes"""

graph=StateGraph(BMI)
#Creating nodes
graph.add_node('calculate_bmi',calculate_bmi)
graph.add_node('label_bmi',label_bmi)
#creating Edge
graph.add_edge(START,'calculate_bmi')
graph.add_edge('calculate_bmi','label_bmi')
graph.add_edge('calculate_bmi',END)
workflow=graph.compile()

#Execute the graph
initial_state={'weight_kg':23,'height_cm':5}
final_state=workflow.invoke(initial_state)
print(final_state)

from IPython.display import Image
Image(workflow.get_graph().draw_mermaid_png())
