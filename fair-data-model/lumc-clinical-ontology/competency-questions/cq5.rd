# QC5 - What are the cytokine measurement values and the disease severity score answers for a specific patient? 

# person has_role person_study_role 
# person_study_role is realized in measurement_process_; 
  
# measurement_process has_target trait_cytokine_; 
# measurement_process has_quality measurement_process_date_; 
  
# trait_cytokine is_encoded_by cytokine_; 
# trait_cytokine has_measurment_value lum_CCL21_1; 
  
# person has_role person_patient_role_; 
# person_patient_role is realized in severity_score_evaluation_process_; 
  
# severity_score_evaluation_process_ has_input severity_score_measurement_method_; 
# severity_score_measurement_method has_value “Leiden Severity Score”; 
  
# severity_score_evaluation_process_ has_output severity_score_answer_; 
# severity_score_evaluation_process has_quality severity_score_evaluation_process_date_;  

# LUMC prefixes
PREFIX rdf:     <http://www.w3.org/1999/02/22-rdf-syntax-ns#> 
PREFIX rdfs:    <http://www.w3.org/2000/01/rdf-schema#> 
PREFIX xsd:     <http://www.w3.org/2001/XMLSchema#> 
PREFIX owl:     <http://www.w3.org/2002/07/owl#> 
PREFIX dc:     <http://purl.org/dc/terms/> 
PREFIX obo:     <http://purl.obolibrary.org/obo/>
PREFIX ncit:    <http://ncicb.nci.nih.gov/xml/owl/EVS/Thesaurus.owl#> 
PREFIX sio:     <http://semanticscience.org/resource/> 
PREFIX prov:    <http://http://http://www.w3.org/ns/prov#>
PREFIX bc:      <https://rdf.biosemantics.org/resources/beat-covid/>
PREFIX lco:     <http://purl.org/beat-covid/lco.owl#>
PREFIX om:      <http://www.ontology-of-units-of-measure.org/resource/om-2/>

SELECT ?patient_id ?quantitative_trait ?severity_score_answer ?measurement_process_date_ ?severity_score_evaluation_process_date  WHERE {
    ?person a sio:SIO_000498 ;
              sio:SIO_000228 ?person_patient_role ;
              sio:SIO_000228 ?person_study_role .
              

    ?person_patient_role a sio:SIO_000715 ;
                         sio:SIO_000356 ?severity_score_evaluation_process  .

    ?person_study_role a sio:SIO_000883 ;
                         sio:SIO_000356 ?measurement_process .
    
    ?patient_id a lco:clinical_id  ;
                  obo:IAO_0000219 ?person_patient_role .

    ?measurement_process a obo:OBI_0000070 ;
                           sio:SIO_000291 ?trait_cytokine ;
                           sio:SIO_000229 ?quantitative_trait ;
                           sio:SIO_000008 ?measurement_process_date .
    
    ?measurement_process_date_ a obo:NCIT_C25164 .

    ?severity_score_evaluation_process a obo:NCIT_C25214 ;
                                         sio:SIO_000229 ?severity_score_answer ;
                                         dc:conformsTo ?severity_score_measurement_method ;
									     sio:SIO_000217 ?severity_score_evaluation_process_date .

    ?severity_score_evaluation_process_date a obo:NCIT_C25164 .

    ?severity_score_measurement_method a obo:NCIT_C81265 ;
                                         dc:hasVersion ?severity_score_measurement_version ;
                                         om:hasScale ?severity_score_result_scale .

    ?severity_score_answer a obo:CMO:0001109 .

    ?severity_score_result_scale a obo:NCIT:C25664 ;
                                   obo:LABO_0000118 ?scale_min ;
							       obo:LABO_0000119 ?scale_max .

    ?quantitative_trait a obo:IAO_0000109 .

    ?trait_cytokine a sio:SIO_010043 ;
                      sio:SIO_010079 ?cytokine .
    
    ?cytokine a sio:SIO_010035 .

    FILTER(?patient_id = "")
} 
