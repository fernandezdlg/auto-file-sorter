#!/Users/fernandezdlg/miniconda3/bin python
# This is for macOS directories
# Script inspired by blogpost https://rootstack.com/en/blog/how-automate-download-folder-python

import os
import shutil

dirDownloads = "/Users/fernandezdlg/Downloads/"

# Types of files and folders
extVideos = ['.mp4','.mpeg','.mov']
extPdfs = ['.pdf']
extOtherDocs = ['.doc','.docx','.md','.pptx','.ppt','.xls','.xlsx','.djvu','.epub','.key']
extImgs = ['.avif','.jpg','.jpeg','.png','.gif','.heic']
extZips = ['.tar','.gz','.zip','.7z']
extLatex = ['.bib','.tex','.sty','.bibtex']
extSourceCode = ['.py','.c','.cpp','.h','.cu','.cuh']
extJupyterNbs = ['.ipynb']
extCalendar = ['.ics']
extMusic = ['.mp3']

# WARNING: Not including *exacly* the name of all supported destination folders can result in lost files when running shutil.move!!!
subDirs = ['Videos',
'Pdfs',
'OtherDocs',
'Imgs',
'Zips',
'Latex',
'SourceCode',
'JupyterNbs',
'Calendar',
'Music']

# Check if subdir in dir
def checkSubdirInDir(subdir, dir):
    for i in os.scandir(dir):
        if i.is_dir():
            if i.name == subdir:
                return 1
            
    return 0
        

# Create subdirectories if non existent in directory
def confirmDirs(dir, subDirs):
    for subdir in subDirs:
        if checkSubdirInDir(subdir, dir) == 0:
            os.mkdir(dir + '/' + subdir)
    

# Move files function
def moveFile(file, ext):
    # This repetition of loops should be made into a loop of loops for file types
    for i in extVideos:
        if ext == i:
            shutil.move(dirDownloads + file, dirDownloads + 'Videos')
            return 0
    
    for i in extPdfs:
        if ext == i:
            shutil.move(dirDownloads + file, dirDownloads + 'Pdfs')
            return 0
    
    for i in extOtherDocs:
        if ext == i:
            shutil.move(dirDownloads + file, dirDownloads + 'OtherDocs')
            return 0
    
    for i in extImgs:
        if ext == i:
            shutil.move(dirDownloads + file, dirDownloads + 'Imgs')
            return 0
    
    for i in extZips:
        if ext == i:
            shutil.move(dirDownloads + file, dirDownloads + 'Zips')
            return 0
    
    for i in extLatex:
        if ext == i:
            shutil.move(dirDownloads + file, dirDownloads + 'Latex')
            return 0
    
    for i in extSourceCode:
        if ext == i:
            shutil.move(dirDownloads + file, dirDownloads + 'SourceCode')
            return 0
    
    for i in extJupyterNbs:
        if ext == i:
            shutil.move(dirDownloads + file, dirDownloads + 'JupyterNbs')
            return 0
    
    for i in extCalendar:
        if ext == i:
            shutil.move(dirDownloads + file, dirDownloads + 'Calendar')
            return 0

    for i in extMusic:
        if ext == i:
            shutil.move(dirDownloads + file, dirDownloads + 'Music')
            return 0
    


def main():
    confirmDirs(dirDownloads,subDirs)

    for sam in os.scandir(dirDownloads):
        if sam.is_file():
            fileName = sam.name
            fileExt = os.path.splitext(fileName)[1]
            try:
                moveFile(fileName,fileExt)
            except:
                print("Error, one file was not moved due to naming duplicate")


if __name__ == "__main__":
    main()
