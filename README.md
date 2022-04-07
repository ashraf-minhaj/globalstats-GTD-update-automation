# globalstats-GTD-update-automation
 Python Selenium Script to automate GlobalStats Tracked Data update

### set up server
#### 1. Log in to server droplet

```
ssh -i ~/.ssh/algorithms_key root@YOUR_IP
```

#### 2. install pip
`apt install -y python3 python3-pip`

#### 3. install python packages/libraries
`pip3 install selenium`

`pip3 install webdriver_manager`

`pip3 install pyvirtualdisplay`

#### 4. install chrome
* chrome dependency `apt install -y libxss1 libappindicator1 libindicator7`

* download chrome `wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb`

* dpkg to install `dpkg -i google-chrome*.deb`

* if fails it fixes `apt install -y -f`

#### installing chromedriver
It is deprecated. No hard install is needed.

#### Test code
`python3 main.py test`