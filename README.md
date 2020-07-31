# xml_translation
1. Pre-requists:
  1. Python 3x
  2. Libraries / Dependencies
      numpy==1.19.1
      pandas==1.1.0
      python-dateutil==2.8.1
      pytz==2020.1
      six==1.15.0
      xlrd==1.2.0
      xmltodict==0.12.0
  3. Source files such as lookup.xlsx and translate.py are the heart of this task.
      
2. Create a virtual environment: virtualenv <venv_name>
  1. Activate Virtual Environment: activate <venv_name> or cd scripts\ and activate
  2. Install requirements.txt file: pip install -r requirements.txt

3. Finally, Run: python translate.py to see the outcome.

4. Output will be stored as XML in the same application root directory: 
  Example:
    source_XML_1_EN.xml
    source_XML_2_EN.xml
    
    source_XML_1_JP.xml
    source_XML_2_JP.xml
  
    NOTE: You may open the output files in chrome or any browser to view the xml data.
