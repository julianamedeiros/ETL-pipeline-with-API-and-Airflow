# ETL Pipeline with API and Airflow/Docker

The goal of this project was to learn how to extract data from an API and orchestrate a pipeline with Apache Airflow. Nowadays, it is quite hard to find substantial data from API available for free. 
The [IGDB Video Games Database](https://www.igdb.com/api) is a very nice database to practice data extraction and processing, although the data itself is not so interesting to provide complex analysis. 

In this repository, you will find a folder containing the ETL pipeline files (extraction, processing and loading), and a main file that the previous functions assigned in **tasks**.
These tasks are the DAG tasks to be imported on the Airflow\dags file. 

I used Docker to run Airflow on my Windows.
