from pathlib import Path
import uuid

from adb_shell.adb_device import AdbDevice
from adb_shell.auth.sign_pythonrsa import PythonRSASigner
from adb_shell.transport.usb_transport import UsbTransport
from tqdm import tqdm

import settings


def get_device_temp_dir(device_dir='/sdcard'):
    unique = str(uuid.uuid4())
    return f'{device_dir}/temp{unique}/'


def get_rsa_signer():
    # Load the public and private keys
    with open(settings.RSA_KEY) as f:
        priv = f.read()
    with open(settings.RSA_KEY + '.pub') as f:
        pub = f.read()
    return PythonRSASigner(pub, priv) 


def run_file_transfer():
    # find device and connect
    signer = get_rsa_signer()
    transport = UsbTransport.find_adb()
    device = AdbDevice(transport)
    device.connect(rsa_keys=[signer], auth_timeout_s=0.1)
    # if getting LIBUSB_ERROR_ACCESS [-3] on device.connect try `adb kill-server`; see for more https://github.com/JeffLIrion/adb_shell/issues/114

    # create temp dir in folder accessible to adb pull
    temp_dir = get_device_temp_dir()
    device.shell(f'mkdir -p {temp_dir}')

    base_path = '/data_mirror/data_ce/null/0/games.wfs.anothereden/'

    for desc, img_search in settings.PATHS_TO_SEARCH.items():
        # get list of all images
        img_list = device.shell(f"su 0 sh -c 'ls -1 {base_path + img_search}'").split('\r\n')

        for img_path in tqdm(img_list[:-1], desc=desc):
            img = img_path.split('/')[-1] #12345.png
            dir_path = img_path.replace(base_path, '/').replace(img, '') #/path/to/files/
            dest_path = temp_dir + dir_path[1:] #/dest/path/to/files/
            
            # mkdirs and copy to temp dir accessible to adb pull
            device.shell(f"su 0 sh -c 'mkdir -p {dest_path} && cp {img_path} {dest_path}'")

            # mkdirs in PC destination
            mkdir_path = settings.PC_DESTINATION_PATH + dir_path
            Path(mkdir_path).mkdir(parents=True, exist_ok=True)

            # pull file into destination
            device.pull(dest_path + img, mkdir_path + img)

    print('Files transferred, cleaning up device...')
    # delete temp dir on device
    device.shell(f'rm -rf {temp_dir}', read_timeout_s=60)
    print('Temp directory deleted on device.')
    print('Done!')


def main():
    if settings.PC_DESTINATION_PATH == '/path/to/dir/' or settings.RSA_KEY == '/path/to/file':
        print('Update settings.py for copy destination path and/or RSA key path')
    else:
        run_file_transfer()


if __name__ == '__main__':
    main()