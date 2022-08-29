import streamlit as st
from drmanagement import project_mngt
# declaring varibales for image_file and csv_file
image_file = 'template.png' 
csv_file = 'my_project_plan.csv'
# if __name__ == '__main__':
# loading image file and csv to project_mngt function
project_mngt(image_file, csv_file)