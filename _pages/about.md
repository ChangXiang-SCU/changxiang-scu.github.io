---
permalink: /
title: "About"
excerpt: "Xiang Chang, PhD student at HKUST (Guangzhou): HCI/HRI, human factors of automated driving, multimodal sensing"
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

Hi! I'm **Xiang Chang (畅想)**, a PhD student in **Robotics and Autonomous Systems** at **The Hong Kong University of Science and Technology (Guangzhou)**, advised by **Prof. Dengbo He** and co-advised by **Prof. Jun Ma**. I received dual M.S. degrees from **Cornell Tech** in 2026, where I worked with **Prof. Wendy Ju** and **Prof. Angelique Taylor**, and I was a visiting student researcher at **Stanford University** in summer 2025.

I study how people interact with automated and robotic systems in safety-critical settings, especially **autonomous vehicles**. My work spans four threads:  
1) **Human factors and safety of automated driving**: how drivers, passengers, and pedestrians perceive, predict, and calibrate trust in AVs and robotaxis;  
2) **HCI/HRI for intent communication**: legible cues and adaptive behaviors, such as gesture-based eHMI and socially adaptive AV driving policies;  
3) **Multimodal physiological sensing**: EEG, eye tracking, and PPG/HRV pipelines for real-time driver-state estimation in VR, simulator, and on-road studies;  
4) **LLM-based multi-agent systems**: understanding how agent teams coordinate and fail in safety-critical workflows such as emergency care.

My work has appeared at **CHI**, **AutomotiveUI**, **HFES ASPIRE**, and **SIGGRAPH (Posters)**, and in **Human Factors** and **Scientific Data**. I review for **CHI**, **AutomotiveUI**, **Transportation Research Part F**, and **Acta Psychologica**.

**Google Scholar citations**  
<a href='https://scholar.google.com/citations?user=k_03qNkAAAAJ'>
  <img src="https://img.shields.io/endpoint?url={{ url | url_encode }}&logo=Google%20Scholar&labelColor=f6f6f6&color=9cf&style=flat&label=citations">
</a>



<span class='anchor' id='news'></span>
# 🔥 News
- *2026.09*: &nbsp;Started my PhD in Robotics and Autonomous Systems at **HKUST (Guangzhou)**, advised by Prof. Dengbo He.
- *2026.07*: &nbsp;**CTA-STGT**, our work on EEG-based eVTOL pilot workload estimation, was accepted to **AutomotiveUI 2026 Works in Progress**.
- *2026.07*: &nbsp;**Beyond Benchmark Accuracy** was accepted to the **COLM 2026 Workshop on LLM/VLM Deployment Opportunities and Risks in Healthcare**.
- *2026.05*: &nbsp;**GraspAuto** was accepted to **SIGGRAPH 2026 Posters** (91 of 379 submissions accepted).
- *2026.05*: &nbsp;Graduated from **Cornell Tech** with dual M.S. degrees.
- *2026.04*: &nbsp;Our naturalistic-driving EEG dataset was published in **Scientific Data**.
- *2025.10*: &nbsp;Presented our robotaxi trust study and served as **Session Chair (ST4: Pedestrian Behavior & Interactions)** at **HFES ASPIRE 2025** in Chicago.
- *2025.06*: &nbsp;Joined **Stanford University** as a visiting student researcher to study mind-wandering in automated urban driving.
- *2025.06*: &nbsp;Our paper on **contingent AV driving behaviors** was accepted to **AutomotiveUI 2025**.
- *2024.04*: &nbsp;Published our work on **gesture-based eHMI for AV–pedestrian interaction** at **CHI 2024**.

<span class='anchor' id='publications'></span>
# 📝 Publications

### Journal Articles

<!-- Human Factors 2026 -->
<div class='paper-box'>
  <div class='paper-box-image'>
    <div>
      <div class="badge">Human Factors 2026</div>
      <img src='images/thumb_paper_human_factors.png?v=4' alt="Trust Evolvement in Robotaxis" width="100%">
    </div>
  </div>
  <div class='paper-box-text' markdown="1">
**Users’ Trust Evolvement in Fully Driverless Robotaxis During First Ride: An On-Road Study.**<br>
Zhenyu Wang, Weiyin Xie, Haolong Hu, **Xiang Chang**, Meng Sun, and Dengbo He.<br>
*Human Factors*, 68(6), 788–805, 2026.<br>
[DOI](https://doi.org/10.1177/00187208261420147)<span class='show_paper_citations' data='k_03qNkAAAAJ:W7OEmFMy1HYC'></span>
  </div>
</div>

<!-- Scientific Data 2026 -->
<div class='paper-box'>
  <div class='paper-box-image'>
    <div>
      <div class="badge">Scientific Data 2026</div>
      <img src='images/thumb_paper_2025_scientific_data.png?v=4' alt="EEG Dataset for Driving Expertise" width="100%">
    </div>
  </div>
  <div class='paper-box-text' markdown="1">
**An EEG Dataset for Understanding Driving Expertise from Naturalistic Urban Road Experiments.**<br>
Jiangtao Gong, Yueteng Yu, Yancheng Cao, Ruoxuan Yang, **Xiang Chang**, Haoming Tang, Xiaoji Zheng, Yiyao Liu, Shanhe You, Chen Zheng, and Guyue Zhou.<br>
*Scientific Data*, 13, 884, 2026.<br>
[DOI](https://doi.org/10.1038/s41597-026-07223-1) · [Code](https://github.com/AIR-DISCOVER/ExpertDrivingDataset)<span class='show_paper_citations' data='k_03qNkAAAAJ:mB3voiENLucC'></span>
  </div>
</div>

### Conference Papers

<!-- AutomotiveUI 2025 -->
<div class='paper-box'>
  <div class='paper-box-image'>
    <div>
      <div class="badge">AutomotiveUI 2025</div>
      <video width="100%" controls playsinline preload="none" poster="images/thumb_paper_2025_autoui.png?v=4">
        <source src="images/paper_2025_autoui.mp4?v=4" type="video/mp4">
        Your browser does not support the video tag.
      </video>
    </div>
  </div>
  <div class='paper-box-text' markdown="1">
**Socially Adaptive Autonomous Vehicles: Effects of Contingent Driving Behavior on Drivers' Experiences.**<br>
Chishang Yang, **Xiang Chang**, Debargha Dey, Zhuoqi Xu, Avi Parush, and Wendy Ju.<br>
*AutomotiveUI 2025.*<br>
[DOI](https://doi.org/10.1145/3744333.3747814)<span class='show_paper_citations' data='k_03qNkAAAAJ:zYLM7Y9cAGgC'></span>
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
**The Formation of Trust in Autonomous Vehicles after Interacting with Robotaxis on Public Roads.**<br>
**Xiang Chang**, Zhijie Yi, Yichang Liu, Hongling Sheng, Dengbo He.<br>
*HFES ASPIRE 2025.* **Best Paper Finalist.**<br>
[DOI](https://doi.org/10.1177/10711813251358236)<span class='show_paper_citations' data='k_03qNkAAAAJ:Tyk-4Ss8FVUC'></span>
  </div>
</div>

<!-- CHI 2024 -->
<div class='paper-box'>
  <div class='paper-box-image'>
    <div>
      <div class="badge">CHI 2024</div>
      <img src='images/thumb_paper_2024_chi.png?v=4' alt="Gesture-based eHMI for AVs" width="100%">
    </div>
  </div>
  <div class='paper-box-text' markdown="1">
**"It Must Be Gesturing Towards Me": Gesture-Based Interaction between Autonomous Vehicles and Pedestrians.**<br>
**Xiang Chang**, Zihe Chen, Xiaoyan Dong, Yuxin Cai, Tingmin Yan, Haolin Cai, Zherui Zhou, Guyue Zhou, and Jiangtao Gong.<br>
*CHI Conference on Human Factors in Computing Systems, 2024.*<br>
[DOI](https://doi.org/10.1145/3613904.3642029)<span class='show_paper_citations' data='k_03qNkAAAAJ:d1gkVwhDpl0C'></span>
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
**Community-driven Information Accessibility: Online Sign Language Content Creation within d/Deaf Communities.**<br>
Xinru Tang, **Xiang Chang**, Nuoran Chen, Yingjie Ni, RAY LC, and Xin Tong.<br>
*CHI Conference on Human Factors in Computing Systems, 2023.*<br>
[DOI](https://doi.org/10.1145/3544548.3581286)<span class='show_paper_citations' data='k_03qNkAAAAJ:u5HHmVD_uO8C'></span>
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
**Influencing Factors of Resident Satisfaction in Smart Community Services: An Empirical Study in Chengdu.**<br>
Rongxin Jin, Yifan Liu, Lichen Yang, **Xiang Chang**.<br>
*ICEB 2022.*<br>
[Paper](https://aisel.aisnet.org/iceb2022/25)<span class='show_paper_citations' data='k_03qNkAAAAJ:u-x6o8ySG0sC'></span>
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
**Study on the Influencing Factors of Health Information Sharing Behavior of the Elderly under the Normalization of the Pandemic Situation.**<br>
Chenyu Li, Chengxi Sun, **Xiang Chang**, Luoming Liang, Yao Ma, Fan Ke.<br>
*ICEB 2021.* **Best Paper Award.**<br>
[Paper](https://aisel.aisnet.org/iceb2021/48)<span class='show_paper_citations' data='k_03qNkAAAAJ:9yKSN-GCB0IC'></span>
  </div>
</div>

### Posters, Workshops & Extended Abstracts

<!-- SIGGRAPH 2026 Posters -->
<div class='paper-box'>
  <div class='paper-box-image'>
    <div>
      <div class="badge">SIGGRAPH 2026 Posters</div>
      <img src='images/thumb_paper_2026_siggraph.png?v=1' alt="GraspAuto single-tap grasp authoring" width="100%">
    </div>
  </div>
  <div class='paper-box-text' markdown="1">
**GraspAuto: Real-Time Single-Tap Grasp Authoring for VR/AR Experiences.**<br>
Qingxuan Yan and **Xiang Chang**.<br>
*SIGGRAPH 2026 Posters.*<br>
[DOI](https://doi.org/10.1145/3799825.3818766)<span class='show_paper_citations' data='k_03qNkAAAAJ:HDshCWvjkbEC'></span>
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
**Exploring User Needs in Fully Driverless Robotaxis: A Think-Aloud Study of First-Time On-Road Rides.**<br>
Zhenyu Wang, Haolong Hu, Weiyin Xie, **Xiang Chang**, Peixuan Xiong, and Dengbo He.<br>
*AutomotiveUI 2025 Works in Progress.*<br>
[DOI](https://doi.org/10.1145/3744335.3758506)<span class='show_paper_citations' data='k_03qNkAAAAJ:Y0pCki6q_DkC'></span>
  </div>
</div>

- **CTA-STGT: A Cortical Topology-Aware Spatiotemporal Graph Transformer for EEG-Based eVTOL Pilot Cognitive Workload Estimation.**
  Chenglin Liu, Wenjun Zhang, Zhijie Yi, Jiyao Wang, **Xiang Chang**, and Dengbo He.
  *AutomotiveUI 2026 Works in Progress.*
- **Beyond Benchmark Accuracy: Failure Modes of Multi-Agent Coordination in Safety-Critical Clinical Workflows.**
  Yuanchen Bai, Zijian Ding, **Xiang Chang**, and Angelique Taylor.
  *COLM 2026 Workshop on LLM/VLM Deployment Opportunities and Risks in Healthcare.* [OpenReview](https://openreview.net/forum?id=XBc56Lvgzz)

### Preprints

<!-- MARS (arXiv) -->
<div class='paper-box'>
  <div class='paper-box-image'>
    <div>
      <div class="badge">arXiv 2025</div>
      <img src='images/thumb_paper_2025_aaai.png?v=4' alt="Hierarchical multi-agent robotic systems" width="100%">
    </div>
  </div>
  <div class='paper-box-text' markdown="1">
**From MAS to MARS: Coordination Failures and Reasoning Trade-offs in Hierarchical Multi-Agent Robotic Systems within a Healthcare Scenario.**<br>
Yuanchen Bai, Zijian Ding, Shaoyue Wen, **Xiang Chang**, and Angelique Taylor.<br>
*arXiv:2508.04691.*<br>
[arXiv](https://arxiv.org/abs/2508.04691)<span class='show_paper_citations' data='k_03qNkAAAAJ:UeHWp8X0CEIC'></span>
  </div>
</div>

<!-- From Driver to Passenger (arXiv) -->
<div class='paper-box'>
  <div class='paper-box-image'>
    <div>
      <div class="badge">arXiv</div>
      <img src='images/thumb_paper_2026_cscw.png?v=4' alt="Evaluation Gaps in Driving Behaviour" width="100%">
    </div>
  </div>
  <div class='paper-box-text' markdown="1">
**From Driver to Passenger: Understanding Evaluation Gaps in 'Fantastic' Driving Behaviour Delivery.**<br>
Zhijie Yi\*, **Xiang Chang\***, Yueteng Yu, Xinyu Yang, Junrong Lu, Yiyao Liu, Ye Jin, Mengdi Chu, Jingli Qin, Jialin Song, and Jiangtao Gong. (\*Equal contribution)<br>
*arXiv:2311.04150.*<br>
[arXiv](https://arxiv.org/abs/2311.04150)<span class='show_paper_citations' data='k_03qNkAAAAJ:IjCSPb-OGe4C'></span>
  </div>
</div>

### Under Review

- **Supporting Simulated Resuscitation Teams with Multimodal Robotic Feedback: A Qualitative Study of a Robotic Crash Cart.** **Xiang Chang**.
- **GraspAuto: A Unity Toolkit for Surface-Selected Grasp Authoring on Late-Bound 3D Objects.** Qingxuan Yan\*, **Xiang Chang\***, and Dengbo He.

---
<span class='anchor' id='projects'></span>
# 🛠 Projects

<!-- Project: Interactive Device Design Labs -->
<div class='paper-box'>
  <div class='paper-box-image'>
    <div>
      <div class="badge">Cornell Tech INFO5345</div>
      <img src='images/thumb_project_lab_hub.png?v=1' alt="Interactive Device Design Projects" width="100%">
    </div>
  </div>
  <div class='paper-box-text' markdown="1">
**Interactive Device Design (Course Projects).**
A collection of physical computing and interactive prototyping projects utilizing Raspberry Pi, sensors, and actuators to build novel HCI hardware interfaces. Includes experiments with voice interaction (Chatterboxes), physical UIs (Ph-UI), and observant systems.
[GitHub Repository](https://github.com/ChangXiang-SCU/Interactive-Lab-Hub)
  </div>
</div>

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
- *Sept. 2026 – Present*, **The Hong Kong University of Science and Technology (Guangzhou)**, Ph.D. in Robotics and Autonomous Systems. Advisor: Prof. Dengbo He; Co-advisor: Prof. Jun Ma.
- *Aug. 2024 – May 2026*, **Cornell Tech (Cornell University)**, Jacobs Technion-Cornell Dual M.S. in Information Systems (Connective Media) and Applied Information Science (GPA: 4.0/4.3). Advisor: Prof. Wendy Ju.
- *Sept. 2019 – July 2023*, **Sichuan University (SCU)**, B.M. in Information Resource Management (GPA: 3.75/4.0).

<span class='anchor' id='experience'></span>
# 💻 Research Experience
- *Jun. 2025 – Aug. 2025*, Visiting Student Researcher, **Stanford University**, with Dr. Rebecca Currano and Prof. Mark Cutkosky: real-time eye-tracking and physiological sensing for mind-wandering detection in automated urban driving.
- *Aug. 2024 – May 2026*, Graduate Researcher, **Cornell Tech**: AV–driver negotiation (Prof. Wendy Ju) and multi-agent robotic systems for emergency care (Prof. Angelique Taylor).
- *Oct. 2023 – July 2024*, Research Assistant, **HKUST (Guangzhou)**, with Prof. Dengbo He and Prof. Mingming Fan: on-road pedestrian–robotaxi interaction and passenger trust.
- *Mar. 2023 – Sept. 2023*, Research Intern, **Institute for AI Industry Research (AIR), Tsinghua University**, with Prof. Jiangtao Gong: gesture-based eHMI and a naturalistic-driving EEG dataset.
- *Dec. 2022 – Mar. 2023*, Research Assistant, **OPPO Research Institute**.
- *May 2022 – June 2023*, Research Intern, **HCI·X Lab**, with Prof. Ray LC and Prof. Xin Tong: online sign-language content creation in d/Deaf communities.

<span class='anchor' id='service'></span>
# 📋 Academic Service
- **Reviewer**: CHI (2023–2026), AutomotiveUI (2025–2026), Transportation Research Part F, Transportation Research Interdisciplinary Perspectives, Acta Psychologica, Research in Transportation Business & Management.
- **Session Chair**: HFES ASPIRE 2025, ST4: Pedestrian Behavior & Interactions.
