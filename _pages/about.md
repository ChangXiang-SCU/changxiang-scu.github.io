---
permalink: /
title: "About"
excerpt: "Xiang Chang — HCI, Human-Centered Automation, AV–Human Interaction"
author_profile: true
redirect_from:
  - /about/
  - /about.html
---

{% if site.google_scholar_stats_use_cdn %}
{% assign gsDataBaseUrl = "https://cdn.jsdelivr.net/gh/" | append: site.repository | append: "@" %}
{% else %}
{% assign gsDataBaseUrl = "https://raw.githubusercontent.com/" | append: site.repository | append: "/" %}
{% endif %}
{% assign url = gsDataBaseUrl | append: "google-scholar-stats/gs_data_shieldsio.json" %}

<span class='anchor' id='about-me'></span>

Hi! I’m **Xiang Chang** — a master’s student in Connective Media at **Cornell Tech** (’26) preparing a PhD application. I study how people interact with **automation** in safety-critical contexts, especially **autonomous vehicles (AVs)**. My goal is to design interfaces and behaviors that communicate intent clearly, adapt to the human in the loop, and maintain **trust and safety** from first contact to long-term use.

My research threads come together around three themes:  
1) **Human-centered automation & HCI** — modeling how drivers and pedestrians perceive, predict, and calibrate trust in automated systems;  
2) **AV–human interaction (eHMI & policy)** — designing expressive, legible cues (e.g., gesture-based eHMI) and evaluating AV yielding policies that reduce hesitation and conflict;  
3) **Multimodal sensing for cognition** — building pipelines that pair **eye tracking** and **PPG/HRV** with behavioral events in VR and on-road studies to capture attention, workload, and confidence in real time.

Methodologically, I combine **experimental design** (lab/VR field studies), lightweight **prototyping** (Unity/Unreal, web), and **signal processing** to translate noisy, real-world data into interpretable measures—then close the loop with design/behavior changes. I’ve worked with **Tobii** eye trackers and **Polar** PPG, built time-aligned logging for event streams and physiology, and analyzed trust/hesitation as outcomes that interfaces can meaningfully shift.

My recent work includes papers at **CHI 2023** and **CHI 2024**, plus a study on **contingent AV driving** accepted to **AutomotiveUI 2025**. Ongoing projects explore first-ride trust in fully driverless services and mind-wandering detection in automated urban driving. I also review for **CHI**, **AutomotiveUI**, and **Transportation Research Part F**. I’m actively seeking **PhD opportunities (Fall 2026)** and collaborations that blend behavioral science with robust sensing and prototyping.

**Google Scholar citations**  
<a href='https://scholar.google.com/citations?user=k_03qNkAAAAJ'>
  <img src="https://img.shields.io/endpoint?url={{ url | url_encode }}&logo=Google%20Scholar&labelColor=f6f6f6&color=9cf&style=flat&label=citations">
</a>



# 🔥 News
- *2022.02*: &nbsp;🎉🎉 Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus ornare aliquet ipsum, ac tempus justo dapibus sit amet. 
- *2022.02*: &nbsp;🎉🎉 Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus ornare aliquet ipsum, ac tempus justo dapibus sit amet. 

<span class='anchor' id='publications'></span>
# 📝 Publications 

<!-- CHI 2023 -->
<div class='paper-box'>
  <div class='paper-box-image'>
    <div>
      <div class="badge">CHI 2023</div>
      <img src='images/pubs/chi2023_accessibility.jpg' alt="Community-driven sign-language content creation" width="100%">
    </div>
  </div>
  <div class='paper-box-text' markdown="1">
**Community-driven Information Accessibility: Online Sign Language Content Creation within d/Deaf Communities.**  
*CHI Conference on Human Factors in Computing Systems, 2023.*  
<span class='show_paper_citations' data='k_03qNkAAAAJ:u5HHmVD_uO8C'></span> · [DOI](https://doi.org/10.1145/3544548.3581286) · [PDF](#)
  </div>
</div>

<!-- ICEB 2022 -->
<div class='paper-box'>
  <div class='paper-box-image'>
    <div>
      <div class="badge">2022</div>
      <img src='images/pubs/iceb2022_smart_community.jpg' alt="Smart community service satisfaction" width="100%">
    </div>
  </div>
  <div class='paper-box-text' markdown="1">
**Influencing Factors of Resident Satisfaction in Smart Community Services: An Empirical Study in Chengdu.**  
*ICEB 2022.*  
<span class='show_paper_citations' data='k_03qNkAAAAJ:u-x6o8ySG0sC'></span> · [PDF](#)
  </div>
</div>

<!-- ICEB 2021 -->
<div class='paper-box'>
  <div class='paper-box-image'>
    <div>
      <div class="badge">2021</div>
      <img src='images/pubs/iceb2021_health_info.jpg' alt="Health information sharing of the elderly" width="100%">
    </div>
  </div>
  <div class='paper-box-text' markdown="1">
**Study on the Influencing Factors of Health Information Sharing Behavior of the Elderly under the Normalization of the Pandemic Situation.**  
*ICEB 2021 — Best Paper.*  
<span class='show_paper_citations' data='k_03qNkAAAAJ:9yKSN-GCB0IC'></span> · [PDF](#)
  </div>
</div>

<!-- arXiv 2025 -->
<div class='paper-box'>
  <div class='paper-box-image'>
    <div>
      <div class="badge">arXiv 2025</div>
      <img src='images/pubs/mas_to_mars.jpg' alt="MARS: hierarchical multi-agent robotic systems" width="100%">
    </div>
  </div>
  <div class='paper-box-text' markdown="1">
**From MAS to MARS: Coordination Failures and Reasoning Trade-offs in Hierarchical Multi-Agent Robotic Systems within a Healthcare Scenario.**  
*arXiv, 2025.*  
<span class='show_paper_citations' data='k_03qNkAAAAJ:UeHWp8X0CEIC'></span> · [PDF](#) · [Code](#)
  </div>
</div>

---
<span class='anchor' id='projects'></span>
## Projects

<!-- Project 1 -->
<div class='paper-box'>
  <div class='paper-box-image'>
    <div>
      <div class="badge">AutomotiveUI 2025</div>
      <img src='images/projects/contingent_avs.jpg' alt="Contingent AV driving behavior study" width="100%">
    </div>
  </div>
  <div class='paper-box-text' markdown="1">
**Socially Adaptive AVs: Drivers’ Experiences under Contingent Driving.**  
VR driving-simulator study comparing **contingent** vs. always/never-yield AV policies; contingent behavior reduced hesitation and stress.  
[Paper](#) · [Preprint](#) · [Video](#)
  </div>
</div>

<!-- Project 2 -->
<div class='paper-box'>
  <div class='paper-box-image'>
    <div>
      <div class="badge">Stanford VSR 2025</div>
      <img src='images/projects/mind_wandering.jpg' alt="Mind-wandering detection pipeline" width="100%">
    </div>
  </div>
  <div class='paper-box-text' markdown="1">
**Mind-Wandering Detection in Automated Urban Driving.**  
Built a real-time Unity → eye tracking + PPG pipeline (event tagging, IBI/HRV) to study attention in automated urban driving.  
[Demo](#) · [Code](#)
  </div>
</div>

<!-- Project 3 -->
<div class='paper-box'>
  <div class='paper-box-image'>
    <div>
      <div class="badge">On-road</div>
      <img src='images/projects/robotaxi_trust.jpg' alt="Robotaxi first-ride trust" width="100%">
    </div>
  </div>
  <div class='paper-box-text' markdown="1">
**Robotaxi First-Ride Trust.**  
On-road study of fully driverless rides; modeling **first-ride trust formation** and its evolution after exposure.  
[Preprint](#)
  </div>
</div>

<!-- Project 4 -->
<div class='paper-box'>
  <div class='paper-box-image'>
    <div>
      <div class="badge">eHMI</div>
      <img src='images/projects/gesture_ehmi.jpg' alt="Gesture-based eHMI prototypes" width="100%">
    </div>
  </div>
  <div class='paper-box-text' markdown="1">
**Gesture-based eHMI.**  
Prototyped and evaluated **gesture-based** external HMI for AV–pedestrian communication; informs the CHI’24 paper above.  
[Design Notes](#) · [Video](#)
  </div>
</div>

---

# 🎖 Honors and Awards
- *2021.10* Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus ornare aliquet ipsum, ac tempus justo dapibus sit amet. 
- *2021.09* Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus ornare aliquet ipsum, ac tempus justo dapibus sit amet. 

# 📖 Educations
- *2019.06 - 2022.04 (now)*, Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus ornare aliquet ipsum, ac tempus justo dapibus sit amet. 
- *2015.09 - 2019.06*, Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus ornare aliquet ipsum, ac tempus justo dapibus sit amet. 

# 💬 Invited Talks
- *2021.06*, Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus ornare aliquet ipsum, ac tempus justo dapibus sit amet. 
- *2021.03*, Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus ornare aliquet ipsum, ac tempus justo dapibus sit amet.  \| [\[video\]](https://github.com/)

# 💻 Internships
- *2019.05 - 2020.02*, [Lorem](https://github.com/), China.