
.. _$_02-core-08-relationships:

=======================
Generic Verbs and Nouns
=======================

.. _return-to-top-02-core-08-relationships:

This section addresses:

.. rst:role:: USDA #12

   Support capture/documentation of metadata for food composition and non-composition data.

.. note::

   The following terms are members of a :ref:`class <terms-class>` of ontology-independent-terms. These terms map to **specific terms** in ontologies. The summary below identifies:
   
   - :class:`verb` (a.k.a. predicate, relationship, object property)
   
   - noun (a.k.a. thing, object) specified as **X** and **Y**. A more precise term is specified as **{noun}**. A precise noun, as specified by an :ref:`authority <terms-Authority>`, is identified on |N|_. Many examples are listed in |G|_.

`isA <http://en.wikipedia.org/wiki/Is-a>`_ Relationships
--------------------------------------------------------

.. csv-table::
   :header: "Relationship", "Inverse"

   "X :class:`includesSpecific` Y", "Y :class:`isA` X"
   "", "Taxon :class:`isA` Taxon"
   "", "Food product :class:`isA` Food product"
   "", "Food product :class:`isOneOf` {Food product list}"
   "", "X :class:`inheritsTo` Y"
   "", "Y :class:`inheritsFrom` X"

WordNet whole-part Relationships (`Holonymy/meronymy <http://en.wikipedia.org/wiki/Holonymy>`_)
-----------------------------------------------------------------------------------------------

.. csv-table::
   :header: "Relationship", "Inverse"

   "X :class:`containsSubstance` Y", "Y :class:`substanceContainedIn` X"
   "FoodProduct :class:`containsSubstance`", ""
   "|nbsp| |nbsp| {Substance, amount in total, amount in solids, label claim (yes/no) }", ""
   "X :class:`hasIngredient` Y", "Y :class:`ingredientOf` X"
   "FoodProduct :class:`hasIngredient`", ""
   "|nbsp| |nbsp| {Food product, rank, total ingredient in total product, ", ""
   "|nbsp| |nbsp| ingredient solids in product solids {purpose list} }", ""
   "FoodProduct :class:`mayHaveIngredient`", ""
   "|nbsp| |nbsp| {Food product, rank, total ingredient in total product, ", ""
   "|nbsp| |nbsp| ingredient solids in product solids {purpose list} }", ""
   "X :class:`madeFrom` Y", "Y :class:`usedToMake` X"
   "Container :class:`usesStructuralStrengthMaterial` Substance", ""
   "Container :class:`usesCoatingMaterial` Substance", ""
   "FoodProduct :class:`isMadeFrom` FoodProduct", ""
   "FoodProduct :class:`isDerivedFrom`", ""
   "|nbsp| |nbsp| {Food source, environment, agricultural treatment, growth stage}", ""
   "FoodProduct :class:`isPartOf` {Anatomical part, growth stage, cut, grade}", ""
   "FoodProduct :class:`isExtractedSubstance`", ""
   "|nbsp| |nbsp| {Extracted substance, extracting substance, process, ", ""
   "|nbsp| |nbsp| temperature, duration, sequence_ID.}", ""
   "FoodProduct :class:`hadRemovedSubstance` {Extracted substance, etc.}", ""
   "X :class:`yieldsPortion` Y", "Y :class:`portionOf` X"
   "X :class:`spatiallyIncludes` Y", "Y :class:`spatiallyIncludedIn` X"
   "X :class:`hasComponent` Y", "Y :class:`componentOf` X"
   "FoodProduct :class:`containsDish` FoodProduct", ""

Additional Relationships
------------------------

.. csv-table::
   :header: "Relationship", "Inverse"

   "X :class:`causes` Y", "Y :class:`causedBy` X"
   "X :class:`instrumentFor` Y", "Y :class:`performedByInstrument` X"
   "X :class:`processFor` Y", "Y :class:`usesProcess` X"
   "X :class:`appliedTo` Y", "Y :class:`underwentProcess` X"
   "FoodProduct :class:`underwentProcess`", ""
   "|nbsp| |nbsp| {Process, equipment, temperature, duration,", ""
   "|nbsp| |nbsp| place/stage, sequence_ID, {purpose list} }", ""
   "FoodProduct :class:`isForSpecialUse` {Use/diet, {country list} }", ""
   "FoodProduct :class:`madeFor` {Consumer, {country list} }", ""
   "FoodProduct :class:`usuallyConsumedFor` {Meal type, {country list} }", ""
   "{Taxon, AnatomicalPart} :class:`usedFor` {purpose, priority {country list} }", ""
   "Substance :class:`usedFor` {purpose, priority, food product}", ""
   "X :class:`beneficialFor` Y", "Y :class:`benefitsFrom` X"
   "X :class:`treatmentFor` Y", "Y :class:`treatedWith` X"
   "X :class:`harmfulFor` Y", "Y :class:`harmedBy` X"
   "Substance :class:`harmfulFor` {harmful effect, strength, food product}", ""
   "X :class:`growsIn` Y", "Y :class:`growthEnvironmentFor` X"
   "X :class:`hasPhase` Y", "Y :class:`phaseOf` X"
   "FoodProduct :class:`hasState` Physical state", ""
   "X :class:`hasForm` Y", "Y :class:`isFormOf` X"
   "FoodProduct :class:`hasForm` Physical form", ""
   "Container :class:`hasForm` Physical form", ""
   "FoodProduct :class:`packedIn` Container", ""
   "X :class:`hasPrice` MoneyAmount", ""
   "Substance :class:`measuredIn` Unit of measurement", ""

:ref:`Return to top <return-to-top-02-core-08-relationships>`

.. |N| replace:: Data Integration
.. _N: $_02-core-15-integration.html

.. |G| replace:: Glossary of Terms
.. _G: $_07-glossary.html

.. |_| unicode:: 0x80

.. |nbsp| unicode:: 0xA0

