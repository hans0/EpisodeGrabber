from re import sub
import subprocess

def get_local_hostname():
  # Linux
  hostname_proc = subprocess.run(
    args=['hostname', '-I'],
    capture_output=True,
  )
  # macOS
  if hostname_proc.returncode != 0:
    hostname_proc = subprocess.run(
      args=['ipconfig', 'getifaddr', 'en0'],
      capture_output=True,
    )
    host_str = str(hostname_proc.stdout)
    return host_str[2:-3]
  host_str = str(hostname_proc.stdout)
  return host_str.split(' ')[0][2:].strip()

print(get_local_hostname())