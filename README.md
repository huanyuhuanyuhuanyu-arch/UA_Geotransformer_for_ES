[![Code DOI](https://zenodo.org/badge/1067845994.svg)](https://doi.org/10.5281/zenodo.17243850)
[![Data DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.17251210.svg)](https://doi.org/10.5281/zenodo.17251210)
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/huanyuhuanyuhuanyu-arch/UA_Geotransformer_for_ES/blob/main/notebooks/UA_suitability_Geotransformer_for_ES.ipynb)

# UA Suitability – GeoTransformer for ES (Open Code & Data)

This repository shares the **code and datasets** accompanying the manuscript. The primary goal is **open availability** (not full push-button replication). A Colab entry and minimal local setup are provided for convenience.

## Quick start

**Option A – Colab (one-click entry)**  
Use the badge above. Run the first cell “Reproducibility Setup”, then run the rest in order.

**Option B – Local**
```bash
conda env create -f environment.yml
conda activate ua-geotransformer-repro
python -m pip install -r requirements.txt
jupyter lab
# open notebooks/UA_suitability_Geotransformer_for_ES.ipynb
```

**Option C – Script**
```bash
python src/main.py --config configs/default.yaml
```

**Data access**  
See `data/README.md` for the Data DOI and direct links. The notebook includes a light **Data Download** cell (no checksums).

## Repository layout
- `notebooks/` – main analysis notebook (Colab-friendly).
- `configs/` – default paths & parameters (`default.yaml`).
- `src/` – placeholders for modular scripts.
- `data/` – (empty) folder for user-side downloads: `data/raw`, `data/processed`.

## Citation
Code: 10.5281/zenodo.17243850  
Data: 10.5281/zenodo.17251210

## License
MIT (replace if your preference differs).
