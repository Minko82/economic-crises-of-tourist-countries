# ✈️ **Data Visualization**: Economic Crises of Tourist-Dependent Countries

## 📝 **Project Description**

This project is a Python script that visualizes and compares tourism-driven economies—such as the Maldives, Fiji, and others—using key economic indicators. It analyzes data to reveal patterns in **economic sustainability**, **tourism dependency**, and **crisis vulnerability**, leveraging visual tools to make insights clear and compelling.

<br>

---

## 🎨 **Visualizations**

### 1. GDP Visualization
<p align="center">
  <img src="https://github.com/user-attachments/assets/7fcfb1db-aabd-4aa5-9d60-d78f6bf158f7" alt="GDP Visualization" width="70%">
</p>

### 2. Unemployment vs Arrivals
<p align="center">
  <img src="https://github.com/user-attachments/assets/4777f218-e4e9-45ab-9dae-147e141ba619" alt="Unemployment vs Arrivals" width="70%">
</p>


### 3. Metrics Over Time
<p align="center">
  <img src="https://github.com/user-attachments/assets/c5ef9899-0c79-485f-81c4-0b91391f37f2" alt="Metrics Over Time" width="70%">
</p>


### 4. Country Comparisons
<p align="center">
  <img src="https://github.com/user-attachments/assets/15efc149-4ab9-4aca-8eb4-cc000153f4ad" alt="Country Comparisons" width="70%">
</p>



<br>

---

## 📂 **Dataset**

View **Data** folder for more details.
- **Tourism and Economic Metrics:** The dataset is sourced from [World Bank Open Data](https://data.worldbank.org/)
  - Number of Arrivals
  - Unemployment Rates (%)
  - GDP (in USD)
  - Tourism Spending (as % of GDP)
- **Geographic Data:** GeoJSON files sourced from [Natural Earth Data](https://www.naturalearthdata.com/)
- **Additional Economic Indicators:** Aggregated from various country reports and statistical databases.


<br>

---

## 💻 **Tools and Technologies**
- Python
- Altair
- Pandas
- GeoJSON
- Illustrator
- ArcGIS

<br>

---

## 🚀 **How to Use**

### **Option 1: Run with Google Colab (Recommended)**
1. Upload the **final-visualizations.ipynb** notebook to Google Colab
   
2. Update Altair:
   
   If you’re running the project in Google Colab, update your Altair version to avoid compatibility issues. Run the following line of code in a Colab cell:
   ```bash
   pip install -U altair vega_datasets
   ```

   After running this, go to **Runtime > Restart Runtime** in the Colab menu.

3. Run the Notebook:
   
   Execute all cells in the notebook to generate visualizations and analyze data.

---

### **Option 2: Run with Jupyter Notebook**
1. Clone and open the repository:  
   ```bash
   git clone https://github.com/Minko82/economic-crises-of-tourist-countries.git
   cd economic-crises-of-tourist-countries
   ```

2. Launch the Notebook:

   ```bash
   jupyter notebook final-visualizations.ipynb
   ```
   
---

### **Option 3: Run with Python Command Line**

1. Clone and open the repository:  
   ```bash
   git clone https://github.com/Minko82/economic-crises-of-tourist-countries.git
   cd economic-crises-of-tourist-countries
   ```

2. Run the Python script from the Command Line:
   ```bash
   python final_travel.py
   ```
