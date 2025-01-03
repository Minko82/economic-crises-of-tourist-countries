import pandas as pd
import altair as alt

# Load GDP data
gdp_data_url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vSrhCFO8_5hlJkCJ8xWT9YsRHz64UUPfWClp0ZiUYEM10_FxQgmwaIHETyIcruKBhH9d1C1LZSbNBfn/pub?output=csv"
gdp_data = pd.read_csv(gdp_data_url)
gdp_melted = gdp_data.melt(id_vars=["Country Name"], var_name="Year", value_name="GDP")
gdp_melted['Year'] = gdp_melted['Year'].astype(int)
gdp_melted['GDP'] = pd.to_numeric(gdp_melted['GDP'], errors='coerce')
gdp_melted['Percentage Change GDP'] = gdp_melted.groupby('Country Name')['GDP'].pct_change() * 100

# Load Number of Arrivals data
arrivals_data_url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vQaaAL3uUEECVUrM_UY0auvnzGGtnMCalpxhjsnvWYT7GeZD0vXt1EjOQK_7Eg1dZPDjhwxJXvSak6Y/pub?output=csv"
arrivals_data = pd.read_csv(arrivals_data_url)
arrivals_melted = arrivals_data.melt(id_vars=["Country Name"], var_name="Year", value_name="Number of Arrivals")
arrivals_melted['Year'] = arrivals_melted['Year'].astype(int)
arrivals_melted['Number of Arrivals'] = pd.to_numeric(arrivals_melted['Number of Arrivals'], errors='coerce')
arrivals_melted['Percentage Change Arrivals'] = arrivals_melted.groupby('Country Name')['Number of Arrivals'].pct_change() * 100

# Merge GDP and Number of Arrivals datasets
merged_data = pd.merge(arrivals_melted, gdp_melted, on=['Country Name', 'Year'])

# Filter data for Fiji and Maldives (2014-2020)
filtered_data = merged_data[merged_data['Country Name'].isin(['Fiji', 'Maldives'])]

# Add a red zero line
zero_line = alt.Chart(pd.DataFrame({'y': [0]})).mark_rule(color='darkgrey').encode(
    y='y:Q'
)

# Dropdown menu with an empty option for showing all countries
dropdown = alt.binding_select(
    options=[None] + list(merged_data['Country Name'].unique()),
    labels=['All'] + list(merged_data['Country Name'].unique()),
    name="Select Country: "
)
country_selection = alt.selection_single(fields=['Country Name'], bind=dropdown, name="Country", empty='all')

custom_color_scale = alt.Scale(
    domain=['Maldives', 'Fiji'],  # Specify the countries
    range=['orange', 'blue']  # Corresponding colors
)
# Function to add country labels at the end
def add_labels(chart, data, y_field):
    return chart + alt.Chart(data).transform_filter(
        alt.datum.Year == 2020  # Last year in the dataset
    ).mark_text(
        align='left',
        dx=5,
        fontSize=12
    ).encode(
        x='Year:O',
        y=y_field,
        text='Country Name:N',
        color=alt.Color('Country Name:N', legend=None)
    )



# Update the arrivals chart
arrivals_chart_all = alt.Chart(filtered_data).mark_line(point=True).encode(
    x=alt.X('Year:O', axis=alt.Axis(labelAngle=-45, title=None, labelFontSize=12)),
    y=alt.Y('Percentage Change Arrivals:Q', scale=alt.Scale(zero=True), axis=alt.Axis(title=None)),
    tooltip=['Year', 'Country Name', 'Percentage Change Arrivals'],
    color=alt.Color('Country Name:N')  # Apply custom scale
).properties(
    title="Number of Arrivals Change (%)",
    width=250,
    height=200
) + zero_line

arrivals_chart_all = add_labels(arrivals_chart_all, filtered_data, 'Percentage Change Arrivals')

# Update the GDP chart
gdp_chart_all = alt.Chart(filtered_data).mark_line(point=True).encode(
    x=alt.X('Year:O', axis=alt.Axis(labelAngle=-45, title=None, labelFontSize=12)),
    y=alt.Y('Percentage Change GDP:Q', scale=alt.Scale(zero=True), axis=alt.Axis(title=None)),
    tooltip=['Year', 'Country Name', 'Percentage Change GDP'],
    color=alt.Color('Country Name:N')  # Apply custom scale
).properties(
    title="GDP Change (%)",
    width=250,
    height=200
) + zero_line


gdp_chart_all = add_labels(gdp_chart_all, filtered_data, 'Percentage Change GDP')

arrivals_chart_filtered = alt.Chart(merged_data).mark_line(point=True).encode(
    x=alt.X('Year:O', axis=alt.Axis(labelAngle=-45, title=None, labelFontSize=12)),
    y=alt.Y('Percentage Change Arrivals:Q', scale=alt.Scale(zero=True), axis=alt.Axis(title=None)),
    tooltip=['Year', 'Country Name', 'Percentage Change Arrivals'],
    color=alt.Color('Country Name:N')
).transform_filter(
    country_selection
).properties(
    title="Number of Arrivals Change (%) (Filtered)",
    width=250,
    height=200
) + zero_line

gdp_chart_filtered = alt.Chart(merged_data).mark_line(point=True).encode(
    x=alt.X('Year:O', axis=alt.Axis(labelAngle=-45, title=None, labelFontSize=12)),
    y=alt.Y('Percentage Change GDP:Q', scale=alt.Scale(zero=True), axis=alt.Axis(title=None)),
    tooltip=['Year', 'Country Name', 'Percentage Change GDP'],
    color=alt.Color('Country Name:N')
).transform_filter(
    country_selection
).properties(
    title="GDP Change (%) (Filtered)",
    width=250,
    height=200
) + zero_line

# Align and combine charts
final_chart = alt.vconcat(
    alt.hconcat(arrivals_chart_all, gdp_chart_all),
    alt.hconcat(arrivals_chart_filtered, gdp_chart_filtered)
).add_selection(
    country_selection
).configure_title(
    fontSize=14,
    anchor='middle',
    font='Arial'
).configure_axis(
    labelFontSize=12,
    title=None  # Remove all axis titles
)

# Display the combined chart
final_chart

import pandas as pd
import altair as alt

# Load GDP data
gdp_data_url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vSrhCFO8_5hlJkCJ8xWT9YsRHz64UUPfWClp0ZiUYEM10_FxQgmwaIHETyIcruKBhH9d1C1LZSbNBfn/pub?output=csv"
gdp_data = pd.read_csv(gdp_data_url)
gdp_melted = gdp_data.melt(id_vars=["Country Name"], var_name="Year", value_name="GDP")
gdp_melted['Year'] = gdp_melted['Year'].astype(int)
gdp_melted['GDP'] = pd.to_numeric(gdp_melted['GDP'], errors='coerce')
gdp_melted['Percentage Change GDP'] = gdp_melted.groupby('Country Name')['GDP'].pct_change() * 100

# Load Number of Arrivals data
arrivals_data_url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vQaaAL3uUEECVUrM_UY0auvnzGGtnMCalpxhjsnvWYT7GeZD0vXt1EjOQK_7Eg1dZPDjhwxJXvSak6Y/pub?output=csv"
arrivals_data = pd.read_csv(arrivals_data_url)
arrivals_melted = arrivals_data.melt(id_vars=["Country Name"], var_name="Year", value_name="Number of Arrivals")
arrivals_melted['Year'] = arrivals_melted['Year'].astype(int)
arrivals_melted['Number of Arrivals'] = pd.to_numeric(arrivals_melted['Number of Arrivals'], errors='coerce')
arrivals_melted['Percentage Change Arrivals'] = arrivals_melted.groupby('Country Name')['Number of Arrivals'].pct_change() * 100

# Merge GDP and Number of Arrivals datasets
merged_data = pd.merge(arrivals_melted, gdp_melted, on=['Country Name', 'Year'])

# Filter data for Fiji and Maldives (2014-2020)
filtered_data = merged_data[merged_data['Country Name'].isin(['Fiji', 'Maldives'])]

# Add a red zero line
zero_line = alt.Chart(pd.DataFrame({'y': [0]})).mark_rule(color='darkgrey').encode(
    y='y:Q'
)

# Dropdown menu with an empty option for showing all countries
dropdown = alt.binding_select(
    options=[None] + list(merged_data['Country Name'].unique()),
    labels=['All'] + list(merged_data['Country Name'].unique()),
    name="Select Country: "
)
country_selection = alt.selection_single(fields=['Country Name'], bind=dropdown, name="Country", empty='all')

# Function to add country labels at the end
def add_labels(chart, data, y_field):
    return chart + alt.Chart(data).transform_filter(
        alt.datum.Year == 2020  # Last year in the dataset
    ).mark_text(
        align='left',
        dx=5,
        fontSize=12
    ).encode(
        x='Year:O',
        y=y_field,
        text='Country Name:N',
        color=alt.Color('Country Name:N', legend=None)
    )

# Create charts
arrivals_chart_all = alt.Chart(filtered_data).mark_line(point=True).encode(
    x=alt.X('Year:O', axis=alt.Axis(labelAngle=-45, title=None, labelFontSize=12)),
    y=alt.Y('Percentage Change Arrivals:Q', scale=alt.Scale(zero=True), axis=alt.Axis(title=None)),
    tooltip=['Year', 'Country Name', 'Percentage Change Arrivals'],
    color=alt.Color('Country Name:N', legend=alt.Legend(title="Country", labelFontSize=12, titleFontSize=14))
).properties(
    title="Number of Arrivals Change (%)",
    width=250,
    height=200
) + zero_line

arrivals_chart_all = add_labels(arrivals_chart_all, filtered_data, 'Percentage Change Arrivals')

gdp_chart_all = alt.Chart(filtered_data).mark_line(point=True).encode(
    x=alt.X('Year:O', axis=alt.Axis(labelAngle=-45, title=None, labelFontSize=12)),
    y=alt.Y('Percentage Change GDP:Q', scale=alt.Scale(zero=True), axis=alt.Axis(title=None)),
    tooltip=['Year', 'Country Name', 'Percentage Change GDP'],
    color=alt.Color('Country Name:N', legend=alt.Legend(title="Country", labelFontSize=12, titleFontSize=14))
).properties(
    title="GDP Change (%)",
    width=250,
    height=200
) + zero_line

gdp_chart_all = add_labels(gdp_chart_all, filtered_data, 'Percentage Change GDP')

arrivals_chart_filtered = alt.Chart(merged_data).mark_line(point=True).encode(
    x=alt.X('Year:O', axis=alt.Axis(labelAngle=-45, title=None, labelFontSize=12)),
    y=alt.Y('Percentage Change Arrivals:Q', scale=alt.Scale(zero=True), axis=alt.Axis(title=None)),
    tooltip=['Year', 'Country Name', 'Percentage Change Arrivals'],
    color=alt.Color('Country Name:N', legend=alt.Legend(title="Country", labelFontSize=12, titleFontSize=14))
).transform_filter(
    country_selection
).properties(
    title="Number of Arrivals Change (%) (Filtered)",
    width=250,
    height=200
) + zero_line

gdp_chart_filtered = alt.Chart(merged_data).mark_line(point=True).encode(
    x=alt.X('Year:O', axis=alt.Axis(labelAngle=-45, title=None, labelFontSize=12)),
    y=alt.Y('Percentage Change GDP:Q', scale=alt.Scale(zero=True), axis=alt.Axis(title=None)),
    tooltip=['Year', 'Country Name', 'Percentage Change GDP'],
    color=alt.Color('Country Name:N', legend=alt.Legend(title="Country", labelFontSize=12, titleFontSize=14))
).transform_filter(
    country_selection
).properties(
    title="GDP Change (%) (Filtered)",
    width=250,
    height=200
) + zero_line

# Align and combine charts
final_chart = alt.vconcat(
    alt.hconcat(arrivals_chart_all, gdp_chart_all),
    alt.hconcat(arrivals_chart_filtered, gdp_chart_filtered)
).add_selection(
    country_selection
).configure_title(
    fontSize=14,
    anchor='middle',
    font='Arial'
).configure_axis(
    labelFontSize=12,
    title=None  # Remove all axis titles
)

# Display the combined chart
final_chart

import pandas as pd
import altair as alt

# Load GDP data
gdp_data_url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vSrhCFO8_5hlJkCJ8xWT9YsRHz64UUPfWClp0ZiUYEM10_FxQgmwaIHETyIcruKBhH9d1C1LZSbNBfn/pub?output=csv"
gdp_data = pd.read_csv(gdp_data_url)
gdp_melted = gdp_data.melt(id_vars=["Country Name"], var_name="Year", value_name="GDP")
gdp_melted['Year'] = gdp_melted['Year'].astype(int)
gdp_melted['GDP'] = pd.to_numeric(gdp_melted['GDP'], errors='coerce')

# Load Number of Arrivals data
arrivals_data_url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vQaaAL3uUEECVUrM_UY0auvnzGGtnMCalpxhjsnvWYT7GeZD0vXt1EjOQK_7Eg1dZPDjhwxJXvSak6Y/pub?output=csv"
arrivals_data = pd.read_csv(arrivals_data_url)
arrivals_melted = arrivals_data.melt(id_vars=["Country Name"], var_name="Year", value_name="Number of Arrivals")
arrivals_melted['Year'] = arrivals_melted['Year'].astype(int)
arrivals_melted['Number of Arrivals'] = pd.to_numeric(arrivals_melted['Number of Arrivals'], errors='coerce')

# Load UnEmployment Rate data
unemployment_data_url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vSJKu8jPGN3hc6jotxuBfWFgSEaue_Fdwv3GySHtleZT03dRf5VPl-wlBgvt6B6hWYWz2r-2b2-t6z_/pub?output=csv"
unemployment_data = pd.read_csv(unemployment_data_url)
unemployment_melted = unemployment_data.melt(
    id_vars=["Country Name"], var_name="Year", value_name="UnEmployment Rate"
)
unemployment_melted['Year'] = unemployment_melted['Year'].astype(int)
unemployment_melted['UnEmployment Rate'] = pd.to_numeric(unemployment_melted['UnEmployment Rate'], errors='coerce')

# Filter data for Fiji and Maldives (2014-2020)
filtered_gdp = gdp_melted[(gdp_melted['Year'] >= 2014) & (gdp_melted['Year'] <= 2020) & (gdp_melted['Country Name'].isin(['Fiji', 'Maldives']))]
filtered_arrivals = arrivals_melted[(arrivals_melted['Year'] >= 2014) & (arrivals_melted['Year'] <= 2020) & (arrivals_melted['Country Name'].isin(['Fiji', 'Maldives']))]
filtered_unemployment = unemployment_melted[(unemployment_melted['Year'] >= 2014) & (unemployment_melted['Year'] <= 2020) & (unemployment_melted['Country Name'].isin(['Fiji', 'Maldives']))]

# Function to create individual charts
def create_chart(data, y_field, title):
    return alt.Chart(data).mark_line(point=True).encode(
        x=alt.X('Year:O', title=None),
        y=alt.Y(y_field, title=None),
        color=alt.Color('Country Name:N', legend=None),
        tooltip=['Year', 'Country Name', y_field]
    ).properties(
        title=title,
        width=300,
        height=300
    ) + alt.Chart(data[data['Year'] == 2020]).mark_text(
        align='left', dx=5, fontSize=12
    ).encode(
        x='Year:O',
        y=y_field,
        text='Country Name:N',
        color=alt.Color('Country Name:N', legend=None)
    )

# Create charts
gdp_chart = create_chart(filtered_gdp, 'GDP', "GDP (USD)")
arrivals_chart = create_chart(filtered_arrivals, 'Number of Arrivals', "Number of Arrivals")
unemployment_chart = create_chart(filtered_unemployment, 'UnEmployment Rate', "Unemployment Rate (%)")

# Combine the charts horizontally
combined_charts = alt.hconcat(
    gdp_chart,
    arrivals_chart,
    unemployment_chart
)

combined_charts

import pandas as pd
import altair as alt

# Load GDP data
gdp_data_url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vSrhCFO8_5hlJkCJ8xWT9YsRHz64UUPfWClp0ZiUYEM10_FxQgmwaIHETyIcruKBhH9d1C1LZSbNBfn/pub?output=csv"
gdp_data = pd.read_csv(gdp_data_url)
gdp_melted = gdp_data.melt(id_vars=["Country Name"], var_name="Year", value_name="GDP")
gdp_melted['Year'] = gdp_melted['Year'].astype(int)
gdp_melted['GDP'] = pd.to_numeric(gdp_melted['GDP'], errors='coerce')
gdp_melted['Percentage Change GDP'] = gdp_melted.groupby('Country Name')['GDP'].pct_change() * 100

# Load Number of Arrivals data
arrivals_data_url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vQaaAL3uUEECVUrM_UY0auvnzGGtnMCalpxhjsnvWYT7GeZD0vXt1EjOQK_7Eg1dZPDjhwxJXvSak6Y/pub?output=csv"
arrivals_data = pd.read_csv(arrivals_data_url)
arrivals_melted = arrivals_data.melt(id_vars=["Country Name"], var_name="Year", value_name="Number of Arrivals")
arrivals_melted['Year'] = arrivals_melted['Year'].astype(int)
arrivals_melted['Number of Arrivals'] = pd.to_numeric(arrivals_melted['Number of Arrivals'], errors='coerce')
arrivals_melted['Percentage Change Arrivals'] = arrivals_melted.groupby('Country Name')['Number of Arrivals'].pct_change() * 100

# Load UnEmployment Rate data
unemployment_data_url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vSJKu8jPGN3hc6jotxuBfWFgSEaue_Fdwv3GySHtleZT03dRf5VPl-wlBgvt6B6hWYWz2r-2b2-t6z_/pub?output=csv"
unemployment_data = pd.read_csv(unemployment_data_url)
unemployment_melted = unemployment_data.melt(id_vars=["Country Name"], var_name="Year", value_name="UnEmployment Rate")
unemployment_melted['Year'] = unemployment_melted['Year'].astype(int)
unemployment_melted['UnEmployment Rate'] = pd.to_numeric(unemployment_melted['UnEmployment Rate'], errors='coerce')
unemployment_melted['Percentage Change UnEmployment'] = unemployment_melted.groupby('Country Name')['UnEmployment Rate'].pct_change() * 100

# Filter data for Fiji and Maldives (2014-2020)
filtered_gdp = gdp_melted[(gdp_melted['Year'] >= 2014) & (gdp_melted['Year'] <= 2020) & (gdp_melted['Country Name'].isin(['Fiji', 'Maldives']))]
filtered_arrivals = arrivals_melted[(arrivals_melted['Year'] >= 2014) & (arrivals_melted['Year'] <= 2020) & (arrivals_melted['Country Name'].isin(['Fiji', 'Maldives']))]
filtered_unemployment = unemployment_melted[(unemployment_melted['Year'] >= 2014) & (unemployment_melted['Year'] <= 2020) & (unemployment_melted['Country Name'].isin(['Fiji', 'Maldives']))]

# Function to create individual charts
def create_chart(data, y_field, title):
    return alt.Chart(data).mark_line(point=True).encode(
        x=alt.X('Year:O', title=None),
        y=alt.Y(y_field, title=None, scale=alt.Scale(zero=True)),
        color=alt.Color('Country Name:N', legend=None),
        tooltip=['Year', 'Country Name', y_field]
    ).properties(
        title=title,
        width=300,
        height=300
    ) + alt.Chart(data[data['Year'] == 2020]).mark_text(
        align='left', dx=5, fontSize=12
    ).encode(
        x='Year:O',
        y=y_field,
        text='Country Name:N',
        color=alt.Color('Country Name:N', legend=None)
    )

# Create charts for percentage change
gdp_chart = create_chart(filtered_gdp, 'Percentage Change GDP', "GDP (% Change)")
arrivals_chart = create_chart(filtered_arrivals, 'Percentage Change Arrivals', "Number of Arrivals (% Change)")
unemployment_chart = create_chart(filtered_unemployment, 'Percentage Change UnEmployment', "Unemployment Rate (% Change)")

# Combine the charts horizontally
combined_charts = alt.hconcat(
    gdp_chart,
    arrivals_chart,
    unemployment_chart
)

combined_charts

import pandas as pd
import altair as alt

# Load Number of Arrivals data
arrivals_data = pd.read_csv(
    'https://docs.google.com/spreadsheets/d/e/2PACX-1vQaaAL3uUEECVUrM_UY0auvnzGGtnMCalpxhjsnvWYT7GeZD0vXt1EjOQK_7Eg1dZPDjhwxJXvSak6Y/pub?output=csv'
)
arrivals_melted = arrivals_data.melt(
    id_vars=['Country Name'], var_name='Year', value_name='Number of Arrivals'
)
arrivals_melted['Year'] = arrivals_melted['Year'].astype(int)

# Load UnEmployment Rate data
unemployment_data = pd.read_csv(
    'https://docs.google.com/spreadsheets/d/e/2PACX-1vSJKu8jPGN3hc6jotxuBfWFgSEaue_Fdwv3GySHtleZT03dRf5VPl-wlBgvt6B6hWYWz2r-2b2-t6z_/pub?output=csv'
)
unemployment_melted = unemployment_data.melt(
    id_vars=['Country Name'], var_name='Year', value_name='UnEmployment Rate'
)
unemployment_melted['Year'] = unemployment_melted['Year'].astype(int)

# Load GDP data
gdp_data = pd.read_csv(
    'https://docs.google.com/spreadsheets/d/e/2PACX-1vSrhCFO8_5hlJkCJ8xWT9YsRHz64UUPfWClp0ZiUYEM10_FxQgmwaIHETyIcruKBhH9d1C1LZSbNBfn/pub?output=csv'
)
gdp_melted = gdp_data.melt(id_vars=["Country Name"], var_name="Year", value_name="GDP")
gdp_melted['Year'] = gdp_melted['Year'].astype(int)

# Filter data for Fiji and Maldives (2014-2020)
filtered_arrivals = arrivals_melted[(arrivals_melted['Year'] >= 2014) & (arrivals_melted['Country Name'].isin(['Fiji', 'Maldives']))]
filtered_unemployment = unemployment_melted[(unemployment_melted['Year'] >= 2014) & (unemployment_melted['Country Name'].isin(['Fiji', 'Maldives']))]
filtered_gdp = gdp_melted[(gdp_melted['Year'] >= 2014) & (gdp_melted['Country Name'].isin(['Fiji', 'Maldives']))]

# Merge datasets
merged_data = pd.merge(
    pd.merge(filtered_arrivals, filtered_unemployment, on=['Country Name', 'Year']),
    filtered_gdp, on=['Country Name', 'Year']
)

# Define selection mechanisms
point_selection = alt.selection_single(
    fields=['Year', 'Country Name'],
    empty='all',  # Show all data by default when no selection is made
    name="Point"
)

year_dropdown = alt.binding_select(
    options=sorted(merged_data['Year'].unique()),
    name="Select Year: "
)
year_selection = alt.selection_single(
    fields=['Year'],
    bind=year_dropdown,
    name="Year",
    empty="all"  # Show all data when no year is selected
)

# Define background selection to reset year filter
background_selection = alt.selection_single(
    on='click',  # Trigger on click
    empty='all',  # Show all data when no selection is made
    name="Background",
    clear=True  # Allow clearing the selection
)

# Chart dimension
chart_dimension = 300

# Chart: Number of Arrivals vs. UnEmployment Rate
chart1 = alt.Chart(merged_data).mark_circle(size=100).encode(
    x=alt.X('Number of Arrivals:Q', title=None, scale=alt.Scale(zero=False)),
    y=alt.Y('UnEmployment Rate:Q', title=None, scale=alt.Scale(zero=False)),
    color=alt.condition(
        point_selection & background_selection,
        alt.Color('Country Name:N'),  # Removed custom scale for default colors
        alt.value('lightgray')
    ),
    opacity=alt.condition(
        year_selection,
        alt.value(1),
        alt.value(0.5)  # Dim non-selected points
    ),
    tooltip=['Year', 'Country Name', 'Number of Arrivals', 'UnEmployment Rate']
).properties(
    title='Unemployment Rate (%) vs. Number of Arrivals',
    width=chart_dimension,
    height=chart_dimension
).add_selection(
    point_selection,
    year_selection,
    background_selection
)

# Chart: GDP vs. UnEmployment Rate
chart2 = alt.Chart(merged_data).mark_circle(size=100).encode(
    x=alt.X('GDP:Q', title= None, scale=alt.Scale(zero=False)),
    y=alt.Y('UnEmployment Rate:Q', title=None , scale=alt.Scale(zero=False)),
    color=alt.condition(
        point_selection & background_selection,
        alt.Color('Country Name:N'),  # Removed custom scale for default colors
        alt.value('lightgray')
    ),
    opacity=alt.condition(
        year_selection,
        alt.value(1),
        alt.value(0.5)  # Dim non-selected points
    ),
    tooltip=['Year', 'Country Name', 'GDP', 'UnEmployment Rate']
).properties(
    title='Unemployment Rate (%) vs. GDP (USD)',
    width=chart_dimension,
    height=chart_dimension
).add_selection(
    point_selection,
    year_selection,
    background_selection
)

# Combine the charts
combined_charts = alt.hconcat(chart1, chart2).resolve_scale(size='independent')

combined_charts

import pandas as pd
import altair as alt

# Define the color mapping for Fiji and Maldives
color_mapping = {
    'Fiji': 'blue',
    'Maldives': 'orange'
}

# Function to create color encoding with fixed color mapping
def get_color_encoding(data):
    return alt.Color(
        'Country Name:N',
        scale=alt.Scale(domain=list(color_mapping.keys()), range=list(color_mapping.values())),
        legend=alt.Legend(title="Country", labelFontSize=12, titleFontSize=14)  # Keep the legend settings
    )



