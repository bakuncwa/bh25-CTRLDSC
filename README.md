# 🌾 LigtasAni: Soil pH Prediction Web App for Flood-Resilient Farming

**🏆 Placed Top 5 out of 90+ participants** at the Computer Society of Ateneo's **Blue Hacks 2025**, themed *Disaster Risk Management and Reduction in the Philippines*.
Developed by **Ctrl+DSC** (Association of Information Management, Benilde).

---

## 📍 Project Description

**LigtasAni** is a Python Django-based web application that predicts soil acidity using farm geolocation data and theoretical soil pH sensor input. Targeted at flood-prone areas like Nueva Ecija, it aims to support Filipino farmers with real-time, predictive recommendations on whether their soil is too acidic or saline—enabling them to proactively take measures to prevent crop yield loss during or before floods.

---

## 💡 Objectives

From **February 22–23, 2025**, Ctrl+DSC participated in a 24-hour hackathon (Blue Hacks 2025) hosted by CompSAt Gear at the Ateneo de Manila University. Focused on addressing flood-induced soil degradation in Nueva Ecija, we prototyped **LigtasAni** to help rice farmers better manage soil health through actionable ML-driven insights.

---

---

## 💡 Problem Statement

Nueva Ecija plays a crucial role in national rice production, yet frequent severe flooding disrupts agricultural activities and threatens farmers’ livelihoods (Paz-Alberto et al., 2018). Urban flood hazards in areas such as Cabanatuan City, Bongabon, and Gabaldon are classified as high, occurring at least once per decade. The Philippines increasingly depends on rice imports (3.8 MMT in 2023; projected 4.9 MMT in 2025) due to declining local yields (Congressional Policy and Budget Research Department, 2024). Addressing flooding and soil degradation is critical for stable production.

**Target Users:**  
Large and small-scale rice farmers who directly experience crop loss due to flooding and soil acidity.

---

## 💡 Solution Pathways

LigtasAni transforms crop management by:

- Providing real-time soil analysis using integrated IoT sensors (“Grainy”).
- Enabling predictive recommendations on soil health and acidity.
- Helping farmers adjust practices proactively to mitigate environmental and climate-related risks.
- Reducing yield losses and cultivating healthier, more resilient crops.

**Solution Features:**

| Feature Type | Feature Description |
|-------------|-------------------|
| **Core** | Soil Acidity Prediction Model (CatBoostClassifier, 90% accuracy, 100% precision), Location-based risk assessment |
| **Enabling** | Lime Application Alerts, Nutrient Deficiency Detection (N, Zn, Mg) |
| **Enhancing** | Interactive Django web application for data visualization and recommendations |

---

## 📊 Business & Marketing Strategy

**Business Models:**

1. **Enterprise Model (Public-Private Partnership):**  
   LGUs purchase enterprise licenses covering 5,000–50,000 farmers per municipality. Nationwide scaling possible via disaster resilience programs.

2. **Subsidized Subscription Model:**  
   Farmers access premium features free of charge; government agencies fund the service.

**Market Scope:**

| Metric | Value |
|--------|-------|
| Total Addressable Market (TAM) | 1.49M rice farms; potential revenue ~14.9B PHP/year |
| Serviceable Addressable Market (SAM) | Central Luzon: 346,000 farms |
| Target Adoption | 10–20% adoption → 34,600–69,200 paying farms |
| Annual Subscription Fee | Basic Tier: 3,000 PHP/farm; Premium Tier: 6,000 PHP/farm |
| Annual Revenue Estimates | 103.8M PHP (10% adoption, Basic) – 415.2M PHP (20% adoption, Premium) |
| Estimated Annual Profit (30% margin) | 52–104M PHP |

---

## 🧠 Machine Learning Model

* Achieved **90% accuracy** and **100% precision** in classifying soil acidity.
* Data modeling involved theoretical values gathered for soil pH sensors.
* Converted ionic concentration of acid/base-related chemicals (e.g., **H⁺, Zn, Mn, Fe, Cu, P, Na, N**) to g/dm³.
* Calculated rainfall increases (mm) correlating to hydrogen ion concentration shifts.
* Acidity defined as hydrogen ion concentration equivalent to **pH 1–6**.
* Built using:

  * **Logistic Regression**
  * **CatBoostClassifier** (Gradient Boosted Decision Trees)

---

## 🏆 Key Takeaways

- Flood-prone agricultural regions require predictive and preventive solutions rather than reactive disaster alerts.
- ML-powered soil health recommendations improve resilience and productivity.
- Strategic partnerships with LGUs and government agencies enable wide adoption and sustainability.
- Scalable platform design allows expansion to other crops and regions prone to climate risks.

--

## 🔧 Tech Stack

| Category           | Technology / Library          |
|-------------------|-------------------------------|
| **Backend**        | Python, Django, SQLite3, Apache Spark |
| **Frontend**       | HTML, CSS, JavaScript        |
| **Machine Learning** | Scikit-learn, pandas, CatBoost |
| **Database**       | SQLite3                      |

---

## 👩‍💻 Team Ctrl+DSC – Roles and Responsibilities

| Name                         | Role                                         |
| ---------------------------- | -------------------------------------------- |
| **Gabrielle Ysabel Almirol** | ML Developer, Front-End & Back-End Developer |
| **Jan Andrei Montenegro**    | Front-End & Back-End Developer               |
| **Andrea Ochotorena**        | UI Designer, Researcher                      |
| **Nicole Vera Cruz**         | Illustrator, Researcher, Presenter           |

- Constructed predictive multiple logistic regression recommendation CatboostClassifier GBDT model via scikit-lean and model loader for hydrogen molar ionic concentration’ acid dissociation affecting soil acidity or alkalinity per rainfall increase (mm); achieved 90% accuracy, 100% precision, 94% F1 score, and 100% recall.
- Loaded the soil classification model into Django web-based application with JSON API architecture to process rainfall impact on soil concentration values fed from sqlite3 database.
- Developed dynamic front-end features using HTML, CSS, JavaScript functions with optimized asset loading times.

---

## 📌 References

1. Paz-Alberto, A. et al., 2018. Flood hazard mapping and impacts.  
2. Congressional Policy and Budget Research Department, 2024. Rice imports and local yields.  
3. PSA, 2022. Census of Agriculture and Fisheries.  
4. PhilRice Ricelytics, Valuations, 2023.  
5. Malaya Business Insight, 2022. Blue-collar job seekers on the rise.  
6. Philippine Statistics Authority, 2023. Urban Barangays in the Philippines.
