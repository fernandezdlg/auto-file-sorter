#!/Users/fernandezdlg/miniconda3/bin python
# This is for macOS directories
# Script inspired by blogpost https://rootstack.com/en/blog/how-automate-download-folder-python

# Imports:
import os
import shutil

# User directory to be sorted
dirDownloads = '/Users/fernandezdlg/DownloadsTest'

# Types of files and folders
extVideos      = ['.mp4','.mpeg','.mov']
extPdfs        = ['.pdf']
extDiverseDocs = ['.doc','.docx','.md','.pptx','.ppt','.xls','.xlsx','.djvu','.epub','.key']
extImgs        = ['.avif','.jpg','.jpeg','.png','.gif','.heic']
extZips        = ['.tar','.gz','.zip','.7z']
extLatex       = ['.bib','.tex','.sty','.bibtex']
extSourceCode  = ['.py','.c','.cpp','.h','.cu','.cuh']
extJupyterNbs  = ['.ipynb']
extCalendar    = ['.ics']
extMusic       = ['.mp3']

# WARNING: Not including *exacly* the name of all supported destination folders can result in lost files when running shutil.move!!!
subDirs = ['Videos',
           'Pdfs',
           'DiverseDocs',
           'Imgs',
           'Zips',
           'Latex',
           'SourceCode',
           'JupyterNbs',
           'Calendar',
           'Music']

# Dictionary of subDirs and respective extensions:
dictSubDirs = {
    'Videos'      : extVideos,
    'Pdfs'        : extPdfs,
    'DiverseDocs' : extDiverseDocs,
    'Imgs'        : extImgs,
    'Zips'        : extZips,
    'Latex'       : extLatex,
    'SourceCode'  : extSourceCode,
    'JupyterNbs'  : extJupyterNbs,
    'Calendar'    : extCalendar,
    'Music'       : extMusic
}    

# Check if subdir in dir
def checkSubdirInDir(subdir, dir):
    for i in os.scandir(dir):
        if i.is_dir() and i.name == subdir:
            return 1
    return 0
        

# Create subdirectories if non existent in directory
def confirmDirs(dir, subDirs):
    for subdir in subDirs:
        if checkSubdirInDir(subdir, dir) == 0:
            os.mkdir(dir + '/' + subdir)


def safeMove(src_filepath, dst_filepath):
    # Move only if directory exists and there is no file with the same name
    if os.path.exists(os.path.dirname(dst_filepath)):
        if not os.path.exists(dst_filepath):
            shutil.move(src_filepath, dst_filepath)
    else: 
        print('Error when moving: ' + src_filepath + ' file was not moved due to naming duplicate or non-existent directory')


# Move files function
def moveFiles(file, ext):
    # This switch is ugly:
    for category in dictSubDirs:
        if ext in dictSubDirs[category]:
            safeMove(dirDownloads +'/'+ file, dirDownloads +'/'+ category + '/' + file)
            return 0
 

def main():
    confirmDirs(dirDownloads,subDirs)

    for sam in os.scandir(dirDownloads):
        if sam.is_file():
            fileName = sam.name
            fileExt = os.path.splitext(fileName)[1]
            try:
                moveFiles(fileName,fileExt)
            except:
                print('Error, one file was not moved due to naming duplicate')


if __name__ == '__main__':
    main()
