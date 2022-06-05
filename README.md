# Water-Quality-Prediction

![Water Quality Prediction using ML](https://blogger.googleusercontent.com/img/a/AVvXsEiHrZdVR_SYZlet6AWey5jdTFtEP9g6Gy6C2anoiHAO6v3hd--kRwJ2L3ZmFjCGkg9xq4682U6oJziUVM6DbJUVV0mN6vSIo3wLIn5WqbJIpdoqjaBrP2qcmBS-CK4gXhnOB1KpBBvcNeedCGiukXzp_Ihq5r877qpIypKwd4wI3_-pQyE5jSSLrQ=w1600)
![Water Quality Prediction](https://raw.githubusercontent.com/jaykumar1607/Water-Quality/main/water_sanitation.gif)
![Water Quality Prediction](https://cdn.shopify.com/s/files/1/2007/8935/articles/what-is-tap-water_1024x.png?v=1552331561)

## Deployed Web Application

Link: https://water-quality-prediction-sam.herokuapp.com/

## Context

<p>Access to safe drinking-water is essential to health, a basic human right and a component of effective policy for health protection. This is important as a health and development issue at a national, regional and local level. In some regions, it has been shown that investments in water supply and sanitation can yield a net economic benefit, since the reductions in adverse health effects and health care costs outweigh the costs of undertaking the interventions.</p>

<p>Safe and readily available water is important for public health, whether it is used for drinking, domestic use, food production or recreational purposes. Improved water supply and sanitation, and better management of water resources, can boost countries’ economic growth and can contribute greatly to poverty reduction. Contaminated water and poor sanitation are linked to transmission of diseases such as cholera, diarrhoea, dysentery, hepatitis A, typhoid, and polio. Absent, inadequate, or inappropriately managed water and sanitation services expose individuals to preventable health risks. This is particularly the case in health care facilities where both patients and staff are placed at additional risk of infection and disease when water, sanitation, and hygiene services are lacking. Globally, 15% of patients develop an infection during a hospital stay, with the proportion much greater in low-income countries.</p>

<p>So, I took some motivation from this to use this Water Quality dataset to understand what consitutes to safe and potable water and apply machine learning to it to distinguish between Potable and Non-Potable water.</p>

## Content

<p>The water_potability.csv file contains water quality metrics for 3276 different water bodies.</p>

<table>
  <tr>
    <th><b>Feature</b></th>
    <th><b>Description</b></th>
  </tr>
  <tr>
    <td>pH Value</td>
    <td>PH is an important parameter in evaluating the acid–base balance of water. It is also the indicator of acidic or alkaline condition of water status. WHO has recommended maximum permissible limit of pH from 6.5 to 8.5. The current investigation ranges were 6.52–6.83 which are in the range of WHO standards.</td>
  </tr>
  <tr>
    <td>Hardness</td>
    <td>Hardness is mainly caused by calcium and magnesium salts. These salts are dissolved from geologic deposits through which water travels. The length of time water is in contact with hardness producing material helps determine how much hardness there is in raw water. Hardness was originally defined as the capacity of water to precipitate soap caused by Calcium and Magnesium.</td>
  </tr>
  <tr>
    <td>Solids (Total dissolved solids - TDS)</td>
    <td>Water has the ability to dissolve a wide range of inorganic and some organic minerals or salts such as potassium, calcium, sodium, bicarbonates, chlorides, magnesium, sulfates etc. These minerals produced un-wanted taste and diluted color in appearance of water. This is the important parameter for the use of water. The water with high TDS value indicates that water is highly mineralized. Desirable limit for TDS is 500 mg/l and maximum limit is 1000 mg/l which prescribed for drinking purpose.</td>
  </tr>
  <tr>
    <td>Chloramines</td>
    <td>Chlorine and chloramine are the major disinfectants used in public water systems. Chloramines are most commonly formed when ammonia is added to chlorine to treat drinking water. Chlorine levels up to 4 milligrams per liter (mg/L or 4 parts per million (ppm)) are considered safe in drinking water.</td>
  </tr>
  <tr>
    <td>Sulfate</td>
    <td>Sulfates are naturally occurring substances that are found in minerals, soil, and rocks. They are present in ambient air, groundwater, plants, and food. The principal commercial use of sulfate is in the chemical industry. Sulfate concentration in seawater is about 2,700 milligrams per liter (mg/L). It ranges from 3 to 30 mg/L in most freshwater supplies, although much higher concentrations (1000 mg/L) are found in some geographic locations.</td>
  </tr>
  <tr>
    <td>Conductivity</td>
    <td>Pure water is not a good conductor of electric current rather’s a good insulator. Increase in ions concentration enhances the electrical conductivity of water. Generally, the amount of dissolved solids in water determines the electrical conductivity. Electrical conductivity (EC) actually measures the ionic process of a solution that enables it to transmit current. According to WHO standards, EC value should not exceeded 400 μS/cm.</td>
  </tr>
  <tr>
    <td>Organic_carbon</td>
    <td>Total Organic Carbon (TOC) in source waters comes from decaying natural organic matter (NOM) as well as synthetic sources. TOC is a measure of the total amount of carbon in organic compounds in pure water. According to US EPA < 2 mg/L as TOC in treated / drinking water, and < 4 mg/Lit in source water which is use for treatment.</td>
  </tr>
  <tr>
    <td>Trihalomethanes</td>
    <td>THMs are chemicals which may be found in water treated with chlorine. The concentration of THMs in drinking water varies according to the level of organic material in the water, the amount of chlorine required to treat the water, and the temperature of the water that is being treated. THM levels up to 80 ppm is considered safe in drinking water.</td>
  </tr>
  <tr>
    <td>Turbidity</td>
    <td>The turbidity of water depends on the quantity of solid matter present in the suspended state. It is a measure of light emitting properties of water and the test is used to indicate the quality of waste discharge with respect to colloidal matter. The mean turbidity value obtained for Wondo Genet Campus (0.98 NTU) is lower than the WHO recommended value of 5.00 NTU.</td>
  </tr>
  <tr>
    <td>Potability</td>
    <td>Indicates if water is safe for human consumption where 1 means Potable and 0 means Not potable.</td>
  </tr>
</table>


