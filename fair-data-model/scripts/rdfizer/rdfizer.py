# @name: rdfizer.py
# @description: Script to generate RDF data
# @version: 1.0
# @date: 28-04-2021
# @author: Núria Queralt Rosinach
# @email: n.queralt_rosinach@lumc.nl

"""Script to generate RDF data for Beat-COVID cytokine clinical measurements"""

import sys, os
from rdflib import Namespace, Graph, BNode, Literal
from rdflib.namespace import RDF, RDFS, XSD, DCTERMS

# Prefixes
bc = Namespace("https://rdf.biosemantics.org/resources/beat-covid/")
bco = Namespace("http://purl.org/beat-covid/cytokines-semantic-model.owl#")
obo = Namespace("http://purl.obolibrary.org/obo/")
sio = Namespace("http://semanticscience.org/resource/")
efo = Namespace("http://www.ebi.ac.uk/efo/")
prov = Namespace("http://http://http://www.w3.org/ns/prov#")

has_output = sio.SIO_000229
has_value = sio.SIO_000300

# Functions
def generate_rdf(variables_tuple):
    """
    This function generates an RDF data structure from a tuple of values
    :param variables_tuple:
    :return:
    """

    # binds
    rdf = Graph()
    rdf.bind("bc", bc)
    rdf.bind("bco", bco)
    rdf.bind("obo", obo)
    rdf.bind("sio", sio)
    rdf.bind("efo", efo)
    rdf.bind("prov", prov)

    # entry
    lab = bc[variables_tuple[0]]
    sample = bc[variables_tuple[0]]

    # add triples to entry
    # lab measurement process entry
    rdf.add(lab, RDF.type, bco.OBI_0000070)

    # sample process entry
    rdf.add(sample, RDF.type, bco.SIO_001049)

    return rdf


if __name__ == "__main__":
    # # args
    # if len(sys.argv) < 3:
    #     print("Missing input parameters. Usage:")
    #     print(f"\tpython {sys.arv[0] cytokine_csv_file_path rdf_dir_path}")
    #     exit(1)
    #
    # # output
    # out_path = sys.argv[2]
    # if not os.path.isdir(out_path): os.makedirs(out_path)
    #
    # # rdf
    # with open(sys.argv[1]) as file:
    #     # skip header
    #     next(file)
    #
    #     for line in file:
    #         values_tuple = line.rstrip().split(",")
    #         rdf = generate_rdf(values_tuple)
    #         rdf.serialize(f"{out_path}/{values_tuple[0].zfill(5)}.ttl", format="turtle")
    for line in open("/home/nur/workspace/beat-covid/fair-data-model/cytokine/synthetic-data/BEAT-COVID1_excel_export_2020-05-28_Luminex_synthetic-data.csv"):
        print(f"{line}")