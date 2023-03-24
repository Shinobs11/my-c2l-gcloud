import subprocess
import asyncio
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
from time import sleep
import os

log_path = "logs"
def createTPUs(tpu_name, zone, project, tpu_version, accelerator_type: str,  tpu_count , preemptible:bool = True, verbosity: str = "info"):
  def _createTPU(tpu_number, output_file):    
    if preemptible:
      subprocess.call(
          [
              "gcloud",
              "compute",
              "tpus",
              "tpu-vm",
              "create", f"{tpu_name}_{tpu_number}",
              "--zone", zone,
              "--project", project,
              "--version", tpu_version,
              "--network=default",
              "--accelerator-type", accelerator_type,
              "--preemptible"
          ],
          stdout=f,
          stderr=f
    )
    else:
      subprocess.call(
          [
              "gcloud",
              "compute",
              "tpus",
              "tpu-vm",
              "create", f"{tpu_name}_{tpu_number}",
              "--zone", zone,
              "--project", project,
              "--version", tpu_version,
              "--network=default",
              "--accelerator-type", accelerator_type,
          ],
          stdout=f,
          stderr=f
    )
        
  
  promises = []
  results = []
  with ThreadPoolExecutor(max_workers=tpu_count) as executor:
    if not os.path.exists(log_path):
      os.makedirs(log_path)
    for tpu_number in range(tpu_count):
        f = open(f"{log_path}/{tpu_name}_{tpu_number}.log", "w+")
        executor.submit(_createTPU, tpu_number, f)
    for future in asyncio.as_completed(promises):
      try:
        results.append(future.result())
      except:
          print("Error getting results")
          pass


if __name__ == "__main__":
    while True:

      createTPUs(
          tpu_name="v38_pt",
          zone="us-central1-f",
          project="jmclin2-c2l",
          tpu_version="tpu-vm-pt-1.13",
          accelerator_type="v3-8",
          tpu_count=5,
          preemptible=False,
          verbosity="info"
      )
      # createTPUs(
      #     tpu_name="v38_tf",
      #     zone="us-central1-f",
      #     project="jmclin2-c2l",
      #     tpu_version="tpu-vm-tf-2.10.0",
      #     accelerator_type="v3-8",
      #     tpu_count=2,
      #     preemptible=False,
      #     verbosity="info"
      # )
      # createTPUs(
      #     tpu_name="v28_tf",
      #     zone="us-central1-f",
      #     project="jmclin2-c2l",
      #     tpu_version="tpu-vm-tf-2.10.0",
      #     accelerator_type="v2-8",
      #     tpu_count=2,
      #     preemptible=False,
      #     verbosity="info"
      # )
      sleep(30)