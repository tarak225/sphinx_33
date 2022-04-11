
.. _$_02-core-11-mathematics:

=====================
Nutrition Mathematics
=====================

.. _return-to-top-02-core-11-mathematics:

This section addresses:

.. rst:role:: USDA #3

   Develop capability for checking the quality of incoming data based on general database principles and specific ARS analytics.

.. rst:role:: USDA #5

   Allow incorporation of ARS analytics for expanding the database.

.. attention::

   This section applies to :ref:`USDA prime data <terms-USDA-Prime>`, not to :ref:`USDA select data <terms-USDA-Select>`. For explanation of USDA prime and USDA select data, see `Deposition Workflow <$_02-core-10-deposition-1-OnLine-OnMessage.html#deposition-workflow>`_

-----------------------------------
OnTask - Ontomatica workflow engine
-----------------------------------

Examples of :ref:`USDA mathematics <terms-USDA-Mathematics>` |_| processed by :ref:`OnTask <terms-OnTask>` |_| deposition workflow:

- Validate: sum of :ref:`proximates <terms-Proximate>` |_| is less than or equal to 100.

- Validate: sum of carbohydrate :ref:`fractions <terms-Fraction>` |_| is less than or equal to total :ref:`carbohydrates <terms-Carbohydrate>`.

- Validate: sum of individual :ref:`fatty acids <terms-Fatty-Acid>` |_| is less than or equal to total :ref:`fat <terms-Fat>`.

- Validate: sum of individual :ref:`carotenoids <terms-Carotenoid>` |_| times the appropriate :ref:`factors <terms-Factor>` |_| is less than or equal to :ref:`vitamin A <terms-Vitamin-A>` |_| value.

- Validate: each food has :ref:`refuse value <terms-Refuse-Value>`.

- Validate: each food has at least one :ref:`household measure <terms-Household-Measure>`.

- Compute: value of missing value for FNDDS nutrient :ref:`component <terms-Component>`.

- Compute: :ref:`retention values <terms-Retention-Value>` |_| based on :ref:`cooking method <terms-Cooking-Method>`.

- Email: food record to :ref:`depositor <terms-Depositor>` |_| for review.

---------------
Sample workflow
---------------

.. figure:: $_02-core-11-mathematics-USDA-processes_.png
   :align: center

:ref:`Return to top <return-to-top-02-core-11-mathematics>`

.. |_| unicode:: 0x80

