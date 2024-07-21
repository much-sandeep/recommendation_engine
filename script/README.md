For Linux

Installing the Google Chrome

```

wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
sudo dpkg -i google-chrome-stable_current_amd64.deb

If there is any issue occured due to the dependencies you can use the following command
sudo apt-get install -f
and run the dpkg command

```

# Errors and their solutions

Error : libnss3.so: cannot open shared object file: No such file or directory

```
sudo apt-get install -y libnss3 libgconf-2-4 libxi6 libgdk-pixbuf2.0-0 libxcomposite1 libasound2 libxrender1 libxrandr2 libu2f-udev libxtst6 libatk1.0-0 libatspi2.0-0

```
