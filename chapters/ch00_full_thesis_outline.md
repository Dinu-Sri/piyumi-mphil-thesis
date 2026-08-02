---
title: "Organization of the Thesis"
status: "working draft - included in thesis build"
source: "chapters/thesis_outline.md; chapters/ch00_detailed_thesis_outline.md"
created: "2026-08-02"
last_updated: "2026-08-02"
---

# Organization of the Thesis

This thesis is organized around two connected research phases. The first and major phase focuses on improving the optical performance of CsI(Tl)-based scintillation detectors through the development of an enhanced reflective coating. The second phase connects the improved detector concept to a personal radiation monitoring network, showing how detector-level improvement can support centralized real-time monitoring through a Personal Radiation Detector (PRD) and Central Alarm Station (CAS) framework.

## Chapter 1: Introduction

Chapter 1 introduces the background and justification for the research. It explains the importance of radiation detection in medical imaging, environmental monitoring, nuclear facilities, and border-security applications. The chapter then introduces scintillation detectors and the specific problem of scintillation photon propagation loss, where secondary photons generated inside the scintillator may escape, scatter, or be absorbed before reaching the photodetector.

The chapter identifies the limitations of currently used reflective coatings, especially practical limitations associated with MgO coating performance, bonding, uniformity, and optical efficiency. It also introduces the applied monitoring problem: personal radiation detectors are useful for front-line officers, but standalone PRD systems need stronger integration with centralized alarm stations for real-time reporting and response.

The chapter establishes the research gap, objectives, research questions, scope, and limitations. The main objective is to enhance CsI(Tl)-based scintillation detector performance by developing an optimized reflective coating system and demonstrating its practical applicability within a personal radiation monitoring framework.

## Chapter 2: Introduction to Radiation Detection and Monitoring Systems

Chapter 2 will review the scientific and technical background required for the study. It will begin with the history and principles of radioactivity and radiation detection, including radiation interactions with matter and the evolution of radiation detector technologies.

The chapter will compare major detector types, including gas-filled detectors, scintillation detectors, and semiconductor detectors. It will then focus on scintillation detector operation, including scintillation crystal behavior, photon generation, photodetector coupling, and the role of optical reflection in improving light collection.

The literature review will also cover reflective coating materials and coating strategies used in scintillation detectors. It will discuss MgO-based coatings and alternative white oxide materials such as TiO2, Al2O3, ZnO, and BaSO4. The review will consider properties relevant to this study, including absorbance, diffuse reflectance, particle size, refractive behavior, binder compatibility, coating adhesion, hygroscopicity, and long-term stability.

The final part of the chapter will review wireless radiation monitoring networks, PRD systems, mesh communication, and CAS-based monitoring approaches. This provides the context for linking detector-material improvement with field-level monitoring and alarm communication.

## Chapter 3: Materials, Characterization and System Prototyping Techniques

Chapter 3 describes the methodology used in the study. The methodology is organized into two phases.

Phase 1 focuses on the material-science development of the reflective coating. It describes the selection of coating materials, including TiO2, MgO, Al2O3, ZnO, and BaSO4, and the evaluation of binder systems such as PVP, PVAc, and CMC. It also explains the selection of solvents and coating methods, with attention to the hygroscopic nature of CsI(Tl).

The characterization methods include particle size analysis, UV-visible spectroscopy, diffuse reflectance spectroscopy, X-ray diffraction, digital colorimetry, visual compatibility observations, and coating-thickness measurement. Since CsI(Tl) has an emission peak near 550 nm, optical behavior near this wavelength is treated as a critical evaluation point.

Phase 2 describes the system prototyping approach for the PRD-CAS communication concept. This includes hardware prototyping, PCB integration, network layout configuration, software environment, remote monitoring, and dashboard or central alarm integration.

## Chapter 4: Development of an Enhanced Coating for a Scintillation Detector

Chapter 4 presents the first research study, which develops and evaluates reflective coatings for CsI(Tl)-based scintillation detector enhancement. The chapter explains the preparation of coating samples using selected oxide materials and binder combinations. Initial coating trials are performed on glass substrates because actual CsI(Tl) crystals are moisture-sensitive, expensive, and limited in availability.

The chapter reports baseline characterization of coating materials and binders, visual compatibility observations, absorbance behavior at 550 nm, and diffuse reflectance comparisons. It also explains why the doctor-blade method was replaced by spin coating for improved coating uniformity.

The chapter identifies TiO2 + PVP as the most suitable coating formulation based on the combined optical and practical coating-performance evidence available in the current draft. Further optimization considers binder concentration, coating thickness, surface stability, and practical handling behavior.

## Chapter 5: Development of a Personal Radiation Monitoring Network

Chapter 5 will present the second phase of the thesis: the development of a personal radiation monitoring network. This chapter will describe how the detector concept is connected to a PRD-CAS monitoring framework.

The chapter will include the detector module, SiPM coupling, low-noise PCB design, XBee3 or IEEE 802.15.4 mesh communication, firmware-level count-rate processing, node communication, alarm transmission, and central monitoring. The focus will be on demonstrating how the improved detector concept can support real-time monitoring, bidirectional communication, reduced reporting delay, and centralized alarm handling.

This chapter should clearly distinguish between experimentally validated detector-material results and system-level prototype or application results. Claims about network performance, reliability, latency, power consumption, and field deployment should be supported by measured data or written as planned/future validation points.

## Chapter 6: Conclusions, Recommendations and Future Suggestions

Chapter 6 will summarize the major findings of the thesis. It will state whether the enhanced coating objective was achieved, identify the best coating material and binder combination, and explain the relevance of the optimized coating for improving photon collection in CsI(Tl)-based scintillation detectors.

The chapter will also summarize the PRD-CAS monitoring contribution and explain how material-level detector improvement and network-level monitoring can complement each other. Recommendations will include the preferred coating formulation, application method, and future testing needed before practical detector manufacturing or deployment.

Future work may include direct coating validation on actual CsI(Tl) scintillator surfaces, long-term environmental stability testing, extended gamma irradiation testing, detector-response comparison with coated and uncoated crystals, and full field validation of the PRD-CAS communication network.

## References and Appendices

The References section will include all sources cited in the thesis, formatted consistently according to the selected thesis reference style. The WUSL guideline prefers Harvard referencing; however, the current source drafts use numbered citation markers, so reference-style conversion should be handled carefully during citation cleanup.

Appendices may include raw spectrometer data, coating formulation details, additional characterization outputs, PRD-CAS network code or configuration details, supplementary figures, and published or accepted articles arising from the thesis work.

