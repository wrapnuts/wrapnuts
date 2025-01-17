![](https://github.com/wrapnuts/wrapnuts/blob/main/cli.png)

# Wrapnuts-cli

A CLI that implements the functionality of embedded cashu by interacting with the Nutshell-wallet **[I.]**. This CLI was developed as a proof of concept for embedding cashu. Launch a test flight according to the steps below.

## Roadmap

- [x] Steghide tool by Hetzl, S. **[II.]**
- [x] Embedding cashu in photos (.jpg & .png) 
- [x] Embedding cashu in audio files (.wav)
- [x] Encryption, let users choose passphrase
- [x] Let users choose amount of cashu to wrap
- [x] Support for users connected to multiple mints
- [ ] Support and test more file types

## Requirements

**[I.]** Install [Nutshell](https://github.com/cashubtc/nutshell?tab=readme-ov-file) & **[II.]** [steghide](https://steghide.sourceforge.net/index.php), according to their docs. Or use a package manager, like apt:

1. Install dependencies with apt:

```bash
sudo apt install -y steghide python3-pip python3-qrcode pkg-config python3.10-venv
```
2. Create venv and upgrade pip:

```bash
python3 -m venv cashu_venv
source cashu_venv/bin/activate
```
```bash
python3 -m pip install --upgrade pip
```
3. Install Nutshell:

```bash
pip install cashu
```
4. Test cashu if it does not work, follow Cashu's [README](https://github.com/cashubtc/nutshell?tab=readme-ov-file)

```bash
cashu info
```
## Install wrapnuts

1. Clone repo

```bash
git clone https://github.com/wrapnuts/wrapnuts.git
```
2. Set permissions

```bash
chmod 700 wrapnuts/wrapnuts-cli.py
chmod 700 wrapnuts/.cache/cache.sh
chmod 700 wrapnuts/.cache/redeem.sh
```

## Test flight

1. Make sure to have a compatible file (.jpg, .png, or .wav) in working directory of Wrapnuts-cli and then run:

```bash
python3 wrapnuts-cli.py
```

2. Enter “1” in main menu of Wrapnuts-cli. If no balance is displayed, make sure to fulfill the two requirements:
    - Is Nutshell-wallet connected to a mint?
    - Do you have a balance?

3. If balance is displayed, both requirements are met. Next, enter “2” in main menu to wrap (embed) a cashu. Follow instructions until wrapping process is complete.

4. The file (with the embedded cashu) can be sent to someone else, before it is redeemed with Wrapnuts-cli.

5. To redeem embedded cashu, enter “3” in main menu of Wrapnuts-cli. Follow instructions until the unwrapping process is complete.

## Disclaimer 

The author is NOT a cryptographer and this work has not been reviewed. This means that there is very likely a fatal flaw somewhere. Wrapnuts and Cashu are still experimental and not production-ready.
