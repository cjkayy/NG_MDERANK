import pandas as pd
from py2neo import Graph, Node, Relationship, NodeMatcher



graph = Graph("http://localhost:7474", auth=("neo4j", "Agoni0226!"))

cve = pd.read_csv("D:\\eight_description_clarify_final2.csv", header=None)

''''
cwe699 = Node(label='cwe699', name='cwe699')
graph.merge(cwe699, 'cwe699', 'name')
graph.create(cwe699)

for i in cwe.values:
    cweid = i[0]
    entity1 = i[1]
    label1 = i[2]
    relationship = i[3]
    entity2 = i[4]
    label2 = i[5]

    cwe_node = Node(label="cweid", name=cweid)
    graph.merge(cwe_node, 'cweid', 'name')
    entity_node_1 = Node(label=label1, name=entity1)
    graph.merge(entity_node_1, label1, 'name')
    entity_node_2 = Node(label=label2, name=entity2)
    graph.merge(entity_node_2, label2, 'name')

    graph.create(cwe_node)
    graph.create(entity_node_1)
    graph.create(entity_node_2)

    cwe_entity1 = Relationship(entity_node_1, 'Belong to', cwe_node)
    cwe_entity2 = Relationship(entity_node_2, 'Belong to', cwe_node)
    entity1_entity2 = Relationship(entity_node_1, relationship, entity_node_2)
    cwe699_cwe = Relationship(cwe_node, 'Member of', cwe699)

    graph.create(cwe_entity1)
    graph.create(cwe_entity2)
    graph.create(entity1_entity2)
    graph.create(cwe699_cwe)
    
'''

for j in cve.values:
    cveid = j[0]
    entity1 = j[1]
    label1 = j[2]
    relationship = j[3]
    entity2 = j[4]
    label2 = j[5]

    # cwe_node = Node(label="cweid", name=cweid)
    # graph.merge(cwe_node, 'cweid', 'name')
    cveid_node = Node(label='cveid', name=cveid)
    graph.merge(cveid_node, 'cveid', 'name')
    entity_node_1 = Node(label=label1, name=entity1)
    graph.merge(entity_node_1, label1, 'name')
    entity_node_2 = Node(label=label2, name=entity2)
    graph.merge(entity_node_2, label2, 'name')

    graph.create(cveid_node)
    graph.create(entity_node_1)
    graph.create(entity_node_2)

    # cwe_cve = Relationship(cveid_node, 'Belong to', cwe_node)
    cve_entity1 = Relationship(entity_node_1, 'Belong to', cveid_node)
    cve_entity2 = Relationship(entity_node_2, 'Belong to', cveid_node)
    entity1_entity2 = Relationship(entity_node_1, relationship, entity_node_2)

    # graph.create(cwe_cve)
    graph.create(cve_entity1)
    graph.create(cve_entity2)
    graph.create(entity1_entity2)


