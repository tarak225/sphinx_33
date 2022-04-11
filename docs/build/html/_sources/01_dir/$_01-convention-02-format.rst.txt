
.. _$_02-convention-format:

=======================
Format Used in Proposal
=======================

USDA **requirements** are formatted as follows:

.. rst:role:: USDA #12

   Support capture/documentation of metadata for food composition and non-composition data.

**Ontology terms** are formatted as follows:

- :class:`schema:sameAs` (the schema.org facet term meaning that A is the same as B)
- :class:`ncit:C46090` (the NIH NCI facet term code for the facet term "Glycemic Index")
- :class:`agrontology:isUsedToMake` (the UN FAO term meaning that A is used to make B)

A **word** or **phrase** that is a link to a URL is formatted as follows: `food labeling services for the USDA community <http://www.ontomatica.com/public/organizations/BETV/Intro.html>`_

A **term** that is defined in the glossary is formatted as follows: :ref:`application services <terms-Application-Service>`

A bibliographic **references** is formatted as follows: See :cite:`5002` for more information about ...

.. sidebar:: Sidebar

   Provides complementary detail

**Discussion** about a design or approach.

- point 1
- point 2
- point 3
- point 4

Illustration of a **REST conversation**

.. http:get:: /users/(int:user_id_)/posts/(tag)

.. seealso::
     
   Reference to a related section of the Proposal

.. tip::
   
   Advice based on experience with managing similar issues
   
.. attention::

   Warning that an alternative approach may produce an ineffective result

.. danger::

   Advice that an alternative approach will produce a poor or unintended outcome

.. |_| unicode:: 0x80

