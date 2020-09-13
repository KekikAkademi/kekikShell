# BADlnk v1.0
## Author: github.com/thelinuxchoice/badlnk
## Twitter: twitter.com/linux_choice

Reverse Shell in Shortcut File (.lnk)

![lnk](https://user-images.githubusercontent.com/34893261/66158011-6248c900-e5fb-11e9-84ad-ab04df52786c.png)

### How it works?

Shortcut file (Microsoft Windows 9.x)
LNK is a file extension for a shortcut file used by Microsoft Windows to point to an executable file. LNK stands for LiNK. Shortcut files are used as a direct link to an executable file, instead of having to navigate to the executable. LNK files contain some basic properties, such as the path to the executable file and the “Start-In” directory. LNK files use a curled arrow to indicate they are shortcuts, and the file extension is hidden (even after disabling “Hide Extensions for Known File Types” in Windows Explorer).
The script creates a .lnk file that points to the user's "cmd.exe" file (located in the default folder C:\Windows\System32\cmd.exe) to run a reverse shell through arguments.

### Issues

Once the .lnk file is created, to work, you need to edit it in Windows to remove the quotes in the "target path".

### Features:
FUD (until someone upload it to virustotal)
Port Forwarding using Serveo

## Legal disclaimer:

Usage of BADlnk for attacking targets without prior mutual consent is illegal. It's the end user's responsibility to obey all applicable local, state and federal laws. Developers assume no liability and are not responsible for any misuse or damage caused by this program 

### Usage:
```
git clone https://github.com/thelinuxchoice/badlnk
cd badlnk
bash badlnk.sh
```

### Donate!
Support the authors:
### Paypal:
https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&hosted_button_id=CLKRT5QXXFJY4&source=url
### LiberaPay:
<noscript><a href="https://liberapay.com/thelinuxchoice/donate"><img alt="Donate using Liberapay" src="https://liberapay.com/assets/widgets/donate.svg"></a></noscript>
