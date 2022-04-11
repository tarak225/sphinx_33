
.. _$_02-core-19-non-composition:

====================
Non-composition Data
====================

.. _return-to-top-02-core-19-non-composition:

This section addresses:

.. rst:role:: USDA #9

   Support input and storage of various non-composition data types (metabolomic profiles; DNA barcodes; taxonomic information; and chromatographic and spectral profiles).

.. attention::

   This section applies to :ref:`USDA prime data <terms-USDA-Prime>`, not to :ref:`USDA select data <terms-USDA-Select>`. For explanation of USDA prime and USDA select data, see `Deposition Workflow <$_02-core-10-deposition-1-OnLine-OnMessage.html#deposition-workflow>`_

Table of Contents
-----------------

.. contents::
   :depth: 1
   :local:

-------------------------------------
Chromatographic and Spectral Profiles
-------------------------------------

Ontomatica deposition service integrates the following terms for use by :ref:`investigators <terms-Investigator>` |_| when depositing chromatographic and spectral profiles.

The `Physico-chemical methods and properties ontology <http://www.ontobee.org/browser/index.php?o=FIX>`_ (FIX) has been parsed and each term below is referenceable. The HUPO Proteomics `Mass Spectrometry ontology <http://www.psidev.info/>`_ (MS) has not been parse. Instead, Ontomatica uses the Essepuntato `Live OWL Documentation Service <http://www.essepuntato.it/lode>`_ (LODE) to display the `MS ontology <http://www.essepuntato.it/lode/owlapi/http://www.ontomatica.com/public/organizations/BETV/ms.owl>`_. Be patient while the LODE service parses the MS ontology OWL file. Once displayed, each facet term code below is searchable.

Ontomatica deposition service will enable :ref:`investigators <terms-Investigator>` |_| to deposit data like this data from USDA:

- Fingerprint data for `Glucoraphanin from Brassica oleracea, genotype Legacy <https://docs.google.com/spreadsheet/pub?key=0ArcX1zlTGgmjdEFpbWNoTTJRMThYVFVCaWFBN3A5RUE&output=html>`_

- Note that spectral data is presented for five different methods of analysis.

In the table below a **Section** is upper case bold and a *Topic* |_| is upper case italic. The spectral term is lower case and associated with its facet term code.

.. csv-table::
   :header: "Spectral Profile Information", "Ontology Term"
   
   "*Deposit Accession*", "`EDAM:data_2091 <http://edamontology.org/data_2091>`_"
   "*Deposit Title*", "`dc:title <http://dublincore.org/documents/2012/06/14/dcmi-terms/?v=terms#title>`_"
   "*Analysis Date*", "`Time <http://www.w3.org/TR/owl-time/>`_"
   "*Deposit Creation, Last Modification Date*", "`Time <http://www.w3.org/TR/owl-time/>`_"
   "*Authors and Affiliations of Deposit*", "`vCard <http://www.w3.org/TR/vcard-rdf/>`_"
   "*Creative Commons License of Re-use of Deposit*", "`Creative Commons <http://creativecommons.org/ns>`_"
   "*Copyright of Deposit*", "`Creative Commons <http://creativecommons.org/ns>`_"
   "*Reference to Spectral Data*", "`CHEMINF_000302 <http://semanticscience.org/resource/CHEMINF_000302>`_"
   "---", "---"
   "**Chemical Compound Information**", ""
   "*Name of Chemical Compound Analyzed*", "`CHEMINF_000140 <http://semanticscience.org/resource/CHEMINF_000140>`_"
   "*Category of Chemical Compound*", "ChEFS"
   "*Molecular Formula of Chemical Compound*", "`CHEMINF_000037 <http://semanticscience.org/resource/CHEMINF_000037>`_"
   "*Monoisotopic Mass of Chemical Compound*", "`CHEMINF_000218 <http://semanticscience.org/resource/CHEMINF_000218>`_"
   "*SMILES String*", "`CHEMINF_000020 <http://semanticscience.org/resource/CHEMINF_000020>`_"
   "*IUPAC International Chemical Identifier (InChIKey)*", "`CHEMINF_000059 <http://semanticscience.org/resource/CHEMINF_000059>`_"
   "**Biological Sample Information**", ""
   "*Identity of Biological Species*", "`EDAM:data_1875 <http://edamontology.org/data_1875>`_"
   "---", "---"
   "**Method of Analysis Information**", ""
   "*Instrument model*", "`MS_1000031 <http://www.essepuntato.it/lode/owlapi/http://www.ontomatica.com/public/organizations/BETV/ms.owl>`_"
   "*Ion analyzer type*", ""
   "chromatography by separation mechanism", "`FIX_0000610 <http://purl.obolibrary.org/obo/FIX_0000610>`_"
   "capillary electrophoresis", "`FIX_0000836 <http://purl.obolibrary.org/obo/FIX_0000836>`_"
   "gas chromatography", "`FIX_0000098 <http://purl.obolibrary.org/obo/FIX_0000098>`_"
   "liquid chromatography", "`FIX_0000608 <http://purl.obolibrary.org/obo/FIX_0000608>`_"
   "*Ionization methods*", "`MS_1000008 <http://www.essepuntato.it/lode/owlapi/http://www.ontomatica.com/public/organizations/BETV/ms.owl>`_"
   "atmospheric pressure ionization mass spectrometry", "`FIX_0000908 <http://purl.obolibrary.org/obo/FIX_0000908>`_"
   "atmospheric pressure photoionization mass spectrometry", "`FIX_0000907 <http://purl.obolibrary.org/obo/FIX_0000907>`_"
   "electron ionization mass spectrometry", "`FIX_0000089 <http://purl.obolibrary.org/obo/FIX_0000089>`_"
   "electrospray ionization mass spectroscopy", "`FIX_0000079 <http://purl.obolibrary.org/obo/FIX_0000079>`_"
   "fast atom bombardment mass spectrometry", "`FIX_0000086 <http://purl.obolibrary.org/obo/FIX_0000086>`_"
   "matrix-assisted laser desorption/ionization mass spectrometry", "`FIX_0000081 <http://purl.obolibrary.org/obo/FIX_0000081>`_"
   "APCI", "`MS_1000070 <http://www.essepuntato.it/lode/owlapi/http://www.ontomatica.com/public/organizations/BETV/ms.owl>`_"
   "APPI", "`MS_1000382 <http://www.essepuntato.it/lode/owlapi/http://www.ontomatica.com/public/organizations/BETV/ms.owl>`_"
   "EI", "`MS_1000389 <http://www.essepuntato.it/lode/owlapi/http://www.ontomatica.com/public/organizations/BETV/ms.owl>`_"
   "ESI", "`MS_1000073 <http://www.essepuntato.it/lode/owlapi/http://www.ontomatica.com/public/organizations/BETV/ms.owl>`_"
   "B", "`MS_1000080 <http://www.essepuntato.it/lode/owlapi/http://www.ontomatica.com/public/organizations/BETV/ms.owl>`_"
   "IT", "`MS_1000264 <http://www.essepuntato.it/lode/owlapi/http://www.ontomatica.com/public/organizations/BETV/ms.owl>`_"
   "Q", "`MS_1000081 <http://www.essepuntato.it/lode/owlapi/http://www.ontomatica.com/public/organizations/BETV/ms.owl>`_"
   "TOF", "`MS_1000084 <http://www.essepuntato.it/lode/owlapi/http://www.ontomatica.com/public/organizations/BETV/ms.owl>`_"
   "*Fourier transformation*", ""
   "Fourier transform-ion cyclotron resonance mass spectrometry", "`FIX_0000083 <http://purl.obolibrary.org/obo/FIX_0000083>`_"
   "*Ion trap analyzer*", ""
   "ion trap mass spectrometry", "`FIX_0000917 <http://purl.obolibrary.org/obo/FIX_0000917>`_"
   "*Data Type*", ""
   "MSn spectrum", "`MS_1000580 <http://www.essepuntato.it/lode/owlapi/http://www.ontomatica.com/public/organizations/BETV/ms.owl>`_"
   "precursor ion spectrum", "`MS_1000341 <http://www.essepuntato.it/lode/owlapi/http://www.ontomatica.com/public/organizations/BETV/ms.owl>`_"
   "*Polarity of Ion Detection*", ""
   "positive thermal ionization mass spectrometry", "`FIX_0000914 <http://purl.obolibrary.org/obo/FIX_0000914>`_"
   "positive thermal ionization mass spectrometry", "`MS_1000030 <http://www.essepuntato.it/lode/owlapi/http://www.ontomatica.com/public/organizations/BETV/ms.owl>`_"
   "negative thermal ionization mass spectrometry", "`FIX_0000915 <http://purl.obolibrary.org/obo/FIX_0000915>`_"
   "negative thermal ionization mass spectrometry", "`MS_1000129 <http://www.essepuntato.it/lode/owlapi/http://www.ontomatica.com/public/organizations/BETV/ms.owl>`_"
   "Ion mode", "`MS_1000465 <http://www.essepuntato.it/lode/owlapi/http://www.ontomatica.com/public/organizations/BETV/ms.owl>`_"
   "*Collision Energy for Dissociation*", ""
   "collision energy", "`MS_1000045 <http://www.essepuntato.it/lode/owlapi/http://www.ontomatica.com/public/organizations/BETV/ms.owl>`_"
   "*Name of Collision Gas*", "ChEFS"
   "collision gas", "`MS_1000419 <http://www.essepuntato.it/lode/owlapi/http://www.ontomatica.com/public/organizations/BETV/ms.owl>`_"
   "*Flow Rate of Desolvation Gas*", ""
   "ion desolvation", "`MS_1000390 <http://www.essepuntato.it/lode/owlapi/http://www.ontomatica.com/public/organizations/BETV/ms.owl>`_"
   "flow rate array", "`MS_1000820 <http://www.essepuntato.it/lode/owlapi/http://www.ontomatica.com/public/organizations/BETV/ms.owl>`_"
   "*Temperature of Desolvation Gas*", ""
   "temperature array", "`MS_1000822 <http://www.essepuntato.it/lode/owlapi/http://www.ontomatica.com/public/organizations/BETV/ms.owl>`_"
   "*Matrix Used in MALDI*", ""
   "MALDI matrix application", "`MS_1000832 <http://www.essepuntato.it/lode/owlapi/http://www.ontomatica.com/public/organizations/BETV/ms.owl>`_"
   "*Name of Reagent Gas*", "ChEFS"
   "*Retention Time on Chromatography*", ""
   "Retention time", "`MS_1000016 <http://www.essepuntato.it/lode/owlapi/http://www.ontomatica.com/public/organizations/BETV/ms.owl>`_"
   "---", "---"
   "**Mass Spectral Data Description**", ""
   "*m/z of Base Peak*", ""
   "base peak", "`MS_1000210 <http://www.essepuntato.it/lode/owlapi/http://www.ontomatica.com/public/organizations/BETV/ms.owl>`_"
   "*Molecular Formula of Derivative*", "PubChem"
   "*Mass of Derivative*", "PubChem"
   "*Type of Focused Ion*", "see footnote [1]_"
   "*m/z of Precursor Ion in MSn spectrum*", ""
   "msPrefix precursor recalculation", "`MS_1000781 <http://www.essepuntato.it/lode/owlapi/http://www.ontomatica.com/public/organizations/BETV/ms.owl>`_"
   "precursor m/z", "`MS_1000504 <http://www.essepuntato.it/lode/owlapi/http://www.ontomatica.com/public/organizations/BETV/ms.owl>`_"
   "*Type of Precursor Ion in MSn*", ""
   "Precursor type", "`MS_ 1000792 <http://www.essepuntato.it/lode/owlapi/http://www.ontomatica.com/public/organizations/BETV/ms.owl>`_"
   "Precursor type", "see footnote [2]_"
   "---", "---"
   "**Mass Spectral Peaks Information**", ""
   "*Data Processing Method of Peak Detection*", ""
   "Data processing", "`MS_1000543 <http://www.essepuntato.it/lode/owlapi/http://www.ontomatica.com/public/organizations/BETV/ms.owl>`_"
   "*Peak Detection*", ""
   "selected ion detection", "`MS_1000091 <http://www.essepuntato.it/lode/owlapi/http://www.ontomatica.com/public/organizations/BETV/ms.owl>`_"
   "peak picking", "`MS_1000035 <http://www.essepuntato.it/lode/owlapi/http://www.ontomatica.com/public/organizations/BETV/ms.owl>`_"
   "*Total Number of Peaks*", ""
   "number of matched peaks", "`MS_1001121 <http://www.essepuntato.it/lode/owlapi/http://www.ontomatica.com/public/organizations/BETV/ms.owl>`_"

Footnotes
^^^^^^^^^

.. [1] Type of Focused Ion. Available types are:

   [M]+, [M]+*, [M+H]+, [2M+H]+, [M+Na]+, [M-H+Na]+, [2M+Na]+, [M+2Na-H]+, [(M+NH3)+H]+, [M+H-H2O]+, [M+H-C6H10O4]+, [M+H-C6H10O5]+, [M]-, [M-H]-, [M-2H]-, [M-2H+H2O]-, [M-H+OH]-, [2M-H]-, [M+HCOO-]-, [(M+CH3COOH)-H]-, [2M-H-CO2]- and [2M-H-C6H10O5]-

.. [2] Precursor type. Available types are:

   [M]+, [M]+*, [M+H]+, [2M+H]+, [M+Na]+, [M-H+Na]+, [2M+Na]+, [M+H-C6H10O4]+, [M-H+OH]-, [M+2Na-H]+, [M+H-C6H10O5]+, [2M-H]-, [M+HCOO-]-, [M]-, [(M+NH3)+H]+, [M+H-H2O]+, [M-H]-, [M-2H+H2O]-, [M-2H]-, [(M+CH3COOH)-H]-, [2M-H-CO2]- and [2M-H-C6H10O5]-

--------------------
Metabolomic Profiles
--------------------

From Wikipedia:

   Metabolomics is the scientific study of chemical processes involving metabolites. Specifically, metabolomics is the "systematic study of the unique chemical fingerprints that specific cellular processes leave behind", the study of their small-molecule metabolite profiles. The metabolome represents the collection of all metabolites in a biological cell, tissue, organ or organism, which are the end products of cellular processes. mRNA gene expression data and proteomic analyses reveal the set of gene products being produced in the cell, data that represents one aspect of cellular function. Conversely, metabolic profiling can give an instantaneous snapshot of the physiology of that cell. One of the challenges of systems biology and functional genomics is to integrate proteomic, transcriptomic, and metabolomic information to provide a better understanding of cellular biology.

Ontomatica Coverage
^^^^^^^^^^^^^^^^^^^

ChEMATIC discussion here

---------------------
Taxonomic Information
---------------------

Replay taxonomic data in several production databases.

:ref:`Return to top <return-to-top-02-core-19-non-composition>`

.. |_| unicode:: 0x80
