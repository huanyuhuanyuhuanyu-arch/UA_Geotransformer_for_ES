# UA Suitability – GeoTransformer for ES (Reproducibility Package)
[![DOI](https://zenodo.org/badge/1067845994.svg)](https://doi.org/10.5281/zenodo.17243850)
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/huanyuhuanyuhuanyu-arch/UA_Geotransformer_for_ES/blob/main/notebooks/UA_suitability_Geotransformer_for_ES.ipynb)

This repository packages the code and instructions to reproduce the results from the manuscript using the original Colab notebook **UA_suitability_Geotransformer_for_ES.ipynb**.

## Quick start

**Option A – Colab**
1. Click the badge above.
2. Follow the first cell instructions to install `requirements.txt` from this repo and set up paths.
3. Run the notebook cells in order.

**Option B – Local**
```bash
conda env create -f environment.yml
conda activate ua-geotransformer-repro
python -m pip install -r requirements.txt
jupyter lab
# open notebooks/UA_suitability_Geotransformer_for_ES.ipynb
```

**Option C – Scripted**
```bash
python src/main.py --config configs/default.yaml
```

## Data access
See `data/README.md` for download links / instructions and integrity checks.
> None of the large datasets are committed to Git. Provide DOIs (Zenodo/OSF) or public mirrors and SHA256 checksums.

## Reproducibility notes
- Random seeds detected in the original notebook: 123, 42, 456 (unify in `configs/default.yaml`).
- GPU not required (no CUDA usage detected).
- Avoid absolute paths (e.g., `/content/...`). Use `configs/default.yaml` and relative paths.

## Citation
Please cite the paper and this code repository. A `CITATION.cff` file can be added after DOI minting.

## License
Choose an appropriate license (MIT/Apache-2.0/CC BY 4.0); replace this section accordingly.
