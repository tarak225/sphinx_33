
.. _$_02-core-16-stakeholders:

=============================
USDA Stakeholder Requirements
=============================

.. _return-to-top-02-core-16-stakeholders:

This section addresses:

.. rst:role:: Ontomatica defined objective

.. attention::

   This section applies to :ref:`USDA prime data <terms-USDA-Prime>`, not to :ref:`USDA select data <terms-USDA-Select>`. For explanation of USDA prime and USDA select data, see `Deposition Workflow <$_02-core-10-deposition-1-OnLine-OnMessage.html#deposition-workflow>`_

Table of Contents
-----------------

.. contents::
   :depth: 3
   :local:

------------------------------------------
ASA24 Data Specifications and Requirements
------------------------------------------

Ontomatica :ref:`label classes <terms-Label-Class>` |_| integrate data requirements for US NIH National Cancer Institute (NCI) `Automated Self-administered 24-hour Recall <http://appliedresearch.cancer.gov/asa24/>`_ (ASA24), including coverage of all specifications below.

^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Ontomatica Coverage - ASA24 Requirements
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

For the term "Glycemic load", Ontomatica imports the NCI thesaurus identifier :class:`ncit:C46090` (facet term code for the facet term "Glycemic Index").

The following ASA terms will need to be defined: :class:`low` :class:`high` :class:`non-term` :class:`other-term` :class:`lean` and :class:`discretionary`

.. hlist::
   :columns: 3

   - Gram weight
   - Energy
   - Total fat
   - Carbohydrate
   - Protein
   - Alcohol
   - Cholesterol
   - Total saturated fatty acids
   - Total monounsaturated fatty acids
   - Total polyunsaturated fatty acids
   - Dietary fiber
   - Retinol
   - Vitamin E as alpha-tocopherol
   - Vitamin K
   - Vitamin C
   - Thiamin (Vitamin B1)
   - Riboflavin (Vitamin B2)
   - Niacin
   - Vitamin B6
   - Total folate
   - Vitamin B12
   - Calcium
   - Phosphorus
   - Magnesium
   - Iron
   - Zinc
   - Copper
   - Selenium
   - Sodium
   - Potassium
   - SFA 4:0 (Butanoic)
   - SFA 6:0 (Hexanoic)
   - SFA 8:0 (Octanoic)
   - SFA 10:0 (Decanoic)
   - SFA 12:0 (Dodecanoic)
   - SFA 14:0 (Tetradecanoic)
   - SFA 16:0 (Hexadecanoic)
   - SFA 18:0 (Octadecanoic)
   - MFA 16:1 (Hexadecenoic)
   - MFA 18:1 (Octadecenoic)
   - MFA 20:1 (Eicosenoic)
   - MFA 22:1 (Docosenoic)
   - PFA 18:2 (Octadecadienoic)
   - PFA 18:3 (Octadecatrienoic)
   - PFA 18:4 (Octadecatetraenoic)
   - PFA 20:4 (Eicosatetraenoic)
   - PFA 20:5 (Eicosapentaenoic)
   - PFA 22:5 (Docosapentaenoic)
   - PFA 22:6 (Docosahexaenoic)
   - Caffeine
   - Beta-carotene
   - Alpha-carotene
   - Beta-cryptoxanthin
   - Lutein + zeaxanthin
   - Lycopene
   - Folate, dietary folate equivalents
   - Food folate
   - Folic acid
   - Vitamin A, retinol activity equivalents
   - Total sugars
   - Total number of grain ounce equivalents
   - Number of whole grain ounce equivalents
   - Number of non-whole grain ounce equivalents
   - Total number of vegetable cup equivalents, exclude legumes
   - Number of dark-green vegetable cup equivalents
   - Number of orange vegetable cup equivalents
   - Number of white potato cup equivalents
   - Number of other starchy vegetable cup equivalents
   - Number of tomato cup equivalents
   - Number of other vegetable cup equivalents
   - Total number of fruit cup equivalents
   - Number of citrus, melon, berry cup equivalents
   - Number of other fruit cup equivalents
   - Total number of milk group (milk, yogurt and cheese) cup equivalents
   - Number of milk cup equivalents
   - Number of yogurt cup equivalents
   - Number of cheese cup equivalents
   - Oz cooked lean meat from meat, poultry, fish
   - Oz cooked lean meat from beef, pork, veal, lamb, and game
   - Oz cooked lean meat from organ meats
   - Oz cooked lean meat from franks, sausages, luncheon meats
   - Oz cooked lean meat from chicken, poultry, and other poultry
   - Oz cooked lean meat from fish, other seafood high in omega-3
   - Oz cooked lean meat from fish, other seafood low in omega-3
   - Oz equivalents of lean meat from eggs
   - Oz equivalents of lean meat from soy product
   - Oz equivalents of lean meat from nuts and seeds
   - Number of cooked dry beans and peas cup equivalents
   - Grams of discretionary oil
   - Grams of discretionary solid fat
   - Teaspoon equivalents of added sugars
   - Total drinks of alcohol
   - Total protein
   - Animal protein
   - Vegetable protein
   - Fructose
   - Galactose
   - Glucose
   - Lactose
   - Maltose
   - Sucrose
   - Starch
   - Total dietary fiber
   - Soluble dietary fiber
   - Insoluble dietary fiber
   - Total vitamin A activity (IU)
   - Beta-carotene equivalents
   - Vitamin D (calciferol)
   - Total alpha-tocopherol equivalents
   - Beta-tocopherol
   - Gamma-tocopherol
   - Delta-tocopherol
   - Pantothenic acid
   - SFA 17:0 (margaric acid)
   - SFA 20:0 (arachidic acid)
   - SFA 22:0 (behenic acid)
   - MUFA 14:1 (myristoleic acid)
   - Tryptophan
   - Threonine
   - Isoleucine
   - Leucine
   - Lysine
   - Methionine
   - Cystine
   - Phenylalanine
   - Tyrosine
   - Valine
   - Arginine
   - Histidine
   - Alanine
   - Aspartic acid
   - Glutamin acid
   - Glycine
   - Proline
   - Serine
   - Aspartame
   - Saccharin
   - Phytic acid
   - Oxalic acid
   - 3-Methylhistidine
   - Sucrose polyester
   - Ash
   - Water
   - Total vitamin A activity (Retinol Equivalents)
   - Trans 18:1 (trans-octadecenoic acid [elaidic acid])
   - Trans 18:2 (trans-octadecadienoic acid [linolelaidic acid]; incl. c-t, t-c, t-t)
   - Trans 16:1 (trans-hexadecenoic acid)
   - Total trans fatty acids
   - Niacin equivalents
   - Omega-3 fatty acids
   - Manganese
   - Vitamin E (IU)
   - Natural alpha-tocopherol (RRR-alpha-tocopherol or d-alpha-tocopherol)
   - Synthetic alpha-tocopherol (all rac-alpha-tocopherol or dl-alpha-tocopherol)
   - Daidzein
   - Genistein
   - Glycitein
   - Coumestrol
   - Biochanin A
   - Formononetin
   - Acesulfame potassium
   - Sucralose
   - Available carbohydrate
   - Glycemic load (glucose reference)
   - Glycemic load (bread reference)
   - Choline
   - Betaine
   - Erythritol
   - Inositol
   - Lactitol
   - Maltitol
   - Mannitol
   - Pinitol
   - Sorbitol
   - Xylitol
   - Nitrogen

---------------------------------------------------
National Food and Nutrient Analysis Program (NFNAP)
---------------------------------------------------

The goals of NFNAP are to improve the quantity and quality of data in the USDA National Nutrient Databank (NDB).

NFNAP has produced annual updates of NDB for Standard Reference and a number of **Special Interest Databases**: isoflavones, choline, proanthocyanidins, fluoride, and flavonoids.

NFNAP is guided by five principle:

1. Identify and rank foods and nutrients for analysis
2. Evaluate existing data for foods and nutrients
3. Develop strategies for sampling
4. Process and analyze foods
5. Review and disseminate results

^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Ontomatica Coverage - NFNAP Requirements
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Ontomatica proposal enables #1, #2 and #4, and specifically with respect to **Special Interest Database** requirements.

:ref:`Return to top <return-to-top-02-core-16-stakeholders>`

.. |_| unicode:: 0x80

