"""Minimal example for FeatureScale."""

from featurescale import featurescale


def main():
 runner = featurescale({"name": "FeatureScale", "dry_run": False})
 result = runner.execute()
 print(result)


if __name__ == "__main__":
 main()