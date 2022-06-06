# Build Patcher
Build Patcher is a simple tool made to make uploading games to itch.io easier

![img](https://i.imgur.com/mLd2D3n.png)

![img](https://i.imgur.com/b7GSMmb.png)

### How To Use

* Select Build File (Zip or Rar)
* Select Target User/GamePage
* Chose Your Target Platform (Windows,Mac,Linux)
* Update Game Version
* Hit The Upload Button!


![gif](https://i.imgur.com/hjB8GDx.gif)


![img](https://i.imgur.com/ohQ9gGt.png)

# Requirements

 <li><a href="https://itch.io/register">itch.io Developer Account</a></li>
 <li><a href="https://itch.io/docs/butler/">itch.io butler</a></li>
 
# Installation

To start using this Tool you need to follow this Steps first.

<b><u>Note: This Is Only One Time Setup</u></b>

<ol>
    <li><a href="#downloading">Download</a></li>
    <li><a href="#butler">Installing Butler</a></li>
    <li><a href="#api-key">Itch Api Token</a></li>
</ol>

### Downloading

First you need to download the [Latest Release](https://github.com/Huntrox/BuildPatcher/releases/latest) 
and unpack it at any directory of your choice


### Butler 

Download Butler from [here](https://itch.io/docs/butler/) and follow the install instructions

after That we need to add the butler installation path it to the system path 

- Open your System Properties

![img](https://i.imgur.com/xJxLFF0.png)

- Then press on Environment Variables

![img](https://i.imgur.com/ljrRjpM.png)

- Select Path and press Edit

![img](https://i.imgur.com/LiY920I.png)

- Add Butler directory path and press ok and save  

![img](https://i.imgur.com/XToAqTV.png)

- To confirm everything works open your Command Prompt and type `butler`
you should see something like that 

![img](https://i.imgur.com/cEAuLLC.png)

- Now Grant butler access to your itch.io account. To do so, simply run the `butler login` command and follow the instructions
- Once you complete the login flow, your credentials will be saved locally. No need To repeat the process
  

### Api Key 

In order for the Software fetch game pages in your account you need to generate Api key from [Here](https://itch.io/user/settings/api-keys)

and click on <b>Generate new API key</b>

![img](https://i.imgur.com/F7XXdA7.png)

after that click on view and copy

<b><ins>Don't share the key anywhere </ins></b>

![img](https://i.imgur.com/I8LvCvv.png)

Finally open `config.txt` and past you Api Key

![img](https://i.imgur.com/nqyL3Kl.png)



 
