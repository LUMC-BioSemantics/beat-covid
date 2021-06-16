# CQ3 – What are is the measurement value for a specific cytokine from a specific patient in a specific measurement process?

# person_ has_role person_study_role_; 
# person_study_id_ denotes person_study_role_; 
# person_study_role is_realized_in measurement_process_ ; 
# measurement_process_X has_output lumc_CCL21_1 ; 
# lumc_CCL21_1 has_value “123” ; 
# measurement_process_X has_target trait_cytokine_Y ; 
# trait_cytokine_Y is_encoded_by cytokine_Z ; 

# LUMC prefixes
PREFIX rdf:     <http://www.w3.org/1999/02/22-rdf-syntax-ns#> 
PREFIX rdfs:    <http://www.w3.org/2000/01/rdf-schema#> 
PREFIX xsd:     <http://www.w3.org/2001/XMLSchema#> 
PREFIX owl:     <http://www.w3.org/2002/07/owl#> 
PREFIX dct:     <http://purl.org/dc/terms/> 
PREFIX obo:     <http://purl.obolibrary.org/obo/>
PREFIX ncit:    <http://ncicb.nci.nih.gov/xml/owl/EVS/Thesaurus.owl#> 
PREFIX sio:     <http://semanticscience.org/resource/> 
PREFIX prov:    <http://http://http://www.w3.org/ns/prov#>
PREFIX bc:      <https://rdf.biosemantics.org/resources/beat-covid/>
PREFIX lco:     <http://purl.org/beat-covid/lco.owl#>

SELECT ?patient_id ?quantitative_trait WHERE {
    ?person a sio:SIO_000498;
              sio:SIO_000228 ?person_study_role .

    ?person_study_role a sio:SIO_000883 ;
                         sio:SIO_000356 ?measurement_process .
    
    ?patient_id a lco:beat_covid_id ;
                  sio:SIO_000300 "BEAT-018"^^xsd:string ;
                  obo:IAO_0000219 ?person_study_role .

    ?measurement_process a obo:OBI_0000070 ;
                           sio:SIO_000291 ?trait_cytokine ;
                           sio:SIO_000229 ?quantitative_trait .

    ?quantitative_trait a obo:IAO_0000109 .

    ?trait_cytokine a sio:SIO_010043 ;
                      sio:SIO_010079 ?cytokine .
    
    ?cytokine a sio:SIO_010035 .
    
    FILTER(?patient_id = "")
    FILTER(?cytokine = "")
} 
