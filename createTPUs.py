import subprocess
import asyncio
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor

log_path = "logs"
def createTPUs(tpu_name, zone, project, tpu_version, accelerator_type: str,  tpu_count , preemptible:bool = True, verbosity: str = "info"):
    def _createTPU(tpu_number):
      with open(f"{log_path}/{tpu_name}_{tpu_number}.log", "w") as f:
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
                "--preemptible" if preemptible else "",
                "--verbosity", verbosity
            ],
            stdout=f,
            stderr=f
      )
    promises = []
    results = []
    with ThreadPoolExecutor(max_workers=tpu_count) as executor:
      for tpu_number in range(tpu_count):
          executor.submit(_createTPU, tpu_number)
      for future in asyncio.as_completed(promises):
        try:
          results.append(future.result())
        except:
           print("Error getting results")
           pass


if __name__ == "__main__":
    
    createTPUs(
        tpu_name="test",
        zone="us-central1-f",
        project="jmclin2-c2l",
        tpu_version="tpu-vm-pt-1.13",
        accelerator_type="v2-8",
        tpu_count=3,
        preemptible=True,
        verbosity="info"
    )