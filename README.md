# ✈️ Travel Economy Visualization Project

## 📝 **Project Description**

Explore and compare tourism-driven economies (like the Maldives and Fiji) by analyzing key metrics, further revealing insights into economic sustainability and dependency on tourism.

<br>

---

## 🎨 **Visualizations**

- **Scatter Plot**: Tourism arrivals vs. unemployment rates to reveal economic dependencies.
- **Choropleth Map**: Tourism spending across countries, showcasing regional disparities.
- **Line Chart**: GDP growth trends over time, highlighting tourism-driven spikes.
- **Bar Chart**: Country-wise analysis of tourism as a percentage of GDP.
- **Interactive Filters**: Dropdown menus and linked brushing for granular data exploration.

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
