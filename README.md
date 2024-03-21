# ae-img-extract

## Usage

```shell
python image_extract.py
```

- Be sure to update [settings.py](settings.py) with local paths to RSA keys and copy destination

## Requirements

- Rooted Android device, with setup granting superuser permissions (via Magisk, SuperSu, etc), connected via USB and in [File Transfer mode](https://support.google.com/android/answer/9064445)

## More Info

- Generally follows a similar process to how Android Studio copies files from a device to a connected PC but using [adb_shell](https://github.com/JeffLIrion/adb_shell/) in python
- These steps include (see also: [How Device File Explorer on Android Studio works](https://medium.com/@liwp.stephen/how-does-android-studio-device-file-explorer-works-62685330e8c8))
    - Create a temporary directory on device in a location accessible by `adb pull` (uses /sdcard/ by default)
    - Get a list of files and copy them to temp directory
    - Use `adb pull` in adb_shell to copy files to PC destination
    - After files are transferred, deletes temporary directory on device to clean up