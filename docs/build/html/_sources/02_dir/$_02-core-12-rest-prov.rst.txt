
.. _$_02-core-12-rest-prov:

=========================
REST Services and Reports
=========================

.. _return-to-top-02-core-12-rest-prov:

This section addresses:

.. rst:role:: USDA #6

   Permit export of composition and analytical data and conversion of composition data to an application development format.

.. rst:role:: USDA #10

   Permit assembly of ad hoc databases to suit individual needs.

.. rst:role:: USDA #11

   Permit export of ad hoc data.

Table of Contents
-----------------

.. contents::
   :depth: 3
   :local:

:ref:`Label project <terms-Label-Project>` |_| data will be available to :ref:`investigators <terms-Investigator>` |_| via :ref:`REST <terms-REST>` |_| (Representational State Transfer) services. REST is a simple stateless architecture that runs over HTTP. REST service reads a designated Web page that contains an XML file in RDF format. XML/RDF file describes and includes label project data. Data is returned to investigator in :ref:`JSON-LD <terms-JSON-LD>` |_| format.

.. figure:: $_02-core-12-rest-prov_.png
   :align: center

-----------------------------
General Structure of REST API
-----------------------------

Structure of a USDA REST :ref:`conversation <terms-Conversation>` |_| :

.. http:get:: /input specification/operation specification/output specification/operation_options

Structure of the USDA REST API is:

::

   http://usda.ars.gov/rest/<input specification>/<operation specification>/[<output specification>]/[<operation options>]

Example: "retrieve food description using food identifier :class:`[USDA_fid]` and :ref:`item <terms-Item>` number 2244"

::

   http://usda.ars.gov/rest/food/USDA_fid/2244/JSON

Query Parameters: Input Specification
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Input portion of URL tells service which records to use as subject of query.

This is further subdivided into two or more locations in URL "path" as follows:

:query parameter title: input specification
:query parameter domain: values may include food, compound, Nutrient Fact Panel (NFP) values and other inputs

For example:

::

                               1          2            3
    <input_specification> = <domain>/<namespace>/<identifiers>


                    2.1     2.2        2.3             2.4
    1   <domain> = food | compound | NFP_values | <other inputs>


                                                       2.n.1                                              2.n.2
    2.1    food domain <namespace> = USDA_fid | sourceid/<source name> | sourceall/<source name> | name | <xref>
    
    2.2    compound domain <namespace> = PC_cid | name | inchikey | <xref>


                                                       2.n.3
    2.3    NFP_values domain <namespace> = NFP_id | type/<NFP type> | sourceall/<source name> | activity/<activity column name> | {_to_be_specified_}

    2.n.1     <source_name> = any valid Branded Food depositor name

    2.n.2     <xref> = xref / {RegistryID | RN | NCBI_ProteinGI | NCBI_TaxonomyID }

    2.n.3     <NFP_type> = all | panel | summary | {_to_be_specified_}

    2.4    <other_inputs_to_be_specified_> = sources / [substance, assay] | conformers

    3    <identifiers> = comma-separated list of positive integers (e.g. PC_cid, USDA_fid, NFP_id) or identifier strings (source, inchikey)

Query Parameters: Operation Specification
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Operation part of URL tells service what to do with input records - such as to retrieve whole record or specific properties of a food.

Construction of this part of "path" will depend on Operation Specification. If no operation is specified, default is to retrieve entire record.

Available operations dependent on Input Specification. For example, certain operations are applicable only to foods, compounds and not :class:`NFP_values`.

For example:

::

                                                             1.n.1                                                             1.n.2
    1.1  food domain <operation_specification> = record | <food_property> | synonyms | PC_cids | NFP_values | classification | <xrefs> | description
    
    1.n.1    <food_property> = property / [comma-separated list of property tags]
    
    1.n.2    <xrefs> = xrefs / [comma-separated list of xrefs tags]
    
    1.3  NFP domain <operation_specification> = record | NFP_ids | USDA_fids | PC_cids | description | summary | classification | xrefs

Query Parameters: Output Specification
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Final portion of URL tells service what output format is desired.

Output format also can be specified in HTTP Accept field of request header.

For example:

::

    <output:specification> = JSON | CSV | TXT

Request: Food property tables
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. http:get:: /input specification

Request properties for a food (USDA_fid) or compound (PC_cid).

::

    http://usda.ars.gov/rest/food/USDA_fid/3114/property/JSON

Return food property table
""""""""""""""""""""""""""

.. csv-table::
   :header: "Property", "Notes"
   :widths: 20, 20

   "to_be_specified", "to_be_specified"
   "to_be_specified", "to_be_specified"

Variation: Return Nutrient Fact Panel <NFP_type>
""""""""""""""""""""""""""""""""""""""""""""""""

.. csv-table::
   :header: "Options", "Allowed Values", "meaning"
   :widths: 20, 20, 20

   "NFP_type", "all, primary, secondary", "Type of NFP to return given, USDA_fids, PC_cids"

Variation: Return dates
"""""""""""""""""""""""

.. csv-table::
   :header: "Date", "Meaning"
   :widths: 20, 20

   "Deposition", "when an USDA_fid or NFP_id first appeared"
   "Modification", "when an USDA_fid or NFP_id was last modified"
   "Hold", "when an USDA_fid or NFP_id will be released"
   "Creation", "when a USDA_fid or NFP_id first appeared"
   "Deprecation", "when a USDA_fid or NFP_id is no longer active"

Variation: Return Cross References <xrefs>
""""""""""""""""""""""""""""""""""""""""""

.. csv-table::
   :header: "Cross Reference", "Meaning"
   :widths: 20, 20

   "RegistryID", "external registry identifier"
   "PubMedID", "NCBI PubMed identifier"
   "DBURL", "external database home page URL"
   "TaxonomyID", "NCBI taxonomy identifier"
   "SourceName", "external depositor name"
   "SourceCategory", "depositor category(ies)"

--------------------------------------------------
Quality Control using Provenance Ontology and REST
--------------------------------------------------

Several :ref:`conversation <terms-Conversation>` |_| types will be supported.

For example, Ontomatica :ref:`imports <terms-Import-Ontology>` |_| the Provenance Ontology :class:`[prov]`.

The following illustrates a :ref:`curator <terms-Curator>` |_| using :class:`[prov]`:

- Alanna wishes to verify that a new data set correctly addresses previous error.
- David :class:`[ex:David]` documents Alanna's instructions :class:`[ex:instructions]` in a plan :class:`[prov:Plan]`.
- David then generates a new dataset :class:`[ex:dataset2]` that implements correction activity :class:`[ex:correct1]`.
- Alanna confirms :class:`[prov:Plan]` and executes a :class:`diff` (difference) to contrast :class:`[ex:dataset2]` with :class:`[ex:dataset1]`.

Curator uses a REST conversation to implement the example above.

.. seealso:: Model sites that implement REST

   - `ChemAxon concepts <http://www.chemaxon.com/products/jchem-web-services/>`_
   - `ChemAxon application programming interface (APIs) <https://restdemo.chemaxon.com/apidocs/>`_

:ref:`Return to top <return-to-top-02-core-12-rest-prov>`

.. |_| unicode:: 0x80
