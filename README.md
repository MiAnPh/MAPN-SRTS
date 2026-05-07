<h1 align="center">Closing the Gap: A Data-Driven Priority Index for Safe Routes to School in Equity Priority Communities</h1>

<div align="center">

  <h3>31 March 2026</h3>

  <p>
    <strong>CP 255 Urban Informatics and Visualization</strong><br>
    <strong>Final Project Report</strong>
  </p>

  <p>[MTC Project #1: Proximity to Neighborhood Amenities]</p>

  <p><i>by</i></p>

  <h3>MAP’N Team 11 (MTC Team)</h3>
  <p>Anwar Baroudi | Phoebe Chiu | Noelani Fixler | Michael Huang</p>

  <hr width="50%">

  <p>
    <strong>Department of City and Regional Planning</strong><br>
    University of California, Berkeley<br>
    230 Bauer Wurster Hall<br>
    Berkeley, CA 94720
  </p>

</div>

## 1. Context and Motivation For Research
The Metropolitan Transportation Commission (MTC), the regional planning agency for the San Francisco Bay Area, is leading efforts to prioritize safety for walking and cycling trips to schools through its Safe Routes to School (SRTS) programs. Initiatives comprise infrastructure- and non-infrastructure-based strategies funded by MTC’s One Bay Area Grant (OBAG). Projects have historically included public education or awareness campaigns, pedestrian or bicyclist training for K-12 students, and infrastructure audits near schools<sup>1</sup>. This traditional focus on pedestrians and cyclists aligns with federal- and state-level SRTS programming but often overlooks students who live beyond a walkable distance, typically defined as 0.5 to 2 miles<sup>2,3</sup>. Despite SRTS global success of improving active transportation safety for school commutes, it often fails to address strategies to close gaps in the transportation network outside of the active transportation context.Gaps in school access are critical areas to investigate within the context of SRTS, as students who use transit to get to school may encounter unique access needs, especially if transit stops are not near school grounds.

SRTS was founded in Denmark in the 1970s with a simple goal of reducing traffic injuries experienced by children on their way to school. This initiative resulted in a 40 percent reduction in child traffic-related injuries, and has since been replicated in countries around the world<sup>4</sup>. Since its introduction to the United States in 1997, the program has expanded its scope to improve safety, encourage physical activity, and foster enjoyable commutes<sup>5</sup>. Thus, including the active transportation considerations/needs of  transit riders within SRTS would further promote the program’s goal of enhancing physical health. Research indicates that first- and last-mile walking distances from transit trips provide moderate-to-vigorous physical activity (MVPA) levels similar to dedicated walking trips, indicating how improving conditions that enable students to access schools via transit is a viable strategy for increasing youth activity levels<sup>6</sup>.

In addition to the safety outcomes facilitated by traditional SRTS programs and policies, the inclusion of transit access within the SRTS framework to support children's trips to school is essential for promoting student academic success and socioeconomic equity. Students relying on public transit often face "time poverty," where every additional 10 minutes of commute time correlates with measurable declines in core subject scores and increased psychological fatigue<sup>7</sup>. In urban settings the typical travel time by public transit is significantly greater than by car, resulting in a major imbalance of transportation reliability as access to a vehicle often provides more predictable and reliable travel outcomes. 

Furthermore, access to higher quality schools is increased with household access to a vehicle<sup>8</sup>, while the logistical burden of long bus commutes for transit dependent students can often result in students transferring out of high-quality schools due to the lack of reliable transit options<sup>9</sup>. These patterns in transportation disparities are correlated by race: Black students travel further to school than their white or Hispanic peers, often navigating less efficient transit networks to reach desired campuses<sup>10</sup>. Students in Equity Priority Communities (EPCs), defined as Census tracts that have a significant concentration of underserved populations<sup>11</sup>, often reside in what are regarded as “essential service deserts" where school access is highly correlated with limited healthcare and food resources<sup>12</sup>. Equity Priority Communities (EPCs) are a designation used by the Metropolitan Transportation Commission (MTC) to identify census tracts with a significant concentration of underserved populations. In the San Francisco Bay Area, a tract is designated as an EPC if it meets specific thresholds for at least two of the following eight indicators: people of color, low-income households (below 200% of the federal poverty level), limited English proficiency, zero-vehicle households, seniors aged 75 and over, people with disabilities, single-parent families, and severely rent-burdened households. For the purposes of this report, the "Zero-Vehicle Household" metrics and racial distribution are the primary drivers for analyzing school-travel disparities.

Conversely, studies show that students with reliable transportation, such as school bus service, are significantly less likely to be chronically absent<sup>13</sup>, and bridging gaps in financial access to transit by providing free transit passes to high schoolers has been shown to reduce excused absences by as much as 27.5%<sup>14</sup>. We suggest that by focusing on how students who use transit finish the last portion of their trip to get to school, we can facilitate access and promote resilience in the transportation system by creating redundancies in route choice to schools: when one mode of transportation to school, such as walking or biking, or even access to a vehicle, is unavailable, access via pedestrian paths from transit networks can allow sufficient connectivity to educational institutions.

Research on first and last mile trips suggest that walkability improvements near transit are multiplicative; high-quality pedestrian infrastructure within a quarter to half mile catchment area of a bus stop act as a force multiplier for ridership and safety<sup>15</sup>. In EPCs, these network effects may be more pronounced because these areas often have more hostile pedestrian infrastructure (e.g., highway overpasses or wide arterials) that act as absolute, impassable barriers. By removing these weak links in these pedestrian networks, practitioners can effectively double or triple the functional Pedestrian Catchment Area (PCA) for students within a 0.5-mile radius, significantly reducing the barriers for student transit access<sup>16</sup>. 

Despite literature that suggests a pronounced impact of street network connectivity on transit ridership, there remains a modeling gap in the context of student commute patterns: while workforce commute patterns are modeled, there are few formal, large-scale modeling efforts to evaluate how transit-dependent students access education. To begin bridging this modeling gap in access to schools from transit networks, we are investigating how this gap is distributed amongst three EPCs within neighborhoods in the MTC region. Tile2Net, an open-source platform using a semantic segmentation model to create digital representations of roads, sidewalks, crosswalks, and other pedestrian infrastructure, can provide detailed data on the material conditions affecting pedestrian access to schools from transit stops. Because Tile2Net’s first and only supported region in California is Alameda County, the three EPCs our project will evaluate will be in Alameda County to enable us to leverage Tile2Net. Analyzing at the EPC Census tract level will also allow us to test our model on a small, yet regionally impactful scale, in alignment with MTC’s support for SRTS programs in the Bay Area. 

To improve access to schools for pedestrians, we will use detailed pedestrian path networks obtained from Tile2Net to take a disaggregated approach; we can map out existing pedestrian routes from bus stops to schools, and note specific gaps. By highlighting those gaps that have the greatest detriment to school accessibility, we can help prioritize projects that most improve said accessibility. We can also compare the accessibility by pedestrians to schools to the accessibility for drivers to highlight the regions with the greatest disparities.

Below, we develop and visualize our methodology to show a precise relationship between pedestrian routes that serve schools and bus stop locations, to quantify the transportation barriers that could lead to chronic absenteeism and educational inequity. 

### A) Stakeholder Considerations and Anticipated Impact
The motivation for this study evolved from a broad examination of pedestrian network connectivity and access to amenities to a targeted analysis of connecting pedestrians to schools from the transit network in the context of SRTS, specifically focusing on MTC’s EPCs. Earlier  project drafts included a wide array of amenities, such as grocery stores and healthcare facilities, but feedback from MTC and academic advisors to adjust the project scope in favor of a more narrowly defined research question encouraged us to turn toward SRTS. We selected schools as our focus since trips to school are high-frequency, non-discretionary daily trips, made by vulnerable populations who often can’t and don’t drive. Moreover, SRTS is an explicit priority within MTC’s key planning interests. This selection allows us the flexibility to test our model in the context of differing street networks and urban typologies. In the future, we could select different areas of focus for this analysis as relevant for further research. 

### B) Unit of Analysis, Measures and Metrics
To most accurately model the student pathways and origin-destination (OD) pairs, we have explicitly established high-frequency transit stops as the primary origin point for the last mile of school commutes. We are defining high-frequency transit stops as stops with service every 20-minutes or less (three trips per hour) during the morning and afternoon peak service hours, in alignment with the AB 2553 redefinition<sup>17</sup>. Our model utilizes this standard to identify gaps where physical infrastructure barriers force transit-dependent students into commutes that exceed this legally-defined threshold for accessibility. Through our analysis, we aim to explore the differences between options for a driver, who may have multiple redundant paths to a campus, as compared to access for a transit-and-sidewalk-reliant pedestrian. To normalize our analysis across both travel modes, we will tether the origin point of vehicle and pedestrian trips from a transit node, in this case, bus stops. Though we recognize those who travel by vehicle will often have greater flexibility in route choice as they are not limited by a fixed-route system, our project aims to specifically examine disparities in access that remain for pedestrians, considering first-last mile, even after completing the transit portion of their trips. 

If a path in the pedestrian network is missing compared to the vehicle road network, we can identify it as a spot where pedestrian access is disproportionately lower than auto access. Drawing from studies on pedestrian connectivity referenced above, we aim to identify locations where multiplier effects can be applied, by making relatively small yet impactful connections in pedestrian networks. 
## 2. Methodology
### A) Data Description
The project's data includes sociodemographic information about schools and Census tracts within MTC EPCs, as well as spatial information about the transportation network surrounding these locations, including the street network, pedestrian network, and bus stops. 

The MTC/ABAG dataset on Plan Bay Area (PBA) 2050 Equity Priority Communities includes information for 339 EPC Census tracts as a GeoJSON file, based on the 2014-2018 5-Year American Community Survey (ACS). Relevant information for this project includes each EPC’s Census GEOID and geometry for spatial visualizations and triangulation with other resources providing more recent data for research analysis. The 2020-2024 5-Year ACS shapefile from the U.S. Census Bureau provides updated estimates of the share of households without a vehicle within each Census tract. The California Department of Education has separate data sets for all public and private schools throughout California for the 2023-2024 academic year available via GeoJSON. Both data sets include information about school location, as well as the total number of enrolled students for each school. Only the data set on public schools also includes student counts by several demographic groups, including race/ethnicity, socioeconomically disadvantaged, and students eligible for free or reduced meals. We selected the 2020-2024 ACS estimates for households without a vehicle and demographic information for the 2023-2024 academic year for schools within Alameda County to ensure consistency within the data collection period for both data sets. 

Given potential changes or complete reconfiguration of Census tract boundaries, we conducted a brief spatial analysis for our study areas in Alameda County by overlaying the 2018 5-Year ACS PBA 2050 EPC Census tracts over the 2024 5-Year ACS Census tracts with matching GEOIDs to the PBA 2050 EPCs. We found that only 4 out of the 101 EPCs in Alameda County no longer existed in the 2024 5-Year ACS, and only 3.3% of the combined area of all Alameda County EPCs is missing in the estimates for the share of households without a vehicle. Examining the overlaid map, the Census tract boundaries of the EPCs that remained in the 2024 5-Year appeared to be relatively similar to the original 2018 5-Year ACS boundaries.

Information about the transportation network in EPCs in Alameda County originates from one public-facing data set from AC Transit and two open-source data processing platforms, OSMnx and Tile2Net. The AC Transit General Transit Speed Specification (GTFS) CSV file provides information about transit service throughout the AC Transit service area in Alameda and Contra Costa counties. Specifically, GTFS provides the latitude and longitude of bus stop locations, bus stop names, and a link to conduct spatial joins with bus stop locations with other attribute data for each bus stop (e.g., information about the bus lines served by the bus stop). Our analysis will use August 2025 GTFS data, following the AC Transit realignment. Though the data collection period for students and EPC Census tract demographics lags behind the AC Transit GTFS data, we reason that the inclusion of the most recent GTFS data in our final deliverable will provide a more accurate representation of how students travel by foot or on wheels from transit stops to schools, given the most recent data we have on transit stops, schools, and neighborhoods from the data available.

OSMnx and Tile2Net are two Python packages that generate data about street and pedestrian infrastructure. OSMnx produces network graphs that include spatial data for nodes and edges, including location and distance. Tile2Net provides satellite imagery data for Alameda County to generate polygons of pedestrian infrastructure, including roads, sidewalks, crosswalks, and other pedestrian infrastructure (e.g., curb ramps). The computer vision and semantic segmentation model will parse through satellite images of Alameda County at zoom level 19, or 0.3 meters per pixel, to estimate data about the active transportation network. Our research team is still examining the metadata of these platforms to determine the data collection period of these resources.
### B) Data Cleaning and Model Limitations
Our data cleaning process included the following steps for the following categories:

1. California Open Data Portal: The raw school data included both public and private school data so we first standardized this by manually adding a “school type” categorical variable into both public and private datasets prior to merging. A subset of this data was created next by filtering the raw data specifically for Alameda County to ensure local relevance for our analysis. Because the school records did not contain EPC identifiers, a spatial join was required. We conducted sanity checks for whether to consider all schools or only public schools since the California Department of Education was missing demographic data for private schools. By producing figures to determine the relevance of private schools to EPC Census tracts, we chose to focus specifically on public schools, which may require future adjustments to our accessibility analyses and chosen EPC Census tracts.
2. EPC data: Regarding the MTC EPC data, we used a spatial “within” predicate to join school coordinates with the MTC PBA 2050 EPC census tract polygons. We may have to coordinate with MTC about whether their priorities are to run the most current analysis versus the most accurate analysis to the 2014-2018 ACS Census tract boundaries of the Plan Bay Area 2050 EPCs.
3. ACS data: The raw ACS 2020-2024 data provided raw counts rather than percentages. To normalize this, we calculated the proportion of zero vehicle households per tract by dividing households with access to zero vehicles by the total number of households. 
4. AC Transit data (bus stops): open-source data was downloaded from the AC Transit Open Data Portal, and clipped to only include the selected EPCs. Remaining data cleaning for bus stops includes joining the stops with bus lines and schedules to filter out buses that don’t run frequent service during peak hours.
5. Tile2Net (pedestrian pathways): we set the pathway geometries into Tile2Net by obtaining the rectangular envelope of selected EPCs and running Tile2Net, we then clipped the output to our EPCs. Remaining data cleaning for pedestrian pathways includes distinguishing between greenpaths, sidewalks, and crosswalks, and between gaps that are model noise versus genuine service gaps. Manual cleaning may be necessary to distinguish these data.
## 3. Missing Data Analysis
While our model integrates bus, school, and census tract EPC data, it is subject to several forms of “Dark Data”, or data that is missing or hidden during the analytical process, as introduced by David J. Hand in his novel Dark Data: Why What You Don’t Know Matters<sup>18</sup>. This Dark Data is identified and classified in the following sections.
### A) Selection Bias and Target Population Gaps
Our school data, drawn from California Open Data Portal (2023-2024), may omit non-traditional learning institutions such as “learning pods”, unregistered micro-schools post-pandemic, and transitional kindergarten and pre-K programs. This omission can be classified as both selection bias and a mismatch of the target population and the sample population. In other words, the data we are relying on only identifies schools officially registered by the State, leaving out non-traditional and unregistered schools. This bias can result in our conclusions also leaving students omitted by the data, resulting in an incomplete analysis of the impacted target population. 

Since there are no clear cut avenues to mitigate the absence of this data, we will emphasize in our findings, discussion, and implications that the results of our study can only be applied to schools registered with the California Department of Education. 
### B) Self-Selection Bias 
A key missing link in our data acquisition is the travel paths that link schools and households in which students are commuting from. Students in EPCs may self-select into schools outside their district rather than the school nearest to them, which is the assumption our analysis is grounded in. This data is “dark” because we only consider that students will attend their local schools rather than bypassing them for further options. Hand classifies this as self-selection bias; in the context of our analysis it could result in an inaccurate representation of ridership demand at EPC bus stops.

Our analysis is mostly unaffected by this missing data, we are hoping that by focusing on transit stops we are meeting the needs of a large majority of pedestrians using these streets no matter which jurisdiction they are coming from. 
### C) Strategic Dark Data
The transit data we rely on provides scheduled bus frequencies, but may not record instances when buses are too full to stop or other historical reliability disruptions. Hand coins this missing data as strategic dark data. While the transit agencies may report “on-time performances” by skipping stops to meet schedules, this hides the real-life frequency from the data, resulting in the data being incongruent with true rider experience.

We plan to mitigate this by incorporating a reliability buffer into our metrics. Rather than assuming the shortest wait time, we will calculate accessibility based on a “headway +1” basis, assuming a student may miss one full bus cycle due to capacity constraints.
### D) Proxy Bias
Our analysis uses enrollment data from the California Open Data Portal. This data may not account for chronic absences in the student population. Hand classifies this type of missing data as proxy bias. Our analysis treats total enrollment as a proxy for students who will ride buses to get to school. However, if absences are high and recurring for any particular analysis area, we may be overforecasting demand for bus transit. 

We plan to mitigate this dark data by applying weighting factors based on district-level absenteeism rates in EPCs to scale our demand forecast to a more realistic daily ridership level. 
## 4. Initial Results and Visualizations
### A) Equity in School Access
The primary justification for our analysis on bus stop connectivity in relation to school access is the higher degree of transit reliance found within EPCs. As shown in Figure 1, census tracts within EPCs show a higher median proportion of households without access to a vehicle compared to Non-EPC tracts. Most Non-EPC tracts cluster below 10 percent, EPC tracts see vehicle-less rates between 10 and 20 percent with outliers as high as 75 percent. 

This data establishes that for a significant portion of families in EPCs, walking or public transit is not a choice but a necessity when it comes to accessing mandatory daily school attendance. Thus, gaps in pedestrian networks or a lack of bus stop proximity or frequency represents a direct barrier to educational access for students. Consequently, SRTS programs should prioritize EPCs for infrastructure investment and policy intervention. Addressing these specific transit-to-school gaps is a pressing point of equity that allows policymakers and planners to direct resources where the ‘time-tax’ is most prevalent on disadvantaged households and their youth. The following figures provide an overview of our initial results regarding EPCs and public transit access disparities.
<div align="center">
  <img width="512" height="436" alt="EPC" src="https://github.com/user-attachments/assets/3122d685-02b2-45b9-8e90-0f82bc22f57b" /> 
</div>
<p align="center">
  <i><b>Figure 1:</b> EPCs in Alameda County</i>
</p>

<div align="center">
  <img width="600" height="300" alt="epc_geography_changes" src="https://github.com/user-attachments/assets/baead368-29d6-4b29-a5fe-deeb26c6ab45" />
</div>
<p align="center">
  <i><b>Figure 2:</b> Share of Equity Priority Community Geography</i>
</p>

<div align="center">
<img width="750" height="450" alt="alameda_zvhhs_tracts_pct_zvhhs_bxplot" src="https://github.com/user-attachments/assets/d27bcb2e-2fca-4df3-af1a-23e22ad542c6" />
</div>
<p align="center">
  <i><b>Figure 3:</b> Distribution of Share of Zero Vehicle Households in Alameda County Census Tracts</i>
</p>

### B) EPCs as a Focal Point of this Analysis
The following data analyses of school demographics within EPCs compared to Non-EPCs further reinforces why SRTS projects should prioritize EPCs and takes a deeper look at who is being impacted by these transit gaps. 

As shown in Figure 3, schools located within EPCs have a median socioeconomically disadvantaged (SED) population of approximately 92 percent with schools serving a population that is at least 80 percent disadvantaged. *brief SED clarification*. In contrast, schools in Non-EPC tracts show a much wider distribution and a significantly lower median of approximately 37 percent. This indicates that transit-dependent infrastructure in EPCs serves the most economically vulnerable students in Alameda County. 

<div align="center">
<img width="750" height="450" alt="ac_students_sed_SEDpct_bxplot" src="https://github.com/user-attachments/assets/f02d4d61-10d8-496a-8d51-2e91a2ee4ee5" />
</div>
<p align="center">
  <i><b>Figure 4:</b> Distribution of Socioeconomically Disadvantaged Students in Alameda County Schools</i>
</p>

The SED gap is also a racial one, as shown in Figures 4 and 5. The charts show that schools in EPCs serve a student population that is approximately 88 percent BIPOC with a 95 percent confidence interval. Schools in Non-EPCs serve significantly fewer BIPOC students, averaging approximately 72 percent of their student body. This further highlights that when students in EPCs face service gaps at bus stops, students of color are disproportionately impacted. 

<div align="center">
<img width="650" height="450" alt="ac_students_poc_poc_pct_v2_95CI" src="https://github.com/user-attachments/assets/264fc730-f2f3-4291-b26d-9759fcd98619" />
</div>
<p align="center">
  <i><b>Figure 5:</b> Average Share of BIPOC Students in EPC and non-EPC Tracts with 95 Percent Confidence Intervals </i>
</p>

<div align="center">
<img width="750" height="450" alt="ac_students_poc_poc_pct_v2_bxplot" src="https://github.com/user-attachments/assets/125f255b-d5dd-49be-b9d7-e5bd4d47734a" />
</div>
<p align="center">
  <i><b>Figure 6:</b> Boxplot of Average Share of BIPOC Students in EPC and non-EPC Tracts </i>
</p>

According to the breakdown of school types in Figure 6, EPCs are more heavily served by public institutions at 81 percent than the countywide average, which is 74 percent. Thus, the burden of providing safe, accessible transit falls primarily on public infrastructure and public school district coordination. 

<div align="center">
<img width="800" height="350" alt="alameda_school_types" src="https://github.com/user-attachments/assets/3e65592a-25cc-4273-b5ab-dfc291b78da1" />
</div>
<p align="center">
  <i><b>Figure 7:</b> School Type Breakdown (EPCs vs Alameda County) </i>
</p>

In Figures 3 and 4, the presence of outliers, especially in Non-EPC areas, suggests that while the EPC designation captures the majority of the need, there are still pockets of SED transit-reliance outside of the EPC zones. 

While we map the demographics of schools within EPCs, a notable caveat remains as discussed earlier in the missing data analysis regarding students in the EPCs who may be commuting out to schools in Non-EPC areas. These students are not captured in this analysis and their travel paths may be more complex than the transit-reliance being analyzed in this report.  

### B) Generated Maps of EPCs
The following analysis details the spatial relationship between pedestrian infrastructure, high-frequency transit nodes, and K-12 educational institutions across three representative EPC tracts. By layering Tile2Net-extracted pedestrian geometries with bus stop and school data, we can identify specific barriers that contribute to educational inequity. 

#### [insert] EPC Accessibility Analysis (update to current maps)
In the central and eastern portion of the Alameda Census Tract, Map 1 shows relatively high network permeability with respect to the two schools. However, there’s a notable gap west of Main Street. In this area, high-frequency bus stops are distributed less uniformly and gaps in the pedestrian paths are visible as well. Students commuting from the western portion of the EPC face a double burden: they reside at a greater geographic distance from the schools and must navigate significant infrastructure gaps to reach the nearest available bus stop. 

**placeholder **
<p align="center">
  <i><b>Figure 8:</b> Analysis of Pedestrian and Transit Connectivity to Schools within Oakland Airport EPC</i>
</p>

#### [insert] EPC Accessibility Analysis (update to current maps)
The San Leandro EPC highlights a land-use mismatch. The southern residential core possesses a high-density pedestrian grid, indicating strong local walkability. However, as the network moves northwest toward industrial zones, the infrastructure collapses. Pedestrian paths become sparse and disjointed, and high-frequency bus stops disappear entirely.

While these areas are primarily industrial, they often border or contain residential pockets or last-mile segments of a student’s commute. Students living near or adjacent to these industrial buffers are effectively isolated from the transit network. They must traverse long, high-stress distances through areas designed for freight and heavy machinery rather than student safety to access the nearest arterial bus line. This illustrates how industrial zoning acts as a hard barrier to equitable school access.
**placeholder **
<p align="center">
  <i><b>Figure 9:</b> Analysis of Pedestrian and Transit Connectivity to Schools within Nimitz EPC</i>
</p>

#### [insert] EPC Accessibility Analysis (update to current maps)
In the Castro Valley EPC, the primary barrier shifts from land use to topography and structural severance. Unlike the flat grids of the previous sites, the pedestrian network here is disjointed, with paths clustered along ridgelines and valley floors. This creates a high "Topographical Tax"; although two points may appear spatially proximate in a 2D Euclidean model, the actual physical effort and safety risk required to navigate steep, winding terrain without continuous sidewalks are significantly higher.

Furthermore, schools in Figure 10 are situated at the periphery of the pedestrian network. The northernmost school exists in a transit desert, with almost no high-frequency bus stops linking the campus to the residential clusters in the hills. This represents a severe access deficit: students are forced to rely either on private vehicles, which our data shows are statistically more scarce in EPCs, or walk the entirety of high-grade, steep terrain.

**placeholder **
<p align="center">
  <i><b>Figure 9:</b> Analysis of Pedestrian and Transit Connectivity to Schools within West Oakland EPC</i>
</p>

Across all three maps, high-frequency bus stops are located strictly along major arterial roads, with minimal transit penetration into residential clusters. With this context, a walk to the nearest bus stop could mean navigating through industrial zones, steep terrain, or major freeway intersections. This highlights a critical service gap as the bus stop distribution prioritizes regional through-traffic rather than the “last-mile” transportation needs of students.

#### Key Patterns
- Students must navigate high-stress environments, including industrial zones, steep grades, and major freeway intersections, to reach "high-frequency" stops.
- The concentration of stops on arterials assumes a baseline of pedestrian connectivity that our Tile2Net analysis proves is often missing.
- These findings suggest that SRTS funding should not just focus on the school gate, but on the pedestrian-transit interface several blocks away, where the most significant last-mile failures occur.

<iframe 
  src="Alameda_EPC_Schools_Map.html" 
  width="100%" 
  height="600px" 
  style="border:none;">
</iframe>

## References
1. Metropolitan Transportation Commission (MTC), “Bay Area Safe Routes to School.” https://mtc.ca.gov/funding/investment-strategies-commitments/climate-protection/bay-area-safe-routes-school.
2. N. Wexler et al., "Free Transit Passes and School Attendance among High School Students," Transportation Research Record 2675, no. 10 (2021).
3. USDOT, Safe Routes to School (SRTS).
4. Safe Routes Partnership, "History of Safe Routes to School," https://saferoutespartnership.org/safe-routes-school/srts-history/.
5. U.S. Department of Transportation (USDOT), Safe Routes to School (SRTS) Statewide Mobility Assessment Study: Phase I Report (2010).
6. Christine Voss et al., "School-travel by public transit: Rethinking active transportation," Preventive Medicine Reports 2 (2015).
7. Sarah A. Cordes, Amy Ellen Schwartz, and Leanna Stiefel, "The Path to School: The Effects of School Commutes on Attendance and Academic Outcomes," Educational Evaluation and Policy Analysis 44, no. 1 (2022): 45–68.
8. Kristin Blagg et al., The Road to School: How Far Students Travel to School in the Choice-Rich Cities of Denver, Detroit, New Orleans, New York City, and Washington, DC (Urban Institute, 2018).
9. Jon Valant and Jane Arnold Lincove, "Transportation Inequities and School Choice: How Car, Public Transit, and School Bus Access Affect Families’ Options," Educational Researcher 52, no. 6 (2023): 335–347.
10. Blagg et al., The Road to School.
11. Metropolitan Transportation Commission (MTC). "Equity Priority Communities." Plan Bay Area 2050.
12. Y. Guo and C. Brakewood, "Analysis of spatiotemporal transit accessibility and transit inequity of essential services in low-density cities, a case study of Nashville, TN," Transportation Research Part A: Policy and Practice 179 (2024): 103934.
13. Michael A. Gottfried, "Linking Getting to School With Going to School," Educational Evaluation and Policy Analysis 39, no. 4 (2017).
14. Wexler et al., "Free Transit Passes."
15. UPPER Project (EU Transit Consortium), "Giving Catchment Areas a Reality Check: Incorporating Walkability into Transport Planning," Mobility Strategy White Papers, November 2024.
16. California Air Resources Board (CARB), "Street and Network Connectivity: 2025 Policy Brief," Sustainable Communities Research Series, Sacramento, CA, 2025.
17. Housing development: major transit stops: vehicular traffic impact fees, Assemb. Bill 2553, 2023-2024 Reg. Sess., ch. 275, 2024 Cal. Stat. (amending Cal. Pub. Res. Code § 21064.3).
18. David J. Hand, Dark Data: Why What You Don’t Know Matters, (2020).
