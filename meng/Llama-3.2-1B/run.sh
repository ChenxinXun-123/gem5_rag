source Llama-3.2-1B/Llama_venv/bin/activate
rocminfo

# export ROCM_PATH=/opt/rocm-6.1.0
# export PATH=$ROCM_PATH/bin:$PATH
# export LD_LIBRARY_PATH=$ROCM_PATH/lib:$LD_LIBRARY_PATH
# export HSA_PATH=$ROCM_PATH
# source /opt/rocm-6.1.0/bin/rocm-env


# echo --------------------------------------------------------------------------------------------
# ldd /opt/rocm/lib/libamdhip64.so.6
# echo --------------------------------------------------------------------------------------------
# pip list
# echo --------------------------------------------------------------------------------------------
# ls /opt/rocm*
# echo --------------------------------------------------------------------------------------------
# nm -D /opt/rocm/lib/libhsa-runtime64.so.1 | grep hsa_amd_vmem_unmap
# echo --------------------------------------------------------------------------------------------
# echo $LD_LIBRARY_PATH
# echo --------------------------------------------------------------------------------------------

# python3 Llama-3.2-1B/test.py
python3 Llama-3.2-1B/new_test.py
