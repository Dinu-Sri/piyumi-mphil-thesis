---
title: "Thesis Summary"
status: "source-derived summary"
source: "source_documents/thesis_summaries/Thesis Summary.docx"
created: "2026-08-02"
last_updated: "2026-08-02"
---

Thesis Summary:

Development of Enhanced Reflective Coatings for Scintillation Detectors and an Integrated Personal Radiation Monitoring Network

Modern radiological monitoring requires high-sensitivity detectors for applications. which is now essential across nuclear energy, medical imaging, border security, and environmental protection to ensure long-term operational safety. The functionality of the radiation detector is identifying ionizing radiation. Among the various detection technologies, scintillation detectors, particularly those utilizing solid-state scintillators, are most widely employed for the qualitative and quantitative measurement of high-energy electromagnetic radiation such as X-rays and gamma rays.

These detectors function by converting high-energy radiation into low-energy photons. However, a persistent challenge is "propagation loss": many secondary photons escape through uncoupled crystal surfaces before they can reach the photomultiplier. When these photons exit the system without being captured, the detector's overall efficiency is significantly compromised.

This research addresses the photon loss in CsI(Tl) scintillation detectors by developing an improved reflective coating to enhance light collection efficiency. This optimized scintillator was integrated into a Personal Radiation Detector (PRD) designed for centralized radiation monitoring, combining the high sensitivity and simplicity of scintillation-based detection.

The study was conducted in two complementary phases, targeting both material-level efficiency and system-level integration. The first phase focused on minimizing photon escape from Thallium doped Cesium Iodide CsI(Tl) crystals through the development of a high-reflectance coating. Five candidate materials: Industrial grade titanium dioxide (TiO2), magnesium oxide (MgO), aluminum oxide (Al2O3), zinc oxide (ZnO), and barium sulfate (BaSO4) (98% purity) were selected based on literature review, optical properties and diffuse reflectance.

The materials were characterized using UV-visible spectroscopy and X-ray diffraction to confirm purity and structural consistency. Particle size analysis showed a uniform distribution between 10 and 25 um, suitable for forming a scattering interface that enhances light collection near the scintillator's 550 nm emission peak. Baseline optical properties were evaluated using UV-visible spectroscopy over the 300 to 600 nm range, confirmed low absorbance across all candidate oxides revealing lowest absorbance from the Al2O3.

The performance of these materials is highly influenced by their interaction with binding agents used to ensure adhesion to the crystal and maintain the structural and optical properties of the crystal. Three binding agents, polyvinyl pyrrolidone (PVP), carboxymethyl cellulose (CMC), and polyvinyl acetate (PVA) were selected to evaluate. To protect the hygroscopic nature of the Cs(Tl) surface, a non-aqueous solvent, absolute ethanol was used. Absorbance and diffuse reflectance measurements showed that PVP had the lowest absorbance at 550 nm, identifying it as the most suitable binder for reflective coating.

The coating preparation method was modified after the doctor-blade method encountered difficulties in achieving a homogeneous layer. Spin coating was adopted, with optimal conditions identified as 500 rpm for 30 s, yielding consistent and reproducible film thickness and uniformity was confirmed by traveling microscopy.

Fifteen samples, combining five reflective materials with three binders at a fixed wt.% of material: binder: solvent (5 wt.%: 5 wt.%: 90 wt.%), were evaluated and the TiO2 + PVP coating showed the best diffuse reflectance. Five samples with CMC were excluded due to poor adhesion observed by visual inspection, and the remaining ten samples were carried out for further experiments.

Absorbance measurements at 550 nm identified five coatings with lower absorbance than their raw materials: Al2O3 + PVA, TiO2 + PVA, ZnO + PVA, Al2O3 + PVP, and TiO2 + PVP. Although the BaSO4 + PVP showed reduced transmittance (10.09%) compared to the raw material (17.37%), it remained relatively high among the tested samples. From above 10 samples these six coatings were selected for further experimental validation based on overall optical performance.

The six selected coatings were evaluated with uniform thickness of 100 to 120 um and a 20 wt.%: 10 wt.%: 70 wt.% ratio. TiO2 + PVP coating emerged as the optimum sample, a result of the high refractivity of TiO2 and its uniform particle distribution with PVP. Further optimization of the TiO2 + PVP involved varying the binder content (2, 5, 10, and 15 wt.%). Although the 15 wt.% sample yielded the highest reflectance, it resulted in undesirable surface properties, including tackiness and dust attraction, in contrast, lower binder levels (2 and 5 wt.%), showed poor adhesion and "chalking", making them unsuitable for practical applications.

Conversely, the TiO2 + PVP, 20 wt.% : 10 wt.% sample identified as the optimal wt.%. Fabricated via spin-coating method at 500 RPM for 30 seconds to achieve a uniform thickness of 100 - 120 um, this specific ratio balances a high reflectance with the structural durability for industry.

Operational stability was assessed by exposing coatings to cumulative gamma irradiation from 5 to 60 kGy. Post-exposure analysis confirmed the radiological robustness; colorimetric assessments revealed no optical degradation or color change, while XRD verified the preservation of the TiO2 crystalline structure. These results indicate that the coating maintains its optical integrity even under extreme radiation exposure, ensuring detector efficiency for long-term nuclear applications.

Phase 2 focused on bridging the data gap in standalone monitoring by coupling a 2 cm3 CsI(Tl) crystal with a Silicon Photomultiplier (SiPM). The module was integrated into a 4-layer low-noise PCB with IEEE 802.15.4 XBee3 mesh modules, ensuring signal integrity and real-time network connectivity.

A key innovation was firmware-level processing, allowing nodes to analyze count rates locally, reducing power and bandwidth demands. Paired with a low-power mesh network, the system ensured reliable, bidirectional communication with the Central Alarm Station (CAS).

System validation using a 26.5 kBq 137Cs source demonstrated a linear response and reliable data delivery. To manage those, a custom Python-based dashboard was developed to visualize real-time counts per second (CPS) and synchronize automated alarms, ensuring immediate localized response when safety thresholds are breached.

This research offers a comprehensive solution by aligning material science with network engineering. While Phase 1 identified a TiO2+PVP coating as an optimal reflective medium and withstands up to 60 kGy of high radiation, Phase 2 complemented this by developing a scalable, low-power mesh network for centralized real-time monitoring. Together, these advancements form a high-performance, cost-effective framework for the next generation of nuclear security and environmental safety systems.
