import os
import subprocess
import time
#Clear console on unix-sys and use cls on Windows NT family
os.system('cls' if os.name == 'nt' else 'clear')

ans=True
while ans:
  print ('========================================')
  print ('#             WRAPNUTS                 #')
  print ('========================================')
  print("1. Your balance at the mint")
  print("2. Wrap a cashu")
  print("3. Unwrap a cashu")
  print("4. Exit")
  print ('========================================')
  print ()
  ans=input("What do you want to do? Enter number: ")
  
  selected_file = None
  cashu_amount = None
  if ans == '1':
    print ('\n========================================')
    output = subprocess.check_call(['cashu', 'balance'], stderr=subprocess.STDOUT, text=True)
    print ('========================================')
    time.sleep(3)
    os.system('clear')
  elif ans == '2': 
    # List files in current directory
    files_list = [f for f in os.listdir('.') if os.path.isfile(f)]
    # Filter files for simplicity 
    filtered_files = [file for file in files_list if 
    file.endswith(".jpg") or file.endswith(".wav")]
    print ('\n========================================')
    print("Available files to wrap in:\n") 
    while selected_file is None:
      for file in filtered_files: 
        print(file)
      print ('========================================')
      coverfile=input("Enter file name, e.g. cats.jpg: ")
      if coverfile in filtered_files:
        selected_file = coverfile
        break
      else:
        print("Invalid file name! Please try again.")
        print("By entering file name and its extension!\n")
    print ('========================================')
    # Send cashu and capture output in temp file
    while True:
      if cashu_amount is None:
        output = subprocess.check_call(['cashu', 'balance'], stderr=subprocess.STDOUT, text=True)
        print ("Enter amount to wrap: ")
        try:
          nut1 = int(input())
          stored_nut = nut1
          break
        except ValueError:
          print("Invalid input! Please enter an integer.")
          print ('========================================')
    else:
        stored_nut = cashu_amount
        print ('========================================')
    try:
        output = subprocess.check_call(['cashu', 'send', str(stored_nut)], stderr=subprocess.STDOUT, text=True)
        print ('Connecting...')
        # Format output as string
        output = os.popen("cashu pending | head -n 5".format(stored_nut)).readlines()
        output_string = "{}".format(output[4])
        temp_file = ".temp_cashu.txt"
        with open(temp_file, "w") as f:
          f.write(output_string)
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while wrapping cashu ({e.returncode}: {e.cmd})")
        continue
    print ('========================================') 
    print ("Enter your passphrase: ")
    pwd1 = input()
    print ("Re-Enter your passphrase: ")
    pwd2 = input()
    if pwd1 == pwd2: 
        passphrase = pwd1
        # Embed captured output in selected file
        os.system(f"steghide embed -p {passphrase} -cf {coverfile} -ef '{temp_file}'")
        print ('========================================')
        print(f"Cashu successfully wrapped in {coverfile}")
        print ('Loading...')
        os.remove(temp_file)
    else:
        print ('========================================')
        print ("Passphrase does not match.")
        print ("Reloading...")
        with open(temp_file, "r") as f:
         output_string = f.read()
        os.popen(f"cashu receive {output_string}").read().strip()
        os.remove(temp_file)
    os.system('clear')
  elif ans == '3':
    files_list = [f for f in os.listdir('.') if os.path.isfile(f)]
    filtered_files = [file for file in files_list if 
    file.endswith(".jpg") or file.endswith(".wav")]
    print ('\n========================================')
    print("Available files to unwrap from:\n") 
    while selected_file is None:
      for file in filtered_files: 
        print(file)
      print ('========================================')
      stegfile=input('Enter file name, e.g. hotdogs.jpg: ') 
      print ('========================================')
      if stegfile in filtered_files:
        selected_file = stegfile
        break
      else:
        print("Invalid file name! Please try again.")
        print("By entering file name and extension!\n")
    print('This will unwrap cashu into your wallet.')
    os.system('steghide extract -sf ' + stegfile)
    # Receive cashu from extracted secret
    print ('Loading...')
    temp_file = ".temp_cashu.txt"
    with open(temp_file, "r") as f:
      extracted_string = f.read()
    os.popen(f"cashu receive {extracted_string}").read().strip() 
    print ('========================================')
    print(f"Cashu successfully unwrapped from {stegfile}")
    os.remove(temp_file)   
    time.sleep(5)
    os.system('clear')
  elif ans == '4':
    print ('\n========================================') 
    print('See you soon!')
    print ('========================================') 
    break
  else: 
    print ('\n========================================')
    print('Unknown option entered! Please try again.')
    time.sleep(3)
    os.system('clear')
