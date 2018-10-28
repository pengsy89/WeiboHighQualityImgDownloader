@ECHO OFF
SET ROOT_PATH=d:/OneDrive
SET /P WEIBO_ID=Enter Weibo ID:

start cmd /k "cd C:\Python\Python36-32\ && python D:\Code\WeiboHighQualityImgDownloader\WeiboHighQualityImgDownloader\src\downloader.py %ROOT_PATH% %WEIBO_ID%