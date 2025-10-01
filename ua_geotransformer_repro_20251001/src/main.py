import argparse, yaml, os, sys

def run(cfg):
    print("Loaded config:", cfg)
    # TODO: call your pipeline steps here
    # e.g., load data, train model, predict, export figures

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--config", default="configs/default.yaml")
    args = ap.parse_args()
    with open(args.config,"r") as f:
        cfg = yaml.safe_load(f)
    run(cfg)