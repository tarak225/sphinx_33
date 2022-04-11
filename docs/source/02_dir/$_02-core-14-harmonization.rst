
.. _$_02-core-14-harmonization:

=========================
Information Harmonization
=========================

.. _return-to-top-02-core-14-harmonization:

This section addresses:

.. rst:role:: USDA #4

   Allow incorporation ARS ontology for ingredients nomenclature with access to external databases.

.. rst:role:: USDA #8

   Provide links to other nutrition-related databases.

Table of Contents
-----------------

.. contents::
   :depth: 3
   :local:

-------------------
Ontomatica Coverage
-------------------

Ontomatica harmonizes terms defined by the :ref:`authorities <terms-Authority>` |_| below.

Our methods create relationships between :ref:`terms <terms-Term>` |_| by using one or more of the following :ref:`predicates <terms-Predicate>` |_|:

:class:`schema:sameAs` :class:`skos:exactMatch` :class:`skos:closeMatch` :class:`skos:relatedMatch`

Harmonization enables a :ref:`depositor <terms-Depositor>` |_| to use the authority's term, rather than an equivalent USDA term. Harmonization is essential for implementing :ref:`USDA prime <terms-USDA-Prime>`.

-----------
Authorities
-----------

.. csv-table::
   :header: "Domain", "Harmonized Terms from Authorities", "Example"
   :widths: 15, 35, 10

   "Bio-chemistry", "USDA ARS chemicals", ""
   "", "UN FAO INFOODS chemicals", ""
   "", "US NIH PubChem chemicals", ""
   "", "ChEBI chemicals", ""
   "", "USDA NALT chemicals", ""
   "", "USDA ARS GrainGenes (for wheat ontology)", ""
   "", "UN FAO AgroVoc chemicals", ""
   "", "Protein Data Bank (PDB) chemicals", ""
   "", "Bio-chemical references in US Code of Federal Regulation", ""
   "", "US NIH NCI Applied Research chemicals", ""
   "", "US NIH NCI thesaurus chemicals", ""
   "", "ChEMBL bioactive compounds", ""
   "", "UniProt bioactive compounds", ""
   "", "PDB bioactive compounds", ""
   "", "US NIH NCBI Structure bioactive compounds", ""
   "", "US NIH NCBI Taxon for bacteria and virus", ""
   "", "US FDA Unique Ingredient Identifiers (UNII)", ""
   "", "Enzyme Commission (EC) identifiers", ""
   "", "DBpedia terms", ""
   "", "Chemical Abstract Society (CAS) identifiers", ""
   "Agricultural commodities", "IR-4 commodities", ""
   "", "UN FAO AgroVoc commodities", ""
   "", "UN FAO CODEX crop groups", ""
   "", "UN FAO CODEX livestock groups", ""
   "", "UN FAO fish commodities", ""
   "", "USDA NALT commodities", ""
   "", "US EPA Food Commodity Intake Data (FCID)", ""
   "", "Agriculture commodity references in US Code of Federal Regulation", ""
   "", "DBpedia terms", ""
   "Food and meals", "USDA ARS Food Patterns Equivalents Data (FPED) identities", ""
   "", "US NIH NCI Applied Research identities", ""
   "", "Food identities in US Code of Federal Regulation", ""
   "", "UN FAO food groups", ""
   "Analytical methods", "UN INFOODS tags for CODEX methods", ""
   "", "AOAC international methods", ""
   "", "Methods associated with specific analytical devices and equipment", ""

-------------
Example: Fish
-------------

.. csv-table::
   :header: "Aquatic term", "UN FAO term code", "EUNIS term code", "DBpedia term", "AgroVoc term code", "NALT term code"
   :widths: 15, 10, 10, 10, 10, 10

   "Common octopus", "cl_species:OCC", "eunis:60605", "dbpedia:Common_Octopus", "agrovoc:c_5307", "nalt:55627"
   "Angler", "cl_species:MON", "eunis:124874", "dbpedia:Lophius_piscatorius", "agrovoc:c_46042", "nalt:201339"
   "Red mullet", "cl_species:MUT", "eunis:124879", "dbpedia:Mullus_barbatus", "agrovoc:c_43349", "nalt:43361"
   "Great Atlantic scallop", "cl_species:SCE", "eunis:60712", "dbpedia:Pecten_maximus", "agrovoc:c_31159", "nalt:57135"
   "Red swamp crawfish", "cl_species:RCW", "eunis:258990", "dbpedia:Procambarus_clarkii", "agrovoc:c_46824", "nalt:50664"
   "Swordfish", "cl_species:SWO", "eunis:124899", "dbpedia:Swordfish", "agrovoc:c_7559", "nalt:65299"
   "Crested flounder", "cl_species:LFG", "", "dbpedia:Crested_flounder", "agrovoc:c_45572", "nalt:40297"
   "Giant grouper", "cl_species:EEN", "", "dbpedia:Giant_grouper", "agrovoc:c_42341", "nalt:40299"
   "Largemouth black bass", "cl_species:MPS", "eunis:10072", "dbpedia:Largemouth_bass", "agrovoc:c_37035", "nalt:52789"
   "Pacific herring", "cl_species:HEP", "eunis:124939", "dbpedia:Pacific_herring", "agrovoc:c_39009", "nalt:40303"
   "Pandalid shrimps", "cl_species:PDZ", "", "dbpedia:Pandalidae", "agrovoc:c_46467", "nalt:31889"
   "Penaeid shrimps", "cl_species:PEZ", "", "dbpedia:Penaeidae", "agrovoc:c_46269", "nalt:31890"

-----------------------------------------
Example: Variety of Frequently Used Terms
-----------------------------------------

.. csv-table::
   :header: "Term", "UN FAO term code", "NALT term code", "DBpedia term"
   :widths: 15, 10, 10, 10

   "Brassica", "agrovoc:c_1060", "nalt:19293", "dbpedia:Brassica"
   "Flavonoids", "agrovoc:c_2964", "nalt:10004", "dbpedia:Flavonoid"
   "food composition", "agrovoc:c_10961", "nalt:10481", "dbpedia:Food_composition_data"
   "Bioavailability", "agrovoc:c_32390", "nalt:10477", "dbpedia:Bioavailability"
   "Nutritive value", "agrovoc:c_5278", "nalt:10486", "dbpedia:Dietary_Reference_Values"
   "Age", "agrovoc:c_186", "nalt:110", "dbpedia:Ageing"
   "Apples", "agrovoc:c_541", "nalt:11308", "dbpedia:Apple"
   "Processed foods", "agrovoc:c_28228", "nalt:15553", "dbpedia:Processed_food"
   "Carbonated beverages", "agrovoc:c_28261", "nalt:16986", "dbpedia:Soft_drink"
   "Fish products", "agrovoc:c_2930", "nalt:9444", "dbpedia:Fish_products"
   "Milk protein", "agrovoc:c_4831", "nalt:9453", "dbpedia:Milk#Physical_and_chemical_structure"

:ref:`Return to top <return-to-top-02-core-14-harmonization>`

.. |_| unicode:: 0x80

