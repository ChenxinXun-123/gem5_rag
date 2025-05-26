cd vllm_gem5-main/
source vllm_venv/bin/activate

lspci
dkms status | grep amdgpu
rocm-smi
hipcc --version
echo ---------------------------------------------------------------------
rocminfo
echo ---------------------------------------------------------------------
groups
echo ---------------------------------------------------------------------
echo aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
echo aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
echo aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
# rocminfo


python3 main.py