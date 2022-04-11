
.. _$_02-core-10-deposition-2-top-down:

==========================
OnLine Top Down Deposition
==========================

.. _return-to-top-02-core-10-deposition-2-top-down:

Table of Contents
-----------------

.. contents::
   :depth: 3
   :local:

-------
Process
-------

Template-driven process that classifies a food by its similarity to another food.

Templates are :ref:`pre-combined items <terms-Pre-Combined-Item>` specified by ontology terms.

One ontology used by Ontomatica is `Simple Knowledge Object Sharing <http://www.w3.org/2004/02/skos/core#>`_ (SKOS) :cite:`6050`. Example of applying SKOS:

- Initiate :ref:`conversation <terms-Conversation>` by identifying an exact match :class:`skos:exactMatch` or close match :class:`skos:closeMatch` for :ref:`deposition <terms-Deposition>`.


.. figure:: $_02-core-10-deposition-2-top-down_.png
   :align: center

----------------------------
Examples: Pre-Combined Items
----------------------------

Explanation.

.. csv-table::
   :header: "Food Items", ":class:`[langual:FTC]` (LanguaL Facet Term Codes (FTC)"
   :widths: 15, 20

   "Ale, Pasteurized, Bottled", "A0195 B1230 C0102 E0123 H0232 H0246 J0135 M0210 N0040"
   "Almond Extract, in Glass Bottle", "A0215 B1347 C0174 E0123 H0100 H0232 M0130 N0040"
   "Angel Food Cake, Whole", "A0210 B1012 C0210 E0146 H0358 H0319 H0205"
   "Apple Butter", "A0184 B1245 C0140 E0119 H0105"
   "Apple Juice, Bottled, Infant or Junior Food", "A0127 B1245 C0140 E0123 M0203 N0001 P0020"
   "Apple Juice, Unsweetened, Canned", "A0127 B1245 C0140 E0123 J0123 M0194 P0105"
   "Apple Sauce, Unsweetened, Canned", "A0143 B1245 C0229 E0110 J0123 M0194 P0105"
   "Beef and Pork Frankfurter", "A0221 B1105 C0268 E0105 F0014 H0172 H0288 H0306"
   "Beef Stroganoff with Noodles", "A0220 B1079 C0208 E0134 H0191 H0242 H0166"
   "Beef Taco with Lettuce, Tomato and Cheese", "A0102 B1161 C0268 E0105 F0023 H0207 H0152 H0212 H0143 H0253 H0328"
   "Blue Cheese Dressing", "A0136 B1017 C0190 E0110 H0143 H0331 H0253"
   "Boneless Chicken Breast, Raw", "A0273 B1457 C0267 E0150 F0003 Z0004"
   "Broccoli Spears, Quick Frozen", "A0152 B1443 C0144 E0150 J0132"
   "Cauliflower in Cheddar Cheese Sauce", "A0152 B1094 C0237 E0150 H0143 H0184 H0328 H0253 K0033"
   "Cheeseburger, McDonald's", "A0218 B1161 C0268 E0105 F0023 H0207 H0319 H0212 H0256 H0107 H0253 H0143 Z0111"
   "Chicken Noodle Soup, Canned", "A0243 B1457 C0170 E0149 F0014 H0319 H0212 H0171 J0123 M0194"
   "Chicken, Roaster, Whole, Grilled", "A0273 B1457 C0120 E0150 F0014 G0006 Z0054"
   "Chili Con Carne", "A0172 B1161 C0268 E0134 H0212"
   "Chocolate Chip Cookie", "A0203 B1312 C0208 E0140 H0158 H0231 H0119 H0253"
   "Chocolate Ice Cream, Haagen-Dazs", "A0227 B1201 C0195 E0139 F0018 H0158 H0178 H0184 H0185 H0231 H0206 J0136 Z0112"
   "Chocolate Syrup", "A0272 B1012 C0108 E0139 H0231 H0119 H0253 H0368"
   "Coconut Milk", "A0260 B1536 C0214 E0123"
   "Coffee Bean, Roasted", "A0268 B1305 C0132 E0150 F0014 G0003 H0391"
   "Cooked Ham, Canned, Not Smoked", "A0279 B1136 C0268 E0146 F0014 H0253 M0204 Z0024"
   "Corned Beef Hash", "A0212 B1161 C0268 E0134 H0212 H0253 H0227"
   "Cottage Cheese, 4% Milkfat, Creamed", "A0185 B1201 C0245 E0134 H0101"
   "Cranberry Juice Cocktail, in Plastic Bottle", "A0130 B1508 C0140 E0123 H0136 M0184 N0036"
   "Cream Cheese", "A0185 B1201 C0245 E0119 F0018 H0101 J0135"
   "Cream Of Asparagus Soup, (Campbell's)", "A0180 B1415 C0186 E0134 H0319 H0263 H0296 H0279 H0260 H0369 H0388 H0151 H0114"
   "Cream-Style Corn, Golden, (Del Monte)", "A0152 B1595 C0133 E0110 F0014 H0279 H0158 J0123 M0151 N0030 Z0112"
   "Dill Pickle, Packed in Brine", "A0271 B1404 C0140 E0150 H0190 H0200 H0123 K0022"
   "Durum Flour", "A0149 B1079 C0208 E0106"
   "Enriched Corn Meal", "A0149 B1379 C0155 E0117 H0194 H0309 H0310 H0311 H0181"
   "Garlic Powder", "A0113 B1233 C0240 E0106 H0138 J0116"
   "Graham Cracker Pie Crust", "A0140 B1312 C0208 E0153 H0158 H0221 H0319"
   "Grape Jelly", "A0209 B1329 C0140 E0119 H0136 H0200 H0145"
   "Hard Salami, Whole", "A0221 B1105 C0268 E0146 H0119 H0138"
   "Hot Dog, Lower Salt", "A0221 B1134 C0268 E0105 F0014 H0288 H0306 H0172 K0027 M0186 N0036 P0077"
   "Hydrolyzed Whey Protein Concentrate", "A0129 B1201 C0236 E0139 H0277"
   "Infant Formula, Milk-Based", "A0274 B1201 C0235 E0123 H0157 H0159 H0163 H0221 H0194 P0020"
   "Lowfat Chocolate Milk", "A0148 B1201 C0235 E0123 H0158 H0231 H0119 H0253 H0247 J0135 P0024 P0039"
   "Lowfat Cottage Cheese", "A0185 B1201 C0245 E0134 H0101 H0325 P0024 P0039"
   "Macaroni and Cheese", "A0220 B1079 C0208 E0134 H0143 H0328 H0221 H0184 K0003"
   "Maple Syrup", "A0118 B1167 C0271 E0139"
   "Mashed Potato Flakes, Instant", "A0152 B1218 C0240 E0100 H0138 H0169 J0140"
   "Mayonnaise", "A0292 B1017 C0190 E0119 H0185 H0200 H0306 J0149"
   "Minute Rice", "A0125 B1322 C0208 E0150 F0014 H0169 H0309 H0311 H0181 H0194 H0138 J0116 M0156 N0039 P0088 P0095 P0127 P0162 Z0112"
   "Mozzarella Cheese", "A0185 B1201 C0245 E0151 H0107"
   "Peanut Butter, Smooth", "A0260 B1337 C0132 E0119 H0174 H0263 K0003"
   "Pineapple Chunks, Packed in Pineapple Juice", "A0143 B1484 C0229 E0115 K0039"
   "Pizza with Sausage", "A0100 B1312 C0208 E0140 H0143 H0191 H0212"
   "Potato Chip, Salted, in Laminate Bag", "A0228 B1218 C0240 E0145 H0221 H0173 M0144"
   "Raisin, Sundried", "A0143 B1329 C0137 E0150 H0138 J0141"
   "Refried Beans", "A0152 B1368 C0133 E0134 H0221"
   "Ripe Olive, Packed in Brine, Canned", "A0152 B1299 C0139 E0150 K0018 Z0052"
   "Sauerkraut, Canned", "A0271 B1406 C0151 E0100 F0014 H0101 H0367 J0123 K0017 M0194"
   "Shrimp and Pork Egg Roll", "A0103 B1282 C0101 E0105 H0207 H0212 H0319 H0153 H0191"
   "Shrimp Salad", "A0208 B1237 C0173 E0134 H0221 H0200 H0306 H0186"
   "Skim Milk", "A0148 B1201 C0235 E0123 H0248 H0194 H0316 J0135"
   "Soda Water, Unflavored", "A0241 B1217 C0005 E0123 H0109 P0024 P0102"
   "Sour Dough Bread, Loaf", "A0178 B1312 C0208 E0146 H0256"
   "Soy Protein Concentrate", "A0129 B1452 C0236 E0100"
   "Spaghetti Sauce", "A0152 B1276 C0140 E0121 H0151"
   "Tabasco Pepper Sauce", "A0263 B2636 C0167 E0123 H0123 H0151 H0200"
   "Tamale", "A0102 B1379 C0155 E0105 H0207 M0206 N0049"
   "Tomato Soup, Condensed, Canned", "A0180 B1276 C0140 E0119 H0114 M0204"
   "Tomato-Based Barbecue Sauce", "A0263 B1276 C0140 E0121 H0136 H0151"
   "Tonic Water", "A0241 B1217 C0005 E0123 H0105 H0109 H0117"
   "Tuna, Chunk Light, Solid Pack, in Vegetable Oil", "A0267 B1269 C0268 E0125 F0014 H0263 J0123 K0021 M0151 N0023 Z0057"
   "Turkey Salami, Whole", "A0131 B1236 C0268 E0146 H0307 H0306 Z0002"
   "Vanilla Extract", "A0215 B1324 C0133 E0123 H0100 H0232"
   "Vegetable Stock", "A0243 B1579 C0170 E0123"
   "Vodka", "A0120 B1324 C0133 E0123 H0232 H0270"
   "Wheat Germ", "A0149 B1312 C0182 E0100"
   "Whipping Cream, Pressurized", "A0148 B1201 C0154 E0123 J0135 K0015 M0151"
   "White Bread, Loaf", "A0178 B1312 C0208 E0146 H0256"
   "Whitefish Filet, Smoked", "A0267 B2687 C0125 E0152 H0118"
   "Whole Durum Flour", "A0149 B1079 C0133 E0106"
   "Whole Milk, Ultra-pasteurized", "A0148 B1201 C0235 E0123 J0148"
   "Whole Tomatoes, Packed in Tomato Juice", "A0152 B1276 C0140 E0150 K0016"
   "Whole Wheat Flour", "A0149 B1312 C0133 E0106"
   "Whole Wheat Pita Bread", "A0178 B1312 C0133 E0140 H0256"
   "Yogurt", "A0101 B1201 C0235 E0119 H0101"
   "Water, Distilled", "A0112 B1217 C0005 E0123 H0270"
   "Whole Wheat Bread, Loaf", "A0178 B1312 C0133 E0146 H0256"

:ref:`Return to top <return-to-top-02-core-10-deposition-2-top-down>`

.. |_| unicode:: 0x80

