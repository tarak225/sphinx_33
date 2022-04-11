
.. _$_03-detail-7-mathematics-1-intro:

===================================
Introduction: Nutrition Mathematics
===================================

Intro text here

Table of Contents
-----------------

.. contents::
   :depth: 2
   :local:

------
Part 1
------

The UN FAO INFOODS tag for the calculation "amino acids, total essential" is AAE8. There are eight basic essential amino acids. AAE8 is represented as follows:

.. math:: \begin{align}AAE8=\sum_{1}^8(essential-amino-acids)\end{align}

Which reduces to:

.. math::
   \begin{align}
   AAE8=[isoleucine]\\
   +[leucine]\\
   +[lysine]\\
   +[methionine]\\
   +[phenylalanine]\\
   +[threonine]\\
   +[tryptophan]\\
   +[valine]
   \end{align}

Introducing semantic syntax in the form of a `CURIE <http://en.wikipedia.org/wiki/CURIE>`_ where the :ref:`authority <terms-Authority>` |_| is "infoods" and the `Universal Resource Identifier <http://en.wikipedia.org/wiki/Uniform_resource_identifier>`_ is the unique INFOODS "tag":

.. math::
   \begin{align}[infoods:AAE8]=[infoods:ILE]\\
   +[infoods:LEU]\\
   +[infoods:LYS]\\
   +[infoods:MET]\\
   +[infoods:PHE]\\
   +[infoods:THR]\\
   +[infoods:TRP]\\
   +[infoods:VAL]
   \end{align}

Now replace the operator symbol "+" with its equivalent semantic operator :class:`[ncit:C64911]`.

.. math::
   \begin{align}
   [infoods:AAE8]=[infoods:ILE]\\
   [ncit:C64911][infoods:LEU]\\
   [ncit:C64911][infoods:LYS]\\
   [ncit:C64911][infoods:MET]\\
   [ncit:C64911][infoods:PHE]\\
   [ncit:C64911][infoods:THR]\\
   [ncit:C64911][infoods:TRP]\\
   [ncit:C64911][infoods:VAL]
   \end{align}

.. raw:: html

   To be absolutely clear, the <font color="red">unit</font> to express a value for an amino acid is:
   
"grams per 100 grams per edible portion" :class:`[vocal:v62177]`:

.. math::
   \begin{align}
   [infoods:AAE8]_{g-100-g-EP}=\\
   ([infoods:ILE][vocal:v62177])\\
   [ncit:C64911]([infoods:LEU][vocal:v62177])\\
   [ncit:C64911]([infoods:LYS][vocal:v62177])\\
   [ncit:C64911]([infoods:MET][vocal:v62177])\\
   [ncit:C64911]([infoods:PHE][vocal:v62177])\\
   [ncit:C64911]([infoods:THR][vocal:v62177])\\
   [ncit:C64911]([infoods:TRP][vocal:v62177])\\
   [ncit:C64911]([infoods:VAL][vocal:v62177])
   \end{align}

Each amino acid in a sample will have a <value> in the form of a floating point number :class:`[xsd:float]`:

.. math::
   \begin{align}
   [infoods:AAE8]_{[vocal:v62177]}=\\
   ([infoods:ILE][vocal:v62177][xsd:float]<value>)\\
   [ncit:C64911]([infoods:LEU][vocal:v62177][xsd:float]<value>)\\
   [ncit:C64911]([infoods:LYS][vocal:v62177][xsd:float]<value>)\\
   [ncit:C64911]([infoods:MET][vocal:v62177][xsd:float]<value>)\\
   [ncit:C64911]([infoods:PHE][vocal:v62177][xsd:float]<value>)\\
   [ncit:C64911]([infoods:THR][vocal:v62177][xsd:float]<value>)\\
   [ncit:C64911]([infoods:TRP][vocal:v62177][xsd:float]<value>)\\
   [ncit:C64911]([infoods:VAL][vocal:v62177][xsd:float]<value>)
   \end{align}

------
Part 2
------

A semantic record will have the following syntax:

:class:`[infoods:AAE8]` :class:`[vocal:v62177]` = :class:`[infoods:ILE]` :class:`[vocal:v62177]` :class:`[xsd:float]` <value> :class:`[ncit:C64911]` :class:`[infoods:LEU]` :class:`[vocal:v62177]` :class:`[xsd:float]` <value> :class:`[ncit:C64911]` :class:`[infoods:LYS]` :class:`[vocal:v62177]` :class:`[xsd:float]` <value> :class:`[ncit:C64911]` :class:`[infoods:MET]` :class:`[vocal:v62177]` :class:`[xsd:float]` <value> :class:`[ncit:C64911]` :class:`[infoods:PHE]` :class:`[vocal:v62177]` :class:`[xsd:float]` <value> :class:`[ncit:C64911]` :class:`[infoods:THR]` :class:`[vocal:v62177]` :class:`[xsd:float]` <value> :class:`[ncit:C64911]` :class:`[infoods:TRP]` :class:`[vocal:v62177]` :class:`[xsd:float]` <value> :class:`[ncit:C64911]` :class:`[infoods:VAL]` :class:`[vocal:v62177]` :class:`[xsd:float]` <value>

The operator symbol "=" is replaced with its equivalent semantic operator :class:`[ncit:C54125]`. A complete semantic record will have the following syntax:

:class:`[infoods:AAE8]` :class:`[vocal:v62177]` :class:`[ncit:C54125]` :class:`[infoods:ILE]` :class:`[vocal:v62177]` :class:`[xsd:float]` <value> :class:`[ncit:C64911]` :class:`[infoods:LEU]` :class:`[vocal:v62177]` :class:`[xsd:float]` <value> :class:`[ncit:C64911]` :class:`[infoods:LYS]` :class:`[vocal:v62177]` :class:`[xsd:float]` <value> :class:`[ncit:C64911]` :class:`[infoods:MET]` :class:`[vocal:v62177]` :class:`[xsd:float]` <value> :class:`[ncit:C64911]` :class:`[infoods:PHE]` :class:`[vocal:v62177]` :class:`[xsd:float]` <value> :class:`[ncit:C64911]` :class:`[infoods:THR]` :class:`[vocal:v62177]` :class:`[xsd:float]` <value> :class:`[ncit:C64911]` :class:`[infoods:TRP]` :class:`[vocal:v62177]` :class:`[xsd:float]` <value> :class:`[ncit:C64911]` :class:`[infoods:VAL]` :class:`[vocal:v62177]` :class:`[xsd:float]` <value>

The structure above is in a format that can be sent "over the wire" (e.g. HTTP or FTP). The structure is `serialized <http://en.wikipedia.org/wiki/Serialization>`_.

-------------
Serialization
-------------

Serialization is the process of taking an object instance (e.g. the food item and its related data) and converting it to a format that can be transported across a network or persisted to storage (such as a file or database). The serialized format contains the object's state information. De-serialization is the process of using the serialized state to reconstruct the object from the serialized state to its original state.

Ontomatica uses OWL to define objects and logic, and the :ref:`JSON-LD <terms-JSON-LD>` |_| format to serialize data structure. De-serialized JSON-LD structures are restored to their OWL format.

The next step is to associate the <value> for amino acids with the method of analysis (analytical method) used by the investigator when analyzing the food sample.

.. |_| unicode:: 0x80

