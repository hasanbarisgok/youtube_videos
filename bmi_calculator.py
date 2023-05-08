# bmi = weight (kg) / height (m^2)  


import streamlit as st 

class calculator: 
    
    def __init__(self):
        
        self.input_areas()
    
    def input_areas(self):
        
        self.input_pname = st.text_input("Enter your name: ")
        
        self.input_weight = st.number_input("Enter your Weight (KG)")
        
        self.input_height = st.number_input("Enter your weight (CM)")
    
        
        
        if self.input_weight and self.input_height:
            
            self.all_buttons()
            
    
    def all_buttons(self):
    
        self.calculate_button = st.button("Calculate your BMI! ")
        
        if self.calculate_button: 
            
            self.calculate_bmi()
            
            self.show_bmi_info()
        
    
    def calculate_bmi(self):
        
        self.input_height = self.input_height / 100 #converted m to cm
        
        self.bmi = self.input_weight / (self.input_height ** 2) #cm to cm ^ 2 
        
        
    
    def show_bmi_info(self):
        
        st.write("Your BMI Infos are: ")
        
        st.write("Person Name: ", self.input_pname)
        
        st.write("Calculated BMI: ", self.bmi)
        

abc = calculator()