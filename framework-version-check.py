import fnmatch
import os, sys
import xml.etree.ElementTree

#/Users/eltonalves/Documents/tfs/Produtos
def scanFiles(folder):
    for root, dirnames, filenames in os.walk(folder):
        for filename in fnmatch.filter(filenames, '*.csproj'):
            e = xml.etree.ElementTree.parse(os.path.join(root, filename)).getroot() 
            for framework in e.iter('TargetFramework'):
                    print(filename.replace('.csproj',''))+';'+framework.text



def run():
    scanFiles(sys.argv[1])

if __name__ == '__main__':
    run()