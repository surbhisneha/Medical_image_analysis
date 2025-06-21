import streamlit as st

st.title("About Pneumonia")

st.write("""
Pneumonia is an infection that inflames the air sacs in one or both lungs, which can fill with fluid or pus, causing cough with phlegm or pus, fever, chills, and difficulty breathing. It can range from mild to life-threatening, particularly affecting infants, young children, the elderly, and individuals with weakened immune systems.
""")

st.subheader("Causes of Pneumonia")
st.write("""
Pneumonia can be caused by a variety of infectious agents, including:

- **Bacteria:**
  - Streptococcus pneumoniae: The most common cause.
  - Mycoplasma pneumoniae: Causes atypical or walking pneumonia.
  - Haemophilus influenzae: Particularly in children.
  - Legionella pneumophila: Causes Legionnaires' disease.

- **Viruses:**
  - Influenza virus.
  - Respiratory syncytial virus (RSV).
  - SARS-CoV-2 (the virus causing COVID-19).

- **Fungi:**
  - Histoplasma: Common in areas with bird or bat droppings.
  - Coccidioides: Found in certain parts of the U.S. Southwest.
  - Pneumocystis jirovecii: Affects people with weakened immune systems.

- **Other Factors:**
  - Aspiration pneumonia: Occurs when food, drink, vomit, or saliva is inhaled into the lungs.
""")

st.subheader("Symptoms")
st.write("""
- Cough, which may produce phlegm.
- Fever, sweating, and chills.
- Shortness of breath.
- Chest pain, especially when breathing or coughing.
- Fatigue and muscle aches.
- Nausea, vomiting, or diarrhea.
- Confusion or changes in mental awareness (especially in older adults).
""")

st.subheader("Diagnosis")
st.write("""
- **Physical Exam:** Listening to the lungs for abnormal sounds.
- **Chest X-ray:** To visualize inflammation in the lungs.
- **Blood Tests:** To check for infection and identify the causative organism.
- **Sputum Test:** Analyzing mucus to identify the pathogen.
- **Pulse Oximetry:** Measures oxygen levels in the blood.
- **CT Scan:** Provides a more detailed image of the lungs if needed.
- **Pleural Fluid Culture:** Testing fluid from the pleura (the membrane surrounding the lungs).
""")

st.subheader("Treatment")
st.write("""
- **Bacterial Pneumonia:** Treated with antibiotics. The type of antibiotic depends on the specific bacterium.
- **Viral Pneumonia:** Typically managed with rest and fluids, though antiviral medications may be used in certain cases (e.g., influenza).
- **Fungal Pneumonia:** Treated with antifungal medications.

**Supportive Care:**
- Rest and hydration.
- Fever reducers and pain relievers.
- Cough medicine, although coughing helps clear the lungs.
""")

st.subheader("Prevention")
st.write("""
- **Vaccination:** Vaccines such as the pneumococcal vaccine and the flu vaccine can prevent some types of pneumonia.
- **Good Hygiene:** Regular handwashing and avoiding smoking.
- **Healthy Lifestyle:** A strong immune system through a balanced diet, regular exercise, and adequate sleep.
- **Avoiding Sick Contacts:** Minimizing exposure to people with respiratory infections.
""")

st.subheader("Complications")
st.write("""
- Bacteremia: Bacteria spreading to the bloodstream.
- Lung Abscess: Pus-filled cavities in the lung.
- Pleural Effusion: Fluid accumulation around the lungs.
- Acute Respiratory Distress Syndrome (ARDS): Severe, acute lung dysfunction.
- Organ Failure: In severe cases, pneumonia can lead to failure of multiple organs.
""")

st.subheader("Resources")
st.write("""
For more information, the following resources are valuable:

- [Centers for Disease Control and Prevention (CDC) Pneumonia Information](https://www.cdc.gov/pneumonia/index.html)
- [World Health Organization (WHO) Pneumonia Overview](https://www.who.int/health-topics/pneumonia#tab=tab_1)
- [American Lung Association (ALA) Pneumonia Page](https://www.lung.org/lung-health-diseases/lung-disease-lookup/pneumonia)

These organizations provide comprehensive information on symptoms, treatment options, prevention strategies, and the latest research on pneumonia.
""")

st.write("For more detailed information, consider consulting a healthcare provider or a specialized medical professional.")
