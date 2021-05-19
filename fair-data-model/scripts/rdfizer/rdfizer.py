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
def generate_rdf(variables_dict):
    """
    This function generates an RDF data structure from a tuple of values
    :param variables_dict:
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
    if not variables_dict['clinical_id']: variables_dict['clinical_id'] = "NA"
    person = bc["person/BEATCOVID_" + variables_dict['beat_id'] + "_CLINICAL_" + variables_dict['clinical_id']]
    sample = bc["sample/BEATCOVID_" + variables_dict['record_id']]

    # add triples to entry
    # LAB MEASUREMENTS (MEASUREMENT PROCESS)
    i = 0
    for measurement in variables_dict.keys():
        if "lum_date_" in measurement: continue
        if "lum" in measurement:
            i += 1
            device_string, protein_string, kit_string = measurement.split("_")
            # kit
            kit = bc["lab/kit_" + kit_string]
            # device
            device = bc["lab/device_" + device_string]
            # measurement process date
            measurement_process_date = bc["lab/measurement_process_date/BEATCOVID_"
                                          + variables_dict['lum_date_meas']]
            # attribute/object
            trait = bc["trait/BEATCOVID_" + variables_dict['record_id']
               + protein_string]
            # gene
            gene = bc["gene/" + i.zfill(5)]
            # role
            person_study_role = bc["role/BEATCOVID_" + variables_dict['beat_id']
                                   + variables_dict['record_id']]
            # ward
            # institute
            # person age
            # identifier
            # measurement
            quantitative_trait = bc["lab/quantitative_trait/BEATCOVID_" + variables_dict['record_id']
                                  + measurement]
            # unit
            #print(i, measurement, device, protein, kit)
            # lab measurement process
            lab_meas_process = bc["lab/measurement_process/BEATCOVID_" + variables_dict['record_id']
                                  + measurement]
            rdf.add((lab_meas_process, RDF.type, obo.OBI_0000070))
            
    rdf.add((person, RDF.type, obo.OBI_0000070))

    # sample process entry
    rdf.add((sample, RDF.type, sio.SIO_001049))

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
    out_path = "/home/nur/workspace/beat-covid/fair-data-model/rdf"
    if not os.path.isdir(out_path): os.makedirs(out_path)
    header = 1
    rows_list = list()
    for line in open("/home/nur/workspace/beat-covid/fair-data-model/cytokine/synthetic-data/BEAT-COVID1_excel_export_2020-05-28_Luminex_synthetic-data.csv"):
        if header:
                header_tuple = line.rstrip().split("\t")
                header = 0
                continue
        values_tuple = line.rstrip().split("\t")
        raw_data_dict = dict(zip(header_tuple,values_tuple))
        rows_list.append(raw_data_dict)
    for row in rows_list:
        crf = generate_rdf(row)
        crf.serialize(f"{out_path}/{row['record_id'].zfill(5)}.ttl", format="turtle")
        #print(f"row: {row}\nheader: {header_tuple}\nvalues: {values_tuple}")
    print(f"row: {row}")

