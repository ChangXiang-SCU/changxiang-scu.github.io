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



<span class='anchor' id='news'></span>
# 🔥 News
- *2025.08*: &nbsp;Started a visiting student researcher stint at **Stanford University** to study mind-wandering in automated urban driving.
- *2025.06*: &nbsp;Serving as **Session Chair (ST4: Pedestrian Behavior & Interactions)** at **ASPIRE 2025**.
- *2025.05*: &nbsp;Our paper on **contingent AV driving behaviors** was accepted to **AutomotiveUI 2025**.
- *2024.04*: &nbsp;Published our work on **gesture-based eHMI for AV–pedestrian interaction** at **CHI 2024**.

<span class='anchor' id='publications'></span>
# 📝 Publications

<!-- CHI 2024 -->
<div class='paper-box'>
  <div class='paper-box-image'>
    <div>
      <div class="badge">CHI 2024</div>
      <img src='images/thumb_paper_2024_chi.png?v=4' alt="Gesture-based eHMI for AVs" width="100%">
    </div>
  </div>
  <div class='paper-box-text' markdown="1">
**"It Must Be Gesturing Towards Me": Gesture-Based Interaction between Autonomous Vehicles and Pedestrians.**
**Xiang Chang**, Zihe Chen, Xiaoyan Dong, Yuxin Cai, Tingmin Yan, Haolin Cai, Zherui Zhou, Guyue Zhou, and Jiangtao Gong.
*CHI Conference on Human Factors in Computing Systems, 2024.*
<span class='show_paper_citations' data='k_03qNkAAAAJ:TFP_iSt0sucC'></span> · [DOI](https://doi.org/10.1145/3613904.3642029) · [PDF](https://doi.org/10.1145/3613904.3642029)
  </div>
</div>

<!-- AutomotiveUI 2025 -->
<div class='paper-box'>
  <div class='paper-box-image'>
    <div>
      <div class="badge">AutomotiveUI 2025</div>
      <video width="100%" controls playsinline poster="images/thumb_paper_2025_autoui.png?v=4">
        <source src="images/paper_2025_autoui.mp4?v=4" type="video/mp4">
        Your browser does not support the video tag.
      </video>
    </div>
  </div>
  <div class='paper-box-text' markdown="1">
**Socially Adaptive Autonomous Vehicles: Effects of Contingent Driving Behavior on Drivers' Experiences.**
Chishang Yang, **Xiang Chang**, Debargha Dey, Zhuoqi Xu, Avi Parush, and Wendy Ju.
*AutomotiveUI 2025.*
<span class='show_paper_citations' data='k_03qNkAAAAJ:IjCSPb-OGe4C'></span> · [DOI](https://doi.org/10.1145/3744333.3747814) · [PDF](https://doi.org/10.1145/3744333.3747814)
  </div>
</div>

<!-- ASPIRE 2025 -->
<div class='paper-box'>
  <div class='paper-box-image'>
    <div>
      <div class="badge">ASPIRE 2025</div>
      <img src='images/thumb_paper_2025_aspire.png?v=4' alt="Trust formation after robotaxi rides" width="100%">
    </div>
  </div>
  <div class='paper-box-text' markdown="1">
**The Formation of Trust in Autonomous Vehicles after Interacting with Robotaxis on Public Roads.**
**Xiang Chang**, Zhijie Yi, Yichang Liu, Hongling Sheng, Dengbo He.
*ASPIRE 2025.*
[DOI](https://doi.org/10.1177/10711813251358236) · [PDF](https://doi.org/10.1177/10711813251358236)
  </div>
</div>

<!-- AutoUI 2025 WIP -->
<div class='paper-box'>
  <div class='paper-box-image'>
    <div>
      <div class="badge">AutoUI WIP 2025</div>
      <img src='images/thumb_paper_2025_autoui_wip.png?v=4' alt="Robotaxi first-ride study" width="100%">
    </div>
  </div>
  <div class='paper-box-text' markdown="1">
**Exploring User Needs in Fully Driverless Robotaxis: A Think-Aloud Study of First-Time On-Road Rides.**
Zhenyu Wang, Haolong Hu, Weiyin Xie, **Xiang Chang**, Peixuan Xiong, and Dengbo He.
*AutomotiveUI 2025 Works in Progress.*
[DOI](https://doi.org/10.1145/3744335.3758506) · [PDF](https://doi.org/10.1145/3744335.3758506)
  </div>
</div>

<!-- CHI 2023 -->
<div class='paper-box'>
  <div class='paper-box-image'>
    <div>
      <div class="badge">CHI 2023</div>
      <img src='images/thumb_paper_2023_chi.png?v=4' alt="Community-driven sign-language content creation" width="100%">
    </div>
  </div>
  <div class='paper-box-text' markdown="1">
**Community-driven Information Accessibility: Online Sign Language Content Creation within d/Deaf Communities.**
Xinru Tang, **Xiang Chang**, Nuoran Chen, Yingjie Ni, RAY LC, and Xin Tong.
*CHI Conference on Human Factors in Computing Systems, 2023.*
<span class='show_paper_citations' data='k_03qNkAAAAJ:u5HHmVD_uO8C'></span> · [DOI](https://doi.org/10.1145/3544548.3581286) · [PDF](https://doi.org/10.1145/3544548.3581286)
  </div>
</div>

<!-- ICEB 2022 -->
<div class='paper-box'>
  <div class='paper-box-image'>
    <div>
      <div class="badge">ICEB 2022</div>
      <img src='images/thumb_paper_2022_iceb.png?v=4' alt="Smart community service satisfaction" width="100%">
    </div>
  </div>
  <div class='paper-box-text' markdown="1">
**Influencing Factors of Resident Satisfaction in Smart Community Services: An Empirical Study in Chengdu.**
Rongxin Jin, Yifan Liu, Lichen Yang, **Xiang Chang**.
*ICEB 2022.*
<span class='show_paper_citations' data='k_03qNkAAAAJ:u-x6o8ySG0sC'></span> · [PDF](https://aisel.aisnet.org/iceb2022/25)
  </div>
</div>

<!-- ICEB 2021 -->
<div class='paper-box'>
  <div class='paper-box-image'>
    <div>
      <div class="badge">ICEB 2021</div>
      <img src='images/thumb_paper_2021_iceb.png?v=4' alt="Health information sharing of the elderly" width="100%">
    </div>
  </div>
  <div class='paper-box-text' markdown="1">
**Study on the Influencing Factors of Health Information Sharing Behavior of the Elderly under the Normalization of the Pandemic Situation.**
Chenyu Li, Chengxi Sun, **Xiang Chang**, Luoming Liang, Yao Ma, Fan Ke.
*ICEB 2021 — Best Paper.*
<span class='show_paper_citations' data='k_03qNkAAAAJ:9yKSN-GCB0IC'></span> · [PDF](https://aisel.aisnet.org/iceb2021/48)
  </div>
</div>

### Working Manuscripts & Under Review

<!-- Scientific Data -->
<div class='paper-box'>
  <div class='paper-box-image'>
    <div>
      <div class="badge">Scientific Data</div>
      <img src='images/thumb_paper_2025_scientific_data.png?v=4' alt="EEG Dataset for Driving Expertise" width="100%">
    </div>
  </div>
  <div class='paper-box-text' markdown="1">
**An EEG Dataset for Understanding Driving Expertise from Naturalistic Urban Road Experiments.**
Jiangtao Gong, Yueteng Yu, Yancheng Cao, Ruoxuan Yang, **Xiang Chang**, Haoming Tang, Xiaoji Zheng, Yiyao Liu, Shanhe You, Chen Zheng, and Guyue Zhou.
*Scientific Data (Under Review).*
[Code](https://github.com/AIR-DISCOVER/ExpertDrivingDataset.git)
  </div>
</div>

<!-- CSCW 2026 -->
<div class='paper-box'>
  <div class='paper-box-image'>
    <div>
      <div class="badge">CSCW 2026</div>
      <img src='images/thumb_paper_2026_cscw.png?v=4' alt="Evaluation Gaps in Driving Behaviour" width="100%">
    </div>
  </div>
  <div class='paper-box-text' markdown="1">
**From Driver to Passenger: Understanding Evaluation Gaps in 'Fantastic' Driving Behaviour Delivery.**
Zhijie Yi*, **Xiang Chang***, Yueteng Yu, Xinyu Yang, Junrong Lu, Yiyao Liu, Ye Jin, Mengdi Chu, Jingli Qin, Jialin Song, and Jiangtao Gong. (*Equal contribution)
*CSCW 2026 (Under Review).*
  </div>
</div>

<!-- AAAI 2026 -->
<div class='paper-box'>
  <div class='paper-box-image'>
    <div>
      <div class="badge">AAAI 2026</div>
      <img src='images/thumb_paper_2025_aaai.png?v=4' alt="Hierarchical multi-agent robotic systems" width="100%">
    </div>
  </div>
  <div class='paper-box-text' markdown="1">
**From MAS to MARS: Coordination Failures and Reasoning Trade-offs in Hierarchical Multi-Agent Robotic Systems within a Healthcare Scenario.**
Yuanchen Bai, Zijian Ding, Shaoyue Wen, **Xiang Chang**, and Angelique Taylor.
*AAAI 2026 (Under Review).*
<span class='show_paper_citations' data='k_03qNkAAAAJ:UeHWp8X0CEIC'></span> · [PDF](https://arxiv.org/abs/2508.04691)
  </div>
</div>

<!-- Human Factors -->
<div class='paper-box'>
  <div class='paper-box-image'>
    <div>
      <div class="badge">Human Factors</div>
      <img src='images/thumb_paper_human_factors.png?v=4' alt="Trust Evolvement in Robotaxis" width="100%">
    </div>
  </div>
  <div class='paper-box-text' markdown="1">
**Users’ Trust Evolvement in Fully Driverless Robotaxis During First Ride: An On-road Study.**
Zhenyu Wang, Weiyin Xie, Haolong Hu, **Xiang Chang**, Meng Sun, and Dengbo He.
*Human Factors (Under Review).*
  </div>
</div>

---
<span class='anchor' id='projects'></span>
# 🛠 Projects

<!-- Project 2 (Mind-Wandering) - Kept as it is not a paper yet -->
<div class='paper-box'>
  <div class='paper-box-image'>
    <div>
      <div class="badge">Stanford VSR 2025</div>
      <img src='images/thumb_project_mind_wandering.png?v=5' alt="Mind-wandering detection pipeline" width="100%">
    </div>
  </div>
  <div class='paper-box-text' markdown="1">
**Mind-Wandering Detection in Automated Urban Driving.**
Built a real-time Unity → eye tracking + PPG pipeline (event tagging, IBI/HRV) to study attention in automated urban driving.
Real-time integration of Tobii XR eye tracking and Polar PPG with synchronized event tagging for attention and workload analysis.
  </div>
</div>

---

<span class='anchor' id='honors-and-awards'></span>
# 🎖 Honors and Awards
- *2025* **Gary Marsden Travel Awards**, The ACM Special Interest Group on Computer-Human Interaction.
- *2021* **Best Paper Award**, International Conference on Electronic Business (ICEB 2021).
- *2021* **Uniqlo Scholarship for Academic Excellence**, SCU (5/10,000 in university).
- *2019-2021* **Merit-based Scholarship**, SCU (Top 10% in department).

<span class='anchor' id='educations'></span>
# 📖 Education
- *Aug. 2024 – May 2026*, **Cornell Tech (Cornell University)** — Jacobs Technion-Cornell Dual M.S. in Connective Media (GPA: 4.0/4.3).
- *Sept. 2019 – July 2023*, **Sichuan University (SCU)** — B.M. in Information Resource Management (GPA: 3.75/4.0).

<span class='anchor' id='internships'></span>
# 💻 Internships
- *Jun. 2025 – Aug. 2025*, Visiting Student Researcher, **Stanford University** — mind-wandering detection in automated driving.
- *Aug. 2024 – Present*, Graduate Researcher, **Cornell Tech** — multi-agent robotic systems for ER onboarding and AV driver negotiation.
- *Oct. 2023 – July 2024*, Research Assistant, **Hong Kong University of Science and Technology** — pedestrian–AV interaction datasets.
- *Mar. 2023 – Sept. 2023*, Intern Researcher, **Institute for AI Industry Research, Tsinghua University** — robotaxi trust and AV eHMI.
- *Dec. 2022 – Mar. 2023*, Research Assistant, **OPPO Research Institute** — HCI research support.
