
# Path to RSA key; to generate an RSA public/private key pair use rsa/adbkeygen.py
RSA_KEY = '/path/to/file'

# Local path that files will be copied to
PC_DESTINATION_PATH = '/path/to/dir/'

# Path(s) on device to search for files; key is used as a label for progress bar during transfer
PATHS_TO_SEARCH = {
    '1. Command' : 'files/contents/1/files/character/command/**/*.png',
    '1. Party Portrait' : 'files/contents/1/files/character/party_portrait/**/*.png',
    '1. Base' : 'files/contents/1/files/character/base/**/*.png',
    '2. Command' : 'files/contents/2/files/character/command/**/*.png',
    '2. Party Portrait' : 'files/contents/2/files/character/party_portrait/**/*.png',
    '2. Base' : 'files/contents/2/files/character/base/**/*.png',
    '2. EN Lottery BG' : 'files/contents/2/files/i18n/en/files/ui/lottery/bg/*.png',
    '2. EN Lottery Top Cell' : 'files/contents/2/files/i18n/en/ui/lottery/lottery_top_cell/*.png',

    #'3. Command' : 'files/contents/3/files/character/command/**/*.png',
    #'3. Party Portrait' : 'files/contents/3/files/character/party_portrait/**/*.png',
    #'3. Base' : 'files/contents/3/files/character/base/**/*.png',
    #'5. Command' : 'files/contents/5/files/character/command/**/*.png',
    #'5. Party Portrait' : 'files/contents/5/files/character/party_portrait/**/*.png',
    #'5. Base' : 'files/contents/5/files/character/base/**/*.png',
    #'6. Command' : 'files/contents/6/files/character/command/**/*.png',
    #'6. Party Portrait' : 'files/contents/6/files/character/party_portrait/**/*.png',
    #'6. Base' : 'files/contents/6/files/character/base/**/*.png',
    #'13. Command' : 'files/contents/13/files/character/command/**/*.png',
    #'13. Party Portrait' : 'files/contents/13/files/character/party_portrait/**/*.png',
    #'13. Base' : 'files/contents/13/files/character/base/**/*.png',
    #'14. Command' : 'files/contents/14/files/character/command/**/*.png',
    #'14. Party Portrait' : 'files/contents/14/files/character/party_portrait/**/*.png',
    #'14. Base' : 'files/contents/14/files/character/base/**/*.png',
}