
.. _$_02-core-10-deposition-3-bottom-up:

===========================
OnLine Bottom Up Deposition
===========================

Table of Contents
-----------------

.. contents::
   :depth: 3
   :local:

-------
Process
-------

Ontology driven process that classifies a food according to precise ontology terms.

- Initiate :ref:`conversation <terms-Conversation>` |_| by traversing a :ref:`graph <terms-Graph>` |_| and selecting appropriate terms.

- Use a broad term when there is insufficient information to use a more narrow, precise term.

:ref:`Conversation <terms-Conversation>` |_| has three stages:

- identify unique terms [source; part of source; origin of source]

- identify combinations of terms that are :ref:`jointWith <terms-jointWith>` |_| and :ref:`disjointWith <terms-disjointWith>`

- identify data associated with ontology terms.

-------
Concept
-------

.. figure:: $_02-core-10-deposition-3-bottom-up_.png
   :align: center

-----------
Vocal Terms
-----------

terms to support bottom-up

.. |_| unicode:: 0x80

