from dataclasses import asdict
from operator import itemgetter
from typing import Any, Dict, TypeVar, List
from returns.maybe import Maybe
from toolz import curry
from app.db.neo4j_database import driver
import toolz as t

T = TypeVar('T')

@curry
def create_node(node_type: str, object: T) -> Maybe:
    object_as_dict = asdict(object)
    with driver.session() as session:
        query = f"""
        CREATE (n:{node_type} {{ {', '.join([f'{k}: ${k}' for k in object_as_dict])} }})
        RETURN n"""

        params = object_as_dict

        res = session.run(query, params).single()
        return (
            Maybe.from_optional(res.get("n")).map(lambda n: {
                "id": n.element_id.split(":")[2],
                "properties": dict(n)
            })
        )

@curry
def get_node_by_id(node_type: str, node_id: int) -> List[T]:
    with driver.session() as session:
        query = f"""
        MATCH (n:{node_type})
        WHERE ID(n) = $node_id
        RETURN n
        """
        params = {"node_id": node_id}

        res = session.run(query, params).data()

        return t.pipe(
            res,
            t.partial(t.pluck, "n"),
            list
        )

@curry
def delete_all_nodes(node_type: str) -> Dict[str, Any]:
    with driver.session() as session:
        query = f"""
        MATCH (n:{node_type})
        DETACH DELETE n
        RETURN COUNT(*) as deletedCount
        """
        res = session.run(query).single()["deletedCount"]
        return {"success": res > 0, "deletedCount": res}

@curry
def create_relationship(relationship_type: str,source_type: str,target_type: str,source_node_id: int, target_node_id: int,
                        relationship_props: Dict[str, Any] = None) -> Maybe:
    with driver.session() as session:
        props_clause = ""
        if relationship_props:
            props_clause = f"{{ {', '.join([f'{k}: ${k}' for k in relationship_props.keys()])} }}"
        query = f"""
            MATCH (s:{source_type}) WHERE s.id = $source_node_id
            MATCH (t:{target_type}) WHERE t.id = $target_node_id
            MERGE (s)-[r:{relationship_type} {props_clause}]->(t)
            RETURN r
            """
        params = {"source_node_id": source_node_id, "target_node_id": target_node_id, **(relationship_props or {})}
        res = session.run(query, params).single()
        return Maybe.from_optional(res).map(itemgetter('r')).map(lambda x: dict(x))