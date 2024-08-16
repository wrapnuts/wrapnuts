![](https://github.com/wrapnuts/wrapnuts/blob/main/wrapnuts.png)

This CLI was developed as a proof of concept for embedding cashu. Launch a test flight according to the steps below.

# Wrapnuts-cli

A Cashu-wallet based on Nutshell **[I.]** that implements the functionality of embedded cashu.

## Roadmap

- [x] Main menu
- [x] Steghide tool by Hetzl, S. **[II.]**
- [x] Embedding cashu in photos
- [x] Embedding cashu in audio files
- [x] Extracting and redeeming embedded cashu
- [x] Encryption, let users choose passphrase
- [x] Let users choose amount of cashu to wrap


## Requirements

**[I.]**  Install [Nutshell](https://github.com/cashubtc/nutshell?tab=readme-ov-file) according to their docs & **[II.]** install [steghide](https://steghide.sourceforge.net/index.php) according to their docs or use a package manager, like apt:

1. Install dependencies with apt:

```bash
sudo apt install -y steghide python3-pip python3-qrcode pkg-config
```
2. Upgrade pip:

```bash
sudo pip3 install --upgrade pip
```
3. Install cashu:

```bash
sudo pip install cashu
```
4. Test cashu if it does not work, follow Cashu's [README](https://github.com/cashubtc/nutshell?tab=readme-ov-file)

```bash
cashu info
```

## Test flight

1. Go to the working directory of Nutwraps-cli and then run it:

```bash
python3 wrapnuts-cli.py
```

2. Enter “1” in the main menu of wrapnuts-cli. If the balance is not displayed, make sure to fulfill the two requirements:
    - Is the Cashu-wallet connected to a mint?
    - and does it have a balance?

3. If balance is displayed, both requirements have been met. Next, enter “2” in the main menu of Wrapnuts-cli to wrap a cashu and follow the instructions until the wrapping process is complete.

4. Enter “1” in main menu of Wrapnuts-cli to see that your balance has changed accordingly. The file with the embedded cashu can either be shared with another user or redeemed with Nutwraps-cli.

5. To redeem embedded cashu, enter “3” in the main menu of Wrapnuts-cli and follow the instructions until the unwrapping process is complete.

## Disclaimer 

The author is NOT a cryptographer and this work has not been reviewed. This means that there is very likely a fatal flaw somewhere. Wrapnuts and Cashu are still experimental and not production-ready.
