# Using Competency Questions for Data Model Verification

This folder contains Competency Questions (Gruninger & Fox, 1995) that were constructed to verify the semantic model. The set of CQs was extracted, refined and answered with support from domain experts and modellers. In literature, CQs are claimed as an efficient way of testing models, since they are based on real questions. It is also argued that CQs help to define design project requirements, such as adherence to process models and identification of stakeholders (Falbo, 2004).

In this folder, CQS are answered in SPARQL queries for reusability purposes. We are aware of the possibility to checking the model by answering CQs using ShEx or Shacl. However, we decided to use SPARQL since queries can be reused in our project and by external users.

# Reasoning
The questions presented here were built in an attempt to cover all modules from the data model, namely biosample, clinical, lab measurement and severity score.

## CQ1 – What are all the samples (and their annotations) that were collected from a patient?
This question intends to address samples collected for patients, but also the metadata around this concept, such as the target organ and the sampling process date.

## CQ2 - What are the measurement values for the samples collected from a specific patient for a specific measurement process?
This question complements the previous one by adding the values measured from the collected samples. The quantitative traits are the main results of this question.

## CQ3 - What are is the measurement value for a specific cytokine from a specific patient in a specific measurement process?
This question covers the clinical measurement module of our data model, returning cytokine measurement data, but also measurement data, the targeted cytokine and patient.

## CQ4 - What are the severity score measurements of a patient and which measurement method was used?
This question aims to verify the severity score measurement module. Consequently, the result contains data about the severity score measurement value and all metadata about the measurement: date, method, method scale, method version and target patient.

## CQ5 - What are the cytokine measurement values and the disease severity score answers for a specific patient?
This question investigates the relationship between cytokine measurement values and severity score measurement values. By returning structured data about cytokine and severity score (and surrounding metadata), this question intends to leverage the power of the data model in providing structured data for further analysis. This question verifies the connection with the severity score and lab measurement model modules.

## CQ6 - What are the severity score measurement and age of each patient?
The results of this question can be used to find patterns and relationships between severity score measurements and patient properties such as age. The purpose of this question is to relate the severity score measurement module with patient information.

# License
The content of this folder is licensed under the [MIT License](https://opensource.org/licenses/MIT).

# References
- de Almeida Falbo, R. (2014, September). SABiO: Systematic Approach for Building Ontologies. In ONTO. COM/ODISE@ FOIS.
- Grüninger, M., Fox, M.S., Methodology for the Design and Evaluation of Ontologies. Workshop on Basic Ontological Issues in Knowledge Sharing, 1995
