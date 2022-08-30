from airflow import DAG

############################################################################################
############                      JEITO ERRADO               ###############################
############################################################################################
#task_1 = Operator(dag = dag)
#task_2 = Operator(dag = dag)
#task_3 = Operator(dag = dag)


##########################################################################################
############                       JEITO CORRETO                   #######################
##########################################################################################
"""
This will be useful because you wont need to write Operator(dag = dag)
dag will always be treated as dag so you don`t need to pass it as an argument
"""
#with DAG() as dag:
    #task_1 = Operator()

##########################################################################################
############             DEFINING THE DAG ID                 #############################
##########################################################################################
"""
The DAG ID is the UNIQUE identifier of your DAG and you have to make sure it is UNIQUE
across all of your DAGs, otherwise you might end up with behaviors where the must recent DAG
is take into your count so you will be able to see it on the UI but not the older one.

Your dag_id will always be the name of your dag file
"""

with DAG(dag_id = 'simple_dag') as dag:
    #task_1 = Operator(), this line is only illustrative you dont have an class called Operator()
    None
