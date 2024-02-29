# immich-wallpaper-downloader
A Python script that connects to an [Immich](https://www.immich.app/) server, and downloads a few random files. 

This is useful if, like me, you want to use some of these photos as a wallpaper. I call this script from a cron job, so that a few files get downloaded. Then Windows or Mac OS or whatever then picks a few photos from this directory to set as wallpaper.

## How to get going
 - Clone the directory using git: `git clone https://github.com/dasos/immich-wallpaper-downloader` (or just grab the script)
 - Add config. See what is needed with `python3 wallpaper.py -h`
   - [ConfigArgParse](https://github.com/bw2/ConfigArgParse) is used. So you can create your own config file, or use environment variables, or use command line options.
   - I create a config file in my home directory, then pass it to the script with `python3 wallpaper.py -c ~/.immich-wallpaper-downloader.conf`
   - You will add your api_key in this file. Please protect the file properly: `chmod 600 ~/.immich-wallpaper-downloader.conf`
 - Sort out your virtual environment. `python3 -m venv venv; source venv/bin/activate`
 - Install the requirements `python3 -m pip install -r requirements.txt`
   - Note that an older version of urllib is specified because of Mac OS
 - Set up a cron job, or Windows Task Scheduler or whatever to run the script. This may be tricky because of the virtual environment. What worked for me is (almost exactly) this cron job on Mac OS: `50 * * * * /Users/<user>/immich-wallpaper-downloader/venv/bin/python /Users/<user>/immich-wallpaper-downloader/wallpaper.py -c /Users/<user>/.immich-wallpaper-downloader.conf`
 - Set up [Windows](https://support.microsoft.com/en-us/windows/change-your-desktop-background-image-175618be-4cf1-c159-2785-ec2238b433a8) or [Mac OS](https://support.apple.com/en-gb/guide/mac-help/mchlp3013/mac) to look in the folder you've chosen in the config, and have it change the wallpaper. I have the wallpaper change every 30 minutes, which picks from the 10 the script downloads. This gives me a different photo on every screen.
 - Enjoy your photos!