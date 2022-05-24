import glob
import os
import argparse
import shutil
def glob_name_to_txt(root_folder,save_path=''):
    with open(save_path, "w") as axlspd:
        for f in glob.glob(f"{root_folder}/*.png"):
            fpath, fname = os.path.split(f)
            rname, extname = os.path.splitext(fname)
            dirtup = (f, rname)
            axlspd.write(rname+'\n')

def glob_xml_then_move(root_folder,save_folder='save_xml'):
    xml_paths = glob.glob(f"{root_folder}/*.xml")
    for xml_path in xml_paths:
        shutil.copy(xml_path,save_folder)


def main():
    parser = argparse.ArgumentParser(
        description='This script support converting voc format xmls to coco format json')
    parser.add_argument('--root_name', type=str, default=None,
                        help='path to file contain image')
    parser.add_argument('--save_name', type=str, default=None,
                        help='path to save the names as text file')
    parser.add_argument('--root_xml', type=str, default=None,
                        help='path to directory contain xml voc file')
    parser.add_argument('--save_xml', type=str, default=None,
                        help='path save directory of xml file')
    args = parser.parse_args()
    glob_name_to_txt(root_folder=args.root_name,save_path=args.save_name)
    glob_xml_then_move(root_folder=args.root_xml,save_folder=args.save_xml)


if __name__ == '__main__':
    main()
