# Example of Running a Phoenix Experiment against a Phoenix Instance running in a Container

## 0) Install Deps
```
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt --upgrade
```

## 1) Get Phoenix running in docker

See Phoenix docs for more details <https://docs.arize.com/phoenix/deployment/docker>

# Phoenix image is pegged to same version as in the requirements.txt, these should be kept in sync
```bash
docker run -p 6006:6006 -p 4317:4317 -i -t arizephoenix/phoenix:version-4.23.0
```
