# vLLM Gem5 Project

## Installation Instructions

1. Install Git LFS (Large File Storage):
```bash
sudo apt-get install git-lfs
git lfs install
```

2. Download the model (requires adding ssh key to Huggingface account with access to Llama3.2):

```bash
chmod +x download_llama.sh
./download_llama.sh
```

3. Set up Python virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate
```

4. Install dependencies:
```bash
pip install -r requirements.txt
```

5. Run example program:
```bash
source venv/bin/activate # if not done already
python main.py
```