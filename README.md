# 🌾 LigtasAni: Soil pH Prediction Web App for Flood-Resilient Farming

**🏆 Placed Top 5 out of 90+ participants** at the Computer Society of Ateneo's **Blue Hacks 2025**, themed *Disaster Risk Management and Reduction in the Philippines*.
Developed by **Ctrl+DSC** (Association of Information Management, Benilde).

---

## 📍 Project Overview

**LigtasAni** is a Python Django-based web application that predicts soil acidity using farm geolocation data and theoretical soil pH sensor input. Targeted at flood-prone areas like Nueva Ecija, it aims to support Filipino farmers with real-time, predictive recommendations on whether their soil is too acidic or saline—enabling them to proactively take measures to prevent crop yield loss during or before floods.

---

## 💡 Motivation

From **February 22–23, 2025**, Ctrl+DSC participated in a 24-hour hackathon (Blue Hacks 2025) hosted by CompSAt Gear at the Ateneo de Manila University. Focused on addressing flood-induced soil degradation in Nueva Ecija, we prototyped **LigtasAni** to help rice farmers better manage soil health through actionable ML-driven insights.

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

## 🔧 Tech Stack

* **Backend:** Python, Django, SQLite3
* **Frontend:** HTML, CSS, JavaScript
* **Machine Learning:** Scikit-learn, CatBoost
* **Database:** SQLite3

---

## 👩‍💻 Team Ctrl+DSC – Roles and Responsibilities

| Name                         | Role                                         |
| ---------------------------- | -------------------------------------------- |
| **Gabrielle Ysabel Almirol** | ML Developer, Front-End & Back-End Developer |
| **Jan Andrei Montenegro**    | Front-End & Back-End Developer               |
| **Andrea Ochotorena**        | UI Designer, Researcher                      |
| **Nicole Vera Cruz**         | Illustrator, Researcher, Presenter           |
