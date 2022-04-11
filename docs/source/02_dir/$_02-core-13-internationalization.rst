
.. _$_02-core-13-internationalization:

==============================
International Data and Methods
==============================

This section addresses:

.. rst:role:: Ontomatica defined objective

.. attention::

   This section applies to :ref:`USDA prime data <terms-USDA-Prime>`, not to :ref:`USDA select data <terms-USDA-Select>`. For explanation of USDA prime and USDA select data, see `Deposition Workflow <$_02-core-10-deposition-1-OnLine-OnMessage.html#deposition-workflow>`_

Ontomatica proposes, as part of :ref:`label project<terms-Label-Project>` |_|, to implement :ref:`complete system<terms-Complete-System>` |_| for two national :ref:`authorities<terms-Authority>` |_| - USA and GBR (UK).

Ontomatica will identify countries.

Then, for a specific country and for a specific food, Ontomatica will illustrate the distribution of energy (kilocal, kilojoule) as defined by the national authority.

For example:

.. csv-table::
   :header: "Country", "ISO 3", "UN FAO", "DBpedia"
   :widths: 15, 10, 10, 20

   "United Kingdom", "GBR", "826", "dbpedia:United_Kingdom"
   "United States", "USA", "840", "dbpedia:United_States"

Energy illustration is generated using UN FAO :ref:`INFOODS<terms-INFOODS>` |_| and authority values.

Note below: USDA and GBR use different analytical methods when reporting values.

Methods

::

   EC carbohydrates	CHOPL = (SUGAR [ncit:C38046]) + (SUGOH [ncit:C38046])

   GBR carbohydrates	CHOAVLM = (MNSAC [ncit:C38046]) + (DISAC [ncit:C38046]) + (DEXTN [ncit:C38046]) + (STARCHM [ncit:C38046]) + (GLYCM [ncit:C38046])

   USA carbohydrates (food: whole wheat)	CHOCDF = 100 g - ((NT [vocal:Kjeldahl] x [infoods:XPROT] 5.83 [xsd:float]) + (WATER [ncit:C38046]) + (FAT [ncit:C38046]) + (ASH [ncit:C38046])g)

   GBR fiber	FIBTS = (GLUCNB [ncit:C38046]) + (CELLU [ncit:C38046]) + (HEMCEL [ncit:C38046]) + (INULN [ncit:C38046]) + (LIGN [ncit:C38046]) + (PECT [ncit:C38046])

   USA fiber	FIBTG [aoac:978.10] = (FIBSOL [ncit:C38046]) + (FIBINS [ncit:C38046]) + (NSP [ncit:C38046])

Legend

- ALL CAPS = INFOODS_identifier.
- Method format = [method-ontology-prefix : ontology-identifier].
- ncit = NIH NCI thesaurus.
- ncit:C38046 = Unspecified.
- XPROT = protein conversion factor.
- XPROT value = 5.83 for the food: whole wheat.
- XPROT is a floating point number [xsd:float].


.. |_| unicode:: 0x80

