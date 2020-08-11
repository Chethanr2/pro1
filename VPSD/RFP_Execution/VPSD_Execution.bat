@echo off 
Rem Execution and verification of the business rules configured in VPSD application

pytest -v -s --html=Business_Rules/Business_rules.html --self-contained-html Business_Rules/Test_Business_rules_Execusion.py

Rem Execution and verification of Masters configured in VPSD application and Validation of any changes in masters

pytest -v -s --html=Execution_Reports/Masters_Stop_Type.html --self-contained-html Test_Masters_Stop_Type.py
pytest -v -s --html=Execution_Reports/Masters_Route_Type.html --self-contained-html Test_Masters_Route_Type.py
pytest -v -s --html=Execution_Reports/Masters_Service_Type.html --self-contained-html Test_Masters_Service_Type.py
pytest -v -s --html=Execution_Reports/Masters_Station_Type.html --self-contained-html Test_Masters_Station_Type.py
pytest -v -s --html=Execution_Reports/Masters_Route_Catogery.html --self-contained-html Test_Masters_Route_catogery.py
pytest -v -s --html=Execution_Reports/Masters_Route_Variant.html --self-contained-html Test_Masters_Route_variant.py
pytest -v -s --html=Execution_Reports/Masters_Depot.html --self-contained-html Test_Masters_Depot.py