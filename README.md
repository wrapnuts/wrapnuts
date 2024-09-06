![](https://github.com/wrapnuts/wrapnuts/blob/main/wrapnuts.png)

This CLI was developed as a proof of concept for embedding cashu. Launch a test flight according to the steps below.

# Wrapnuts-cli

A CLI that implements the functionality of embedded cashu by interacting with the Nutshell-wallet **[I.]** 

## Roadmap

- [x] Steghide tool by Hetzl, S. **[II.]**
- [x] Embedding cashu in photos (.jpg & .png) 
- [x] Embedding cashu in audio files (.wav)
- [x] Encryption, let users choose passphrase
- [x] Let users choose amount of cashu to wrap
- [ ] Support and test more file types
- [x] Support for Nutshell-wallet if connected to multiple mints


## Requirements

**[I.]** Install [Nutshell](https://github.com/cashubtc/nutshell?tab=readme-ov-file) & **[II.]** [steghide](https://steghide.sourceforge.net/index.php), according to their docs. Or use a package manager, like apt:

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

1. Make sure to have a .jpg or .png or .wav file in the working directory of Wrapnuts-cli and then run:

```bash
python3 wrapnuts-cli.py
```

2. Enter “1” in main menu of Wrapnuts-cli. If no balance is displayed, make sure to fulfill the two requirements:
    - Is the Nutshell-wallet connected to a mint?
    - Does it have a balance?

3. If balance is displayed, both requirements have been met. Next, enter “2” in main menu to embed (wrap) a cashu. Then follow the instructions until the wrapping process is complete.

4. The file with the embedded cashu can either be shared with another user or redeemed by the same user with Wrapnuts-cli.

5. To redeem embedded cashu from a file, enter “3” in main menu of Wrapnuts-cli. Then follow the instructions until the unwrapping process is complete.

## Disclaimer 

The author is NOT a cryptographer and this work has not been reviewed. This means that there is very likely a fatal flaw somewhere. Wrapnuts and Cashu are still experimental and not production-ready.
