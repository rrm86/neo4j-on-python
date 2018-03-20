from neo4jrestclient.client import GraphDatabase
from neo4jrestclient import client
 
db = GraphDatabase("http://localhost:7474", username="neo4j", password="1234")
# Create people nodes
def createpeople(str):
    people = db.labels.create("Pessoa")
    p1 = db.nodes.create(nome=str)
    people.add(p1)

def deletepeople(str):
    query = "MATCH (n{nome:'%s'}) DETACH DELETE (n)"% (str)
    out = db.query(query, data_contents=True)
    print(out.rows)

createpeople("Maria")
#deletepeople("Eu")


''' 
tema = db.labels.create("Tema")
b1 = db.nodes.create(nome="Gastronomia")
b2 = db.nodes.create(nome="Musica")
# You can associate a label with many nodes in one go
tema.add(b1, b2)



#create relationship
#p1.relationships.create("gosta", b1)
#p1.relationships.create("gosta", b2)

#
q = 'MATCH (u:Pessoa)-[r:gosta]->(m:Tema) WHERE u.nome="Eu" RETURN u, type(r), m'
# "db" as defined above
results = db.query(q, returns=(client.Node, str, client.Node))
for r in results:
    print("(%s)-[%s]->(%s)" % (r[0]["nome"], r[1], r[2]["nome"]))
    '''