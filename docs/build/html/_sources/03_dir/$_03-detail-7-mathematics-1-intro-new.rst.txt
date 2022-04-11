
.. _$_03-detail-7-mathematics-1-intro-new:

=============================================================
Guidelines for Converting Units, Denominators and Expressions
=============================================================

Intro text here

Table of Contents
-----------------

.. contents::
   :depth: 1
   :local:

----------
Background
----------

The source of this text is :cite:`3332`.

Conversion of food data is done in the areas of nutrition (i.e. food composition and dietary assessment) and food safety (exposure assessment), and when reporting analytical data, including their publication in scientific articles.

Food composition data are expressed in a variety of ways, depending on national conventions, practices of various institutions and journals requirements. However, to aggregate or compare data from diverse sources, it is often necessary to convert them.

A common source of error in the use of compositional data is their conversions from one unit, denominator or expression to another. We use comprehensive guidelines developed by FAO/INFOODS.

----------
Objectives
----------

With the goal to increase the quality of compositional data, the guidelines have the following objectives:

   * to provide a comprehensive list of possible conversions;

   * to standardize component conversions regarding units (e.g. |gram|, |millig|, or |microg|), denominators (e.g. |per| 100 |gram| edible portion) and expressions used in food composition, dietary assessment and exposure assessment;

   * to promote the publication, e.g. in scientific journals, of all necessary data to be able to convert them into edible portion on fresh weight bases. For example, to provide water, fat or protein content if data are expressed |per| dry weight, |percent| of total fatty or amino acid, respectively;

   * to motivate researchers and compilers to always accompany their compositional data with explicit units, denominators and expressions to ensure their correct use;

   * to motivate users to pay more attention to units, denominators and expressions of compositional data; and

   * to make users aware of some unusual conversions (e.g. the use of the Sheppard factors for converting fatty acid methyl ester into fatty acids)

-------------------------------
Changing denominators and units
-------------------------------

In general, for food composition purposes it is recommended to use a metric unit (|gram|, |millig| or |microg|). As food is typically consumed on the fresh weight basis and only the edible portion is eaten, food composition data are usually reported as '|per| 100 |gram| edible portion on fresh weight basis (EP)'. On the other hand, scientific articles often report data as '|per| 100 |gram| dry matter (DM)' which is useful for scientific purposes to easily compare food contents in a standardized way without the influence of the changing water content. However, in order to be useful for food composition purposes, the water content is needed so that the values can be converted to EP.

Some denominators should be avoided, for example 'individual amino acid (AA) as |gram| |per| 100 |gram|' because it is not obvious if they refer to, for example, '|per| 100 |gram| edible portion' or '|per| 100 |gram| protein' or to '|per| 100 |gram| dry matter'. To avoid ambiguity, it is therefore recommended to always provide a precise description of the denominator. Examples are:

   * |per| 100 |gram| edible portion on fresh weight basis (preferred expression in food composition)

   * |per| 100 |gram| dry matter of edible food

   * |per| |gram| total protein of edible portion on fresh weight basis

   * |per| |gram| total protein of edible portion on dry matter basis

   * |per| |gram| total lipid of edible portion on dry matter basis

   * |per| |gram| total lipid of edible food on fresh weight basis

   * |per| 100 |gram| total food (edible and inedible parts of the food) on fresh weight basis

   * |per| 100 |gram| total food (edible and inedible parts of the food) on dry matter basis

   * |per| |gram| total lipid of total food (edible and inedible food) on fresh weight basis

In food safety '|per| |kilog| food' is the preferred expression in compositional data, sometimes without specifically indicating if total food or edible portion is meant, or if it is on fresh or dry matter basis.

If data are not expressed as '|per| 100 |gram| edible portion on fresh weight basis (EP)', additional data should be provided so that values can be calculated as '|per| 100 |gram| EP':

   * An edible coefficient needs to be reported if data are expressed as '|per| total food'.

   * Water (or dry matter) content in 100 |gram| EP needs to be reported if data are expressed as '|per| |percent| or |gram| dry matter of the edible portion'.

   * Lipid content in 100 |gram| fresh food needs to be reported if data are expressed as '|per| |percent| or |gram| fat/total lipid of the edible portion', or as '|per| total fatty acids (FA) of the edible portion'.

   * Protein content in 100 |gram| fresh food needs to be reported if data are expressed as '|per| |percent| or |gram| protein of the edible portion'.

   * Density needs to be reported if data are expressed |per| volume, e.g. as '|per| 100 |millil|' or '|per| |liter|'.

The use of some units should be avoided such as ppm (parts |per| million), ppb (parts |per| billion), |percent| and International Units (IU); it is better to use true metric units where the unit and the denominator are well defined such as |millig|/|kilog| or |microg|/|gram| (while well defining the denominators - see above).

In the following tables, formulas and examples are given of how to convert different units and denominators to each other. If appropriate, INFOODS tagnames are used for component identification (see :ref:`INFOODS`).

-----------
Conversions
-----------

^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Changing denominators (with same units) where no additional data are needed
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Elements to create proper matrix units:

.. csv-table::
   :header: "Term", "Term value"

   "**From**", ""
   "From expression", "|per|"
   "From unit", "|kilog|"
   "From unit", "|gram|"
   "From qualifier", "|ediblep|"
   "**To**", ""
   "To expression", "|per|"
   "To unit", "|gram|"
   "To qualifier", "|ediblep|"
   "**Operator**", ""
   "Operation", "|divide|"
   "Operation", "|multiply|"
   "Operation", "|equal|"

Example illustrated in text:

   122 |millig| |per| |kilog| |divide| 10 |equal| 12.2 |millig| |per| 100 |gram| |ediblep|

Example illustrated in semantic markup:

   

.. |gram| unicode:: 0x67
.. |millig| unicode:: 0x6d 0x67
.. |microg| unicode:: 0xB5 0x67
.. |percent| unicode:: 0x25
.. |millil| unicode:: 0x6d 0x6c
.. |kilog| unicode:: 0x6b 0x67
.. |liter| unicode:: 0x4c
.. |ediblep| unicode:: 0x45 0x50
.. |per| unicode:: 0x70 0x65 0x72
.. |divide| unicode:: 0xF7
.. |multiply| unicode:: 0xD7
.. |equal| unicode:: 0x3d
.. |_| unicode:: 0x80

