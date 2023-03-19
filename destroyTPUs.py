import subprocess



def createTPUs(tpu_names, zone, project, tpu_version, accelerator_type: str,  tpu_count , preemptible:bool = True, verbosity: str = "info"):
    for tpu in tpu_names:
        subprocess.call(
            [
                "gcloud",
                "compute",
                "tpus",
                "tpu-vm",
                "delete", f"{tpu}",
                "--zone", zone,
                "--project", project,
                "--version", tpu_version,
                "--network=default",
                "--accelerator-type", accelerator_type,
                "--preemptible" if preemptible else "",
                "--verbosity", verbosity
            ]
        )
