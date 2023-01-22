# FakerRegisterCustomersDE

Project for studying ETL for the data engineering area.

This system is responsible for generating fake from fictitious customers data using the Python Faker library. These data are then used to feed a customer class in Python, where they are passed through data validation using regular expressions.

The customer class has the following attributes: name, lastname, email, phone, document, age, height, weight and country. These attributes are randomly generated by Faker and then passed through data validation using regular expressions.

The data validation is done through regular expression functions, which check if the generated data is valid. For example, the email validation function checks if the generated email has a valid format (xxx@xxx.xxx).

After validation, the data is stored in a list of tuples, which can be transformed into a Spark DataFrame for data analysis.

Additionally, the validation process also generates boolean columns named 'check_valid_' for each data, indicating whether the data is valid or not.

## Requirements
To use Spark on a local machine, you need to have the following installed:

Spark
Hadoop
Pyspark
JDK

You can install pyspark using the command pip install pyspark.
In addition, you also need to have the Faker library installed. You can install it using the command pip install faker.

Please note that, in order to use Spark on a local machine, you also need to have a Java Development Kit (JDK) installed on your local machine.
