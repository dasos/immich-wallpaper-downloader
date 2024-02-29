import os, requests, json, configargparse
from urllib.parse import urlparse

p = configargparse.ArgParser(formatter_class=configargparse.ArgumentDefaultsRawHelpFormatter, default_config_files=['default.conf'])
p.add('-c', '--config', is_config_file=True, help='config file path')
p.add('--api_key', required=True, help='Immich API key, generated in the UI', env_var='IMMICH_API_KEY')
p.add('--baseurl', required=True, help='The URL of the Photoprism server (ie, https://immich.example.com)')
p.add('--quantity', help='How many photos to download', default='10')
p.add('--output_directory', required=True, help='Where to put the files.')

options = p.parse_args()


# A little helper function to reduce code
def request_wrap(url, params=None):
    immich_server = options.baseurl
    api_key = options.api_key

    immich_parsed_url = urlparse(immich_server)
    base_url = f"{immich_parsed_url.scheme}://{immich_parsed_url.netloc}"
    api_url = f"{base_url}/api"

    headers = {"x-api-key": api_key}

    return requests.get(api_url + url, headers=headers, params=params)


#First, lets get a list of photos

params = {"count": options.quantity}
response = request_wrap("/asset/random", params) # TODO: more than random?...

response.raise_for_status()


# Then loop through them, downloading as we go
d = 1
for a in response.json():

    filename = os.path.expanduser(f"{options.output_directory}/wallpaper_{d}.jpg")
    
    print (f"Downloading {a['originalFileName']} as {filename}")

    r = request_wrap(f"/asset/thumbnail/{a['id']}?format=JPEG")

    with open(filename, 'wb') as fd:
        fd.write(r.content)
    
    d = d + 1

