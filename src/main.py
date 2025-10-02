import argparse, yaml

def run(cfg):
    print("Loaded config:")
    print(yaml.dump(cfg, sort_keys=False))
    # TODO: plug your pipeline here using cfg['paths']
    # e.g., read rasters from cfg['paths'], stack drivers, train/infer, export outputs

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--config", default="configs/default.yaml")
    args = ap.parse_args()
    with open(args.config, "r") as f:
        cfg = yaml.safe_load(f)
    run(cfg)