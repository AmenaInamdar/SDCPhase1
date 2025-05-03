import subprocess

sumo_binary = "sumo-gui"  # or "sumo" for no-GUI
config_file = "sumo_config.sumocfg"

subprocess.run([sumo_binary, "-c", config_file])
