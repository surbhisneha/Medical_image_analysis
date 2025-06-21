import streamlit as st

st.title("About Brain Tumors")

st.write("""
A brain tumor is an abnormal growth of cells in or around the brain. These growths can be benign (non-cancerous) or malignant (cancerous), and their impact on health can vary significantly based on their type, location, and growth rate.
""")

st.subheader("Types of Brain Tumors")
st.write("""
- **Primary Brain Tumors:** Originate in the brain itself.
  - **Gliomas:** Develop from glial cells. Subtypes include:
    - Astrocytomas: Including glioblastomas, which are aggressive.
    - Oligodendrogliomas: Often slower growing.
    - Ependymomas: Develop in the lining of the ventricles.
  - **Meningiomas:** Arise from the meninges, usually benign.
  - **Schwannomas:** Develop from Schwann cells, often benign.
  - **Pituitary Adenomas:** Affect the pituitary gland, usually benign.
  - **Medulloblastomas:** Most common in children, malignant.
- **Secondary (Metastatic) Brain Tumors:** Cancer that has spread to the brain from another part of the body.
""")

st.subheader("Symptoms")
st.write("""
- Headaches (often worse in the morning)
- Seizures
- Nausea and vomiting
- Vision or hearing problems
- Changes in speech, balance, or mood
- Cognitive changes (memory problems, confusion)
""")

st.subheader("Diagnosis")
st.write("""
- **Neurological Exam:** Assesses symptoms.
- **Imaging:** MRI and CT scans to locate and evaluate the tumor.
- **Biopsy:** Surgical procedure to obtain a tissue sample for analysis.
- **Molecular Testing:** Identifies specific genes, proteins, and other factors unique to the tumor.
""")

st.subheader("Treatment Options")
st.write("""
- **Surgery:** The primary treatment for accessible tumors, aiming to remove as much of the tumor as possible.
- **Radiation Therapy:** Uses high-energy beams to kill cancer cells.
  - External Beam Radiation: The most common form.
  - Brachytherapy: Places radioactive material inside the body near the tumor.
- **Chemotherapy:** Uses drugs to kill cancer cells, often used in combination with other treatments.
- **Targeted Therapy:** Drugs that target specific molecules involved in tumor growth.
- **Immunotherapy:** Boosts the body's immune system to fight cancer.
- **Steroids:** Reduce swelling around the tumor.
- **Clinical Trials:** Research studies testing new treatments.
""")

st.subheader("Prognosis")
st.write("""
Prognosis depends on factors such as the type of tumor, its location, whether it is benign or malignant, and the patient’s overall health. For example, glioblastomas have a poor prognosis, while benign meningiomas have a much better outlook after treatment.
""")

st.subheader("Support and Resources")
st.write("""
- [National Cancer Institute (NCI) Brain Tumor Information](https://www.cancer.gov/types/brain)
- [American Brain Tumor Association (ABTA) Website](https://www.abta.org/)
- [Brain Tumor Foundation](https://www.braintumorfoundation.org/)

These organizations provide resources, support groups, and information on the latest research and treatments.
""")

st.subheader("Research and Advances")
st.write("""
Research in brain tumors is ongoing, with advances in genetics, targeted therapies, and minimally invasive surgical techniques improving outcomes. The advent of personalized medicine, which tailors treatment based on the genetic makeup of the tumor, holds promise for more effective and less toxic treatments.
""")

st.write("For more detailed information, consider consulting a healthcare provider or a specialized medical professional.")
