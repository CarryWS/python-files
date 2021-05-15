import zipfile,sys,os
##################################
#zip file set
try:
    zipfilepath = sys.argv[1]
    print('set argv OK')
except:
    print('argv error')
    exit()
##################################
#if file is zip or rar
if zipfilepath[-4:] == '.rar':
    filetype = 'rar'
    print('rar yes')
else:
    if zipfilepath[-4:] == '.zip':
        filetype = 'zip'
        print('zip yes')
    else:
        print('not a zip or rar file')
        sys.exit()

print('file type is '+filetype)
##################################

if filetype == 'rar':
    def extractall(file,path_):
        os.popen('unrar x '+str(file)+' '+str(path_)+'\\')

    try:
        os.mkdir(zipfilepath[:-4])#if no error,means the folder is not have
        os.removedirs(zipfilepath[:-4])
        print('folder not have')
    except:#means the folder is have
        import os
        import shutil
        filelist=[]
        rootdir=zipfilepath[:-4]
        filelist=os.listdir(rootdir)                #列出该目录下的所有文件名
        for f in filelist:
            filepath = os.path.join( rootdir, f )
            if os.path.isfile(filepath):
                os.remove(filepath)
                print(str(filepath)+" removed")
            elif os.path.isdir(filepath):
                shutil.rmtree(filepath,True)
                print("dir "+str(filepath)+" removed!")
        shutil.rmtree(rootdir,True)
        print('removed folder')
        print('folder is have')


    extractall(zipfilepath,zipfilepath[:-4])


else:
    try:
        os.mkdir(zipfilepath[:-4])#if no error,means the folder is not have
        os.removedirs(zipfilepath[:-4])
        print('folder not have')
    except:#means the folder is have
        import os
        import shutil
        filelist=[]
        rootdir=zipfilepath[:-4]
        filelist=os.listdir(rootdir)                #列出该目录下的所有文件名
        for f in filelist:
            filepath = os.path.join( rootdir, f )
            if os.path.isfile(filepath):
                os.remove(filepath)
                print(str(filepath)+" removed")
            elif os.path.isdir(filepath):
                shutil.rmtree(filepath,True)
                print("dir "+str(filepath)+" removed!")
        shutil.rmtree(rootdir,True)
        print('removed folder')
    zipfile.ZipFile(zipfilepath).extractall(zipfilepath[:-4])
