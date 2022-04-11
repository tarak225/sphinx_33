
.. _$_02-core-02-deliverables:

============
Deliverables
============

Ontomatica will deliver a :ref:`complete system <terms-Complete-System>` |_| composed of:

- :ref:`Application services <terms-Application-Service>` |_| for :ref:`end-users <terms-End-User>`
- :ref:`Deposition services <terms-Deposition-Service>` |_| for :ref:`food suppliers <terms-Food-Supplier>` |_| and :ref:`investigators <terms-Investigator>`
- :ref:`Data services <terms-Data-Service>` |_| for production applications and investigators
- :ref:`Infrastructure services <terms-Infrastructure-Service>` |_| for executing all services under demanding on-line conditions
- :ref:`Operating services <terms-Operating-Service>` |_| for managing and controlling all services
- :ref:`Development services <terms-Development-Service>` |_| for information :ref:`curators <terms-Curator>` |_| and :ref:`food compilers <terms-Food-Compiler>`

Ontomatica :ref:`Navigator <terms-Navigator>`, similar to a GPS navigator, enables a user to select categories-of-interest. 
Each selection presents more specific categories. 
Categories are implemented as :ref:`application services <terms-Application-Service>` |_| that manipulate :ref:`label classes <terms-Label-Class>`. 
Ontomatica has developed a library of label classes. 
USDA will identify the label classes required for :ref:`label project <terms-Label-Project>`. 
Ontomatica then will package USDA-identified classes to operate in label project applications. 
Label classes are composed of :ref:`facets <terms-Facet>`, :ref:`predicates <terms-Predicate>` |_| and :ref:`data <terms-Data>`. 
Ontomatica Navigator loads label classes and :ref:`items <terms-Item>` |_| that are members of label classes. 

Navigator presents information in two views: 

- :ref:`Listing page <terms-Listing-Page>` |_| where :ref:`items <terms-Item>` |_| that are members of label classes are displayed
- :ref:`Landing page <terms-Landing-Page>` |_| where all properties of a single :ref:`item <terms-Item>` |_| are displayed

Ontomatica deposition services:

- Accept data from food suppliers and investigators
- Validate data deposits
- Add value to deposits
- Update :ref:`data services <terms-Data-Service>`

Two options are available to deposit data:

- :ref:`Message deposit <terms-Message-Deposit>` |_| is an electronic submissions from GS1
- :ref:`Web deposit <terms-Web-Deposit>` |_| is an on-line interface for food suppliers and investigators

Ontomatica application, deposition and data services will support two data groups:

- :ref:`USDA select <terms-USDA-Select>` |_| data that meets the requirements for managing GS1 data
- :ref:`USDA prime <terms-USDA-Prime>` |_| data that meets and exceeds USDA food :ref:`composition <terms-Food-Composition-Data>` |_| and :ref:`non-composition <terms-Food-Non-Composition-Data>` information requirements

Ontomatica deposition services will automate :ref:`current USDA NDL/FSRG practices <terms-USDA-NDL-FSRG-Practice>` used to produce  current USDA databases.

Ontomatica :ref:`data services <terms-Data-Service>` |_| manage data deposits. Data services have two components:

- Data for application services that is stored in :ref:`MySQL <terms-MySQL>`
- Data for food suppliers and investigators that is available through :ref:`REST <terms-REST>` |_| services

All services execute on :ref:`infrastructure services <terms-Infrastructure-Service>`. The major components of infrastructure services are:

- :ref:`Intel Xeon servers <terms-Intel-Xeon-server>`
- :ref:`LAMP <terms-LAMP>` |_| (Linux, Apache, MySQL and PHP - Perl - Python)
- :ref:`Operating services <terms-Operating-Service>` |_| that monitor primary CPU and storage and :ref:`failover <terms-Failover>` |_| to secondary services when necessary

Curators and food compilers use Ontomatica :ref:`development services <terms-Development-Service>` |_| to manage and maintain deposits. Development services also manage the process of promoting a new version of label project applications:

- from :ref:`development <terms-Development>`
- to :ref:`quality assurance <terms-Quality-Assurance>`
- to :ref:`production <terms-Production>`

Ontomatica will provide source code for application services, deposition services, data services, and development service according to licensing terms.

See :ref:`Services, Products and Technologies <$_02-core-06-services>` |_| for detail.

.. |_| unicode:: 0x80

