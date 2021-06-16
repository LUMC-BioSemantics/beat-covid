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

    # entries
    # Entity
    if not variables_dict['clinical_id']: variables_dict['clinical_id'] = "NA"
    person = bc["person/BEATCOVID_" + variables_dict['beat_id'] + "_CLINICAL_" + variables_dict['clinical_id']]

    # LAB MEASUREMENTS (MEASUREMENT PROCESS) MODEL
    # Identifier
    person_study_id = bc["person_study_id/" + variables_dict['beat_id']]

    # Role
    person_study_role = bc["person_study_role/BEATCOVID_" + variables_dict['record_id']
                           + "_" + variables_dict['beat_id']]

    # age
    age = bc["person_age/" + variables_dict['age']]

    # ward
    ward = bc["ward/" + variables_dict['ward']]

    # institute
    institute = bc["institute/" + variables_dict['institute_abbreviation']]

    # measurement process date
    measurement_process_date = bc["lab/measurement_process_date/BEATCOVID_"
                                  + variables_dict['lum_date_meas']]

    # BIOSAMPLES (SAMPLING PROCESS) MODEL
    # Biosample
    biosample = bc["biosample/BEATCOVID_" + variables_dict['record_id']]

    # Process
    sampling_process = bc["biosample/sampling_process/BEATCOVID_"
                          + variables_dict['record_id']]

    # order
    order = bc["biosample/order_" + variables_dict['order']]

    # sampling process date
    sampling_process_date = bc["biosample/sampling_process_date/BEATCOVID_"
                               + variables_dict['date_sampling']]

    # Attribute/object
    organ = "blood_serum"
    biosample_object = bc["object/" + organ]

    # Role
    person_donor_role = bc["person_donor_role/BEATCOVID_" + variables_dict['record_id']]

    # Identifier
    person_donor_id = bc["person_donor_id/" + variables_dict['beat_id']]
    biosample_id = bc["biosample/biosample_id/BEATCOVID_" + variables_dict['record_id']]


    # CLINICAL OBSERVATIONS (EXAMINATION PROCESS) MODEL
    # Identifier
    clinical = bc["clinical/patient_id/" + variables_dict['clinical_id']]

    # Observation
    # observation = bc["clinical/observation/BEATCOVID_" + variables_dict['clinical_observations']]



    # add triples to entry
    # LAB MEASUREMENTS (MEASUREMENT PROCESS) MODEL
    # Entity
    rdf.add((person, RDF.type, sio.SIO_000498))
    rdf.add((person, sio.SIO_000228, person_study_role))
    rdf.add((person, sio.SIO_000228, person_donor_role))
    #rdf.add((person, sio.SIO_000228, person_patient_role))
    #rdf.add((person, sio.SIO_000008, bc.phenotype_))


    # Identifier
    rdf.add((person_study_id, RDF.type, bco.beat_covid_id))
    rdf.add((person_study_id, sio.SIO_000300, Literal(variables_dict['beat_id'], datatype=XSD.string)))
    rdf.add((person_study_id, obo.IAO_0000219, person_study_role))

    # age
    rdf.add((age, RDF.type, sio.SIO_001013))
    rdf.add((age, sio.SIO_000300, Literal(variables_dict['age'], datatype=XSD.integer)))
    rdf.add((age, sio.SIO_000001, person_study_role))

    # ward
    rdf.add((ward, RDF.type, obo.NCIT_C21541))
    rdf.add((ward, sio.SIO_000300, Literal(variables_dict['ward'], datatype=XSD.string)))
    rdf.add((ward, RDFS.label, Literal(variables_dict['ward'], lang='en')))
    rdf.add((ward, obo.BFO_0000050, institute))

    # institute
    rdf.add((institute, RDF.type, sio.SIO_000688))
    rdf.add((institute, sio.SIO_000300, Literal(variables_dict['institute_abbreviation'], datatype=XSD.string)))
    rdf.add((institute, RDFS.label, Literal(variables_dict['institute_abbreviation'], lang='en')))

    # Role
    rdf.add((person_study_role, RDF.type, sio.SIO_000883))
    rdf.add((person_study_role, obo.RO_0001025, ward))
    rdf.add((person_study_role, obo.RO_0001025, institute))

    # measurement process date
    rdf.add((measurement_process_date, RDF.type, obo.NCIT_C25164))
    rdf.add((measurement_process_date, DCTERMS.date, Literal(variables_dict['lum_date_meas'], datatype=XSD.date)))


    # BIOSAMPLES (SAMPLING PROCESS) MODEL
    # Process
    rdf.add((sampling_process, RDF.type, sio.SIO_001049))
    rdf.add((sampling_process, sio.SIO_000291, biosample_object))
    rdf.add((sampling_process, sio.SIO_000230, person))
    rdf.add((sampling_process, sio.SIO_000229, biosample))
    rdf.add((sampling_process, obo.RO_0002091, order))
    rdf.add((sampling_process, sio.SIO_000008, sampling_process_date))

    # Biosample
    rdf.add((biosample, RDF.type, sio.SIO_001050))
    rdf.add((biosample, sio.SIO_000628, biosample_object))

    # Attribute/object
    rdf.add((biosample_object, RDF.type, sio.SIO_010003))
    rdf.add((biosample_object, obo.BFO_0000050, person))

    # order
    rdf.add((order, RDF.type, obo.NCIT_C48906))
    rdf.add((order, sio.SIO_000300, Literal(variables_dict['order'], datatype=XSD.string)))

    # sampling process date
    rdf.add((sampling_process_date, RDF.type, obo.NCIT_C25164))
    rdf.add((sampling_process_date, DCTERMS.date, Literal(variables_dict['date_sampling'], datatype=XSD.date)))

    # Role
    rdf.add((person_donor_role, RDF.type, obo.OBI_1110087))
    rdf.add((person_donor_role, sio.SIO_000356, sampling_process))

    # Identifier
    # biosample
    rdf.add((biosample_id, RDF.type, bco.record_id))
    rdf.add((biosample_id, sio.SIO_000300, Literal(variables_dict['record_id'], datatype=XSD.string)))
    rdf.add((biosample_id, sio.SIO_000672, biosample))
    # person_donor
    rdf.add((person_donor_id, RDF.type, obo.NCIT_C164796))
    rdf.add((person_donor_id, obo.IAO_0000219, person_donor_role))


    # CLINICAL OBSERVATIONS (EXAMINATION PROCESS) MODEL
    # Identifier
    rdf.add((clinical, RDF.type, bco.clinical_id))

    # Observation
    # observation = bc["clinical/observation/BEATCOVID_" + variables_dict['clinical_observations']]

    # Lab measurement information
    measurement_number = 0
    for measurement in variables_dict.keys():
        if "lum_date_" in measurement:
            continue
        if "lum" in measurement:
            measurement_number += 1
            device_string, protein_string, kit_string = measurement.split("_")
            # kit
            kit = bc["lab/kit_" + kit_string]
            rdf.add((kit, RDF.type, obo.OBI_0000272))
            rdf.add((kit, sio.SIO_000300, Literal(kit_string, datatype=XSD.string)))
            rdf.add((kit, RDFS.label, Literal(f"Kit {kit_string}", lang='en')))
            # device
            device = bc["lab/device_" + device_string]
            rdf.add((device, RDF.type, obo.OBI_0000968))
            rdf.add((device, sio.SIO_000300, Literal(device_string, datatype=XSD.string)))
            if device_string == "lum":
                rdf.add((device, RDFS.label, Literal("Luminex", lang='en')))
            # Attribute/object
            trait = bc["trait/" + protein_string]
            rdf.add((trait, RDF.type, sio.SIO_010043))
            rdf.add((trait, sio.SIO_000300, Literal(protein_string, datatype=XSD.string)))
            rdf.add((trait, obo.BFO_0000050, person))
            # cytokine gene
            gene = bc["gene/" + protein_string]
            rdf.add((gene, RDF.type, sio.SIO_010035))
            rdf.add((trait, sio.SIO_010079, gene))
            # Measurement
            quantitative_trait = bc["lab/quantitative_trait/BEATCOVID_" + variables_dict['record_id']
                                    + "_" + measurement + "_" + str(measurement_number)]
            rdf.add((quantitative_trait, RDF.type, obo.IAO_0000109))
            rdf.add((quantitative_trait, RDFS.label, Literal(measurement, datatype=XSD.string)))
            rdf.add((quantitative_trait, sio.SIO_000221, efo.EFO_0004385))
            if variables_dict[measurement] == 'OOR <' or variables_dict[measurement] == 'OOR >':
                rdf.add((quantitative_trait, sio.SIO_000300, Literal(variables_dict[measurement], datatype=XSD.string)))
            else:
                rdf.add((quantitative_trait, sio.SIO_000300, Literal(variables_dict[measurement], datatype=XSD.float)))
            rdf.add((quantitative_trait, sio.SIO_000628, trait))
            rdf.add((trait, sio.SIO_000216, quantitative_trait))
            # unit
            unit = bc["lab/measurement_unit/pg_ml"]
            rdf.add((unit, RDF.type, obo.IAO_0000003))
            rdf.add((unit, RDFS.label, Literal("pg/ml", datatype=XSD.string)))
            # print(measurement_number, measurement, device, protein, kit)
            # Process
            lab_meas_process = bc["lab/measurement_process/BEATCOVID_" + variables_dict['record_id']
                                  + measurement]
            rdf.add((lab_meas_process, RDF.type, obo.OBI_0000070))
            rdf.add((lab_meas_process, sio.SIO_000291, trait))
            rdf.add((lab_meas_process, sio.SIO_000230, biosample))
            rdf.add((lab_meas_process, sio.SIO_000229, quantitative_trait))
            rdf.add((lab_meas_process, sio.SIO_000008, measurement_process_date))
            rdf.add((lab_meas_process, DCTERMS.conformsTo, kit))
            rdf.add((lab_meas_process, sio.SIO_000132, device))
            rdf.add((lab_meas_process, sio.SIO_000628, clinical))
            rdf.add((lab_meas_process, prov.wasInformedBy, sampling_process))
            # role
            rdf.add((person_study_role, sio.SIO_000356, lab_meas_process))

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
    for line in open("/home/nur/workspace/beat-covid/fair-data-model/cytokine/synthetic-data/"
                     "BEAT-COVID1_excel_export_2020-05-28_Luminex_synthetic-data.csv"):
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
        # print(f"row: {row}\nheader: {header_tuple}\nvalues: {values_tuple}")
    print(f"row: {row}")

